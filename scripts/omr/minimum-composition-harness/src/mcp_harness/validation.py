from __future__ import annotations

from typing import Any

from .state import StateStore, object_ref


def semantic_validate_operator(operator: str, state: dict[str, Any], store: StateStore, public: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    ledger_ids = {e["evidence_id"] for e in store.ledger()["entries"]}
    missing_evidence = [e for e in state["meta"].get("evidence_refs", []) if e not in ledger_ids]
    if missing_evidence:
        errors.append(f"MCP-E030_UNKNOWN_EVIDENCE_REF: {missing_evidence}")

    def exact_ref_matches(ref: dict[str, Any], candidates: list[dict[str, Any]]) -> bool:
        return any(ref == object_ref(candidate) for candidate in candidates)
    if operator == "O1":
        required = [o for o in state["obligations"] if o["class"] in {"explicit-required", "entailed-required"}]
        if not required:
            errors.append("MCP-E110_REQUIREDNESS_BASIS_MISSING: no required obligation")
        for ob in state["obligations"]:
            if ob["class"] == "entailed-required" and not ob.get("basis"):
                errors.append(f"MCP-E110_REQUIREDNESS_BASIS_MISSING: {ob['id']}")
            unknown = sorted(set(ob.get("source_refs", [])) - ledger_ids)
            if unknown:
                errors.append(f"MCP-E030_UNKNOWN_EVIDENCE_REF: {ob['id']} -> {unknown}")
        for constraint in state["constraints"]:
            unknown = sorted(set(constraint.get("source_refs", [])) - ledger_ids)
            if unknown:
                errors.append(f"MCP-E030_UNKNOWN_EVIDENCE_REF: {constraint['id']} -> {unknown}")
    elif operator == "O2":
        gc_candidates = store.currents("GoalContract")
        if not exact_ref_matches(state["goal_contract_ref"], gc_candidates):
            errors.append("MCP-E020_PARENT_REF_MISMATCH: CapabilityModel.goal_contract_ref")
        caps = {c["id"]: c for c in state["capabilities"]}
        required_obs = {
            o["id"] for o in (store.current("GoalContract", "main") or {}).get("obligations", [])
            if o["class"] in {"explicit-required", "entailed-required"}
        }
        traced = {row["obligation_ref"] for row in state["obligation_coverage"] if row["capability_refs"]}
        if required_obs - traced:
            errors.append(f"MCP-E210_INCOMPLETE_BIDIRECTIONAL_TRACE: {sorted(required_obs-traced)}")
        if state["derivation_boundary"].get("asset_component_terms_used"):
            errors.append("MCP-E220_INDEPENDENCE_CONTAMINATION")
        for cap in caps.values():
            if not cap["obligation_refs"]:
                errors.append(f"MCP-E210_UNTRACED_CAPABILITY: {cap['id']}")
    elif operator == "O3":
        if not exact_ref_matches(state["goal_contract_ref"], store.currents("GoalContract")):
            errors.append("MCP-E020_PARENT_REF_MISMATCH: CoverageMap.goal_contract_ref")
        if not exact_ref_matches(state["capability_model_ref"], store.currents("CapabilityModel")):
            errors.append("MCP-E020_PARENT_REF_MISMATCH: CoverageMap.capability_model_ref")
        for coverage in state["coverage_entries"]:
            refs = coverage.get("evidence_refs", [])
            if not refs:
                errors.append(f"MCP-E330_COVERAGE_WITHOUT_EVIDENCE: {coverage['capability_ref']}")
            unknown = sorted(set(refs) - ledger_ids)
            if unknown:
                errors.append(f"MCP-E030_UNKNOWN_EVIDENCE_REF: {coverage['capability_ref']} -> {unknown}")
            if coverage["classification"] != "unknown-insufficient-evidence" and not coverage.get("asset_behavior_refs"):
                errors.append(f"MCP-E330_COVERAGE_WITHOUT_BEHAVIOR_REF: {coverage['capability_ref']}")
        impacts = state["impact_assessments"]
        for impact in impacts:
            for fact in impact.get("propagation_facts", []):
                unknown = sorted(set(fact.get("evidence_refs", [])) - ledger_ids)
                if unknown:
                    errors.append(f"MCP-E030_UNKNOWN_EVIDENCE_REF: impact {impact['gap_ref']} -> {unknown}")
            if impact["impact_job_required"] and impact["o4_readiness"] != "block-only":
                errors.append(f"MCP-E421_IMPACT_JOB_NOT_BLOCK_ONLY: {impact['gap_ref']}")
            if impact["change_reach"] == "unknown" and impact["o4_readiness"] == "intervention-ready":
                errors.append(f"MCP-E420_UNKNOWN_REACH_MARKED_READY: {impact['gap_ref']}")
        if state["overall_o4_readiness"]["status"] == "intervention-ready":
            if any(i["o4_readiness"] != "intervention-ready" for i in impacts):
                errors.append("MCP-E420_OVERALL_READINESS_CONFLICT")

        # Enforce the decisive dependency-impact boundary from public facts, not evaluator secrets.
        dep = str(public.get("dependency_map", "")).strip().lower()
        if state["gap_entries"] and dep in {"unavailable", "unavailable.", "none", "not supplied"}:
            if not impacts:
                errors.append("MCP-E422_MISSING_IMPACT_BLOCK_FOR_UNKNOWN_DEPENDENCIES")
            for impact in impacts:
                if not impact["impact_job_required"] or impact["o4_readiness"] != "block-only":
                    errors.append(f"MCP-E422_UNKNOWN_DEPENDENCIES_MUST_BLOCK: {impact['gap_ref']}")
            if state["overall_o4_readiness"]["status"] != "block-only":
                errors.append("MCP-E422_OVERALL_UNKNOWN_DEPENDENCIES_MUST_BLOCK")
        if state["gap_entries"] and "second-degree" in dep:
            if not any(i["second_degree_or_broader_refs"] for i in impacts):
                errors.append("MCP-E423_EXPLICIT_SECOND_DEGREE_FACT_OMITTED")
            # Explicit second-degree facts do not always mean the proposed change itself
            # reaches those consumers. C08A-style fixtures expose systemic consumers so O3
            # can preserve success semantics while classifying a confirmation-only patch.
            # The hard requirement here is disclosure of the broader refs; O4 then maps
            # immutable reach facts to a bounded addition or restructure.
    elif operator == "O4":
        cvs = store.currents("CoverageMap")
        if not exact_ref_matches(state["coverage_map_ref"], cvs):
            errors.append("MCP-E020_PARENT_REF_MISMATCH: ChangeDecision.coverage_map_ref")
        if any(cv["overall_o4_readiness"]["status"] == "block-only" for cv in cvs):
            if state["decision"] != "blocked-by-insufficient-impact-knowledge":
                errors.append("MCP-E510_O4_WITHOUT_IMPACT_KNOWLEDGE")
        if state["decision"] == "bounded-capability-addition":
            impacts = [i for cv in cvs for i in cv["impact_assessments"]]
            target_refs = set(state.get("target_gap_refs", []))
            relevant = [i for i in impacts if not target_refs or i["gap_ref"] in target_refs]
            allowed_reach = {"named-elements-only", "n-plus-1"}
            if (
                not relevant
                or any(i["change_reach"] not in allowed_reach or i["o4_readiness"] != "intervention-ready" for i in relevant)
                or any(i["change_reach"] == "broader-than-n-plus-1" for i in impacts if i["gap_ref"] in target_refs)
            ):
                errors.append("MCP-E520_INVALID_BOUNDED_ADDITION")
        if state["evidence_ceiling"] != str(public.get("evidence_stage", "design-time")):
            stages = ["design-time", "simulated", "live-runtime", "post-implementation", "production-observed"]
            if stages.index(state["evidence_ceiling"]) > stages.index(str(public.get("evidence_stage", "design-time"))):
                errors.append("MCP-E610_EVIDENCE_PROMOTION")
    return errors
