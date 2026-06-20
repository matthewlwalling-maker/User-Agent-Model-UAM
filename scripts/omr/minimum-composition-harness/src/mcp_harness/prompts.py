from __future__ import annotations

import json
from pathlib import Path
from typing import Any


OPERATOR_NAMES = {
    "O1": "Normalize Goal and Obligations",
    "O2": "Derive Required Capabilities",
    "O3": "Assess Capability Coverage",
    "O4": "Choose Intervention or Stop",
}


def _read_first_existing(authority_dir: Path, names: list[str]) -> str:
    for name in names:
        path = authority_dir / name
        if path.exists():
            return path.read_text(encoding="utf-8")
    raise FileNotFoundError(f"None of these authority files exist in {authority_dir}: {names}")


def cached_system_block(text: str, ttl: str) -> dict[str, Any]:
    return {"type": "text", "text": text, "cache_control": {"type": "ephemeral", "ttl": ttl}}


def operator_system(authority_dir: Path, operator: str, ttl: str) -> list[dict[str, Any]]:
    runtime = _read_first_existing(
        authority_dir,
        ["OMR_Operator_Prototype_Runtime_v0.2.md", "P3_Operator_Runtime_Contracts_v0.1.md"],
    )
    evidence_capture = _read_first_existing(
        authority_dir,
        ["OMR_Evidence_Capture_Protocol_v0.1.md", "P6_AB_Run_and_Evidence_Capture_Protocol_v0.1.md"],
    )
    static = (
        "You are executing the frozen Minimum Composition operator prototype. "
        "The deterministic harness owns selection, packet construction, hashing, persistence, and validation. "
        "You own only the selected constrained-generative transform. Do not use knowledge outside the supplied messages.\n\n"
        f"<OMR_RUNTIME>\n{runtime}\n</OMR_RUNTIME>\n\n"
        f"<EVIDENCE_CAPTURE_PROTOCOL>\n{evidence_capture}\n</EVIDENCE_CAPTURE_PROTOCOL>"
    )
    dynamic = (
        f"Execute only {operator} - {OPERATOR_NAMES[operator]}. Return exactly the structured response. "
        "The response schema is a transport projection of P2: return an empty meta object because the harness owns "
        "identity, ancestry, revision, freshness, and hashing. For O2, report only asset_component_terms_used inside "
        "derivation_boundary; the harness derives the condition and packet facts from the recorded request. "
        "For O1 GoalContract obligations, IDs must use the canonical OB-* form such as OB-1, never OBL-1. "
        "For O1 GoalContract constraints, IDs must use the canonical CT-* form such as CT-1, never CON-1. "
        "For O2 CapabilityModel, capabilities[*].obligation_refs and obligation_coverage[*].obligation_ref must "
        "contain only OB-* IDs copied from the committed GoalContract obligations. CT-* constraint IDs may inform "
        "capability behavior, success conditions, scope boundaries, evidence statements, and rationale text, but must "
        "never appear in obligation_refs or obligation_coverage.obligation_ref. "
        "For O2, asset_component_terms_used must be empty unless an actual forbidden asset component or section label "
        "from asset exposure influenced derivation; ordinary goal/request terms are not asset component terms. "
        "For O3, every non-unknown coverage entry, including absent coverage, must cite at least one concrete "
        "asset_behavior_ref. For absent coverage, cite the concrete asset behavior or explicit absence evidence "
        "supporting the absence; if no concrete behavior or explicit absence reference is available, classify the "
        "entry as unknown-insufficient-evidence instead of absent. "
        "For O4, ChangeDecision.stop_reason and the wrapper stop.code and stop.reason must be non-empty strings; "
        "never emit empty stop fields. "
        "Internal operators O1-O3 must set visible_answer to an empty string. O4 must provide a concise user-facing visible_answer that states "
        "the conclusion, evidence ceiling, verification need, and stop basis without mentioning System A/B or predicting the experiment winner."
    )
    return [cached_system_block(static, ttl), {"type": "text", "text": dynamic}]


def legacy_system(authority_dir: Path, ttl: str) -> list[dict[str, Any]]:
    runtime = _read_first_existing(
        authority_dir,
        ["AB_Runtime_Authority_Reference_v1.1.md", "03_Agent_Builder_Assessment_Contract_v1.0.md"],
    )
    procedure = _read_first_existing(
        authority_dir,
        ["AB_GoalCompleteness_Procedure_and_Evals_v1.1.md", "04_Goal-Completeness_and_Open-Architecture_Procedure_v1.0.md"],
    )
    static = (
        "You are the unchanged legacy Agent Builder Goal-Completeness control. Execute the supplied procedure faithfully. "
        "Do not use the Minimum Composition operators or typed-state contracts. Return a normal user-facing assessment, "
        "not JSON, and preserve every required procedural artifact the legacy sources themselves require.\n\n"
        f"<AB_RUNTIME_AUTHORITY>\n{runtime}\n</AB_RUNTIME_AUTHORITY>\n\n"
        f"<AB_GOAL_COMPLETENESS_PROCEDURE_AND_EVALS>\n{procedure}\n</AB_GOAL_COMPLETENESS_PROCEDURE_AND_EVALS>"
    )
    return [cached_system_block(static, ttl)]


def packet_message(packet: dict[str, Any]) -> str:
    return "Execute the selected operator from this complete ExecutionPacket. Do not rely on any omitted context.\n\n" + json.dumps(packet, indent=2, ensure_ascii=False)


def fixture_text(public: dict[str, Any], include_asset: bool = True) -> str:
    data = dict(public)
    if not include_asset:
        data.pop("asset", None)
        data.pop("dependency_map", None)
    return json.dumps(data, indent=2, ensure_ascii=False)
