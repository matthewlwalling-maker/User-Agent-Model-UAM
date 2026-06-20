from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from .config import RunConfig
from .util import utc_now


@dataclass
class ProviderResult:
    context_id: str
    request: dict[str, Any]
    response: dict[str, Any] | None
    text: str | None
    parsed_json: dict[str, Any] | None
    usage: dict[str, Any]
    preflight_input_tokens: int | None
    wall_latency_ms: int
    model_latency_ms: int | None
    error: dict[str, Any] | None
    started_at: str
    ended_at: str


class UsageWindowExhausted(RuntimeError):
    """Raised when Codex reports a plan usage/rate/credit limit during an attempt."""

    def __init__(self, message: str, result: ProviderResult):
        super().__init__(message)
        self.result = result


class Provider(Protocol):
    def invoke(
        self,
        *,
        system: list[dict[str, Any]] | str,
        messages: list[dict[str, Any]],
        max_tokens: int,
        output_schema: dict[str, Any] | None = None,
        context_id: str | None = None,
        preflight: bool = True,
    ) -> ProviderResult: ...


def _flatten_system(system: list[dict[str, Any]] | str) -> str:
    if isinstance(system, str):
        return system
    parts: list[str] = []
    for block in system:
        if isinstance(block, dict):
            parts.append(str(block.get("text", "")))
        else:
            parts.append(str(block))
    return "\n\n".join(p for p in parts if p)


def _render_transcript(system: list[dict[str, Any]] | str, messages: list[dict[str, Any]]) -> str:
    lines = [
        "<SYSTEM_INSTRUCTIONS>",
        _flatten_system(system),
        "</SYSTEM_INSTRUCTIONS>",
        "",
        "<CONVERSATION_TRANSCRIPT>",
    ]
    for message in messages:
        role = str(message.get("role", "user")).upper()
        content = message.get("content", "")
        if isinstance(content, list):
            content = json.dumps(content, ensure_ascii=False)
        lines.extend([f"<{role}>", str(content), f"</{role}>"])
    lines.extend([
        "</CONVERSATION_TRANSCRIPT>",
        "",
        "Execute the latest user instruction under the system instructions. Do not inspect the filesystem, use tools, browse, or rely on information not present above. Return only the requested final response.",
    ])
    return "\n".join(lines)


def _parse_jsonl(text: str) -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    non_json: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
            if isinstance(value, dict):
                events.append(value)
            else:
                non_json.append(line)
        except json.JSONDecodeError:
            non_json.append(line)
    return events, non_json


def _codex_error_kind(returncode: int, events: list[dict[str, Any]], stderr: str) -> tuple[str, bool]:
    text = "\n".join([stderr] + [json.dumps(x, ensure_ascii=False) for x in events]).lower()
    usage_markers = (
        "usage limit", "rate limit", "insufficient credits", "credit balance", "quota",
        "too many requests", "limit reached", "usage cap",
    )
    if any(marker in text for marker in usage_markers):
        return "provider-usage-limit", True
    if returncode != 0:
        return "CodexCLIError", False
    return "CodexOutputError", False


class CodexCLIProvider:
    """Codex CLI adapter using the user's existing ChatGPT-managed Codex login.

    Every invoke is a fresh `codex exec` process. The harness supplies the full allowed
    transcript, uses an empty temporary workspace, disables tools and web search, and
    captures the JSONL event stream plus the exact final message.
    """

    def __init__(self, config: RunConfig):
        p = config.provider
        self.config = config
        self.binary = str(p.get("binary", "codex"))
        resolved = shutil.which(self.binary)
        if not resolved and Path(self.binary).exists():
            resolved = str(Path(self.binary).resolve())
        if not resolved:
            raise RuntimeError(f"Codex CLI executable not found: {self.binary}")
        self.binary = resolved
        self.command_prefix = [sys.executable, self.binary] if self.binary.endswith(".py") else [self.binary]
        self.model = str(p["model"])
        self.reasoning_effort = str(p.get("reasoning_effort", "high"))
        self.model_verbosity = str(p.get("model_verbosity", "low"))
        self.timeout = float(p.get("timeout_seconds", 1800))
        self.auth_mode = str(p.get("auth_mode", "auto"))
        self.ephemeral = bool(p.get("ephemeral", False))
        self.ignore_user_config = bool(p.get("ignore_user_config", False))
        self.ignore_rules = bool(p.get("ignore_rules", True))
        self.history_persistence = str(p.get("history_persistence", "none"))
        self.extra_args = [str(x) for x in p.get("extra_args", [])]

    @staticmethod
    def _usage(events: list[dict[str, Any]]) -> dict[str, Any]:
        usage: dict[str, Any] = {}
        for event in events:
            if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
                usage = dict(event["usage"])
        # Normalize names used by the existing harness while retaining native fields.
        usage.setdefault("input_tokens", 0)
        usage.setdefault("cached_input_tokens", 0)
        usage.setdefault("output_tokens", 0)
        usage.setdefault("reasoning_output_tokens", 0)
        usage["cache_read_input_tokens"] = int(usage.get("cached_input_tokens", 0) or 0)
        usage["cache_creation_input_tokens"] = 0
        usage["provider"] = "codex_cli"
        return usage

    @staticmethod
    def _thread_id(events: list[dict[str, Any]]) -> str | None:
        for event in events:
            if event.get("type") == "thread.started" and event.get("thread_id"):
                return str(event["thread_id"])
        return None

    def invoke(
        self,
        *,
        system: list[dict[str, Any]] | str,
        messages: list[dict[str, Any]],
        max_tokens: int,
        output_schema: dict[str, Any] | None = None,
        context_id: str | None = None,
        preflight: bool = True,
    ) -> ProviderResult:
        del preflight  # Codex JSONL usage is authoritative after the turn; no separate count call is needed.
        requested_context_id = context_id or f"ctx-{uuid.uuid4()}"
        prompt = _render_transcript(system, messages)
        started_at = utc_now()
        start = time.perf_counter()

        with tempfile.TemporaryDirectory(prefix="mch-codex-") as temp:
            workdir = Path(temp)
            final_path = workdir / "final_message.txt"
            schema_path = workdir / "output_schema.json"
            command = [
                *self.command_prefix,
                "exec",
                "--json",
                "--skip-git-repo-check",
                "--sandbox",
                "read-only",
                "--model",
                self.model,
                "--output-last-message",
                str(final_path),
                "--cd",
                str(workdir),
                "-c",
                f'model_reasoning_effort="{self.reasoning_effort}"',
                "-c",
                f'model_verbosity="{self.model_verbosity}"',
                "-c",
                'approval_policy="never"',
                "-c",
                'web_search="disabled"',
                "-c",
                "features.shell_tool=false",
                "-c",
                f'history.persistence="{self.history_persistence}"',
            ]
            if self.ephemeral:
                command.append("--ephemeral")
            if self.ignore_user_config:
                command.append("--ignore-user-config")
            if self.ignore_rules:
                command.append("--ignore-rules")
            if self.auth_mode in {"chatgpt", "api"}:
                command.extend(["-c", f'forced_login_method="{self.auth_mode}"'])
            if output_schema is not None:
                schema_path.write_text(json.dumps(output_schema, ensure_ascii=False, indent=2), encoding="utf-8")
                command.extend(["--output-schema", str(schema_path)])
            command.extend(self.extra_args)
            command.append("-")

            request_record = {
                "provider": "codex_cli",
                "command": command,
                "model": self.model,
                "reasoning_effort": self.reasoning_effort,
                "model_verbosity": self.model_verbosity,
                "sandbox": "read-only",
                "tools_disabled": True,
                "web_search": "disabled",
                "auth_mode": self.auth_mode,
                "ephemeral": self.ephemeral,
                "ignore_user_config": self.ignore_user_config,
                "ignore_rules": self.ignore_rules,
                "history_persistence": self.history_persistence,
                "requested_context_id": requested_context_id,
                "prompt": prompt,
                "messages": messages,
                "system": system,
                "output_schema": output_schema,
                "max_tokens_requested_but_not_cli_enforced": max_tokens,
            }

            try:
                completed = subprocess.run(
                    command,
                    input=prompt,
                    text=True,
                    encoding="utf-8",
                    capture_output=True,
                    timeout=self.timeout,
                    check=False,
                    env=os.environ.copy(),
                )
                elapsed = int((time.perf_counter() - start) * 1000)
                events, non_json_stdout = _parse_jsonl(completed.stdout)
                final_text = final_path.read_text(encoding="utf-8") if final_path.exists() else None
                usage = self._usage(events)
                actual_thread = self._thread_id(events)
                response_record = {
                    "returncode": completed.returncode,
                    "events": events,
                    "non_json_stdout": non_json_stdout,
                    "stderr": completed.stderr,
                    "final_message": final_text,
                    "thread_id": actual_thread,
                }
                parsed: dict[str, Any] | None = None
                error: dict[str, Any] | None = None
                if completed.returncode == 0 and final_text is not None:
                    if output_schema is not None:
                        try:
                            value = json.loads(final_text)
                            if not isinstance(value, dict):
                                raise ValueError("Structured final output is not a JSON object")
                            parsed = value
                        except Exception as exc:
                            error = {"type": type(exc).__name__, "message": str(exc), "usage_limit": False}
                else:
                    kind, usage_limit = _codex_error_kind(completed.returncode, events, completed.stderr)
                    error = {
                        "type": kind,
                        "message": completed.stderr.strip() or "Codex did not produce a final message",
                        "returncode": completed.returncode,
                        "usage_limit": usage_limit,
                    }
                return ProviderResult(
                    context_id=actual_thread or requested_context_id,
                    request=request_record,
                    response=response_record,
                    text=final_text,
                    parsed_json=parsed,
                    usage=usage,
                    preflight_input_tokens=None,
                    wall_latency_ms=elapsed,
                    model_latency_ms=None,
                    error=error,
                    started_at=started_at,
                    ended_at=utc_now(),
                )
            except subprocess.TimeoutExpired as exc:
                elapsed = int((time.perf_counter() - start) * 1000)
                return ProviderResult(
                    context_id=requested_context_id,
                    request=request_record,
                    response={"stdout": exc.stdout, "stderr": exc.stderr},
                    text=None,
                    parsed_json=None,
                    usage={},
                    preflight_input_tokens=None,
                    wall_latency_ms=elapsed,
                    model_latency_ms=None,
                    error={"type": "CodexTimeout", "message": str(exc), "usage_limit": False},
                    started_at=started_at,
                    ended_at=utc_now(),
                )
            except Exception as exc:
                elapsed = int((time.perf_counter() - start) * 1000)
                return ProviderResult(
                    context_id=requested_context_id,
                    request=request_record,
                    response=None,
                    text=None,
                    parsed_json=None,
                    usage={},
                    preflight_input_tokens=None,
                    wall_latency_ms=elapsed,
                    model_latency_ms=None,
                    error={"type": type(exc).__name__, "message": str(exc), "usage_limit": False},
                    started_at=started_at,
                    ended_at=utc_now(),
                )


def build_provider(config: RunConfig) -> Provider:
    provider_type = str(config.provider.get("type", ""))
    if provider_type == "codex_cli":
        return CodexCLIProvider(config)
    raise RuntimeError(f"Unsupported provider.type: {provider_type}")


def total_input_tokens(usage: dict[str, Any], preflight: int | None = None) -> int:
    # Codex reports input_tokens inclusive of cached tokens, with cached_input_tokens as a subset.
    if usage.get("provider") == "codex_cli" or "cached_input_tokens" in usage:
        return int(usage.get("input_tokens", 0) or preflight or 0)
    keys = ["input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"]
    total = sum(int(usage.get(k, 0) or 0) for k in keys)
    return total or int(preflight or 0)
