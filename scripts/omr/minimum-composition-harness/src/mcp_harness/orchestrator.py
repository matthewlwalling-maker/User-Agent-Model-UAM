from __future__ import annotations

import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from .blinding import load_or_create_key
from .config import RunConfig
from .exporter import build_evaluator_packets
from .fixtures import Fixture, iter_cells, load_all_fixtures
from .legacy_runner import run_legacy_attempt
from .operator_runner import run_operator_attempt
from .provider import UsageWindowExhausted, build_provider
from .schemas import SchemaRegistry, count_optional_properties
from .sources import verify_sources
from .storage import append_execution_index, append_manual_intervention
from .util import atomic_write_json, atomic_write_text, read_json, sha256_file, utc_now


def _codex_local_check(config: RunConfig, require_auth: bool) -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []
    binary_name = str(config.provider.get("binary", "codex"))
    binary = shutil.which(binary_name)
    result: dict[str, Any] = {"binary_requested": binary_name, "binary_resolved": binary}
    if not binary:
        errors.append(f"Codex CLI executable not found: {binary_name}")
        return result, errors
    try:
        version = subprocess.run([binary, "--version"], text=True, capture_output=True, timeout=30, check=False)
        result["version_returncode"] = version.returncode
        result["version"] = (version.stdout or version.stderr).strip()
        if version.returncode != 0:
            errors.append("Codex CLI version check failed")
    except Exception as exc:
        errors.append(f"Codex CLI version check failed: {type(exc).__name__}: {exc}")
    try:
        auth = subprocess.run([binary, "login", "status"], text=True, capture_output=True, timeout=30, check=False)
        result["auth_returncode"] = auth.returncode
        result["auth_status"] = (auth.stdout or auth.stderr).strip()
        result["authenticated"] = auth.returncode == 0
        if require_auth and auth.returncode != 0:
            errors.append("Codex CLI is not authenticated; `codex login status` returned non-zero")
    except Exception as exc:
        result["authenticated"] = False
        if require_auth:
            errors.append(f"Codex authentication check failed: {type(exc).__name__}: {exc}")
    return result, errors


def doctor(config: RunConfig, *, require_provider_auth: bool = False) -> dict[str, Any]:
    source_check = verify_sources(config.authority_dir, config.fixture_view)
    errors = list(source_check.errors)
    codex_check, codex_errors = _codex_local_check(config, require_provider_auth)
    errors.extend(codex_errors)
    try:
        fixtures = load_all_fixtures(config)
    except Exception as exc:
        fixtures = []
        errors.append(f"Fixture/holdout load failed: {type(exc).__name__}: {exc}")
    schema_stats: dict[str, Any] = {}
    try:
        schemas = SchemaRegistry(config.authority_dir / "P2_State_Schemas_v0.1.json")
        dummy = {
            "object_id": "doctor", "revision": 1, "branch_id": "main", "projection": "material",
            "packet_hash": "0" * 64, "independence_condition": "separate-context",
            "asset_seen_in_current_context": False, "parent_refs": [],
        }
        for operator in ("O1", "O2", "O3", "O4"):
            transport = schemas.operator_output_schema(operator, dummy)
            encoded = json.dumps(transport, sort_keys=True)
            schema_stats[operator] = {
                "bytes": len(encoded.encode("utf-8")),
                "optional_properties": count_optional_properties(transport),
                "contains_local_refs": '"$ref"' in encoded or '"$defs"' in encoded,
                "contains_conditionals": any(token in encoded for token in ('"allOf"', '"if"', '"then"')),
            }
            if schema_stats[operator]["optional_properties"] != 0:
                errors.append(f"{operator} CLI output schema contains optional properties")
            if schema_stats[operator]["contains_local_refs"] or schema_stats[operator]["contains_conditionals"]:
                errors.append(f"{operator} CLI output schema contains unsupported/deferred constructs")
    except Exception as exc:
        errors.append(f"Transport schema construction failed: {type(exc).__name__}: {exc}")

    return {
        "ok": not errors,
        "run_series_id": config.run_series_id,
        "status": config.status,
        "authority_dir": str(config.authority_dir),
        "fixture_view": str(config.fixture_view),
        "source_records": source_check.records,
        "fixture_count": len(fixtures),
        "provider": "codex_cli",
        "codex_check": codex_check,
        "operator_transport_schema_stats": schema_stats,
        "errors": errors,
    }


def _all_attempts(config: RunConfig, fixtures: list[Fixture]) -> list[dict[str, Any]]:
    attempts: list[dict[str, Any]] = []
    for fixture, condition, replicate in iter_cells(fixtures, config):
        for system in ("operator", "legacy"):
            attempt_id = f"{config.run_series_id}__{fixture.cell_id}__{condition}__r{replicate}__{system}"
            complete = (config.run_root / "attempts" / attempt_id / "attempt_summary.json").exists()
            attempts.append({
                "cell_id": fixture.cell_id,
                "condition": condition,
                "replicate": replicate,
                "system": system,
                "attempt_id": attempt_id,
                "already_complete": complete,
            })
    return attempts


def plan(config: RunConfig) -> dict[str, Any]:
    fixtures = load_all_fixtures(config)
    cells = list(iter_cells(fixtures, config))
    attempts = _all_attempts(config, fixtures)
    completed = sum(1 for x in attempts if x["already_complete"])
    return {
        "run_series_id": config.run_series_id,
        "fixture_cells": len(fixtures),
        "condition_replicate_cells": len(cells),
        "system_attempts": len(attempts),
        "completed_attempts": completed,
        "remaining_attempts": len(attempts) - completed,
        "estimated_model_calls": {
            "operator_min": len(cells) * 4,
            "legacy_min": len(cells),
            "note": "Seeded-state cases may use fewer operator calls; SC legacy cells use two calls.",
        },
        "attempts": attempts,
    }


def initialize_run(config: RunConfig, fixtures: list[Fixture], doctor_report: dict[str, Any]) -> dict[str, Any]:
    config.run_root.mkdir(parents=True, exist_ok=True)
    (config.run_root / "private").mkdir(exist_ok=True)
    source_check = verify_sources(config.authority_dir, config.fixture_view)
    if not source_check.ok:
        raise RuntimeError("Source validation failed: " + "; ".join(source_check.errors))
    manifest_path = config.run_root / "Run_Manifest.json"
    config_sha = sha256_file(config.path)
    if manifest_path.exists():
        existing = read_json(manifest_path)
        if existing.get("config_sha256") != config_sha:
            raise RuntimeError("Frozen run configuration changed after the run series started")
        if existing.get("source_records") != source_check.records:
            raise RuntimeError("Frozen source records changed after the run series started")
        frozen_codex = existing.get("codex_check") or {}
        current_codex = doctor_report.get("codex_check") or {}
        for field in ("binary_resolved", "version"):
            if frozen_codex.get(field) != current_codex.get(field):
                raise RuntimeError(
                    f"Codex runtime changed after the run series started: {field} "
                    f"was {frozen_codex.get(field)!r}, now {current_codex.get(field)!r}. "
                    "Start a new run series rather than mixing runtimes."
                )
        return existing
    manifest = {
        "run_series_id": config.run_series_id,
        "created_at": utc_now(),
        "status": config.status,
        "harness_version": "0.2.0-codex-cli",
        "python": sys.version,
        "platform": platform.platform(),
        "provider": {k: v for k, v in config.provider.items() if "key" not in k.lower()},
        "codex_check": doctor_report.get("codex_check"),
        "execution": config.execution,
        "blinding": {k: v for k, v in config.blinding.items() if k != "seed"},
        "fixture_view_sha256": sha256_file(config.fixture_view),
        "source_records": source_check.records,
        "config_path": str(config.path),
        "config_sha256": config_sha,
    }
    atomic_write_json(manifest_path, manifest)
    atomic_write_json(config.run_root / "Source_and_Digest_Record.json", source_check.records)
    manual_log = config.run_root / "Manual_Intervention_Log.jsonl"
    if not manual_log.exists():
        atomic_write_text(manual_log, "")
    atomic_write_json(config.run_root / "Public_Fixture_Index.json", [
        {"cell_id": f.cell_id, "case_id": f.case_id, "title": f.title} for f in fixtures
    ])
    return manifest


def _write_completion(config: RunConfig, completion: dict[str, Any], pause: dict[str, Any] | None = None) -> None:
    report = dict(completion)
    report["pause"] = pause
    atomic_write_json(config.run_root / "Run_Completeness_Report.json", report)
    lines = [
        f"# Run Completeness Report — {config.run_series_id}", "",
        f"- Complete: **{completion['complete']}**",
        f"- Expected attempts: {completion['expected_attempts']}",
        f"- Present attempts: {completion['present_attempts']}",
        f"- Failed system attempts retained as evidence: {completion['failed_attempts']}",
        f"- Invalid/missing comparative cells: {len(completion['invalid_cells'])}",
        f"- Paused for usage window: **{bool(pause)}**",
    ]
    if pause:
        lines.extend([f"- Pause occurred before/inside attempt: `{pause.get('attempt_id')}`", "- Resume by rerunning the same frozen config after Codex usage resets or credits are added."])
    lines.extend(["", "## Invalid cells", ""])
    lines.extend([f"- {x}" for x in completion["invalid_cells"]])
    atomic_write_text(config.run_root / "Run_Completeness_Report.md", "\n".join(lines) + "\n")


def run(config: RunConfig, *, cases: set[str] | None = None) -> dict[str, Any]:
    doctor_report = doctor(config, require_provider_auth=True)
    if not doctor_report["ok"]:
        raise RuntimeError("Doctor failed: " + "; ".join(doctor_report["errors"]))
    all_fixtures = load_all_fixtures(config)
    execution_fixtures = all_fixtures
    if cases:
        execution_fixtures = [f for f in all_fixtures if f.cell_id in cases or f.case_id in cases]
        if not execution_fixtures:
            raise ValueError(f"No configured fixtures match --cases {sorted(cases)}")
    initialize_run(config, all_fixtures, doctor_report)
    all_cells = list(iter_cells(all_fixtures, config))
    key_cells = [(f.cell_id, condition, replicate) for f, condition, replicate in all_cells]
    system_key = load_or_create_key(
        config.run_root / "private" / "system_key.json", key_cells, int(config.blinding.get("seed", 1))
    )
    provider = build_provider(config)
    schemas = SchemaRegistry(config.authority_dir / "P2_State_Schemas_v0.1.json")
    summaries: list[dict[str, Any]] = []
    pause: dict[str, Any] | None = None

    try:
        for fixture, condition, replicate in iter_cells(execution_fixtures, config):
            operator_id = f"{config.run_series_id}__{fixture.cell_id}__{condition}__r{replicate}__operator"
            operator = run_operator_attempt(config, fixture, condition, replicate, provider, schemas)
            append_execution_index(config.run_root, operator)
            summaries.append(operator)

            legacy_id = f"{config.run_series_id}__{fixture.cell_id}__{condition}__r{replicate}__legacy"
            legacy = run_legacy_attempt(config, fixture, condition, replicate, provider)
            append_execution_index(config.run_root, legacy)
            summaries.append(legacy)
    except UsageWindowExhausted as exc:
        active_id = locals().get("legacy_id") if 'legacy_id' in locals() and not (config.run_root / "attempts" / locals().get("legacy_id", "") / "attempt_summary.json").exists() else locals().get("operator_id")
        pause = {
            "type": "provider-usage-window",
            "attempt_id": active_id,
            "message": str(exc),
            "recorded_at": utc_now(),
            "provider_context_id": exc.result.context_id,
        }
        atomic_write_json(config.run_root / f"Run_Pause_Record_{utc_now().replace(':','').replace('-','')}.json", pause)
        append_manual_intervention(config.run_root, {
            "attempt_id": active_id,
            "trigger": "provider-usage-window",
            "actor": "platform",
            "change": "Run paused automatically; frozen config, prompts, sources, and completed attempts were not changed.",
            "reason": str(exc),
            "affected_attempt": active_id,
            "whether_behavioral_scoring_contaminated": False,
            "before_ref": active_id,
            "after_ref": None,
        })

    completion = validate_run(config, fixtures=all_fixtures)
    packets: dict[str, Path] = {}
    if completion["complete"]:
        packets = build_evaluator_packets(config, all_fixtures, system_key)
    _write_completion(config, completion, pause)
    return {
        "summaries": summaries,
        "packets": {k: str(v) for k, v in packets.items()},
        "completion": completion,
        "pause": pause,
    }


def validate_run(config: RunConfig, fixtures: list[Fixture] | None = None) -> dict[str, Any]:
    fixtures = fixtures or load_all_fixtures(config)
    cells = list(iter_cells(fixtures, config))
    expected: list[str] = []
    invalid: list[str] = []
    failed = 0
    present = 0
    for fixture, condition, replicate in cells:
        for system in ("operator", "legacy"):
            attempt_id = f"{config.run_series_id}__{fixture.cell_id}__{condition}__r{replicate}__{system}"
            expected.append(attempt_id)
            summary_path = config.run_root / "attempts" / attempt_id / "attempt_summary.json"
            visible_path = config.run_root / "attempts" / attempt_id / "visible_answer.txt"
            if not summary_path.exists() or not visible_path.exists():
                invalid.append(f"{attempt_id}: missing summary or visible output")
                continue
            present += 1
            summary = read_json(summary_path)
            if summary.get("status") == "failed":
                failed += 1
            if not (config.run_root / "attempts" / attempt_id / "public_fixture.json").exists():
                invalid.append(f"{attempt_id}: missing public fixture capture")
            if system == "operator" and not (config.run_root / "attempts" / attempt_id / "selector_records.json").exists():
                invalid.append(f"{attempt_id}: missing selector records")
    complete = not invalid and present == len(expected)
    return {
        "complete": complete,
        "expected_attempts": len(expected),
        "present_attempts": present,
        "remaining_attempts": len(expected) - present,
        "failed_attempts": failed,
        "invalid_cells": invalid,
        "checked_at": utc_now(),
    }


def usage_summary(config: RunConfig) -> dict[str, Any]:
    attempts_dir = config.run_root / "attempts"
    totals = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_output_tokens": 0}
    attempts = 0
    if attempts_dir.exists():
        for path in attempts_dir.glob("*/attempt_summary.json"):
            data = read_json(path)
            attempts += 1
            for key in totals:
                totals[key] += int(data.get(key, 0) or 0)
    uncached = max(0, totals["input_tokens"] - totals["cached_input_tokens"])
    estimated_credits = (
        uncached * 125 / 1_000_000
        + totals["cached_input_tokens"] * 12.5 / 1_000_000
        + totals["output_tokens"] * 750 / 1_000_000
    )
    return {
        "run_series_id": config.run_series_id,
        "completed_attempts": attempts,
        **totals,
        "uncached_input_tokens": uncached,
        "estimated_credits_at_2026_06_gpt_5_5_rate_card": round(estimated_credits, 3),
        "note": "Estimate only. Codex plan inclusion, account-specific limits, promotions, and rate-card changes are not inferred by the harness.",
    }


def recover_attempt(config: RunConfig, attempt_id: str, *, note: str) -> dict[str, Any]:
    """Run a separately retained recovery attempt; never overwrites or upgrades first-pass evidence."""
    original_path = config.run_root / "attempts" / attempt_id / "attempt_summary.json"
    if not original_path.exists():
        raise FileNotFoundError(f"Original attempt summary not found: {attempt_id}")
    original = read_json(original_path)
    if original.get("status") != "failed":
        raise ValueError("Recovery is allowed only for a retained failed attempt")
    fixtures = {f.cell_id: f for f in load_all_fixtures(config)}
    cell_id = str(original["cell_id"])
    if cell_id not in fixtures:
        raise ValueError(f"Fixture not found for recovery: {cell_id}")
    base = attempt_id
    existing = list((config.run_root / "attempts").glob(base + "__recovery*"))
    recovery_id = f"{base}__recovery{len(existing)+1:02d}"
    provider = build_provider(config)
    fixture = fixtures[cell_id]
    system = str(original["system"])
    if system == "operator":
        schemas = SchemaRegistry(config.authority_dir / "P2_State_Schemas_v0.1.json")
        result = run_operator_attempt(
            config, fixture, str(original["condition"]), int(original["replicate"]), provider, schemas,
            attempt_id_override=recovery_id, recovery_of=attempt_id,
        )
    elif system == "legacy":
        result = run_legacy_attempt(
            config, fixture, str(original["condition"]), int(original["replicate"]), provider,
            attempt_id_override=recovery_id, recovery_of=attempt_id,
        )
    else:
        raise ValueError(f"Unknown system in attempt summary: {system}")
    result["manual_intervention_count"] = 1
    result["recovery_note"] = note
    atomic_write_json(config.run_root / "attempts" / recovery_id / "attempt_summary.json", result)
    append_manual_intervention(config.run_root, {
        "attempt_id": recovery_id,
        "recovery_of": attempt_id,
        "trigger": "first-pass-failure-recovery",
        "actor": "human",
        "change": f"Created separate recovery attempt {recovery_id}; first-pass artifacts unchanged.",
        "reason": note,
        "affected_attempt": attempt_id,
        "whether_behavioral_scoring_contaminated": True,
        "before_ref": attempt_id,
        "after_ref": recovery_id,
        "tokens_added": result.get("recovery_tokens", 0),
        "latency_added_ms": result.get("recovery_latency_ms", 0),
    })
    append_execution_index(config.run_root, result)
    return result
