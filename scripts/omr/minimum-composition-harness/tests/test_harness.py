from __future__ import annotations

import json
from pathlib import Path

import yaml

from mcp_harness.blinding import generate_system_key
from mcp_harness.config import load_config
from mcp_harness.fixtures import load_executor_fixtures
from mcp_harness.schemas import SchemaRegistry, count_optional_properties
from mcp_harness.seeding import prepare_public_initial_state, seed_goal
from mcp_harness.selector import select
from mcp_harness.sources import verify_sources
from mcp_harness.state import StateStore, finalize_hash, metadata, object_ref, seed_ledger
from mcp_harness.validation import semantic_validate_operator


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_DIR = ROOT / "authorities_current"
FIXTURE_VIEW = AUTHORITY_DIR / "P5_Executor_View_v0.1.yaml"


def pilot_config(tmp_path: Path) -> Path:
    raw = yaml.safe_load((ROOT / "configs/manual_pilot.example.yaml").read_text())
    raw["run_series_id"] = "test-run"
    raw["paths"]["authority_dir"] = str(AUTHORITY_DIR)
    raw["paths"]["fixture_view"] = str(FIXTURE_VIEW)
    raw["paths"]["output_root"] = str(tmp_path / "runs")
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(raw, sort_keys=False))
    return path


def test_source_freeze_clean(tmp_path):
    cfg = load_config(pilot_config(tmp_path))
    result = verify_sources(cfg.authority_dir, cfg.fixture_view)
    assert result.ok, result.errors


def test_fixture_expansion_has_variants():
    fixtures = load_executor_fixtures(FIXTURE_VIEW)
    ids = {f.cell_id for f in fixtures}
    assert {"C08A", "C08B", "C09A", "C09B"} <= ids
    assert len(fixtures) == 14


def test_selector_rejects_o3_before_o2(tmp_path):
    schemas = SchemaRegistry(AUTHORITY_DIR / "P2_State_Schemas_v0.1.json")
    public = {
        "user_request": "Map this asset's coverage now.",
        "goal_constraints": ["Safely execute and confirm an update."],
        "asset_version": "v1",
        "asset": "asset",
        "evidence_stage": "design-time",
        "initial_state": "Committed GoalContract exists; CapabilityModel is absent; asset is supplied.",
    }
    store = StateStore(schemas, "attempt", "material")
    store.add(seed_ledger("attempt", public, "material"))
    prepare_public_initial_state(store, public, "PB")
    sel = select(store, public, explicit_request="O3")
    assert sel.selected_operator == "O2"
    assert any(r["code"] == "MCP-E400_O3_BEFORE_O2" for r in sel.rejected_operators)


def test_blinding_is_deterministic():
    cells = [("C01", "PB", 1), ("C01", "SC", 1)]
    assert generate_system_key(cells, 42) == generate_system_key(cells, 42)
    key = generate_system_key(cells, 42)
    cell = key["cells"]["C01__PB__r1"]
    assert {cell["A"], cell["B"]} == {"operator", "legacy"}


def test_operator_schema_is_constructible():
    schemas = SchemaRegistry(AUTHORITY_DIR / "P2_State_Schemas_v0.1.json")
    schema = schemas.operator_output_schema("O2", {
        "object_id": "CM-test-main", "revision": 1, "branch_id": "main", "projection": "material",
        "packet_hash": "a" * 64, "independence_condition": "separate-context", "asset_seen_in_current_context": False,
        "parent_refs": [],
    })
    state_schema = schema["properties"]["state_object"]
    assert state_schema["type"] == "object"
    assert state_schema["properties"]["meta"]["properties"] == {}
    assert set(state_schema["properties"]["derivation_boundary"]["properties"]) == {"asset_component_terms_used"}
    assert "$defs" not in schema
    assert "$ref" not in json.dumps(schema)
    assert "contains" not in json.dumps(schema)
    assert "if" not in json.dumps(schema)
    assert count_optional_properties(schema) == 0


def test_operator_prompt_names_goal_constraint_id_pattern():
    from mcp_harness.prompts import operator_system

    blocks = operator_system(AUTHORITY_DIR, "O1", "none")
    prompt = "\n".join(block["text"] for block in blocks)
    assert "OB-1" in prompt
    assert "never OBL-1" in prompt
    assert "CT-1" in prompt
    assert "never CON-1" in prompt
    assert "O1-O3" in prompt
    assert "asset_component_terms_used must be empty" in prompt
    assert "obligation_refs" in prompt
    assert "obligation_coverage" in prompt
    assert "only OB-* IDs" in prompt
    assert "CT-* constraint IDs" in prompt
    assert "never appear in obligation_refs" in prompt
    assert "including absent coverage" in prompt
    assert "unknown-insufficient-evidence" in prompt
    assert "ChangeDecision.stop_reason" in prompt
    assert "stop.code" in prompt
    assert "stop.reason" in prompt
    assert "non-empty strings" in prompt


def _minimal_state(kind: str, object_id: str, producer: str, extra: dict) -> dict:
    obj = {"meta": metadata(object_id=object_id, kind=kind, revision=1, branch="main", producer=producer, projection="material"), **extra}
    return finalize_hash(obj)


def test_o4_bounded_addition_allows_named_and_n_plus_one_reach(tmp_path):
    schemas = SchemaRegistry(AUTHORITY_DIR / "P2_State_Schemas_v0.1.json")
    public = {
        "user_request": "Assess whether Agent Spec v1 is complete.",
        "goal_constraints": ["Only approved adjustments may be written."],
        "asset_version": "agent-spec-v1",
        "asset": "asset",
        "evidence_stage": "design-time",
    }
    store = StateStore(schemas, "attempt", "material")
    store.add(seed_ledger("attempt", public, "material"))
    coverage = _minimal_state("CoverageMap", "CO-test-main", "O3", {
        "overall_o4_readiness": {"status": "intervention-ready", "blocking_gap_refs": [], "basis": "Ready."},
        "impact_assessments": [
            {"gap_ref": "GAP-1", "change_reach": "n-plus-1", "o4_readiness": "intervention-ready"},
            {"gap_ref": "GAP-2", "change_reach": "named-elements-only", "o4_readiness": "intervention-ready"},
        ],
    })
    store.add(coverage, validate=False)
    decision = {
        "meta": {},
        "coverage_map_ref": object_ref(coverage),
        "decision": "bounded-capability-addition",
        "target_gap_refs": ["GAP-1", "GAP-2"],
        "evidence_ceiling": "design-time",
    }
    errors = semantic_validate_operator("O4", decision, store, public)
    assert "MCP-E520_INVALID_BOUNDED_ADDITION" not in errors


def test_o3_second_degree_refs_do_not_force_systemic_reach_when_preserved(tmp_path):
    schemas = SchemaRegistry(AUTHORITY_DIR / "P2_State_Schemas_v0.1.json")
    public = {
        "user_request": "Add a missing confirmation requirement near writeback.",
        "goal_constraints": ["Preserve safe write authorization and consistent success semantics."],
        "asset_version": "writeback-system-v4",
        "asset": "The canonical WriteResult contract is defined beside the core writeback instruction.",
        "dependency_map": "WriteResult is consumed by orchestrator -> tool adapter -> retry controller -> rollback controller -> audit compiler -> user output. Changing success semantics requires schema and interface revisions across second-degree consumers.",
        "evidence_stage": "design-time",
    }
    store = StateStore(schemas, "attempt", "material")
    store.add(seed_ledger("attempt", public, "material"))
    goal = _minimal_state("GoalContract", "GO-test-main", "O1", {"obligations": [], "constraints": []})
    caps = _minimal_state("CapabilityModel", "CA-test-main", "O2", {"capabilities": []})
    store.add(goal, validate=False)
    store.add(caps, validate=False)
    coverage = {
        "meta": {},
        "goal_contract_ref": object_ref(goal),
        "capability_model_ref": object_ref(caps),
        "coverage_entries": [{
            "capability_ref": "CAP-1",
            "classification": "absent",
            "evidence_refs": ["EV-ASSET"],
            "asset_behavior_refs": ["EV-ASSET"],
        }],
        "gap_entries": [{"gap_id": "GAP-1"}],
        "impact_assessments": [{
            "gap_ref": "GAP-1",
            "change_reach": "n-plus-1",
            "o4_readiness": "intervention-ready",
            "impact_job_required": False,
            "second_degree_or_broader_refs": ["tool adapter", "retry controller", "rollback controller", "audit compiler", "user output"],
            "propagation_facts": [{"evidence_refs": ["EV-DEPENDENCY"]}],
        }],
        "overall_o4_readiness": {"status": "intervention-ready", "blocking_gap_refs": [], "basis": "Second-degree refs disclosed; success semantics preserved."},
    }
    errors = semantic_validate_operator("O3", coverage, store, public)
    assert "MCP-E423_EXPLICIT_SECOND_DEGREE_FACT_OMITTED" not in errors
    assert "MCP-E423_EXPLICIT_SYSTEMIC_REACH_UNDERCLASSIFIED" not in errors

from mcp_harness.fixtures import Fixture
from mcp_harness.operator_runner import run_operator_attempt
from mcp_harness.legacy_runner import run_legacy_attempt
from mcp_harness.provider import ProviderResult
from mcp_harness.util import sha256_text, utc_now


class DeterministicMockProvider:
    """Exercises orchestration and validation only; never represents model capability."""

    def __init__(self, p2_path: Path):
        self.registry = json.loads(p2_path.read_text(encoding="utf-8"))
        self.counter = 0

    @staticmethod
    def _ref(obj):
        m = obj["meta"]
        return {k: m[k] for k in ("object_id", "object_kind", "revision", "branch_id", "content_hash")}

    @staticmethod
    def _packet(messages):
        text = messages[-1]["content"]
        return json.loads(text[text.index("{"):])

    @staticmethod
    def _fixed_meta(output_schema, kind):
        del output_schema, kind
        return {}

    def invoke(self, *, system, messages, max_tokens, output_schema=None, context_id=None, preflight=True):
        self.counter += 1
        started = utc_now()
        if output_schema is None:
            text = (
                "Scaling gate: Material — mock orchestration validation only.\n"
                "Goal Model and Independent Required Capability Model complete.\n"
                "— Independent capability model complete; asset assessment begins below. —\n"
                "Coverage assessment complete. Evidence stage: design-time.\n"
                "No material change needed. Verification remains required for runtime claims."
            )
            return ProviderResult(
                context_id=context_id or f"mock-{self.counter}", request={"messages": messages},
                response={"content": [{"type": "text", "text": text}], "usage": {"input_tokens": 10, "output_tokens": 10}},
                text=text, parsed_json=None, usage={"input_tokens": 10, "output_tokens": 10},
                preflight_input_tokens=10, wall_latency_ms=1, model_latency_ms=None, error=None,
                started_at=started, ended_at=utc_now(),
            )
        packet = self._packet(messages)
        operator = packet["operator_id"]
        kind = packet["requested_output_kind"]
        meta = self._fixed_meta(output_schema, kind)
        inputs = [x["snapshot"] for x in packet["input_objects"]]
        by_kind = {}
        for obj in inputs:
            by_kind.setdefault(obj["meta"]["object_kind"], []).append(obj)
        if operator == "O1":
            intake = packet["external_inputs"][0]
            obs = [{
                "id": "OB-PRIMARY", "statement": intake["user_request"], "class": "explicit-required",
                "basis": "Direct request.", "source_refs": ["EV-REQUEST"], "confidence": "high",
            }]
            constraints = [{
                "id": f"CT-{i}", "statement": str(v), "basis": "Direct constraint.",
                "source_refs": [f"EV-CONSTRAINT-{i}"],
            } for i, v in enumerate(intake.get("goal_constraints", []), 1)]
            state = {
                "meta": meta, "target_ref": packet["run_id"], "outcome_statement": intake["user_request"],
                "obligations": obs, "constraints": constraints, "assessment_profile": packet["profile"],
                "profile_basis": "Mock path exercises schema and orchestration.", "unresolved_ambiguities": [],
                "freeze_state": "committed", "requested_claim": intake["evidence_stage"],
                "authorized_decision_scope": "assess", "alternative_interpretations": [], "excluded_methods": [],
            }
        elif operator == "O2":
            gc = by_kind["GoalContract"][0]
            cap = {
                "id": "CAP-PRIMARY", "behavior": "Satisfy the committed required outcome.",
                "obligation_refs": [o["id"] for o in gc["obligations"] if o["class"] in {"explicit-required", "entailed-required"}],
                "success_condition": "Required behavior is established.", "scope_boundary": "No coverage claim.",
                "confidence": "medium", "requiredness": "required",
            }
            state = {
                "meta": meta, "goal_contract_ref": self._ref(gc), "capabilities": [cap],
                "obligation_coverage": [{"obligation_ref": x, "capability_refs": ["CAP-PRIMARY"]} for x in cap["obligation_refs"]],
                "derivation_boundary": {
                    "condition": packet["independence_condition"], "input_packet_hash": packet["packet_hash"],
                    "permitted_input_types": ["goal-contract", "goal-evidence"],
                    "forbidden_input_types": ["asset-decomposition", "asset-section-labels", "coverage-judgments", "proposed-edits"],
                    "asset_seen_in_current_context": packet["independence_condition"] == "packet-boundary" and any("Prior broader-context" in str(m.get("content")) for m in messages),
                    "asset_component_terms_used": [],
                },
                "model_completeness": "candidate-complete", "open_questions": [], "capability_relations": [],
                "alternative_model_refs": [], "nonrequired_opportunities": [],
                "sufficiency_rationale": "Mock candidate completeness for harness testing.",
            }
        elif operator == "O3":
            gc = by_kind["GoalContract"][0]; cm = by_kind["CapabilityModel"][0]
            asset_input = next(x for x in packet["external_inputs"] if x["type"] == "asset")
            state = {
                "meta": meta, "capability_model_ref": self._ref(cm), "goal_contract_ref": self._ref(gc),
                "asset_ref": {"asset_id": str(asset_input.get("asset_version") or "asset"), "version": str(asset_input.get("asset_version") or "v1"), "content_hash": sha256_text(str(asset_input.get("asset") or ""))},
                "evidence_ledger_ref": {"object_id": "EL-placeholder", "object_kind": "EvidenceLedger", "revision": 1, "branch_id": "main", "content_hash": "0" * 64},
                "coverage_entries": [{
                    "capability_ref": c["id"], "classification": "full-at-stage", "asset_behavior_refs": ["asset"],
                    "evidence_refs": ["EV-ASSET"], "rationale": "Mock full coverage for orchestration validation.",
                    "confidence": "medium", "unresolved_evidence": [],
                } for c in cm["capabilities"]],
                "gap_entries": [], "impact_assessments": [], "assessment_stage": "design-time",
                "overall_o4_readiness": {"status": "intervention-ready", "blocking_gap_refs": [], "basis": "No material gaps in mock path."},
                "strengths_to_preserve": ["mock-covered behavior"], "failure_scenarios": [], "branch_comparison": [],
            }
        else:
            cv = by_kind["CoverageMap"][0]
            state = {
                "meta": meta, "coverage_map_ref": self._ref(cv), "decision": "no-material-change",
                "target_gap_refs": [], "selected_fix_layer": "not-applicable",
                "change_boundary": {"touched_element_refs": [], "preserved_element_refs": ["assessed asset"], "allowed_neighbor_changes": [], "prohibited_propagation": [], "change_reach": "none", "uncertainty": []},
                "decision_basis": "Mock coverage is complete at design time.", "evidence_ceiling": "design-time",
                "verification_required": ["Runtime verification remains outside this mock."],
                "stop_reason": "Terminal assessment decision reached.", "confidence": "medium",
                "next_consumer_contract": {"consumer_type": "independent-evaluator", "required_inputs": [cv["meta"]["object_id"]]},
                "alternatives_rejected": [], "severity": "low", "residual_risks": [], "optional_opportunities": [],
            }
        payload = {
            "validation": {"status": "valid", "errors": []}, "state_object": state,
            "ledger_append_delta": [], "stop": {"scope": "global" if operator == "O4" else "local", "code": "MOCK", "reason": "Mock orchestration validation."},
            "visible_answer": "No material change needed at design time; runtime verification remains required." if operator == "O4" else "",
        }
        text = json.dumps(payload)
        return ProviderResult(
            context_id=context_id or f"mock-{self.counter}", request={"messages": messages},
            response={"content": [{"type": "text", "text": text}], "usage": {"input_tokens": 10, "output_tokens": 10}},
            text=text, parsed_json=payload, usage={"input_tokens": 10, "output_tokens": 10},
            preflight_input_tokens=10, wall_latency_ms=1, model_latency_ms=None, error=None,
            started_at=started, ended_at=utc_now(),
        )


def test_full_mock_orchestration_pb_and_sc(tmp_path):
    cfg = load_config(pilot_config(tmp_path))
    schemas = SchemaRegistry(AUTHORITY_DIR / "P2_State_Schemas_v0.1.json")
    fixture = load_executor_fixtures(FIXTURE_VIEW)[0]
    provider = DeterministicMockProvider(AUTHORITY_DIR / "P2_State_Schemas_v0.1.json")
    for condition in ("PB", "SC"):
        op = run_operator_attempt(cfg, fixture, condition, 1, provider, schemas)
        leg = run_legacy_attempt(cfg, fixture, condition, 1, provider)
        assert op["status"] == "completed", op
        assert leg["status"] == "completed", leg
        op_dir = cfg.run_root / "attempts" / op["attempt_id"]
        assert (op_dir / "selector_records.json").exists()
        assert (op_dir / "all_state_revisions.json").exists()
        proofs = list((op_dir / "steps").glob("*/context_proof.json"))
        assert proofs
        o2_proof = next(json.loads(p.read_text()) for p in proofs if "_O2_" in str(p.parent.name))
        assert o2_proof["valid"] is True
        if condition == "SC":
            assert o2_proof["asset_text_present_anywhere"] is False
        else:
            assert o2_proof["prior_asset_exposure_observed"] is True
            assert o2_proof["asset_text_present_in_immediate_packet"] is False


def test_all_operator_transport_schemas_are_stable_and_nonoptional():
    schemas = SchemaRegistry(AUTHORITY_DIR / "P2_State_Schemas_v0.1.json")
    expected_a = {
        "object_id": "X-a", "revision": 1, "branch_id": "main", "projection": "material",
        "packet_hash": "a" * 64, "independence_condition": "separate-context",
        "asset_seen_in_current_context": False, "parent_refs": [],
    }
    expected_b = {
        **expected_a,
        "object_id": "X-b", "revision": 7, "branch_id": "branch-b", "packet_hash": "b" * 64,
        "independence_condition": "packet-boundary", "asset_seen_in_current_context": True,
    }
    for operator in ("O1", "O2", "O3", "O4"):
        a = schemas.operator_output_schema(operator, expected_a)
        b = schemas.operator_output_schema(operator, expected_b)
        encoded = json.dumps(a, sort_keys=True)
        assert a == b  # stable grammar; runtime IDs and hashes are code-owned
        assert count_optional_properties(a) == 0
        for forbidden in ('"$ref"', '"$defs"', '"allOf"', '"if"', '"then"', '"contains"'):
            assert forbidden not in encoded


def test_evaluator_first_pass_withholds_identity_key(tmp_path):
    from mcp_harness.exporter import build_evaluator_packets
    from mcp_harness.util import atomic_write_json, atomic_write_text

    cfg = load_config(pilot_config(tmp_path))
    fixture = load_executor_fixtures(FIXTURE_VIEW)[0]
    for system, visible in (("operator", "Visible output one."), ("legacy", "Visible output two.")):
        attempt_id = f"{cfg.run_series_id}__{fixture.cell_id}__PB__r1__{system}"
        path = cfg.run_root / "attempts" / attempt_id
        path.mkdir(parents=True, exist_ok=True)
        atomic_write_json(path / "attempt_summary.json", {"status": "completed", "system": system, "attempt_id": attempt_id})
        atomic_write_text(path / "visible_answer.txt", visible)
    key = generate_system_key([(fixture.cell_id, "PB", 1)], 5)
    packets = build_evaluator_packets(cfg, [fixture], key)
    first_text = "\n".join(p.read_text(encoding="utf-8") for p in packets["first_pass"].rglob("*") if p.is_file())
    trace_names = {p.name for p in packets["trace_audit"].rglob("*") if p.is_file()}
    assert "system_key" not in first_text
    assert '"system": "operator"' not in first_text
    assert '"system": "legacy"' not in first_text
    assert "system_key.json" not in trace_names
    assert (packets["diagnostic"] / "system_key.json").exists()


def test_interrupted_attempt_is_archived(tmp_path):
    from mcp_harness.storage import AttemptWriter
    first = AttemptWriter(tmp_path, "attempt-1")
    first.write_text("partial.txt", "partial")
    second = AttemptWriter(tmp_path, "attempt-1")
    assert second.path.exists()
    archives = list((tmp_path / "interrupted_attempts").glob("attempt-1__*"))
    assert len(archives) == 1
    assert (archives[0] / "partial.txt").read_text() == "partial"


def test_resume_rejects_codex_runtime_drift(tmp_path):
    from mcp_harness.orchestrator import initialize_run
    from mcp_harness.util import atomic_write_json

    cfg = load_config(pilot_config(tmp_path))
    fixtures = load_executor_fixtures(FIXTURE_VIEW)[:1]
    first_report = {
        "codex_check": {
            "binary_resolved": "C:/Tools/codex.exe",
            "version": "codex-cli 1.2.3",
        }
    }
    initialize_run(cfg, fixtures, first_report)

    changed_report = {
        "codex_check": {
            "binary_resolved": "C:/Tools/codex.exe",
            "version": "codex-cli 1.2.4",
        }
    }
    import pytest
    with pytest.raises(RuntimeError, match="Codex runtime changed"):
        initialize_run(cfg, fixtures, changed_report)
