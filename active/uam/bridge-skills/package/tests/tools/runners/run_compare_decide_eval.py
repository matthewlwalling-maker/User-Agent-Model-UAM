#!/usr/bin/env python3
"""Static eval runner for uam.compare-decide only.

This checks source-contract coverage for the compare-specific fixture. It does
not execute model prompts and is not runtime or cross-model evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[3]
TESTS = ROOT / "tests"
SKILL = ROOT / "skills" / "compare-decide" / "SKILL.md"
FIXTURE = TESTS / "suites" / "command-skills" / "compare-decide-cases.yaml"
RECORD = TESTS / "records" / "command-skills" / "compare-decide-eval-record.md"
MANIFEST = ROOT / "MANIFEST.yaml"


@dataclass
class Result:
    case_id: str
    status: str
    notes: str


CASE_PATTERNS: dict[str, list[str]] = {
    "compare-delta-001": [
        "`delta`",
        "same objective",
        "gains and regressions",
        "Rank only when",
    ],
    "compare-rank-001": [
        "`rank`",
        "weighted criteria",
        "hard constraints",
        "anti-anchoring pass",
        "decisive criterion",
    ],
    "compare-select-001": [
        "`select`",
        "selection authority",
        "minimum acceptable threshold",
        "reopen the decision",
    ],
    "compare-reconcile-001": [
        "`reconcile`",
        "Align sections",
        "verbatim-critical",
        "rationale ledger",
        "Stop before writing",
    ],
    "compare-baseline-001": [
        "`baseline`",
        "baseline and its source",
        "required capabilities",
        "true gaps from correct omissions",
        "Scope any novelty, readiness, superiority, or parity claim",
    ],
    "compare-consensus-001": [
        "`consensus-check`",
        "independent model",
        "consensus as an anchor",
        "Decompose the gap",
        "falsifier and kill condition",
    ],
    "compare-boundary-001": [
        "donor components",
        "route the selected comparison result to `/build`",
        "Do not write or revise the candidate artifacts",
    ],
    "compare-degrade-001": [
        "independent or blind contexts are unavailable",
        "do not claim blind",
    ],
    "compare-research-001": [
        "retrieval is unavailable",
        "supplied sources only",
        "unverified",
        "gather new external evidence as the main task",
    ],
    "compare-stop-001": [
        "candidate identity, objective, or decision criteria are missing",
        "stop with the smallest blocking question",
    ],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def parse_case_ids() -> list[str]:
    ids: list[str] = []
    for line in read(FIXTURE).splitlines():
        match = re.match(r"\s+- id:\s*([A-Za-z0-9_-]+)\s*$", line)
        if match:
            ids.append(match.group(1))
    return ids


def check_patterns(skill_text: str) -> list[Result]:
    results: list[Result] = []
    nskill = norm(skill_text)
    for case_id in parse_case_ids():
        patterns = CASE_PATTERNS.get(case_id)
        if not patterns:
            results.append(Result(case_id, "FAIL", "no static assertion registered"))
            continue
        missing = [pattern for pattern in patterns if norm(pattern) not in nskill]
        if missing:
            results.append(Result(case_id, "FAIL", "missing: " + "; ".join(missing)))
        else:
            results.append(Result(case_id, "PASS", "required compare contract coverage present"))
    return results


def structural_results(skill_text: str, manifest_text: str) -> list[Result]:
    checks = {
        "structure-skill-file": SKILL.exists(),
        "structure-fixture-file": FIXTURE.exists(),
        "structure-manifest-registration": "compare_decide: tests/suites/command-skills/compare-decide-cases.yaml" in manifest_text,
        "structure-command": "Command: `/compare`" in skill_text,
        "structure-skill-id": "ID: `uam.compare-decide`" in skill_text,
        "structure-writes": "`evidence`: comparison basis" in skill_text and "`state`: decision support" in skill_text,
        "structure-boundary": "must not silently create a best-of-both artifact" in skill_text,
    }
    return [
        Result(case_id, "PASS" if ok else "FAIL", "present" if ok else "missing")
        for case_id, ok in checks.items()
    ]


def write_record(results: list[Result]) -> None:
    total = len(results)
    passed = sum(1 for result in results if result.status == "PASS")
    failed = total - passed
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "# Compare Decide Evaluation Record",
        "",
        f"Run timestamp: `{now}`",
        "",
        "Target revision: `uam.compare-decide` v0.1.0",
        "",
        "Fixture: `tests/suites/command-skills/compare-decide-cases.yaml`",
        "",
        "Runner: `tests/tools/runners/run_compare_decide_eval.py`",
        "",
        "Evidence stage: static validation over design-time fixtures. This is not live-runtime, independent, or cross-model parity evidence.",
        "",
        "## Aggregate",
        "",
        f"- Assertions checked: {total}",
        f"- Passed: {passed}",
        f"- Failed: {failed}",
        "",
        "## Results",
        "",
        "| Case | Result | Notes |",
        "|---|---|---|",
    ]

    for result in results:
        lines.append(f"| {result.case_id} | {result.status} | {result.notes.replace('|', '\\|')} |")

    lines += [
        "",
        "## Claim Limits",
        "",
        "- Passing assertions mean the compare skill text contains the required controls for the compare fixture.",
        "- This does not prove actual prompt behavior, model compliance, provider parity, or readiness for implicit routing.",
        "",
        "## Next Owed",
        "",
        "Forward-test actual `/compare` outputs for delta, rank, select, reconcile, baseline, consensus-check, degradation, and missing-criteria cases.",
        "",
    ]

    RECORD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    if not SKILL.exists() or not FIXTURE.exists() or not MANIFEST.exists():
        print("Compare eval cannot run: required file missing")
        return 1

    skill_text = read(SKILL)
    manifest_text = read(MANIFEST)
    results = structural_results(skill_text, manifest_text)
    results.extend(check_patterns(skill_text))
    write_record(results)

    total = len(results)
    passed = sum(1 for result in results if result.status == "PASS")
    failed = total - passed
    print(f"Compare-decide eval complete: {passed}/{total} passed, {failed} failed")
    print(f"Record: {RECORD}")
    if failed:
        for result in results:
            if result.status != "PASS":
                print(f"FAIL {result.case_id}: {result.notes}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
