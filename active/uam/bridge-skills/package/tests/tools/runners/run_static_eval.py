#!/usr/bin/env python3
"""Static eval runner for the UAM Bridge Skills package.

This runner checks whether the canonical package text covers the behaviors
required by the design-time eval fixtures. It does not execute model prompts and
must not be treated as runtime or cross-model parity evidence.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[3]
TESTS = ROOT / "tests"
RECORD = TESTS / "records" / "static" / "test-suite-eval-record.md"
TARGETED_RECORD = TESTS / "records" / "targeted" / "targeted-static-eval-record.md"
SUITE_PATHS = {
    "align-work-cases.yaml": TESTS / "suites" / "command-skills" / "align-work-cases.yaml",
    "build-artifact-cases.yaml": TESTS / "suites" / "command-skills" / "build-artifact-cases.yaml",
    "compare-decide-cases.yaml": TESTS / "suites" / "command-skills" / "compare-decide-cases.yaml",
    "design-solution-cases.yaml": TESTS / "suites" / "command-skills" / "design-solution-cases.yaml",
    "diagnose-problem-cases.yaml": TESTS / "suites" / "command-skills" / "diagnose-problem-cases.yaml",
    "handoff-state-cases.yaml": TESTS / "suites" / "command-skills" / "handoff-state-cases.yaml",
    "research-evidence-cases.yaml": TESTS / "suites" / "command-skills" / "research-evidence-cases.yaml",
    "review-work-cases.yaml": TESTS / "suites" / "command-skills" / "review-work-cases.yaml",
    "blind-value-proposition-cases.yaml": TESTS / "suites" / "behavioral" / "blind-value-proposition-cases.yaml",
    "pressure-red-cases.yaml": TESTS / "suites" / "pressure" / "pressure-red-cases.yaml",
    "pressure-red-executor-only-cases.yaml": TESTS / "suites" / "pressure" / "pressure-red-executor-only-cases.yaml",
    "routing-cases.yaml": TESTS / "suites" / "routing" / "routing-cases.yaml",
    "object-integrity-cases.yaml": TESTS / "suites" / "object-integrity" / "object-integrity-cases.yaml",
    "evidence-ceiling-cases.yaml": TESTS / "suites" / "evidence-ceiling" / "evidence-ceiling-cases.yaml",
    "degradation-cases.yaml": TESTS / "suites" / "degradation" / "degradation-cases.yaml",
    "overactivation-cases.yaml": TESTS / "suites" / "overactivation" / "overactivation-cases.yaml",
    "cross-model-parity.yaml": TESTS / "suites" / "cross-model-parity" / "cross-model-parity.yaml",
}

COMMAND_TO_SKILL = {
    "/align": "align-work",
    "/design": "design-solution",
    "/build": "build-artifact",
    "/review": "review-work",
    "/compare": "compare-decide",
    "/diagnose": "diagnose-problem",
    "/research": "research-evidence",
    "/handoff": "handoff-state",
}

REQUIRED_SKILL_SECTIONS = [
    "Purpose",
    "Use When",
    "Do Not Use When",
    "Reads",
    "Writes",
    "Modes",
    "Lenses",
    "Procedure",
    "Required Output",
    "Stop Conditions",
    "Boundary",
]


@dataclass
class Result:
    suite: str
    case_id: str
    status: str
    notes: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def suite_path(filename: str) -> Path:
    return SUITE_PATHS[filename]


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def has_all(text: str, patterns: list[str]) -> tuple[bool, list[str]]:
    ntext = norm(text)
    missing = [pattern for pattern in patterns if norm(pattern) not in ntext]
    return not missing, missing


def parse_inline(value: str):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"').strip("'") for item in inner.split(",")]
    return value.strip('"').strip("'")


def parse_cases(path: Path) -> tuple[dict[str, object], list[dict[str, object]]]:
    meta: dict[str, object] = {}
    cases: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    in_cases = False

    for raw in read_text(path).splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "cases:":
            in_cases = True
            continue
        if not in_cases:
            match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", stripped)
            if match:
                meta[match.group(1)] = parse_inline(match.group(2))
            continue
        if line.startswith("  - "):
            current = {}
            cases.append(current)
            rest = line[4:].strip()
            if rest:
                match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", rest)
                if match:
                    current[match.group(1)] = parse_inline(match.group(2))
            continue
        if current is not None and line.startswith("    "):
            match = re.match(r"^\s+([A-Za-z0-9_-]+):\s*(.*)$", line)
            if match:
                current[match.group(1)] = parse_inline(match.group(2))

    return meta, cases


def load_package_texts() -> dict[str, str]:
    texts = {
        "kernel": read_text(ROOT / "KERNEL.md"),
        "manifest": read_text(ROOT / "MANIFEST.yaml"),
        "chain-router-reference": read_text(ROOT / "CHAIN_ROUTER.md"),
        "executor-evaluator-runtime-protocol": read_text(ROOT / "docs" / "executor-evaluator-runtime-protocol.md"),
        "blind-test-protocol": read_text(ROOT / "docs" / "blind-test-protocol.md"),
    }
    for command, skill in COMMAND_TO_SKILL.items():
        texts[command] = read_text(ROOT / "skills" / skill / "SKILL.md")
    texts["all"] = "\n\n".join(texts.values())
    return texts


def structural_checks(texts: dict[str, str]) -> list[Result]:
    results: list[Result] = []
    manifest = texts["manifest"]

    for command, skill in COMMAND_TO_SKILL.items():
        skill_path = ROOT / "skills" / skill / "SKILL.md"
        expected_path = f"skills/{skill}/SKILL.md"
        status = "PASS"
        notes: list[str] = []
        if not skill_path.exists():
            status = "FAIL"
            notes.append("skill file missing")
        if command not in manifest or expected_path not in manifest:
            status = "FAIL"
            notes.append("manifest command/path entry missing")
        for section in REQUIRED_SKILL_SECTIONS:
            if f"## {section}" not in texts[command]:
                status = "FAIL"
                notes.append(f"missing section: {section}")
        results.append(Result("structure", command, status, "; ".join(notes) or "contract sections and manifest entry present"))

    for suite_name in [
        "align-work-cases.yaml",
        "build-artifact-cases.yaml",
        "design-solution-cases.yaml",
        "diagnose-problem-cases.yaml",
        "handoff-state-cases.yaml",
        "research-evidence-cases.yaml",
        "review-work-cases.yaml",
        "blind-value-proposition-cases.yaml",
        "pressure-red-cases.yaml",
        "pressure-red-executor-only-cases.yaml",
        "routing-cases.yaml",
        "object-integrity-cases.yaml",
        "evidence-ceiling-cases.yaml",
        "degradation-cases.yaml",
        "overactivation-cases.yaml",
        "cross-model-parity.yaml",
    ]:
        path = suite_path(suite_name)
        status = "PASS" if path.exists() else "FAIL"
        notes = "fixture present" if path.exists() else "fixture missing"
        if path.exists():
            _, cases = parse_cases(path)
            if not cases:
                status = "FAIL"
                notes = "fixture has no parsed cases"
        results.append(Result("structure", suite_name, status, notes))

    return results


CASE_PATTERNS: dict[str, tuple[str, list[str]]] = {
    # align-work
    "align-clarify-001": ("/align", ["GATE: ASK", "missing load-bearing state", "Do not reconstruct"]),
    "align-clarify-002": ("/align", ["GATE: PREPARE-NOT-EXECUTE", "BLOCKED ACTION", "send"]),
    "align-frame-001": ("/align", ["explicit, entailed, optional, or speculative", "route architecture needs to `/design`"]),
    "align-contract-001": ("/align", ["Outcome", "Constraints and authority", "Evidence ceiling", "Stop/revisit trigger"]),
    "align-branch-001": ("/align", ["GATE: FORK", "preserve branch identity", "/compare"]),
    "align-prioritize-001": ("/align", ["criteria before ranking", "order, recency, or salience bias", "decisive criterion"]),
    "align-scope-001": ("/align", ["Out of scope", "global install", "activation"]),
    "align-routing-001": ("/align", ["Review and improve this specification", "GATE: ASK", "directly modify the artifact"]),
    "align-routing-002": ("/align", ["current provider docs", "routes to `/research`", "claiming current facts"]),
    "align-object-001": ("/align", ["state projection", "artifact compression", "/handoff"]),
    "align-stop-001": ("/align", ["What time is it?", "direct", "material work contract"]),
    "align-degrade-001": ("/align", ["missing load-bearing state", "ask for the packet", "Do not reconstruct"]),
    # build-artifact
    "build-patch-001": ("/build", ["patch", "named section", "Validation performed"]),
    "build-augment-001": ("/build", ["augment", "owning location", "direct first-degree dependencies"]),
    "build-rewrite-001": ("/build", ["rewrite authority", "load-bearing requirements", "Never hide a rewrite"]),
    "build-implement-001": ("/build", ["committed design", "design conflict", "route back to `/design`"]),
    "build-shape-001": ("/build", ["concrete, checkable grammar", "generic polish", "substance-preserving"]),
    "build-compress-001": ("/build", ["load-bearing", "ornamental", "verbatim-critical", "dropped-element ledger"]),
    "build-materialize-001": ("/build", ["target paths", "overwrite authority", "Inspect existing files"]),
    "build-gate-001": ("/build", ["PREPARE-NOT-EXECUTE", "global install / activation", "explicit install authorization"]),
    "build-degrade-001": ("/build", ["file writing is unavailable", "complete file contents", "not written"]),
    "build-evidence-001": ("/build", ["implementation completion", "verification", "cross-model parity"]),
    # design-solution
    "design-explore-001": ("/design", ["generate distinct candidates", "name tradeoffs", "optional opportunities"]),
    "design-architect-001": ("/design", ["independent required capability model", "Visible seal", "Current artifact mapping"]),
    "design-specify-001": ("/design", ["implementation-ready specification", "governance and action gates", "verbatim-critical"]),
    "design-plan-001": ("/design", ["phases", "verification owed", "rollback/revisit triggers"]),
    "design-reconcile-001": ("/design", ["preserve behavior-bearing wording", "rationale ledger", "residual conflicts"]),
    "design-refine-001": ("/design", ["bounded improvement", "preserve settled choices", "route to `architect`"]),
    "design-premortem-001": ("/design", ["strongest opposing case", "observable kill condition", "likely failure causes"]),
    "design-boundary-001": ("/design", ["must not silently create or change", "production artifact", "unless `/build`"]),
    # handoff-state
    "handoff-align-001": ("/handoff", ["Required obligations", "optional opportunities", "speculative ideas", "Next action"]),
    "handoff-design-001": ("/handoff", ["implementation-handoff", "invariants", "Released decisions", "open branches", "Do not implement"]),
    "handoff-build-001": ("/handoff", ["Artifact identities", "Verification owed", "validation", "does not rewrite"]),
    "handoff-review-001": ("/handoff", ["evaluator-handoff", "Evidence ceiling", "verification owed", "claim limits"]),
    "handoff-compare-001": ("/handoff", ["decision-log", "branch identity", "rejected alternatives", "revisit triggers"]),
    "handoff-diagnose-001": ("/handoff", ["confidence", "risks", "verification owed", "next operation"]),
    "handoff-research-001": ("/handoff", ["evidence-handoff", "source map", "contradictions", "freshness requirements"]),
    "handoff-compact-001": ("/handoff", ["compact", "state projection", "artifact identity", "not the substantive spec"]),
    "handoff-missing-source-001": ("/handoff", ["Unavailable:", "missing source", "loadable references", "Do not infer"]),
    "handoff-degrade-001": ("/handoff", ["archive or file creation is unavailable", "Markdown packet", "not performed"]),
    "handoff-resume-001": ("/handoff", ["resume", "stale", "Route the next action to the owning command", "evidence ceiling"]),
    "handoff-parity-001": ("/handoff", ["provider capability assumptions", "degradation notes", "cross-provider", "evidence stage"]),
    # research-evidence
    "research-discover-001": ("/research", ["discover", "source authority", "freshness", "must-have sources"]),
    "research-verify-001": ("/research", ["checkable subclaims", "support status", "scope mismatch", "not inspected"]),
    "research-synthesize-001": ("/research", ["authority, date, scope, and agreement", "direct source claim", "model inference", "implication"]),
    "research-source-map-001": ("/research", ["identity, source type, date, scope, inspected status", "loadable reference", "bare citation"]),
    "research-fact-check-001": ("/research", ["atomic claims", "supported", "partially supported", "contradicted", "uncertain", "unverified", "out of scope"]),
    "research-update-001": ("/research", ["current information may change", "fresh enough", "stale", "Use absolute dates"]),
    "research-contradiction-001": ("/research", ["Preserve contradictions", "authority for which subclaim", "Claim limits"]),
    "research-degrade-001": ("/research", ["No live retrieval available", "Assess only supplied evidence", "exact sources needed", "latest, current, official"]),
    "research-boundary-001": ("/research", ["Do not write artifacts", "next operation must be separately authorized", "must not perform those operations"]),
    "research-high-stakes-001": ("/research", ["legal, medical, financial", "insufficient", "out of scope"]),
    # review-work
    "review-object-001": ("/review", ["review and fix", "read-only review", "recommend `/build`"]),
    "review-completeness-001": ("/review", ["required capability model", "classify coverage", "headings"]),
    "review-readiness-001": ("/review", ["Green", "design-time plausibility", "unverified"]),
    "review-adversarial-001": ("/review", ["hidden trap", "required behavior", "prohibited behavior", "scoring rule", "criticality"]),
    "review-regression-001": ("/review", ["prior version", "current version", "Do not merge or patch"]),
    "review-evidence-001": ("/review", ["Map each claim", "maximum justified claim stage", "verification would upgrade"]),
    "review-blind-grade-001": ("/review", ["Grade against purpose and audience", "Do not invent a flaw", "ship-with-fixes"]),
    "review-degrade-001": ("/review", ["file reading is unavailable", "runtime", "unavailable"]),
    # diagnose-problem
    "diagnose-triage-001": ("/diagnose", ["observed symptom", "expected behavior", "initial failure class"]),
    "diagnose-root-cause-001": ("/diagnose", ["cause map", "plausible alternatives", "state confidence"]),
    "diagnose-premortem-001": ("/diagnose", ["Decision", "Steelman against", "Kill condition"]),
    "diagnose-fix-layer-001": ("/diagnose", ["Trace where the failure originates", "kernel/router", "eval harness"]),
    "diagnose-impact-001": ("/diagnose", ["local failure from systemic pattern", "release", "additional failures"]),
    "diagnose-recovery-001": ("/diagnose", ["smallest sufficient recovery", "next operation", "regression check"]),
    "diagnose-calibration-001": ("/diagnose", ["Require actual burden", "interface friction", "burden reduction"]),
    "diagnose-hypothesis-001": ("/diagnose", ["GATE: HYPOTHESIS", "OBSERVATION NEEDED", "bounded causal model"]),
    "diagnose-boundary-001": ("/diagnose", ["does not patch", "rewrite", "Hand implementation to `/build`"]),
    # routing
    "route-001": ("/build", ["authorized", "scope", "materialize-files"]),
    "route-002": ("/align", ["Review and improve this specification", "ambiguous mutation authority", "directly modify"]),
    "route-003": ("/handoff", ["state projection", "Do not rewrite", "substantive artifacts"]),
    "route-004": ("/research", ["current information", "Provider capability", "without retrieval"]),
    "route-005": ("/compare", ["freeze criteria", "compare before any merge", "must not silently create"]),
    "route-006": ("all", ["next_allowed` is not action authority", "review only", "explicit bounded"]),
    "route-007": ("all", ["bounded_build", "packet_chain", "stop before executing"]),
    "route-008": ("all", ["Adversarial review is required by default", "material changes to routing", "unless `/build`"]),
    # object integrity
    "obj-001": ("/review", ["Default read-only", "must not modify", "unless the user explicitly converts"]),
    "obj-002": ("/diagnose", ["Hand implementation to `/build`", "does not patch", "fix layer"]),
    "obj-003": ("/compare", ["preserving branch identity", "donor components", "must not silently create"]),
    "obj-004": ("/handoff", ["state projection", "artifact", "does not rewrite"]),
    "obj-005": ("/research", ["Contradictory or uncertain findings", "Claim limits", "unsupported claims"]),
    "obj-006": ("all", ["`/review` writes evidence only", "must not mutate", "explicit bounded `/build` authority"]),
    "obj-007": ("all", ["packet", "stop before executing it", "does not rewrite"]),
    "obj-008": ("all", ["preserving branch identity", "route the selected comparison result to `/build`", "must not silently create"]),
    # evidence ceiling
    "evc-001": ("kernel", ["design-time", "cross-model", "production-observed"]),
    "evc-002": ("/review", ["design-time review", "runtime or test execution is unavailable", "limit claims"]),
    "evc-003": ("/research", ["current information may change", "live retrieval is unavailable", "unverified"]),
    "evc-004": ("/compare", ["cross-model", "do not claim measured parity", "evidence checked"]),
    "evc-005": ("all", ["Verification of one edit does not establish package readiness", "runtime behavior", "cross-model parity"]),
    "evc-006": ("all", ["Evidence stage must be scoped to the exact claim", "Fixture design alone is `design-time`"]),
    "evc-007": ("all", ["required run artifacts are missing", "runtime behavior", "readiness gating"]),
    # degradation
    "deg-001": ("/build", ["If file writing is unavailable", "not written"]),
    "deg-002": ("/research", ["No live retrieval available", "Assess only supplied evidence", "unverified"]),
    "deg-003": ("/review", ["runtime or test execution is unavailable", "design-time", "name the tests"]),
    "deg-004": ("/compare", ["independent or blind contexts are unavailable", "do not claim blind"]),
    "deg-005": ("/handoff", ["archive or file creation is unavailable", "Markdown packet", "not performed"]),
    "deg-006": ("all", ["continue only within `KERNEL.md`", "record the missing reference", "auto-continuation"]),
    "deg-007": ("all", ["section-specific loading is unavailable", "load the full reference", "non-executing recommendation"]),
    "deg-008": ("all", ["artifact_reference_unresolved", "loadable-content-missing", "Downstream machine action"]),
    # overactivation
    "over-001": ("kernel", ["Use the fast path", "low-coupling", "Avoid ceremonial routing"]),
    "over-002": ("/align", ["What time is it?", "answer directly", "bridge alignment is unnecessary"]),
    "over-003": ("kernel", ["Use the fast path", "simple", "Avoid ceremonial routing"]),
    "over-004": ("kernel", ["smallest process sufficient", "simple", "Avoid ceremonial routing"]),
    "over-005": ("kernel", ["explicit commands", "Implicit routing is disabled", "/review"]),
    "over-006": ("all", ["merely recommend a next command", "without deciding route authority", "Do not load router reference material"]),
    "over-007": ("all", ["Use the fast path", "low-coupling", "Do not load router reference material"]),
    "over-008": ("all", ["Issue a verdict within the evidence ceiling", "without deciding route authority", "Do not load router reference material"]),
    # cross-model parity
    "parity-001": ("/align", ["Outcome", "Required constraints", "Primary next operation"]),
    "parity-002": ("/build", ["Completed artifact or change summary", "Preservation note", "Validation performed"]),
    "parity-003": ("/review", ["Verdict", "Evidence limits", "Verification"]),
    "parity-004": ("/handoff", ["Committed objective", "Artifact identities", "Evidence ceiling", "Authorized next action"]),
}


def case_checks(texts: dict[str, str], selected_case_ids: set[str] | None = None) -> list[Result]:
    results: list[Result] = []
    found_case_ids: set[str] = set()
    fixture_files = [
        "align-work-cases.yaml",
        "build-artifact-cases.yaml",
        "design-solution-cases.yaml",
        "diagnose-problem-cases.yaml",
        "handoff-state-cases.yaml",
        "research-evidence-cases.yaml",
        "review-work-cases.yaml",
        "routing-cases.yaml",
        "object-integrity-cases.yaml",
        "evidence-ceiling-cases.yaml",
        "degradation-cases.yaml",
        "overactivation-cases.yaml",
        "cross-model-parity.yaml",
    ]

    for filename in fixture_files:
        meta, cases = parse_cases(suite_path(filename))
        suite = str(meta.get("suite_id", filename.replace(".yaml", "")))
        for case in cases:
            case_id = str(case.get("id", "missing-id"))
            if selected_case_ids is not None and case_id not in selected_case_ids:
                continue
            found_case_ids.add(case_id)
            if case_id == "missing-id":
                results.append(Result(suite, case_id, "FAIL", "case id missing"))
                continue
            if case_id not in CASE_PATTERNS:
                results.append(Result(suite, case_id, "FAIL", "no static assertion registered"))
                continue
            target, patterns = CASE_PATTERNS[case_id]
            ok, missing = has_all(texts[target], patterns)
            status = "PASS" if ok else "FAIL"
            notes = "required contract coverage present" if ok else "missing: " + "; ".join(missing)
            results.append(Result(suite, case_id, status, notes))

    if selected_case_ids is not None:
        for case_id in sorted(selected_case_ids - found_case_ids):
            results.append(Result("selection", case_id, "FAIL", "case id not found in loaded fixtures"))

    return results


def manifest_status_checks(texts: dict[str, str]) -> list[Result]:
    results: list[Result] = []
    manifest = texts["manifest"]
    for command, skill in COMMAND_TO_SKILL.items():
        skill_text = texts[command]
        enriched = "Donor Obligation Ledger" in skill_text or "Mode Procedures" in skill_text or "Examples" in skill_text
        expected_status = "v0.1-enriched" if enriched else "v0.1-contracted"
        block_match = re.search(
            rf"- command: {re.escape(command)}\n(?:    .+\n)+?    release_status: ([^\n]+)",
            manifest,
        )
        if not block_match:
            results.append(Result("manifest-status", command, "FAIL", "release_status block missing"))
            continue
        actual = block_match.group(1).strip()
        status = "PASS" if actual == expected_status else "FAIL"
        notes = f"release_status {actual}; expected {expected_status}"
        results.append(Result("manifest-status", command, status, notes))
    return results


def write_record(results: list[Result], record_path: Path, selected_case_ids: set[str] | None = None) -> None:
    total = len(results)
    passed = sum(1 for result in results if result.status == "PASS")
    failed = total - passed
    suites = sorted({result.suite for result in results})
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    run_scope = "selected cases" if selected_case_ids else "full static suite"
    title = "Targeted Static Evaluation Record" if selected_case_ids else "Test Suite Evaluation Record"

    lines = [
        f"# {title}",
        "",
        f"Run timestamp: `{now}`",
        "",
        "Target package: `uam-bridge-skills` v0.1.0",
        "",
        "Runner: `tests/tools/runners/run_static_eval.py`",
        "",
        f"Run scope: `{run_scope}`",
    ]

    if selected_case_ids:
        lines.extend([
            "",
            "Selected case IDs:",
            "",
            *[f"- `{case_id}`" for case_id in sorted(selected_case_ids)],
        ])

    lines += [
        "",
        "Evidence stage: static validation over design-time fixtures. This is not live-runtime, independent, or cross-model parity evidence.",
        "",
        "## Aggregate",
        "",
        f"- Suites checked: {len(suites)}",
        f"- Assertions checked: {total}",
        f"- Passed: {passed}",
        f"- Failed: {failed}",
        "",
        "## Results",
        "",
        "| Suite | Case | Result | Notes |",
        "|---|---|---|---|",
    ]

    for result in results:
        notes = result.notes.replace("|", "\\|")
        lines.append(f"| {result.suite} | {result.case_id} | {result.status} | {notes} |")

    lines += [
        "",
        "## Claim Limits",
        "",
        "- Passing assertions mean the source package text contains the required contract coverage for the fixture.",
        "- Passing assertions do not prove that any provider will follow the contract in live use.",
        "- Cross-model parity remains unproven until provider adapters are run against the parity prompts and outputs are compared.",
        "",
        "## Next Action",
        "",
        "Diagnose any failed assertions by fix layer before treating the explicit-command pilot as eval-gated.",
        "",
    ]

    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run static contract-coverage checks for UAM Bridge Skills eval fixtures."
    )
    parser.add_argument(
        "--case-id",
        action="append",
        default=[],
        help="Case id to score. Repeat for targeted runs. Omitting this preserves the full static suite.",
    )
    parser.add_argument(
        "--record",
        type=Path,
        default=None,
        help="Record output path. Defaults to the global record for full runs and a targeted record for selected runs.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    selected_case_ids = set(args.case_id) if args.case_id else None
    record_path = args.record or (TARGETED_RECORD if selected_case_ids else RECORD)

    texts = load_package_texts()
    results = []
    if selected_case_ids is None:
        results.extend(structural_checks(texts))
        results.extend(manifest_status_checks(texts))
    results.extend(case_checks(texts, selected_case_ids))
    write_record(results, record_path, selected_case_ids)

    total = len(results)
    passed = sum(1 for result in results if result.status == "PASS")
    failed = total - passed
    print(f"Static eval complete: {passed}/{total} passed, {failed} failed")
    print(f"Record: {record_path}")
    if failed:
        for result in results:
            if result.status != "PASS":
                print(f"FAIL {result.suite} {result.case_id}: {result.notes}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
