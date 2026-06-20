from __future__ import annotations

import json
import uuid
from typing import Any

from .config import RunConfig
from .fixtures import Fixture
from .prompts import fixture_text, legacy_system
from .provider import Provider, ProviderResult, UsageWindowExhausted, total_input_tokens
from .storage import AttemptWriter
from .util import sha256_object, utc_now


def _metrics(result: ProviderResult) -> dict[str, int]:
    usage = result.usage or {}
    return {
        "input_tokens": total_input_tokens(usage, result.preflight_input_tokens),
        "cached_input_tokens": int(usage.get("cached_input_tokens", usage.get("cache_read_input_tokens", 0)) or 0),
        "output_tokens": int(usage.get("output_tokens", 0) or 0),
        "reasoning_output_tokens": int(usage.get("reasoning_output_tokens", 0) or 0),
        "wall_latency_ms": result.wall_latency_ms,
        "model_latency_ms": result.model_latency_ms or 0,
    }


def _assistant_content(result: ProviderResult) -> list[dict[str, Any]]:
    if not result.response:
        return [{"type": "text", "text": result.text or ""}]
    content = result.response.get("content", [])
    # Preserve thinking signatures if the provider returned them; omit displayed thinking text unless configured.
    return content or [{"type": "text", "text": result.text or ""}]


def run_legacy_attempt(
    config: RunConfig, fixture: Fixture, condition: str, replicate: int,
    provider: Provider,
    *, attempt_id_override: str | None = None, recovery_of: str | None = None,
) -> dict[str, Any]:
    attempt_id = attempt_id_override or f"{config.run_series_id}__{fixture.cell_id}__{condition}__r{replicate}__legacy"
    writer = AttemptWriter(config.run_root, attempt_id)
    if writer.is_complete() and config.execution.get("resume_completed", True):
        return json.loads((writer.path / "attempt_summary.json").read_text(encoding="utf-8"))
    writer.write_json("public_fixture.json", {"cell_id": fixture.cell_id, "title": fixture.title, "executor_view": fixture.public})
    system = legacy_system(config.authority_dir, str(config.provider.get("prompt_cache_ttl", "1h")))
    max_tokens = int(config.provider.get("max_tokens_legacy", 64000))
    preflight = bool(config.capture.get("preflight_token_count", True))
    results: list[ProviderResult] = []
    context_ids: list[str] = []
    visible_parts: list[str] = []
    failure_source: str | None = None
    context_reconstruction_tokens = 0

    if condition == "SC" and fixture.asset:
        context_id = f"ctx-legacy-sc-{uuid.uuid4()}"
        first_prompt = (
            "Separate-context condition. The asset has not been supplied. Using only the goal, constraints, and unchanged legacy procedure, "
            "produce the complete path/goal basis and independent required capability model, then emit the required independence seal. "
            "Stop immediately after the seal; do not speculate about asset coverage.\n\n" + fixture_text(fixture.public, include_asset=False)
        )
        first_messages = [{"role": "user", "content": first_prompt}]
        proof1 = {
            "condition": "SC",
            "phase": "pre-asset",
            "context_id": context_id,
            "asset_text_present": bool(fixture.asset and fixture.asset in "\n".join(str(m.get("content", "")) for m in first_messages)),
            "transcript_hash": sha256_object(first_messages),
        }
        proof1["valid"] = not proof1["asset_text_present"]
        writer.write_json("contexts/01_pre_asset_proof.json", proof1)
        if not proof1["valid"]:
            result1 = None
        else:
            result1 = provider.invoke(system=system, messages=first_messages, max_tokens=max_tokens, context_id=context_id, preflight=preflight)
            if result1.error and result1.error.get("usage_limit"):
                raise UsageWindowExhausted(result1.error.get("message", "Codex usage window exhausted"), result1)
        if result1 is None or result1.error:
            if result1:
                writer.write_json("calls/01_raw_request.json", result1.request)
                writer.write_json("calls/01_raw_response.json", result1.response or {"error": result1.error})
                results.append(result1)
            success = False
            failure_source = "runtime/model-variance" if result1 and result1.error else "platform-packaging"
        else:
            results.append(result1); context_ids.append(context_id); visible_parts.append(result1.text or "")
            writer.write_json("calls/01_raw_request.json", result1.request)
            writer.write_json("calls/01_raw_response.json", result1.response)
            second_prompt = (
                "Continue the same unchanged legacy assessment after the seal. The asset is now supplied. Complete asset mapping, coverage, "
                "gap/sufficiency, action/fix layer, evidence limitation, verification, complexity, and terminal stop. Do not revise the already sealed "
                "capability model merely to match the asset.\n\nASSET VERSION: " + str(fixture.asset_version) + "\n\nASSET:\n" + fixture.asset
            )
            second_messages = first_messages + [
                {"role": "assistant", "content": _assistant_content(result1)},
                {"role": "user", "content": second_prompt},
            ]
            proof2 = {
                "condition": "SC", "phase": "post-seal-asset-release", "context_id": context_id,
                "asset_text_present": fixture.asset in "\n".join(str(m.get("content", "")) for m in second_messages),
                "transcript_hash": sha256_object(second_messages), "valid": True,
            }
            writer.write_json("contexts/02_post_asset_proof.json", proof2)
            result2 = provider.invoke(system=system, messages=second_messages, max_tokens=max_tokens, context_id=context_id, preflight=preflight)
            if result2.error and result2.error.get("usage_limit"):
                raise UsageWindowExhausted(result2.error.get("message", "Codex usage window exhausted"), result2)
            results.append(result2)
            writer.write_json("calls/02_raw_request.json", result2.request)
            writer.write_json("calls/02_raw_response.json", result2.response or {"error": result2.error})
            if result2.error:
                failure_source = "runtime/model-variance"
                success = False
            else:
                visible_parts.append(result2.text or "")
                success = True
    else:
        context_id = f"ctx-legacy-{condition.lower()}-{uuid.uuid4()}"
        if condition == "PB" and fixture.asset:
            messages = [
                {"role": "user", "content": "Prior broader-context asset exposure for the packet-boundary condition. Do not assess yet.\n\n" + fixture.asset},
                {"role": "assistant", "content": "Context received. I will follow the next instruction."},
                {
                    "role": "user",
                    "content": (
                        "Execute the unchanged Goal-Completeness procedure to terminal. For the goal and independent capability derivation portion, "
                        "use only the goal/constraint packet below even though the broader context has previously seen the asset. Do not call this full "
                        "cognitive independence. After the required seal, assess the previously supplied asset.\n\n" + fixture_text(fixture.public, include_asset=False)
                    ),
                },
            ]
            immediate_has_asset = fixture.asset in str(messages[-1]["content"])
            proof = {
                "condition": "PB", "context_id": context_id,
                "prior_asset_exposure_observed": fixture.asset in str(messages[0]["content"]),
                "asset_text_present_in_immediate_packet": immediate_has_asset,
                "transcript_hash": sha256_object(messages),
            }
            proof["valid"] = proof["prior_asset_exposure_observed"] and not immediate_has_asset
        else:
            messages = [{
                "role": "user",
                "content": "Execute the unchanged Goal-Completeness procedure faithfully and return the complete assessment.\n\n" + fixture_text(fixture.public, include_asset=True),
            }]
            proof = {"condition": "standard", "context_id": context_id, "transcript_hash": sha256_object(messages), "valid": True}
        writer.write_json("contexts/01_context_proof.json", proof)
        if not proof["valid"]:
            success = False
            failure_source = "platform-packaging"
        else:
            result = provider.invoke(system=system, messages=messages, max_tokens=max_tokens, context_id=context_id, preflight=preflight)
            if result.error and result.error.get("usage_limit"):
                raise UsageWindowExhausted(result.error.get("message", "Codex usage window exhausted"), result)
            results.append(result); context_ids.append(context_id)
            writer.write_json("calls/01_raw_request.json", result.request)
            writer.write_json("calls/01_raw_response.json", result.response or {"error": result.error})
            success = result.error is None
            if result.error:
                failure_source = "runtime/model-variance"
            if result.text:
                visible_parts.append(result.text)

    visible_answer = "\n\n--- CONTINUATION AFTER ASSET RELEASE ---\n\n".join(visible_parts)
    if not visible_answer:
        visible_answer = "The legacy control did not produce a complete first-pass output. See retained API/context records."
    writer.write_text("visible_answer.txt", visible_answer + "\n")
    totals = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_output_tokens": 0, "wall_latency_ms": 0, "model_latency_ms": 0}
    for idx, result in enumerate(results):
        m = _metrics(result)
        for k in totals:
            totals[k] += int(m.get(k, 0) or 0)
        if idx > 0:
            context_reconstruction_tokens += int(m.get("input_tokens", 0) or 0)
    trace_markers = [
        "Scaling gate", "Goal", "Capability", "coverage", "Evidence", "No material change", "verification", "reject",
    ]
    marker_count = sum(1 for m in trace_markers if m.lower() in visible_answer.lower())
    trace_completeness = min(1.0, marker_count / 6)
    summary = {
        "attempt_id": attempt_id,
        "run_series_id": config.run_series_id,
        "cell_id": fixture.cell_id,
        "condition": condition,
        "replicate": replicate,
        "system": "legacy",
        "status": "completed" if success else "failed",
        "first_pass_success": success if recovery_of is None else False,
        "recovered_success": success if recovery_of is not None else None,
        "recovery_of": recovery_of,
        "failure_source": failure_source,
        **{k: v for k, v in totals.items() if k != "model_latency_ms"},
        "model_latency_ms": None,
        "latency_scope": "client-wall-clock; server/model latency unavailable",
        "total_tokens": totals["input_tokens"] + totals["output_tokens"],
        "handoff_count": 1 if condition == "SC" and fixture.asset else 0,
        "context_count": len(set(context_ids)) or len(results),
        "clarification_count": 0,
        "manual_intervention_count": 0,
        "state_repair_count": 0,
        "recovery_attempts": 1 if recovery_of else 0,
        "recovery_tokens": (totals["input_tokens"] + totals["output_tokens"]) if recovery_of else 0,
        "recovery_latency_ms": totals["wall_latency_ms"] if recovery_of else 0,
        "context_reconstruction_tokens": context_reconstruction_tokens,
        "trace_required_count": 6,
        "trace_present_count": min(marker_count, 6),
        "trace_completeness": trace_completeness,
        "visible_answer_file": "visible_answer.txt",
        "completed_at": utc_now(),
    }
    writer.complete(summary)
    return summary
