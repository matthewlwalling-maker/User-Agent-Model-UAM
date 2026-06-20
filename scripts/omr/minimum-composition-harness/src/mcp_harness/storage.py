from __future__ import annotations

import csv
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .util import atomic_write_json, atomic_write_text, utc_now


@dataclass
class AttemptWriter:
    root: Path
    attempt_id: str

    def __post_init__(self) -> None:
        self.path = self.root / "attempts" / self.attempt_id
        if self.path.exists() and not (self.path / "attempt_summary.json").exists() and any(self.path.iterdir()):
            archive_root = self.root / "interrupted_attempts"
            archive_root.mkdir(parents=True, exist_ok=True)
            stamp = utc_now().replace(":", "").replace("-", "")
            archived = archive_root / f"{self.attempt_id}__{stamp}"
            shutil.move(str(self.path), str(archived))
        self.path.mkdir(parents=True, exist_ok=True)

    def write_json(self, relative: str, value: Any) -> Path:
        path = self.path / relative
        atomic_write_json(path, value)
        return path

    def write_text(self, relative: str, value: str) -> Path:
        path = self.path / relative
        atomic_write_text(path, value)
        return path

    def complete(self, summary: dict[str, Any]) -> None:
        summary = dict(summary)
        summary.setdefault("completed_at", utc_now())
        self.write_json("attempt_summary.json", summary)

    def is_complete(self) -> bool:
        return (self.path / "attempt_summary.json").exists()


def append_execution_index(run_root: Path, row: dict[str, Any]) -> None:
    path = run_root / "Execution_Index.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists()
    if exists:
        with path.open("r", encoding="utf-8", newline="") as rf:
            if any(existing.get("attempt_id") == row.get("attempt_id") for existing in csv.DictReader(rf)):
                return
    fields = [
        "attempt_id", "run_series_id", "cell_id", "condition", "replicate", "system",
        "status", "first_pass_success", "input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens", "total_tokens",
        "wall_latency_ms", "model_latency_ms", "handoff_count", "context_count", "clarification_count",
        "manual_intervention_count", "state_repair_count", "recovery_attempts", "recovery_tokens",
        "recovery_latency_ms", "context_reconstruction_tokens", "failure_source", "recovery_of", "trace_completeness",
    ]
    with path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def append_manual_intervention(run_root: Path, record: dict[str, Any]) -> Path:
    path = run_root / "Manual_Intervention_Log.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "timestamp": record.get("timestamp", utc_now()),
        "actor": record.get("actor", "human"),
        "trigger": record.get("trigger", record.get("intervention_type", "manual-intervention")),
        "change": record.get("change", record.get("after_ref") or "No artifact overwrite; separate intervention/recovery record."),
        "reason": record.get("reason", ""),
        "affected_attempt": record.get("affected_attempt", record.get("attempt_id")),
        "tokens_added": int(record.get("tokens_added", 0) or 0),
        "latency_added_ms": int(record.get("latency_added_ms", 0) or 0),
        "whether_behavioral_scoring_contaminated": bool(record.get("whether_behavioral_scoring_contaminated", True)),
        "before_ref": record.get("before_ref"),
        "after_ref": record.get("after_ref"),
        "recovery_of": record.get("recovery_of"),
    }
    with path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
    return path
