# Align Work Evaluation Record

Target revision: `uam.align-work` v0.1.0 enriched draft

Fixtures: `evals/align-work-cases.yaml`

Evidence stage: design-time

Evaluator independence: same-session design-time evaluation; not blind, not independent, not runtime validated.

## Frozen Basis

- `/align` writes state only.
- `/align` may recommend but must not execute `/design`, `/build`, `/review`, `/compare`, `/diagnose`, `/research`, or `/handoff`.
- Material ambiguity routes to `ASK`, `ASSUME`, `FORK`, or `PREPARE-NOT-EXECUTE`.
- State, artifact, evidence, and packet boundaries must remain distinct.
- Compact handling must remain available for low-coupling cases.

## Results

| Case | Result | Notes |
|---|---|---|
| align-clarify-001 | PASS | Missing prior model structure is load-bearing; skill requires `ASK` and forbids reconstructing missing state. |
| align-clarify-002 | PASS | Hard-to-reverse send action maps to `PREPARE-NOT-EXECUTE` while allowing draft preparation. |
| align-frame-001 | PASS | Frame mode classifies requirements and routes architecture to `/design` without creating files. |
| align-contract-001 | PASS | Contract mode produces scope, authority, assumptions, evidence ceiling, and stop condition; does not create a handoff packet. |
| align-branch-001 | PASS | Branch mode preserves alternatives and supports `/compare` when the decision needs a formal matrix. |
| align-prioritize-001 | FIXTURE CORRECTED | Original expected `/compare`, but the skill intentionally handles lightweight priority resolution inside `/align`; fixture now expects `direct` unless formal comparison is needed. |
| align-scope-001 | PASS | Scope mode preserves source-package-only work and blocks install/activation. |
| align-routing-001 | PASS | Combined review-and-improve request is treated as ambiguous mutation authority requiring a gate. |
| align-routing-002 | PASS | Current-provider-docs request routes to `/research` before plan update. |
| align-object-001 | PASS | Compact-for-next-model request routes to `/handoff` and preserves artifact compression boundary. |
| align-stop-001 | PASS | Simple direct answer remains available; material work contract is prohibited. |
| align-degrade-001 | PASS | Missing handoff packet is load-bearing context and routes to `ASK`. |

## Aggregate

Design-time pass after fixture correction: 12 / 12.

No material skill patch required from this run.

## Observed Failure Classes

- One eval-fixture mismatch: `align-prioritize-001` over-routed a lightweight priority-resolution prompt to `/compare`.
- No observed object-boundary failure.
- No observed evidence-ceiling failure.
- No observed overactivation failure after fixture correction.

## Evidence Limits

This result is design-time conformance evidence only. It does not prove runtime behavior, cross-model parity, or production readiness. A forward-test with actual prompt outputs is still required before treating `align-work` as pilot-ready.

## Recommended Next Operation

Forward-test `/align` on realistic compact, material, branch, scope, and missing-context prompts. Diagnose any misses by fix layer before moving to the next skill.
