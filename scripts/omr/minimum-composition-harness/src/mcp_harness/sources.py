from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from .util import sha256_file


REQUIRED_CURRENT_SOURCES = {
    "AGENTS.md",
    "AB_Runtime_Authority_Reference_v1.1.md",
    "AB_GoalCompleteness_Procedure_and_Evals_v1.1.md",
    "OMR_Evidence_Capture_Protocol_v0.1.md",
    "OMR_Operator_Prototype_Runtime_v0.2.md",
    "P2_State_Schemas_v0.1.json",
    "P5_Executor_View_v0.1.yaml",
}

FORBIDDEN_EXECUTOR_BASENAMES = {
    "P5_Comparative_Fixture_Pack_v0.1.yaml",
    "minimum_composition_prototype_v0.1.zip",
    "system_ab_key.json",
    "randomized_system_identity_key.json",
}


@dataclass
class SourceCheck:
    ok: bool
    records: list[dict[str, Any]]
    errors: list[str]


def verify_sources(authority_dir: Path, fixture_view: Path) -> SourceCheck:
    errors: list[str] = []
    records: list[dict[str, Any]] = []

    for forbidden in FORBIDDEN_EXECUTOR_BASENAMES:
        hits = list(authority_dir.rglob(forbidden))
        if hits:
            errors.append(f"RUN CONTAMINATED - forbidden executor file present: {hits[0]}")

    lock_path = authority_dir / "HARNESS_SOURCE_LOCK.json"
    if not lock_path.exists():
        errors.append("Missing HARNESS_SOURCE_LOCK.json")
        lock_records: dict[str, dict[str, Any]] = {}
    else:
        lock_records = json.loads(lock_path.read_text(encoding="utf-8-sig")).get("records", {})
        missing_current = sorted(REQUIRED_CURRENT_SOURCES - set(lock_records))
        if missing_current:
            errors.append(f"Harness source lock missing current adopted source entries: {missing_current}")

    for name, lock_record in sorted(lock_records.items()):
        path = fixture_view if name == "P5_Executor_View_v0.1.yaml" else authority_dir / name
        if not path.exists():
            errors.append(f"Missing frozen source: {name}")
            continue

        actual = sha256_file(path)
        expected = lock_record.get("sha256")
        records.append(
            {
                "file": name,
                "expected": expected,
                "actual": actual,
                "match": expected == actual,
                "authority": "HARNESS_SOURCE_LOCK",
            }
        )
        if expected is None:
            errors.append(f"No harness source-lock entry: {name}")
        elif actual != expected:
            errors.append(f"Digest mismatch: {name}")

    return SourceCheck(ok=not errors, records=records, errors=errors)
