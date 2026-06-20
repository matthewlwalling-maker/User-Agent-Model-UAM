# Compression Map v0.1

Date: 2026-06-18
Candidate root: `Context Resources/Runtime/Compressed_Candidate_v0.1/`
Original-source handling: originals remain unchanged in place; no replacement or deletion performed.

## Original to Candidate Trace

| Original source | Classification | Candidate / disposition | Load-bearing content preserved |
|---|---|---|---|
| `AGENTS.md` | Core Instructions | `Compressed_Candidate_v0.1/AGENTS.md` | thin-root role, source lookup, read/write safety, AB/O boundary, evidence ceilings, sentinel retest gate |
| `Context Resources/00_Agent_Builder_Deployment_Manifest_and_Authority_Map_v1.0.md` | Runtime Resource | `AB_Runtime_Authority_Reference_v1.1.md` | package purpose, authority order, locked decisions, release limits, Yellow caveats |
| `Core Instructions/01_Agent_Builder_Core_Router_v1.0.md` | Runtime Resource / Core Router | `AB_Runtime_Authority_Reference_v1.1.md` | PM recognition, anchored parsing, defaults, dispatch, malformed invocation behavior |
| `Context Resources/02_Agent_Builder_Component_Registry_v1.0.md` | Runtime Resource / Legal Registry | `AB_Runtime_Authority_Reference_v1.1.md` | exact modes, lenses, evidence stages, actions, V1-V8 validation, V7 flag rule, N+1/N+2 |
| `Context Resources/03_Agent_Builder_Assessment_Contract_v1.0.md` | Runtime Resource / Contract | `AB_Runtime_Authority_Reference_v1.1.md` | evidence ceiling, fix layer, smallest sufficient change, no-material-change, Material `.goal-completeness` exception |
| `Context Resources/04_Goal-Completeness_and_Open-Architecture_Procedure_v1.0.md` | Runtime Resource / Procedure | `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` | Trivial/Material gate, goal ladder, capability-before-asset order, independence seal, coverage, gaps, action routing, open-architecture legality |
| `Context Resources/05_Agent_Builder_AB1-AB9_Registry_v3.0.md` | Runtime Resource / Lifecycle Registry | `AB_Runtime_Authority_Reference_v1.1.md` | AB1-AB9 role boundaries, handoffs, AB4 primary host, AB9 package role, no AB10 |
| `Eval Suites/06_Goal-Completeness_E1-E12_Adversarial_Eval_Suite_v1.0.md` | Eval Suite / Runtime Eval Reference | `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` | E1-E12 required observables, non-negotiables, pass threshold, miss classes |
| `Context Resources/07_Agent_Builder_Deployment_Quickstart_v1.0.md` | Runtime Resource / Usage | `AB_Runtime_Authority_Reference_v1.1.md` | resource ordering, shorthand examples, valid/invalid invocations, evidence-stage use |
| `Context Resources/08_Agent_Builder_Deployment_Validation_Record_v1.0.md` | Project State / Release Record | `AB_Runtime_Authority_Reference_v1.1.md` and run record | Yellow status, design-time/simulated claim limits, Green/Red conditions |
| `Minimum_Composition_Spike_Architect_Agent_Builder_Experiment_v0.1.md` | Runtime Resource / OMR Architecture | `OMR_Operator_Prototype_Runtime_v0.2.md` | four-operator/five-state hypothesis, falsifiers, Case 8 boundary, compact burden risk, non-replacement status |
| `P1_Prototype_Authority_and_Scope_v0.1.md` | Runtime Resource / OMR Authority | `OMR_Operator_Prototype_Runtime_v0.2.md` | P1-P7 authority, evidence stages, independence conditions, fixed architecture, impact boundary |
| `P2_State_Schemas_v0.1.json` | Runtime Resource / Schema | `P2_State_Schemas_v0.1.json` exact copy | full JSON schema; byte-identical candidate copy |
| `P3_Operator_Runtime_Contracts_v0.1.md` | Runtime Resource / OMR Contracts | `OMR_Operator_Prototype_Runtime_v0.2.md` | execution packet, O1-O4 ownership, read/write boundaries, O3 impact facts, O4 decision mapping, compact packet requirements |
| `P4_Selector_and_State_Transition_Protocol_v0.1.md` | Runtime Resource / OMR Selector | `OMR_Operator_Prototype_Runtime_v0.2.md` | deterministic eligibility, O2-before-O3, stale-parent handling, branch/no-silent-union, hard rejection codes |
| `P5_Executor_View_v0.1.yaml` | Eval Suite / Fixture View | `P5_Executor_View_v0.1.yaml` exact copy | public comparative fixtures; byte-identical candidate copy |
| `P6_AB_Run_and_Evidence_Capture_Protocol_v0.1.md` | Runtime Resource / Evidence Protocol | `OMR_Operator_Prototype_Runtime_v0.2.md` | roles, freeze, equivalent inputs/independence, raw retention, blinded handoff, burden metrics |
| `P7_Prototype_Build_Validation_Record_v0.1.md` | Project State / Build Validation | `OMR_Operator_Prototype_Runtime_v0.2.md` and run record | design-time build PASS claims, known risks, `READY FOR COMPARATIVE EXECUTION` without verdict |
| `PACKAGE_CHECKSUMS.md` | Archive / Provenance | unchanged original; hashes also in checksum artifact | prior package provenance retained |
| `Project State/Sentinel Evidence/SENTINEL_BASELINE_EVIDENCE_RECORD_v0.1.md` | Project State / Sentinel Baseline | `post-compression-sentinel-results_v0.1.md` and run record | S01-S10 pass baseline, compression risk ledger, simulated/design-time ceiling |
| `Sentinel_Baseline_Packet_v0.1/` | Eval Suite | unchanged original; retest references unchanged cases | S01-S10 unchanged case basis |

## Category Placement

Core Instructions:
- Candidate `AGENTS.md`.

Runtime Resources:
- `AB_Runtime_Authority_Reference_v1.1.md`
- `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md`
- `OMR_Operator_Prototype_Runtime_v0.2.md`
- exact `P2_State_Schemas_v0.1.json`
- exact `P5_Executor_View_v0.1.yaml`

Eval Suites:
- unchanged `Eval Suites/06...`
- unchanged `Sentinel_Baseline_Packet_v0.1/`
- `Project State/post-compression-sentinel-results_v0.1.md`

Archive:
- existing `Context Resources/Archive/`
- originals left unchanged in active locations; no archive copy needed for this candidate pass.

Project State:
- compression plan, map, checksums, run record, retest results.

scripts:
- existing executor/validation scripts retained unchanged.

User Data:
- planner examples, blueprints, and exports remain non-governing.

## Adoption Mapping

Upstream review returned `ADOPT`, and the user requested execution of that recommendation. Adoption was performed as a separate file operation.

1. Active root was replaced with the candidate thin root, preserving the pre-compression root in `Context Resources/Archive/PreCompression_Source_v0.1_2026-06-18/`.
2. Candidate runtime references were promoted to active `Context Resources/Runtime/`.
3. Exact P2/P5 were promoted byte-identically.
4. Pre-compression source copies were archived under `Context Resources/Archive/PreCompression_Source_v0.1_2026-06-18/`; original source files also remain in their prior locations for traceability.
5. Sentinel S01-S10 plus mixed AB/O smoke were rerun after active-resource promotion at simulated/design-time evidence.
