# OMR Operator Prototype Runtime v0.2

Compressed from: `Minimum_Composition...`, `P1`, `P3`, `P4`, `P6`, and `P7`.
Status: active adopted runtime reference; P2 schema and P5 fixture view remain exact companion files.
Evidence ceiling: design-time specification unless actual comparative runs are executed.

## 1. Purpose and Boundary

The Operator Model Refinement / Minimum Composition prototype tests whether four contract-bearing operators and five shared state objects can make composition, stale-state detection, evidence provenance, and failure ownership more observable than the unchanged legacy Goal-Completeness baseline.

It is an experiment, not a migration or replacement. It does not authorize implementation, deployment, target-architecture generation, a fifth operator, AB1-AB9 routing for the operator path, or superiority claims without comparative evidence.

AB1-AB9 and O1-O4 are separate systems. AB is lifecycle routing; OMR is a state-sequenced prototype.

## 2. Fixed Architecture

State objects:

1. `GoalContract`
2. `CapabilityModel`
3. `EvidenceLedger`
4. `CoverageMap`
5. `ChangeDecision`

Operators:

1. `O1 Normalize Goal and Obligations`
2. `O2 Derive Required Capabilities`
3. `O3 Assess Capability Coverage`
4. `O4 Choose Intervention or Stop`

The metadata envelope is embedded in the five objects and is not a sixth object. Execution packets, transfer packets, logs, selector records, and fixture records are protocol records, not architectural state objects.

## 3. Evidence, Branch, and State Discipline

Evidence stages:

`design-time`, `simulated`, `live-runtime`, `post-implementation`, `production-observed`.

A stage promotion requires a new scoped ledger entry. Rewording, agreement, handoff, summarization, or model inference cannot promote evidence. The EvidenceLedger is append-only; corrections supersede entries and never erase history.

State rules:

- Downstream objects consume only committed/current upstream revisions unless a contract allows contested branches.
- Exact object ID, revision, branch, parent refs, and content hash must match.
- Parent changes make downstream objects stale until revalidated or regenerated.
- Conflicts remain on branches. No silent union, averaging, or best-of-both merge is permitted.
- Universal decisions proceed only when valid under every live branch; otherwise O4 returns `blocked-by-material-disagreement`.

## 4. Operator Ownership

| Operator | Writes | Reads | Prohibited |
|---|---|---|---|
| O1 | GoalContract; goal/constraint ledger entries | intake, goals, constraints, prior GoalContract branches, supporting evidence | capabilities, coverage, intervention |
| O2 | CapabilityModel; design-time inference ledger entries | committed GoalContract and permitted goal/constraint evidence | asset decomposition, section labels, coverage, proposed edits, intervention |
| O3 | CoverageMap; asset/test evidence entries | committed GoalContract, CapabilityModel, asset, supplied dependency/interface facts, ledger | requiredness/capability changes, final fix/action, target architecture |
| O4 | ChangeDecision only | current CoverageMap and referenced upstream state/evidence | rewriting coverage, adding dependency facts, implementation, testing, packaging, deployment |

Non-owner writes are rejected. O3 cannot smuggle actions into coverage. O4 cannot redo O3 coverage or impact analysis.

## 5. Execution Packet

Every operator receives a complete `ExecutionPacket` and may not rely on conversation memory. It includes run/operator/profile, independence condition, exact input objects, ledger projection, permitted and forbidden reads, selector decision, and expected P2 output schema.

Packet validity:

- object snapshots match exact ID/revision/branch/hash;
- every cited ledger entry is included in the projection;
- a referenced-subset ledger remains one logical ledger by stable ledger ID, revision/digest, included entries, omitted count, and append delta;
- omitted ledger content may not be inferred;
- any forbidden input is a hard failure;
- output must validate against P2 and semantic validation names the P2 error code.

## 6. O1 Contract

Select O1 when no current GoalContract exists, goal/constraint evidence changed, requiredness basis is missing, or material interpretation must branch.

O1 must separate `explicit-required`, `entailed-required`, `optional`, and `speculative`; every class needs a source-backed basis, and every entailed obligation needs a necessity argument. Optional/speculative items cannot drive required capabilities. Compact/material profile is based on coupling and omission risk, not polish.

Failure exits include blocked material ambiguity, no recoverable outcome, missing provenance, branch conflict, and P2 errors `MCP-E100`, `MCP-E110`, `MCP-E120`.

## 7. O2 Contract

Select O2 only when a committed/current GoalContract exists and no current matching CapabilityModel exists, the model is stale, or owner-led adjudication is requested.

Normal material O2 packets prohibit asset text, component names, section labels, coverage judgments, and proposed edits. O2 derives the smallest candidate-complete set of behavioral required capabilities needed for required obligations and constraints. Every capability must trace to a required obligation; every required obligation must be covered.

Independence conditions:

- `packet-boundary`: auditable packet restriction only; not full cognitive independence if broader context saw the asset.
- `separate-context`: execution context has never received the asset.

Forbidden packet content or asset-derived categories trigger `MCP-E220`; discard and rerun clean. Materially disagreeing models remain separate branches and are not unioned.

## 8. O3 Contract and Impact Boundary

Select O3 only with exact committed/current GoalContract and CapabilityModel revisions, fixed asset version/hash, explicit evidence stage, and bounded coverage evidence. O3-before-O2 is rejected with `MCP-E400_O3_BEFORE_O2`.

O3 assesses behavior against every required capability. A label is not behavior. Coverage classifications include `full-at-stage`, `partial`, `nominal-but-ineffective`, `absent`, `duplicated`, `misplaced`, and `unknown-insufficient-evidence`.

For every material gap, O3 must emit:

1. gap type and required-obligation consequence;
2. originating layer candidates;
3. touched elements;
4. first-degree dependencies;
5. known second-degree-or-broader dependencies;
6. semantic centrality;
7. propagation facts with evidence;
8. `change_reach`: `named-elements-only`, `n-plus-1`, `broader-than-n-plus-1`, or `unknown`;
9. dependency-fact completeness;
10. preservation feasibility;
11. material unknowns;
12. `impact_job_required`;
13. `o4_readiness`: `intervention-ready`, `block-only`, or `not-ready`.

Impact analysis becomes a separate job when defensible reach classification requires new source collection, undocumented graph traversal, runtime/platform inspection, causal simulation, implementation design, or ownership/governance adjudication outside coverage. Then O3 sets `impact_job_required=true` and `o4_readiness=block-only`. O3 must not hide that job in prose.

## 9. O4 Contract

Select O4 only when current CoverageMap has `overall_o4_readiness` of `intervention-ready` or `block-only`, or branch-specific maps prove a decision invariant.

O4 treats CoverageMap coverage and impact facts as immutable. It applies this mapping:

| O3 facts | Eligible O4 decision |
|---|---|
| no material gaps; required capabilities adequate at stage | `no-material-change` |
| local defect, reach `named-elements-only`, preservation plausible/established | `local-correction` |
| missing capability, reach `n-plus-1`, no broader propagation | `bounded-capability-addition` |
| reach `broader-than-n-plus-1` or systemic preservation failure | `system-restructure` |
| architecture sufficient but requested claim exceeds evidence | `verification-required` |
| O3 block-only due to separate impact job | `blocked-by-insufficient-impact-knowledge` |
| valid branches imply different decisions | `blocked-by-material-disagreement` |
| requested next operation is unowned by O1-O4 | `stop-unowned-operation` |

O4 may not fill missing impact facts to make an intervention eligible. It chooses the least reach satisfying all material gaps and evidence constraints. One committed ChangeDecision ends the four-operator run; re-entry requires changed parent, new evidence, or revisit trigger.

## 10. Selector Protocol

The selector is deterministic for eligibility, transitions, stale detection, and rejections; reasoning inside an eligible operator is constrained-generative. No model may override selector legality.

Dependency order:

```text
GoalContract -> CapabilityModel -> CoverageMap -> ChangeDecision
```

Hard rejections:

| Attempt | Rejection |
|---|---|
| O3 without committed/current O2 output | `MCP-E400_O3_BEFORE_O2` |
| O4 without current CoverageMap | `MCP-E500_O4_WITHOUT_CURRENT_COVERAGE` |
| O4 intervention when O3 is block-only/not-ready | `MCP-E510_O4_WITHOUT_IMPACT_KNOWLEDGE` |
| O2 packet contains asset decomposition/labels | `MCP-E220_INDEPENDENCE_CONTAMINATION` |
| Non-owner writes another state object | `MCP-E020_ILLEGAL_WRITE_AUTHORITY` |
| Silent branch union | `MCP-E230_SILENT_MODEL_UNION` or `MCP-E610_UNRESOLVED_BRANCH` |

Compact execution may serialize projections together only as four separately validated transforms. Co-serialization does not legalize skipping O2 or letting O4 reanalyze O3.

## 11. Invalidation

- Goal outcome, requiredness, or material constraint revision makes CapabilityModel, CoverageMap, and ChangeDecision stale.
- Optional/speculative wording change may preserve CapabilityModel only with explicit invariance record.
- CapabilityModel revision makes CoverageMap and ChangeDecision stale.
- Asset version/hash change makes CoverageMap and ChangeDecision stale.
- Same-scope new evidence requires CoverageMap revalidation and may stale ChangeDecision.
- CoverageMap revision makes ChangeDecision stale.
- New conflict branch makes dependent state branch-specific or contested.
- Implementation is outside scope; create a new asset version and return to O3.

## 12. A/B Run and Evidence Capture

Roles:

- fixture custodian freezes P5 and withholds hidden evaluator fields;
- run executor executes both systems and captures raw evidence, but does not score;
- independent evaluator performs first-pass blind scoring, then diagnostics;
- builder does not alter a frozen run series after seeing outputs.

Before a run series, freeze SHA-256 of P1-P7 and governing sources, exact prompts/contracts/schema version, unchanged legacy source versions, model/provider/config, fixture digest, timestamp, and run ID.

Equivalent input rule: both systems receive the same public request, constraints, asset content/version, dependency facts, and evidence stage. Operator receives no AB routing/schema. Legacy receives unchanged Assessment Contract, Goal-Completeness Procedure, eval behavior, and required Registry semantics.

Packet-boundary and separate-context conditions must be equivalent across systems before attributing any advantage to context isolation.

Retain raw prompts, outputs, states, selector logs, packets, ledger projections, hashes, rejected selections, manual interventions, repairs, token/latency/handoff/clarification metrics, and first-pass failures. A repaired run never replaces the first-pass record.

## 13. Build Validation and Risks

P7 design-time construction validation recorded:

- five state objects and four operators only;
- P2 valid JSON and examples structurally validate/reject as intended;
- P5 parses as YAML and contains mandatory cases/variants/holdouts;
- O3 does not select interventions;
- O4 does not redo coverage/impact;
- O3-before-O2 and block-only O4 behavior are specified;
- branch/no-silent-union and evidence ceilings are specified;
- equivalent legacy independence protocols exist;
- no runtime/production validation claim exists.

Known experiment risks: Case 8 may falsify the four-operator boundary; compact state may impose unjustified burden; packet-boundary may not reduce anchoring; typed state can create compliance theater; the prototype lacks implementation, target-architecture generation, and lifecycle continuation.

Build disposition remains `READY FOR COMPARATIVE EXECUTION`, not a comparative verdict.
