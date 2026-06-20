from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from .config import RunConfig
from .fixtures import Fixture
from .packets import build_packet
from .prompts import operator_system, packet_message
from .provider import Provider, ProviderResult, UsageWindowExhausted, total_input_tokens
from .schemas import OPERATOR_TO_KIND, SchemaRegistry
from .seeding import prepare_public_initial_state
from .selector import infer_explicit_request, select
from .state import StateStore, finalize_hash, object_ref, seed_ledger
from .storage import AttemptWriter
from .util import sha256_object, sha256_text, utc_now
from .validation import semantic_validate_operator


def _usage(result: ProviderResult) -> dict[str, int]:
    usage = result.usage or {}
    return {
        "input_tokens": total_input_tokens(usage, result.preflight_input_tokens),
        "cached_input_tokens": int(usage.get("cached_input_tokens", usage.get("cache_read_input_tokens", 0)) or 0),
        "output_tokens": int(usage.get("output_tokens", 0) or 0),
        "reasoning_output_tokens": int(usage.get("reasoning_output_tokens", 0) or 0),
        "cache_creation_input_tokens": int(usage.get("cache_creation_input_tokens", 0) or 0),
        "cache_read_input_tokens": int(usage.get("cache_read_input_tokens", 0) or 0),
    }


def _operator_failure_source(operator: str, *, structural: bool = False, semantic_errors: list[str] | None = None) -> str:
    if structural:
        return "state-schema-or-reference"
    semantic_errors = semantic_errors or []
    if operator == "O1":
        return "operator-O1-requiredness"
    if operator == "O2":
        return "operator-O2-derivation-or-independence"
    if operator == "O3":
        return "operator-O3-impact-boundary" if any("MCP-E42" in e for e in semantic_errors) else "operator-O3-coverage"
    if operator == "O4":
        return "operator-O4-decision-or-stop"
    return "runtime/model-variance"


def _context_messages(operator: str, packet: dict[str, Any], fixture: Fixture, condition: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    immediate = packet_message(packet)
    messages: list[dict[str, Any]] = []
    prior_asset_exposure = False
    if operator == "O2" and condition == "PB" and fixture.asset:
        prior_asset_exposure = True
        messages.extend([
            {
                "role": "user",
                "content": "Prior broader-context asset exposure for the packet-boundary condition. Do not answer yet.\n\n" + fixture.asset,
            },
            {
                "role": "assistant",
                "content": "Context received. I will apply only the next operator packet as the immediate O2 input.",
            },
        ])
    messages.append({"role": "user", "content": immediate})
    transcript_content = "\n".join(str(m.get("content", "")) for m in messages)
    asset_present = bool(fixture.asset and fixture.asset in transcript_content)
    immediate_has_asset = bool(fixture.asset and fixture.asset in immediate)
    proof = {
        "condition": condition,
        "operator": operator,
        "prior_asset_exposure_required": operator == "O2" and condition == "PB",
        "prior_asset_exposure_observed": prior_asset_exposure,
        "asset_text_present_anywhere": asset_present,
        "asset_text_present_in_immediate_packet": immediate_has_asset,
        "transcript_hash": sha256_object(messages),
        "valid": True,
    }
    if operator == "O2" and condition == "SC" and asset_present:
        proof["valid"] = False
        proof["error"] = "Separate-context O2 transcript contains asset text"
    if operator == "O2" and condition == "PB" and (not asset_present or immediate_has_asset):
        proof["valid"] = False
        proof["error"] = "Packet-boundary condition must show prior exposure and an asset-free immediate packet"
    return messages, proof


def _apply_envelope(
    state: dict[str, Any], expected: dict[str, Any], operator: str, ledger_ref: dict[str, Any],
    public: dict[str, Any],
) -> dict[str, Any]:
    obj = copy.deepcopy(state)
    meta = obj["meta"]
    meta.update({
        "object_id": expected["object_id"],
        "object_kind": OPERATOR_TO_KIND[operator],
        "schema_version": "mcp-0.1",
        "revision": expected["revision"],
        "branch_id": expected["branch_id"],
        "producer": operator,
        "projection": expected["projection"],
        "freshness": "current",
    })
    meta.setdefault("status", "committed")
    meta.setdefault("created_at", utc_now())
    # The transport layer owns exact packet ancestry; substantive fields remain model-owned.
    parents = [p for p in expected["parent_refs"] if p["object_kind"] != "EvidenceLedger"] + [ledger_ref]
    meta["parent_refs"] = parents
    meta.setdefault("evidence_refs", [])
    meta.setdefault("conflict_refs", [])
    if operator == "O2":
        boundary = obj.setdefault("derivation_boundary", {})
        boundary.update({
            "condition": expected["independence_condition"],
            "input_packet_hash": expected["packet_hash"],
            "permitted_input_types": ["goal-contract", "goal-evidence", "constraint-evidence"],
            "forbidden_input_types": [
                "asset-decomposition", "asset-section-labels", "coverage-judgments", "proposed-edits"
            ],
            "asset_seen_in_current_context": expected["asset_seen_in_current_context"],
        })
        boundary.setdefault("asset_component_terms_used", [])
    if OPERATOR_TO_KIND[operator] == "CoverageMap":
        obj["evidence_ledger_ref"] = ledger_ref
        asset_text = str(public.get("asset") or "")
        asset_version = str(public.get("asset_version") or "asset")
        obj["asset_ref"] = {
            "asset_id": asset_version,
            "version": asset_version,
            "content_hash": sha256_text(asset_text),
        }
    meta["content_hash"] = "0" * 64
    return finalize_hash(obj)


def _run_step(
    *, config: RunConfig, fixture: Fixture, condition: str, branch: str, operator: str,
    selection_record: dict[str, Any], store: StateStore, provider: Provider,
    schemas: SchemaRegistry, writer: AttemptWriter, step_number: int,
) -> tuple[bool, dict[str, Any] | None, dict[str, Any]]:
    packet, expected = build_packet(
        run_id=config.run_series_id,
        operator=operator,
        store=store,
        public=fixture.public,
        selection=selection_record["selection_obj"],
        condition=condition,
        branch=branch,
    )
    messages, proof = _context_messages(operator, packet, fixture, condition)
    step_dir = f"steps/{step_number:02d}_{operator}_{branch}"
    writer.write_json(f"{step_dir}/execution_packet.json", packet)
    writer.write_json(f"{step_dir}/context_proof.json", proof)
    if not proof["valid"]:
        writer.write_json(f"{step_dir}/failure.json", {"type": "context-isolation", "proof": proof})
        return False, None, {"wall_latency_ms": 0, "model_latency_ms": 0, "input_tokens": 0, "output_tokens": 0, "failure_source": "operator-O2-derivation-or-independence"}
    output_schema = schemas.operator_output_schema(operator, expected)
    result = provider.invoke(
        system=operator_system(config.authority_dir, operator, str(config.provider.get("prompt_cache_ttl", "1h"))),
        messages=messages,
        max_tokens=int(config.provider.get("max_tokens_operator", 64000)),
        output_schema=output_schema,
        preflight=bool(config.capture.get("preflight_token_count", True)),
    )
    writer.write_json(f"{step_dir}/raw_request.json", result.request)
    writer.write_json(f"{step_dir}/raw_response.json", result.response or {"error": result.error})
    writer.write_json(f"{step_dir}/provider_metrics.json", {
        **_usage(result),
        "wall_latency_ms": result.wall_latency_ms,
        "model_latency_ms": result.model_latency_ms,
        "latency_scope": "client-wall-clock; server/model latency unavailable",
        "context_id": result.context_id,
        "started_at": result.started_at,
        "ended_at": result.ended_at,
        "error": result.error,
    })
    if result.error and result.error.get("usage_limit"):
        raise UsageWindowExhausted(result.error.get("message", "Codex usage window exhausted"), result)
    if result.error or not result.parsed_json:
        failure_source = "platform-packaging" if result.error and result.error.get("usage_limit") else "runtime/model-variance"
        return False, None, {**_usage(result), "wall_latency_ms": result.wall_latency_ms, "model_latency_ms": result.model_latency_ms, "failure_source": failure_source, "provider_usage_limit": bool(result.error and result.error.get("usage_limit"))}
    payload = result.parsed_json
    writer.write_json(f"{step_dir}/parsed_operator_output.json", payload)
    entries = payload.get("ledger_append_delta", [])
    try:
        # Evidence write authority and stage ceilings are deterministic contract checks.
        if operator == "O4" and entries:
            raise ValueError("MCP-E620_O4_EVIDENCE_APPEND_PROHIBITED")
        stages = ["design-time", "simulated", "live-runtime", "post-implementation", "production-observed"]
        available_stage = str(fixture.public.get("evidence_stage", "design-time"))
        for entry in entries:
            if entry.get("recorded_by") != operator:
                raise ValueError(
                    f"MCP-E031_EVIDENCE_WRITE_AUTHORITY: {entry.get('evidence_id')} recorded_by={entry.get('recorded_by')} operator={operator}"
                )
            if stages.index(str(entry.get("stage", "design-time"))) > stages.index(available_stage):
                raise ValueError(f"MCP-E610_EVIDENCE_PROMOTION: {entry.get('evidence_id')}")
        # State + evidence commit is atomic. A malformed state must not pollute the shared ledger.
        trial = StateStore(
            schema=store.schema,
            attempt_id=store.attempt_id,
            projection=store.projection,
            objects=copy.deepcopy(store.objects),
            incoming_invalid=copy.deepcopy(store.incoming_invalid),
        )
        ledger = trial.append_evidence(entries, operator) if entries else trial.ledger()
        state = _apply_envelope(payload["state_object"], expected, operator, object_ref(ledger), fixture.public)
        structural = schemas.validate_state(state, OPERATOR_TO_KIND[operator])
        semantic = semantic_validate_operator(operator, state, trial, fixture.public)
        model_errors = payload.get("validation", {}).get("errors", [])
        validation = {
            "model_status": payload.get("validation", {}).get("status"),
            "model_errors": model_errors,
            "structural_errors": structural,
            "semantic_errors": semantic,
            "valid": not structural and not semantic,
        }
        writer.write_json(f"{step_dir}/local_validation.json", validation)
        if structural or semantic:
            source = _operator_failure_source(operator, structural=bool(structural), semantic_errors=semantic)
            return False, None, {**_usage(result), "wall_latency_ms": result.wall_latency_ms, "model_latency_ms": result.model_latency_ms, "failure_source": source}
        trial.add(state, validate=False)
        store.objects = trial.objects
        store.incoming_invalid = trial.incoming_invalid
        writer.write_json(f"{step_dir}/committed_state.json", state)
        if entries:
            writer.write_json(f"{step_dir}/ledger_after_append.json", ledger)
        return True, payload, {**_usage(result), "wall_latency_ms": result.wall_latency_ms, "model_latency_ms": result.model_latency_ms}
    except Exception as exc:
        writer.write_json(f"{step_dir}/commit_failure.json", {"type": type(exc).__name__, "message": str(exc)})
        return False, None, {**_usage(result), "wall_latency_ms": result.wall_latency_ms, "model_latency_ms": result.model_latency_ms, "failure_source": "state-schema-or-reference"}


def run_operator_attempt(
    config: RunConfig, fixture: Fixture, condition: str, replicate: int,
    provider: Provider, schemas: SchemaRegistry,
    *, attempt_id_override: str | None = None, recovery_of: str | None = None,
) -> dict[str, Any]:
    attempt_id = attempt_id_override or f"{config.run_series_id}__{fixture.cell_id}__{condition}__r{replicate}__operator"
    writer = AttemptWriter(config.run_root, attempt_id)
    if writer.is_complete() and config.execution.get("resume_completed", True):
        return json.loads((writer.path / "attempt_summary.json").read_text(encoding="utf-8"))
    profile = "compact" if fixture.cell_id in {"C02", "C04", "C11", "HOLDOUT-TRIVIAL-01"} else "material"
    store = StateStore(schema=schemas, attempt_id=attempt_id, projection=profile)
    store.add(seed_ledger(attempt_id, fixture.public, profile))
    preflight = prepare_public_initial_state(store, fixture.public, condition)
    writer.write_json("public_fixture.json", {"cell_id": fixture.cell_id, "title": fixture.title, "executor_view": fixture.public})
    writer.write_json("preflight_state_notes.json", preflight)
    explicit = infer_explicit_request(fixture.public)
    totals = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_output_tokens": 0, "wall_latency_ms": 0, "model_latency_ms": 0}
    contexts: set[str] = set()
    selector_records: list[dict[str, Any]] = []
    for note in preflight.get("notes", []):
        if note.get("type") in {"rejected-state", "incoming-invalid-state"}:
            selector_records.append({
                "selector_result": "rejected-input-state",
                "selected_operator": None,
                "basis": [note.get("description", "Incoming state rejected")],
                "rejected_operators": [{
                    "operator": note.get("kind", "incoming-state"),
                    "code": note.get("code", "MCP-E000_INVALID_INCOMING_STATE"),
                    "reason": note.get("description", "Incoming state rejected"),
                }],
                "input_packet_manifest": {"allowed_refs": [], "forbidden_inputs": []},
                "next_expected_object": None,
                "branch": "main",
            })
    visible_answer = ""
    success = True
    failure_source: str | None = None
    context_reconstruction_tokens = 0
    step = 0

    for i, rec in enumerate(selector_records, 1):
        writer.write_json(f"selector/{i:02d}_preflight.json", rec)

    # Run branch-specific O3 for pre-supplied disagreeing models.
    if store.currents("CapabilityModel") and len(store.currents("CapabilityModel")) > 1:
        for cm in sorted(store.currents("CapabilityModel"), key=lambda x: x["meta"]["branch_id"]):
            branch = cm["meta"]["branch_id"]
            sel = select(store, fixture.public, explicit_request="O3", branch=branch)
            rec = sel.as_dict()
            rec["branch"] = branch
            selector_records.append(rec)
            writer.write_json(f"selector/{len(selector_records):02d}_{branch}.json", rec)
            if sel.selected_operator != "O3":
                failure_source = "selector-legality"
                success = False
                break
            step += 1
            ok, payload, metrics = _run_step(
                config=config, fixture=fixture, condition=condition, branch=branch, operator="O3",
                selection_record={"selection_obj": sel}, store=store, provider=provider, schemas=schemas,
                writer=writer, step_number=step,
            )
            for k in totals:
                totals[k] += int(metrics.get(k, 0) or 0)
            if step > 1:
                context_reconstruction_tokens += int(metrics.get("input_tokens", 0) or 0)
            if not ok:
                failure_source = str(metrics.get("failure_source") or "operator-execution-failure")
                success = False
                break
        if success:
            # O4 compares all live branches in one packet.
            sel = select(store, fixture.public, explicit_request="O4", branch=store.currents("CoverageMap")[0]["meta"]["branch_id"])
            rec = sel.as_dict(); rec["branch"] = "branch-comparison"
            selector_records.append(rec); writer.write_json(f"selector/{len(selector_records):02d}_branch-comparison.json", rec)
            if sel.selected_operator != "O4":
                # Selector's single-branch view can be insufficient; P4 allows O4 when all branch maps are current.
                readiness = {cv["overall_o4_readiness"]["status"] for cv in store.currents("CoverageMap")}
                if readiness <= {"intervention-ready", "block-only"}:
                    from .selector import Selection
                    sel = Selection("selected", "O4", ["all branch CoverageMaps current; branch comparison required"], rec["rejected_operators"], "ChangeDecision")
            step += 1
            ok, payload, metrics = _run_step(
                config=config, fixture=fixture, condition=condition, branch="main", operator="O4",
                selection_record={"selection_obj": sel}, store=store, provider=provider, schemas=schemas,
                writer=writer, step_number=step,
            )
            for k in totals: totals[k] += int(metrics.get(k, 0) or 0)
            if step > 1:
                context_reconstruction_tokens += int(metrics.get("input_tokens", 0) or 0)
            success = ok
            if not ok:
                failure_source = str(metrics.get("failure_source") or "operator-execution-failure")
            if payload:
                visible_answer = payload.get("visible_answer", "")
    else:
        for _ in range(8):
            sel = select(store, fixture.public, explicit_request=explicit if not selector_records else None, branch="main")
            rec = sel.as_dict(); rec["branch"] = "main"
            selector_records.append(rec)
            writer.write_json(f"selector/{len(selector_records):02d}_main.json", rec)
            if sel.selector_result == "terminal":
                break
            if sel.selector_result != "selected" or not sel.selected_operator:
                failure_source = "selector-legality"
                success = False
                break
            step += 1
            ok, payload, metrics = _run_step(
                config=config, fixture=fixture, condition=condition, branch="main", operator=sel.selected_operator,
                selection_record={"selection_obj": sel}, store=store, provider=provider, schemas=schemas,
                writer=writer, step_number=step,
            )
            for k in totals: totals[k] += int(metrics.get(k, 0) or 0)
            if step > 1:
                context_reconstruction_tokens += int(metrics.get("input_tokens", 0) or 0)
            if not ok:
                failure_source = str(metrics.get("failure_source") or "operator-execution-failure")
                success = False
                break
            if payload and sel.selected_operator == "O4":
                visible_answer = payload.get("visible_answer", "")
                break
        else:
            failure_source = "runtime/model-variance"
            success = False

    writer.write_json("all_state_revisions.json", store.snapshots())
    writer.write_json("selector_records.json", selector_records)
    if not visible_answer:
        cd = store.current("ChangeDecision", "main")
        if cd:
            visible_answer = f"Decision: {cd['decision']}\nEvidence ceiling: {cd['evidence_ceiling']}\nStop: {cd['stop_reason']}"
        elif not success:
            visible_answer = "The operator run did not reach a valid terminal ChangeDecision. See retained rejection and validation traces."
    writer.write_text("visible_answer.txt", visible_answer + "\n")
    trace_required = 5
    trace_present = sum([
        bool(selector_records),
        bool(store.currents("GoalContract")),
        bool(store.currents("CapabilityModel")),
        bool(store.currents("CoverageMap")),
        bool(store.currents("ChangeDecision")),
    ])
    summary = {
        "attempt_id": attempt_id,
        "run_series_id": config.run_series_id,
        "cell_id": fixture.cell_id,
        "condition": condition,
        "replicate": replicate,
        "system": "operator",
        "status": "completed" if success else "failed",
        "first_pass_success": success if recovery_of is None else False,
        "recovered_success": success if recovery_of is not None else None,
        "recovery_of": recovery_of,
        "failure_source": failure_source,
        **{k: v for k, v in totals.items() if k != "model_latency_ms"},
        "model_latency_ms": None,
        "latency_scope": "client-wall-clock; server/model latency unavailable",
        "total_tokens": totals["input_tokens"] + totals["output_tokens"],
        "handoff_count": max(0, step - 1),
        "context_count": step,
        "clarification_count": 0,
        "manual_intervention_count": 0,
        "state_repair_count": 0,
        "recovery_attempts": 1 if recovery_of else 0,
        "recovery_tokens": (totals["input_tokens"] + totals["output_tokens"]) if recovery_of else 0,
        "recovery_latency_ms": totals["wall_latency_ms"] if recovery_of else 0,
        "context_reconstruction_tokens": context_reconstruction_tokens,
        "trace_required_count": trace_required,
        "trace_present_count": trace_present,
        "trace_completeness": trace_present / trace_required,
        "visible_answer_file": "visible_answer.txt",
        "completed_at": utc_now(),
    }
    writer.complete(summary)
    return summary
