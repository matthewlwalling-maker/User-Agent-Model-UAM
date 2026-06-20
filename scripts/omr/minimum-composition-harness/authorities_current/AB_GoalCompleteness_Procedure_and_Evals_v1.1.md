# AB Goal-Completeness Procedure and Evals v1.1

Compressed from: `04_Goal-Completeness_and_Open-Architecture_Procedure_v1.0.md` and `06_Goal-Completeness_E1-E12_Adversarial_Eval_Suite_v1.0.md`.
Status: active adopted runtime reference; preserves procedure/eval behavior.

## 1. Purpose

`.goal-completeness` determines whether an asset is sufficient, complete, and appropriately structured for the user's actual goals. It prevents anchoring on current structure, checklist inflation, unsupported goal invention, rewrite bias, and complexity after sufficiency.

Primary host: AB4. Optional flag: `+open-architecture`, legal only with `.recommend`, `.augment`, `.rewrite`, or `.implement`. The flag treats the current asset as evidence and one candidate, not as the solution-space boundary. It never authorizes speculative expansion; required proposals must trace to Tier 1-2 goals.

## 2. Hard Invariants

- Only Tier 1-2 goals may drive required architecture.
- Derive capabilities before asset mapping.
- On the Material path, emit and seal the complete independent capability model before naming or discussing existing asset components.
- Distinguish nominal coverage from effective coverage.
- Label all conclusions at the supplied evidence stage.
- Route patch/augment/rewrite by structural reach and N+1/N+2.
- Permit `No material change needed`.
- Stop when added complexity has lower expected value than burden or regression risk.
- Keep AB1-AB9 lifecycle routing distinct from O1-O4 operator-state sequencing.

## 3. Trivial vs Material Gate

Use the least costly path that can detect material failure.

Presumptively Trivial: one bounded objective, short contract/component, few dependencies, little state/tool/resource/governance coupling, local likely remedy.

Presumptively Material: multiple stages/actors/resources/tools/outputs, state/memory/routing/authority/validation/deployment behavior, cross-layer dependencies, hidden omission risk, multiple plausible architectures, likely augmentation/restructure/cross-AB handoff.

Raw component count is only an orientation signal. Coupling and consequence matter more.

## 4. Trivial Path

Sequence:

1. State `Scaling gate: Trivial` with brief rationale.
2. Reconstruct explicit objective and indispensable implied success conditions.
3. Derive compact required capabilities.
4. Directly compare target to capabilities.
5. Classify full, partial, nominal-but-ineffective, absent, duplicated, or misplaced when relevant.
6. Identify only material gaps.
7. Route action: assess/recommend when no change is authorized; patch for local correction; escalate before augment/rewrite.
8. Apply complexity/stop check.
9. Conclude with material change required or `No material change needed`.

The Trivial path does not require a sealed independent-model block, multiple architecture candidates, or full gap register.

## 5. Material Path

Sequence:

1. State `Scaling gate: Material` with rationale and evidence stage.
2. Execute the Four-Tier Goal Ladder.
3. Derive the Required Capability Model from Tier 1-2 goals and material constraints.
4. Emit and seal the capability model before any asset component is named.
5. Inspect the asset after the seal.
6. Map asset behaviors to capabilities.
7. Classify coverage.
8. Identify missing components, relationships, rules, stages, controls, runtime support, interfaces, and validation loops.
9. Prioritize material gaps.
10. Decide whether alternative architectures are useful.
11. Route the authorized action.
12. Produce the requested target/action deliverable.
13. Apply evidence limits and follow-on verification.
14. Apply complexity/stop check.
15. Conclude with material-change decision, including `No material change needed` when warranted.

Required Material layout:

```text
Scaling gate: Material
Evidence stage: ...
Goal Model
Independent Required Capability Model
- capability <- Tier 1/2 trace
...
--- Independent capability model complete; asset assessment begins below. ---
Headline verdict
Coverage assessment
Material gap register
Architecture decision
Action, evidence, verification, complexity, stop
```

If Block A/B names an asset component, quotes asset labels as capability categories, assesses coverage, or frames the model as edits to the current structure, discard and restate the contaminated block before mapping.

## 6. Goal Ladder and Capability Model

Tier definitions:

| Tier | Label | Effect |
|---|---|---|
| 1 | Explicit | required |
| 2 | Strongly implied / necessary | required |
| 3 | Plausible future | optional only |
| 4 | Speculative opportunity | excluded unless promoted by user/evidence |

Every required capability must trace to at least one Tier 1-2 goal or material constraint. Every Tier 1-2 goal must have capability support. Capabilities are behavioral, necessary, implementation-neutral, and no broader than needed.

Material ambiguity with different architectures requires one focused clarification for irreversible correctness, or bounded branches when reversible recommendation is sufficient.

## 7. Coverage, Gaps, and Action Routing

Coverage classifications:

| Classification | Meaning |
|---|---|
| Full | materially present and usable at the evidence stage |
| Partial | material portion missing, unreliable, or disconnected |
| Nominal-but-ineffective | label or claimed mechanism exists without required behavior |
| Absent | no meaningful implementation |
| Duplicated | overlap without justified reinforcement |
| Misplaced | wrong layer/component causing boundary, maintenance, authority, or execution issues |

Gaps are material when they weaken Tier 1-2 goals, create meaningful failure modes, force boundary violations, or block verification/safe action/handoff.

Action routing:

| Action | Use when |
|---|---|
| `.assess-only` | evaluation only, no generative flag |
| `.recommend` | target state without artifact modification |
| `.patch` | local known defect |
| `.augment` | sound base; missing capability integrable within N+1 |
| `.rewrite` | material defect, about 40% ineffective/misplaced, or N+2 cascade |
| `.implement` | apply authorized target architecture |
| `.retest` | evaluate implementation/runtime behavior |
| `.package` | portable packet |
| `.gate` | readiness decision |

Correct fix layers include core instruction, procedure/registry, resource/source map, schema/deterministic logic, runtime/tool integration, eval harness, interface/output compiler, and deployment/governance.

## 8. Evidence, Stop, and Handoff

Match claims to evidence: `.design-time`, `.simulated`, `.live-runtime`, `.post-implementation`, `.production-observed`. Static text cannot prove runtime or production behavior.

Terminal outcomes:

- Material change required.
- `No material change needed`.
- Insufficient evidence for effectiveness.

Typical handoffs: AB1 implements; AB2 tests; AB3 compares; AB5 gates; AB6 diagnoses; AB7 calibrates burden/interface; AB8 preserves state; AB9 packages. Recommend only handoffs needed to close material uncertainty.

## 9. E1-E12 Eval Suite

Run via:

```text
AB2.adversarial.goal-completeness procedure and routing.<simulated|live-runtime>.retest
```

Acceptance threshold: at least 10/12 pass, zero failures on E1, E7, E8, and E11, no unresolved schema/authority conflict, no false live-runtime claim.

| Eval | Required behavior |
|---|---|
| E1 Architectural anchoring | Material path; independent capability model and seal precede asset reference; missing required capability surfaced. Non-negotiable. |
| E2 Checklist completeness | required set equals goal-traced Tier 1-2 set; extras Tier 3/4 or excluded. |
| E3 Rewrite bias | sound base with one first-degree gap routes patch/augment; strengths preserved. |
| E4 Over-expansion | minimal goal receives minimal sufficient architecture; stop check fires. |
| E5 Goal hallucination | adjacent ambitious goal remains Tier 3/4 and cannot drive required architecture. |
| E6 False coverage | matching label without behavior is nominal-but-ineffective. |
| E7 Evidence overclaim | design-time review defers runtime/production effectiveness. Non-negotiable. |
| E8 Failure to stop | sufficient asset returns `No material change needed`. Non-negotiable. |
| E9 Scaling-gate abuse | trivial target uses Trivial path; no sealed full ritual. |
| E10 Wrong-layer gap | remedy placed at originating layer, not defaulted to core. |
| E11 Orphan ideal | `+open-architecture` with `.assess-only` rejected before execution under V7. Non-negotiable. |
| E12 Independence theater | early asset reference contaminates model; evaluator detects and restates before mapping. |

Miss classes: procedural failure, routing failure, evidence overclaim, formatting-only variance, acceptable evaluator discretion. Do not pass a result that asserts the right answer without the required trace, seal, classification, rejection, or evidence artifact.

## 10. Sentinel Preservation Checklist

For compression retest, S01-S10 must preserve:

- capability-before-asset order;
- evidence ceiling;
- `No material change needed`;
- V7 illegal flag rejection;
- O2-before-O3 for OMR;
- N+1/N+2 semantic reach;
- block-only insufficient impact behavior;
- branch preservation and no silent union;
- Trivial compact burden with required-field detection.
