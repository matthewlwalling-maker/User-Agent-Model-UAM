from __future__ import annotations

import json
import os
from pathlib import Path

import yaml

from mcp_harness.config import load_config
from mcp_harness.provider import CodexCLIProvider


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_DIR = ROOT / "authorities_current"
FIXTURE_VIEW = AUTHORITY_DIR / "P5_Executor_View_v0.1.yaml"


def _config(tmp_path: Path, binary: Path):
    raw = yaml.safe_load((ROOT / "configs/manual_pilot.example.yaml").read_text())
    raw["run_series_id"] = "codex-provider-test"
    raw["paths"]["authority_dir"] = str(AUTHORITY_DIR)
    raw["paths"]["fixture_view"] = str(FIXTURE_VIEW)
    raw["paths"]["output_root"] = str(tmp_path / "runs")
    raw["provider"]["binary"] = str(binary)
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(raw, sort_keys=False))
    return load_config(path)


def _fake_codex(tmp_path: Path) -> Path:
    script = tmp_path / "fake_codex.py"
    script.write_text(
        r'''#!/usr/bin/env python3
import json, pathlib, sys
args=sys.argv[1:]
if args == ["--version"]:
    print("codex-cli 9.9.9-test"); raise SystemExit(0)
if args == ["login", "status"]:
    print("Logged in using ChatGPT"); raise SystemExit(0)
if not args or args[0] != "exec":
    print("unsupported", file=sys.stderr); raise SystemExit(2)
out=None; schema=None
for i,a in enumerate(args):
    if a in ("--output-last-message", "-o"): out=args[i+1]
    if a == "--output-schema": schema=args[i+1]
prompt=sys.stdin.read()
if schema:
    final={"ok": True, "prompt_seen": bool(prompt)}
else:
    final="legacy text output"
pathlib.Path(out).write_text(json.dumps(final) if isinstance(final,dict) else final, encoding="utf-8")
print(json.dumps({"type":"thread.started","thread_id":"thread-test-123"}))
print(json.dumps({"type":"item.completed","item":{"id":"m1","type":"agent_message","text":pathlib.Path(out).read_text()}}))
print(json.dumps({"type":"turn.completed","usage":{"input_tokens":100,"cached_input_tokens":40,"output_tokens":20,"reasoning_output_tokens":5}}))
''',
        encoding="utf-8",
    )
    script.chmod(0o755)
    return script


def test_codex_provider_structured_output_and_metrics(tmp_path):
    provider = CodexCLIProvider(_config(tmp_path, _fake_codex(tmp_path)))
    schema = {
        "type": "object",
        "properties": {"ok": {"type": "boolean"}, "prompt_seen": {"type": "boolean"}},
        "required": ["ok", "prompt_seen"],
        "additionalProperties": False,
    }
    result = provider.invoke(
        system="system rule",
        messages=[{"role": "user", "content": "do it"}],
        max_tokens=100,
        output_schema=schema,
    )
    assert result.error is None
    assert result.context_id == "thread-test-123"
    assert result.parsed_json == {"ok": True, "prompt_seen": True}
    assert result.usage["input_tokens"] == 100
    assert result.usage["cached_input_tokens"] == 40
    assert result.usage["output_tokens"] == 20
    assert result.request["sandbox"] == "read-only"
    assert result.request["tools_disabled"] is True
    assert result.request["auth_mode"] == "auto"
    assert result.request["ignore_user_config"] is False
    assert "--ignore-user-config" not in result.request["command"]
    assert not any("forced_login_method" in str(x) for x in result.request["command"])


def test_codex_provider_plain_text(tmp_path):
    provider = CodexCLIProvider(_config(tmp_path, _fake_codex(tmp_path)))
    result = provider.invoke(
        system="system rule",
        messages=[{"role": "user", "content": "legacy"}],
        max_tokens=100,
    )
    assert result.error is None
    assert result.text == "legacy text output"
    assert result.parsed_json is None


def _fake_limit_codex(tmp_path: Path) -> Path:
    script = tmp_path / "fake_limit_codex.py"
    script.write_text(
        r'''#!/usr/bin/env python3
import json, sys
args=sys.argv[1:]
if args == ["--version"]:
    print("codex-cli 9.9.9-test"); raise SystemExit(0)
if args == ["login", "status"]:
    print("Logged in using ChatGPT"); raise SystemExit(0)
print(json.dumps({"type":"thread.started","thread_id":"thread-limit"}))
print(json.dumps({"type":"error","message":"Usage limit reached. Try again later."}))
print("Usage limit reached. Try again later.", file=sys.stderr)
raise SystemExit(1)
''',
        encoding="utf-8",
    )
    script.chmod(0o755)
    return script


def test_codex_provider_marks_usage_window_exhaustion(tmp_path):
    provider = CodexCLIProvider(_config(tmp_path, _fake_limit_codex(tmp_path)))
    result = provider.invoke(
        system="system",
        messages=[{"role": "user", "content": "test"}],
        max_tokens=100,
    )
    assert result.error is not None
    assert result.error["usage_limit"] is True
    assert result.error["type"] == "provider-usage-limit"
    assert result.context_id == "thread-limit"
