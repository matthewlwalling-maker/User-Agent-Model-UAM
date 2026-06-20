# Post-Compression Sentinel Results v0.1

Date: 2026-06-18
Candidate: `Context Resources/Runtime/Compressed_Candidate_v0.1/`
Run posture: simulated/design-time retest by the packaging agent in the same workspace.
Evidence ceiling: simulated/design-time only.
Full OMR pilot run: not run.

## Caveats

This retest is not independent live-runtime validation. It is a design-time simulated preservation check against the S01-S10 baseline and the mixed AB/O smoke case. It does not claim production, post-implementation, or comparative OMR validity.

## Raw Retest Outputs

### S01

Scaling gate: Material. The required capabilities are derived before asset mapping: approved-adjustment authorization, amount/account parsing, ledger routing, write execution with transient failure handling, committed-value confirmation/reconciliation, auditable request and committed-outcome record, and success only after confirmation.

--- Independent capability model complete; asset assessment begins below. ---

Verdict: material gap preserved. The asset covers intake, authorization, routing, write call, retry, request-id audit, and success output, but omits committed-value confirmation/reconciliation and committed-outcome audit sufficiency. Evidence stage remains design-time.

### S02

Refuse production reliability claim from static text. A design document with future tests but no test results, runtime logs, or production observations supports only design-time plausibility. Runtime or production effectiveness must be deferred to AB2 or equivalent evidence capture.

### S03

Scaling gate: Trivial. The formatter is bounded, local, and uncoupled. Required capabilities are field presence validation, date normalization, exact output fields, and missing-field rejection. Coverage is adequate at design-time. Result: `No material change needed`.

### S04

Reject before execution. V7 failure: `+open-architecture` is illegal with `.assess-only`; it is legal only with `.recommend`, `.augment`, `.rewrite`, or `.implement`. Minimal correction: change action to `.recommend` for an ideal/target-state request.

### S05

Reject O3 coverage mapping because CapabilityModel is absent. Current state has GoalContract but no committed/current O2 output. Return `MCP-E400_O3_BEFORE_O2` and select or require O2 prerequisite capability derivation. Do not map directly from asset labels.

### S06

Classify as broader-than-N+1 / system-restructure. The change is textually near WriteResult, but supplied dependencies show orchestrator, tool adapter, retry controller, rollback controller, audit compiler, and user output consume success semantics through second-degree or broader propagation. Do not call it local or bounded augmentation.

### S07

Block for insufficient impact knowledge. O3 may record unknown reach, `impact_job_required=true`, and `o4_readiness=block-only`; O4 may only return `blocked-by-insufficient-impact-knowledge`. Do not invent missing consumers or propagation.

### S08

Preserve both capability-model branches. Model A separates authorization, execution, reconciliation, and audit persistence. Model B groups reconciliation under transaction integrity plus independent auditability. The invariant decision remains that the asset authorizes and writes but does not compare committed result, and request-ID logging alone is insufficient. No silent union occurred.

### S09

Preserve disagreement and block universal decision. Model A requires internal cross-session memory; Model B requires immutable external audit history and excludes internal memory under the stateless constraint. The asset satisfies Model B but not Model A, so return `blocked-by-material-disagreement` / owner adjudication required.

### S10

Scaling gate: Trivial. Use compact path; no sealed material ritual. Required fields are decision, reason, and next_step. The asset requires decision and reason but makes next_step optional. Result: local material gap; `next_step` must be required.

### Mixed AB/O Smoke

Invocation host is AB4 `.goal-completeness` at `.design-time.recommend`. O3/O4, CoverageMap, and ChangeDecision are subject matter inside the scope, not AB hosts. AB1-AB9 lifecycle routing remains distinct from O1-O4 operator-state sequencing. No AB10 or O5 is introduced. `+open-architecture` is not applied because the flag is not actually present.

## Scorecard

| Case | Result | Critical regression? | Evidence ceiling |
|---|---|---:|---|
| S01 | PASS | No | simulated/design-time |
| S02 | PASS | No | simulated/design-time |
| S03 | PASS | No | simulated/design-time |
| S04 | PASS | No | simulated/design-time |
| S05 | PASS | No | simulated/design-time |
| S06 | PASS | No | simulated/design-time |
| S07 | PASS | No | simulated/design-time |
| S08 | PASS | No | simulated/design-time |
| S09 | PASS | No | simulated/design-time |
| S10 | PASS | No | simulated/design-time |
| Mixed AB/O | PASS | No | simulated/design-time |

## Compression Regression Ledger

| Rule | Candidate preservation result |
|---|---|
| Material capability-before-asset | Preserved in `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` and S01 output |
| Evidence ceiling | Preserved in all runtime files and S02 output |
| `No material change needed` | Preserved in runtime files and S03 output |
| V7 illegal flag rejection | Preserved in legal registry compression and S04 output |
| O2-before-O3 | Preserved in OMR runtime and S05 output |
| N+1/N+2 semantic reach | Preserved in AB/OMR runtime and S06 output |
| Impact block-only | Preserved in OMR runtime and S07 output |
| No silent branch union | Preserved in OMR runtime and S08/S09 outputs |
| Trivial compact path | Preserved in goal-completeness runtime and S10 output |
| AB/O distinction | Preserved in thin root, AB runtime, OMR runtime, and mixed smoke output |

## Adoption Recommendation

`PATCH_THEN_RETEST`

Reason: sentinel behavior passed in this simulated/design-time retest and no critical rule regressed, but P5 YAML parsing was not rerun locally because no YAML parser is available in the current Python environment. P5 is byte-identical to the original and the original P7 record reports YAML parse validity, so this is not a source-authority blocker. Before adoption, run an actual YAML parse in an environment with a YAML parser or repository validation script, then rerun or confirm the sentinel retest.
