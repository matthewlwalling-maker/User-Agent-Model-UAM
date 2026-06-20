from __future__ import annotations

from typing import Any

from .state import StateStore, finalize_hash, metadata, object_ref
from .util import sha256_object, sha256_text


def infer_profile(public: dict[str, Any]) -> str:
    text = " ".join([
        str(public.get("user_request", "")),
        " ".join(map(str, public.get("goal_constraints", []) or [])),
        str(public.get("asset", "")),
    ]).lower()
    trivial_signals = ["three-field", "three field", "bounded", "no tools", "no state", "formatter"]
    material_signals = ["write", "ledger", "system", "dependency", "runtime", "agent", "authorization"]
    if sum(s in text for s in trivial_signals) >= 2 and sum(s in text for s in material_signals) == 0:
        return "compact"
    return "material"


def seed_goal(store: StateStore, public: dict[str, Any], *, branch: str = "main", profile: str | None = None) -> dict[str, Any]:
    profile = profile or infer_profile(public)
    required = {
        "id": "OB-PRIMARY",
        "statement": str(public.get("user_request", "Complete the stated objective.")),
        "class": "explicit-required",
        "basis": "Directly stated in the executor-visible user request.",
        "source_refs": ["EV-REQUEST"],
        "confidence": "high",
    }
    constraints = []
    for i, statement in enumerate(public.get("goal_constraints", []) or [], 1):
        constraints.append({
            "id": f"CT-{i}",
            "statement": str(statement),
            "basis": "Directly supplied executor-visible constraint.",
            "source_refs": [f"EV-CONSTRAINT-{i}"],
        })
    ledger = store.ledger()
    obj = {
        "meta": metadata(
            object_id=f"GC-{store.attempt_id}", kind="GoalContract", revision=store.next_revision("GoalContract", branch),
            branch=branch, producer="import", projection=profile, parent_refs=[object_ref(ledger)],
            evidence_refs=["EV-REQUEST"] + [f"EV-CONSTRAINT-{i}" for i in range(1, len(constraints) + 1)],
        ),
        "target_ref": str(public.get("asset_version") or store.attempt_id),
        "outcome_statement": str(public.get("user_request", "Complete the stated objective.")),
        "obligations": [required],
        "constraints": constraints,
        "assessment_profile": profile,
        "profile_basis": "Seeded from public fixture state for a prerequisite explicitly declared as already committed.",
        "unresolved_ambiguities": [],
        "freeze_state": "committed",
        "requested_claim": str(public.get("evidence_stage", "design-time")),
        "authorized_decision_scope": "assess",
        "alternative_interpretations": [],
        "excluded_methods": [],
    }
    obj = finalize_hash(obj)
    store.add(obj)
    return obj


def seed_capability(
    store: StateStore, gc: dict[str, Any], behavior: str, *, branch: str = "main",
    cap_id: str = "CAP-PRIMARY", condition: str = "packet-boundary",
) -> dict[str, Any]:
    req_obs = [o["id"] for o in gc["obligations"] if o["class"] in {"explicit-required", "entailed-required"}]
    packet_hash = sha256_object({"goal_contract_ref": object_ref(gc), "behavior": behavior, "branch": branch})
    ledger = store.ledger()
    obj = {
        "meta": metadata(
            object_id=f"CM-{store.attempt_id}-{branch}", kind="CapabilityModel",
            revision=store.next_revision("CapabilityModel", branch), branch=branch, producer="import",
            projection=gc["assessment_profile"], parent_refs=[object_ref(gc), object_ref(ledger)],
            evidence_refs=list(gc["meta"].get("evidence_refs", [])),
        ),
        "goal_contract_ref": object_ref(gc),
        "capabilities": [{
            "id": cap_id,
            "behavior": behavior,
            "obligation_refs": req_obs,
            "success_condition": "The stated behavior is materially established at the available evidence stage.",
            "scope_boundary": "Limited to the supplied capability derivation; no asset coverage claim is embedded.",
            "confidence": "medium",
            "requiredness": "required",
        }],
        "obligation_coverage": [{"obligation_ref": ob, "capability_refs": [cap_id]} for ob in req_obs],
        "derivation_boundary": {
            "condition": condition,
            "input_packet_hash": packet_hash,
            "permitted_input_types": ["goal-contract", "goal-evidence", "constraint-evidence"],
            "forbidden_input_types": ["asset-decomposition", "asset-section-labels", "coverage-judgments", "proposed-edits"],
            "asset_seen_in_current_context": condition == "packet-boundary",
            "asset_component_terms_used": [],
        },
        "model_completeness": "candidate-complete",
        "open_questions": [],
        "capability_relations": [],
        "alternative_model_refs": [],
        "nonrequired_opportunities": [],
        "sufficiency_rationale": "Imported from an executor-visible capability-model fixture without changing its substantive claim.",
    }
    obj = finalize_hash(obj)
    store.add(obj)
    return obj


def seed_full_coverage(
    store: StateStore, public: dict[str, Any], gc: dict[str, Any], cm: dict[str, Any], *, branch: str = "main",
    readiness: str = "intervention-ready",
) -> dict[str, Any]:
    ledger = store.ledger()
    asset_text = str(public.get("asset", public.get("initial_state", "Supplied assessment state")))
    version = str(public.get("asset_version", "supplied-state"))
    coverage_entries = []
    for cap in cm["capabilities"]:
        coverage_entries.append({
            "capability_ref": cap["id"],
            "classification": "full-at-stage",
            "asset_behavior_refs": ["fixture.initial_state"],
            "evidence_refs": ["EV-INITIAL-STATE"] if any(e["evidence_id"] == "EV-INITIAL-STATE" for e in ledger["entries"]) else ["EV-ASSET"],
            "rationale": "The executor-visible supplied state declares the assessment facts as valid at design time.",
            "confidence": "medium",
            "unresolved_evidence": [],
        })
    obj = {
        "meta": metadata(
            object_id=f"CV-{store.attempt_id}-{branch}", kind="CoverageMap",
            revision=store.next_revision("CoverageMap", branch), branch=branch, producer="import",
            projection=gc["assessment_profile"], parent_refs=[object_ref(gc), object_ref(cm), object_ref(ledger)],
            evidence_refs=[e for e in ["EV-INITIAL-STATE", "EV-ASSET"] if any(x["evidence_id"] == e for x in ledger["entries"])],
        ),
        "capability_model_ref": object_ref(cm),
        "goal_contract_ref": object_ref(gc),
        "asset_ref": {"asset_id": str(public.get("asset_version", store.attempt_id)), "version": version, "content_hash": sha256_text(asset_text)},
        "evidence_ledger_ref": object_ref(ledger),
        "coverage_entries": coverage_entries,
        "gap_entries": [],
        "impact_assessments": [],
        "assessment_stage": str(public.get("evidence_stage", "design-time")),
        "overall_o4_readiness": {"status": readiness, "blocking_gap_refs": [], "basis": "Supplied state is sufficient for a terminal evidence/authority decision."},
        "strengths_to_preserve": [],
        "failure_scenarios": [],
        "branch_comparison": [],
    }
    obj = finalize_hash(obj)
    store.add(obj)
    return obj


def prepare_public_initial_state(store: StateStore, public: dict[str, Any], condition: str) -> dict[str, Any]:
    notes: list[dict[str, Any]] = []
    initial = str(public.get("initial_state", ""))
    if "Committed GoalContract exists" in initial:
        seed_goal(store, public, profile="material")
    elif "Draft GoalContract" in initial:
        store.incoming_invalid.append({"kind": "GoalContract", "reason": initial, "code": "MCP-E110_REQUIREDNESS_BASIS_MISSING"})
        notes.append({"type": "incoming-invalid-state", "code": "MCP-E110_REQUIREDNESS_BASIS_MISSING", "description": initial})
    if "forbidden field" in str(public.get("asset", "")):
        store.incoming_invalid.append({"kind": "CoverageMap", "reason": "Non-owner draft contains recommended_action", "code": "MCP-E430_O3_INTERVENTION_WRITE"})
        notes.append({"type": "rejected-state", "code": "MCP-E430_O3_INTERVENTION_WRITE", "description": "Draft CoverageMap action field rejected before use."})
    if "CoverageMap is design-time" in initial:
        gc = seed_goal(store, public, profile="material")
        cm = seed_capability(store, gc, "Maintain truthful evidence-stage claims without promotion by handoff wording.", condition="packet-boundary")
        seed_full_coverage(store, public, gc, cm)
    if "valid CoverageMap" in str(public.get("asset", "")) or "valid CoverageMap" in initial:
        gc = seed_goal(store, public, profile="material")
        cm = seed_capability(store, gc, "Respect assessment authority and stop before unowned target-architecture or implementation work.", condition="packet-boundary")
        seed_full_coverage(store, public, gc, cm)
    if public.get("model_A") and public.get("model_B"):
        gc = seed_goal(store, public, profile="material")
        a = seed_capability(store, gc, str(public["model_A"]), branch="model-A", cap_id="CAP-MODEL-A", condition="separate-context" if condition == "SC" else "packet-boundary")
        b = seed_capability(store, gc, str(public["model_B"]), branch="model-B", cap_id="CAP-MODEL-B", condition="separate-context" if condition == "SC" else "packet-boundary")
        # Branch identity is preserved without a circular content-hash reference.
        # O4 receives both exact branch snapshots for explicit comparison.
    return {"notes": notes}
