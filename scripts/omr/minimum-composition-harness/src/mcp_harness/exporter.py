from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from .config import RunConfig
from .fixtures import Fixture
from .util import atomic_write_json, atomic_write_text, read_json, sha256_file, utc_now


GENERIC_OBSERVABLE_CHECKLIST = [
    "Correct outcome or defensible block/stop is stated.",
    "Required goal/capability basis is present before asset mapping where the condition requires it.",
    "Coverage is behavioral rather than label-only.",
    "No claim exceeds the supplied evidence stage.",
    "Sequencing or invocation illegality is rejected rather than silently normalized.",
    "A sufficient asset may terminate with no material change.",
    "Trace-dependent credit remains provisional until the identity-key-withheld trace-audit packet is reviewed.",
]


def _reset(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def build_evaluator_packets(
    config: RunConfig,
    fixtures: list[Fixture],
    system_key: dict[str, Any],
    full_fixtures: Path | None = None,
) -> dict[str, Path]:
    """Build staged evaluator packets after raw execution is locked.

    Stage 1 is behavior-blind. Stage 2 exposes traces under A/B labels while withholding
    the formal key; implementation identity may nevertheless be inferable. Stage 3 reveals
    the key for diagnostic attribution after scores lock.
    """
    first = config.run_root / "Evaluator_First_Pass_Packet"
    trace = config.run_root / "Evaluator_Trace_Audit_Packet"
    diagnostic = config.run_root / "Evaluator_Diagnostic_Packet"
    try:
        for path in (first, trace, diagnostic):
            _reset(path)
    except PermissionError:
        stamp = utc_now().replace(":", "").replace("-", "").replace(".", "").replace("Z", "Z")
        export_root = config.run_root / f"Evaluator_Export_{stamp}"
        first = export_root / "Evaluator_First_Pass_Packet"
        trace = export_root / "Evaluator_Trace_Audit_Packet"
        diagnostic = export_root / "Evaluator_Diagnostic_Packet"
        for path in (first, trace, diagnostic):
            path.mkdir(parents=True)

    by_cell = {f.cell_id: f for f in fixtures}
    attempts = config.run_root / "attempts"
    for cell_key, assignment in system_key["cells"].items():
        parts = cell_key.split("__")
        cell_id, condition, rep = parts[0], parts[1], int(parts[2][1:])
        fixture = by_cell[cell_id]
        outputs: dict[str, Any] = {}
        for blind_label, system in (("A", assignment["A"]), ("B", assignment["B"])):
            attempt_id = f"{config.run_series_id}__{cell_id}__{condition}__r{rep}__{system}"
            path = attempts / attempt_id
            summary = read_json(path / "attempt_summary.json") if (path / "attempt_summary.json").exists() else {"status": "missing"}
            visible = (path / "visible_answer.txt").read_text(encoding="utf-8") if (path / "visible_answer.txt").exists() else "[MISSING OUTPUT]"
            outputs[blind_label] = {
                "status": summary.get("status"),
                "visible_output": visible,
            }
            target = trace / cell_key / blind_label
            if path.exists():
                shutil.copytree(path, target)
            else:
                target.mkdir(parents=True)
                atomic_write_text(target / "MISSING.txt", "Expected raw attempt directory was not present.\n")
        record = {
            "cell_id": cell_id,
            "condition": condition,
            "replicate": rep,
            "public_fixture": fixture.public,
            "presentation_order": assignment["presentation_order"],
            "outputs": outputs,
            "required_observable_checklist": GENERIC_OBSERVABLE_CHECKLIST,
            "instruction": (
                "Score visible behavior first without opening the trace-audit or diagnostic packets. "
                "Lock first-pass scores, then inspect the trace-audit packet to determine whether required evidence artifacts exist."
            ),
        }
        atomic_write_json(first / f"{cell_key}.json", record)
        atomic_write_json(trace / cell_key / "public_fixture.json", fixture.public)
        atomic_write_json(trace / cell_key / "presentation_order.json", {"presentation_order": assignment["presentation_order"]})

    atomic_write_text(
        first / "README.md",
        "# First-pass blinded packet\n\nSystem A/B identities are withheld. Score visible behavior and lock those scores before opening the trace-audit packet. Trace-dependent credit is provisional until Stage 2.\n",
    )
    atomic_write_text(
        trace / "README.md",
        "# Identity-key-withheld trace-audit packet\n\nInspect complete raw traces under A/B labels. The formal A/B key remains withheld, but implementation identity may be inferable from the required traces. Confirm seals, state, selector/rejection, evidence, and burden artifacts before finalizing case passes.\n",
    )

    # Evaluator-only fixture authority is introduced only after runs are locked.
    if full_fixtures:
        if not full_fixtures.exists():
            raise FileNotFoundError(full_fixtures)
        for packet in (first, trace):
            auth = packet / "Evaluator_Scoring_Authority"
            auth.mkdir()
            shutil.copy2(full_fixtures, auth / full_fixtures.name)
            atomic_write_json(auth / "fixture_digest.json", {"file": full_fixtures.name, "sha256": sha256_file(full_fixtures)})

    # Diagnostic packet reveals identity and architecture only after behavioral + trace scoring lock.
    if attempts.exists():
        shutil.copytree(attempts, diagnostic / "attempts")
    shutil.copytree(config.authority_dir, diagnostic / "authorities")
    atomic_write_json(diagnostic / "system_key.json", system_key)
    if (config.run_root / "Execution_Index.csv").exists():
        shutil.copy2(config.run_root / "Execution_Index.csv", diagnostic / "Execution_Index.csv")
    if (config.run_root / "Manual_Intervention_Log.jsonl").exists():
        shutil.copy2(config.run_root / "Manual_Intervention_Log.jsonl", diagnostic / "Manual_Intervention_Log.jsonl")
    if full_fixtures:
        shutil.copy2(full_fixtures, diagnostic / full_fixtures.name)
    atomic_write_json(diagnostic / "export_manifest.json", {
        "created_at": utc_now(),
        "run_series_id": config.run_series_id,
        "stages": ["behavior-blind", "trace-audit-formal-key-withheld", "diagnostic-key-revealed"],
        "full_fixture_pack_included": bool(full_fixtures),
        "full_fixture_sha256": sha256_file(full_fixtures) if full_fixtures else None,
    })
    atomic_write_text(
        diagnostic / "README.md",
        "# Diagnostic packet\n\nOpen only after first-pass behavioral scores and identity-key-withheld trace-audit judgments are locked. This packet reveals the system key and implementation details.\n",
    )
    return {"first_pass": first, "trace_audit": trace, "diagnostic": diagnostic}
