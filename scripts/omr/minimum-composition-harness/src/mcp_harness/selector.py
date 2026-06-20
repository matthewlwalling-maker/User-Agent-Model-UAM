from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .state import StateStore


@dataclass(frozen=True)
class Selection:
    selector_result: str
    selected_operator: str | None
    basis: list[str]
    rejected_operators: list[dict[str, str]]
    next_expected_object: str | None

    def as_dict(self) -> dict[str, Any]:
        return {
            "selector_result": self.selector_result,
            "selected_operator": self.selected_operator,
            "basis": self.basis,
            "rejected_operators": self.rejected_operators,
            "input_packet_manifest": {"allowed_refs": [], "forbidden_inputs": []},
            "next_expected_object": self.next_expected_object,
        }


def infer_explicit_request(fixture: dict[str, Any]) -> str | None:
    req = str(fixture.get("user_request", "")).lower()
    if "map" in req and "coverage" in req:
        return "O3"
    if any(term in req for term in ("choose the smallest fix", "classify the change boundary")):
        return "O4"
    return None


def select(store: StateStore, fixture: dict[str, Any], *, explicit_request: str | None = None, branch: str = "main") -> Selection:
    gc = store.current("GoalContract", branch) or store.current("GoalContract", "main")
    cm = store.current("CapabilityModel", branch)
    cv = store.current("CoverageMap", branch)
    cd = store.current("ChangeDecision", branch)
    rejected: list[dict[str, str]] = []
    basis: list[str] = []

    if cd is not None:
        return Selection("terminal", None, ["current ChangeDecision exists"], [], None)

    goal_needs_owner = gc is None or gc["meta"]["status"] in {"draft", "invalid", "superseded"} or gc["meta"]["freshness"] != "current"
    if goal_needs_owner:
        basis.append("GoalContract missing, noncommitted, invalid, or stale")
        if explicit_request and explicit_request != "O1":
            rejected.append({"operator": explicit_request, "code": "MCP-E100_PREREQUISITE_GOAL", "reason": "GoalContract prerequisite is not committed/current"})
        return Selection("selected", "O1", basis, rejected, "GoalContract")

    if cm is None or cm["meta"]["freshness"] != "current":
        basis.append("GoalContract committed/current and CapabilityModel missing or stale")
        if explicit_request == "O3":
            rejected.append({"operator": "O3", "code": "MCP-E400_O3_BEFORE_O2", "reason": "Coverage cannot run before a committed/current CapabilityModel"})
        elif explicit_request == "O4":
            rejected.append({"operator": "O4", "code": "MCP-E500_O4_WITHOUT_CURRENT_COVERAGE", "reason": "Decision cannot run before capability and coverage state"})
        return Selection("selected", "O2", basis, rejected, "CapabilityModel")

    if cv is None or cv["meta"]["freshness"] != "current":
        if not fixture.get("asset") and not fixture.get("model_A") and not fixture.get("initial_state"):
            return Selection("failure", None, ["asset unavailable for O3"], [], None)
        basis.append("GoalContract and CapabilityModel current; CoverageMap missing or stale")
        if explicit_request == "O4":
            rejected.append({"operator": "O4", "code": "MCP-E500_O4_WITHOUT_CURRENT_COVERAGE", "reason": "Current CoverageMap required"})
        return Selection("selected", "O3", basis, rejected, "CoverageMap")

    readiness = cv.get("overall_o4_readiness", {}).get("status")
    if readiness in {"intervention-ready", "block-only"}:
        basis.append(f"CoverageMap current with O4 readiness={readiness}")
        return Selection("selected", "O4", basis, rejected, "ChangeDecision")
    if readiness == "not-ready":
        rejected.append({"operator": "O4", "code": "MCP-E510_O4_WITHOUT_IMPACT_KNOWLEDGE", "reason": "CoverageMap is not decision-ready"})
        return Selection("failure", None, ["O4 ineligible because impact readiness is not-ready"], rejected, None)
    return Selection("failure", None, ["No operator eligible; malformed readiness state"], rejected, None)
