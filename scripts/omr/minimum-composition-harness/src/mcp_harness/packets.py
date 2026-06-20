from __future__ import annotations

import copy
from typing import Any

from .selector import Selection
from .state import StateStore, object_ref
from .util import sha256_object


PERMITTED = {
    "O1": ["user objective", "goal constraints", "requested claim stage", "existing GoalContract when revising", "goal evidence"],
    "O2": ["committed GoalContract", "goal evidence", "constraint evidence", "prior model branches for adjudication only"],
    "O3": ["GoalContract", "CapabilityModel", "asset version and asset behavior", "dependency/interface facts", "EvidenceLedger"],
    "O4": ["CoverageMap", "GoalContract", "CapabilityModel", "EvidenceLedger", "requested terminal authority/evidence claim"],
}
FORBIDDEN = {
    "O1": ["asset coverage judgments", "intervention choice"],
    "O2": ["asset-decomposition", "asset-section-labels", "coverage-judgments", "proposed-edits"],
    "O3": ["intervention proposal", "target architecture", "new external dependency discovery"],
    "O4": ["new asset evidence", "new dependency facts", "coverage rewrite", "implementation"],
}
KIND = {"O1": "GoalContract", "O2": "CapabilityModel", "O3": "CoverageMap", "O4": "ChangeDecision"}


def build_packet(
    *, run_id: str, operator: str, store: StateStore, public: dict[str, Any],
    selection: Selection, condition: str, branch: str = "main",
) -> tuple[dict[str, Any], dict[str, Any]]:
    objects: list[dict[str, Any]] = []
    if operator == "O1":
        gc = store.current("GoalContract", branch)
        if gc:
            objects.append(gc)
    elif operator == "O2":
        gc = store.current("GoalContract", branch) or store.current("GoalContract", "main")
        if gc:
            objects.append(gc)
    elif operator == "O3":
        gc = store.current("GoalContract", "main")
        cm = store.current("CapabilityModel", branch)
        if gc:
            objects.append(gc)
        if cm:
            objects.append(cm)
    elif operator == "O4":
        gc = store.current("GoalContract", "main")
        cms = store.currents("CapabilityModel")
        cvs = store.currents("CoverageMap")
        if gc:
            objects.append(gc)
        objects.extend(cms)
        objects.extend(cvs)
    ledger = store.ledger()
    external: list[dict[str, Any]] = []
    if operator == "O1":
        external.append({"type": "goal-intake", "user_request": public.get("user_request"), "goal_constraints": public.get("goal_constraints", []), "evidence_stage": public.get("evidence_stage", "design-time")})
        if public.get("initial_state"):
            external.append({"type": "incoming-state-description", "value": public["initial_state"]})
    if operator == "O3":
        external.append({"type": "asset", "asset_version": public.get("asset_version"), "asset": public.get("asset")})
        if "dependency_map" in public:
            external.append({"type": "dependency-map", "value": public.get("dependency_map")})
    if operator == "O4":
        external.append({"type": "requested-terminal-result", "user_request": public.get("user_request"), "evidence_stage": public.get("evidence_stage", "design-time"), "legacy_invocation": public.get("legacy_invocation")})
    independence = "separate-context" if condition == "SC" else "packet-boundary"
    ledger_entries = copy.deepcopy(ledger["entries"])
    projection_mode = "full"
    omitted = 0
    if operator in {"O1", "O2"}:
        allowed_types = {"user-request", "governing-source", "model-inference"}
        filtered = [e for e in ledger_entries if e.get("source_type") in allowed_types and e.get("evidence_id") != "EV-INITIAL-STATE"]
        omitted = len(ledger_entries) - len(filtered)
        ledger_entries = filtered
        projection_mode = "referenced-subset"
    packet = {
        "run_id": run_id,
        "operator_id": operator,
        "requested_output_kind": KIND[operator],
        "profile": (store.current("GoalContract", "main") or {}).get("assessment_profile", store.projection),
        "independence_condition": independence if operator == "O2" else "not-applicable",
        "input_objects": [
            {**object_ref(obj), "snapshot": copy.deepcopy(obj)} for obj in objects
        ],
        "evidence_ledger_projection": {
            "ledger_id": ledger["ledger_id"],
            "revision": ledger["meta"]["revision"],
            "ledger_digest": ledger["meta"]["content_hash"],
            "projection": projection_mode,
            "included_entries": ledger_entries,
            "omitted_entry_count": omitted,
            "append_delta_allowed": operator in {"O1", "O2", "O3"},
        },
        "external_inputs": external,
        "permitted_reads": PERMITTED[operator],
        "forbidden_inputs": FORBIDDEN[operator],
        "selector_decision": selection.as_dict(),
        "expected_output": {"object_kind": KIND[operator], "schema_id": f"P2#/$defs/{KIND[operator]}"},
    }
    packet_hash = sha256_object(packet)
    packet["packet_hash"] = packet_hash
    parents = [object_ref(obj) for obj in objects] + [object_ref(ledger)]
    expected = {
        "object_id": f"{KIND[operator][:2].upper()}-{store.attempt_id}-{branch}",
        "revision": store.next_revision(KIND[operator], branch),
        "branch_id": branch,
        "projection": packet["profile"],
        "packet_hash": packet_hash,
        "independence_condition": independence,
        "asset_seen_in_current_context": operator == "O2" and condition == "PB" and bool(public.get("asset")),
        "parent_refs": parents,
    }
    return packet, expected
