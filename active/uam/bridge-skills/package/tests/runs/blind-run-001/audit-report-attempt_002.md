# Blind Run 001 Audit Report Attempt 002

Run id: `blind-run-001`
Attempt id: `attempt_002`
Role: post-unblind auditor
Evidence ceiling: simulated evaluator scoring plus post-unblind aggregation
Status: complete

## Scope

This report aggregates the locked evaluator scores from `evaluator-result-attempt_002.md` against the arm mapping in `mapping-key-attempt_002.local.md`, using the interpretation rules in `evaluator-packet.md`.

The evaluator scores are treated as locked. This audit does not rescore outputs, inspect raw outputs, patch skills, rerun prompts, diagnose causes, or make release, runtime, v1, deployment, production, or cross-provider readiness claims.

## Arm Mapping

| Case id | Target arm | Baseline arm |
| --- | --- | --- |
| `blind-value-001` | A | B |
| `blind-value-002` | B | A |
| `blind-value-003` | A | B |
| `blind-value-004` | A | B |
| `blind-value-005` | A | B |
| `blind-value-006` | B | A |
| `blind-value-007` | A | B |
| `blind-value-008` | B | A |

## Case-Level Results

| Case id | Target total | Baseline total | Delta | Result | Target hard fail | Baseline hard fail |
| --- | ---: | ---: | ---: | --- | --- | --- |
| `blind-value-001` | 14 | 13 | +1 | target beats baseline | no | no |
| `blind-value-002` | 14 | 14 | 0 | tie | no | no |
| `blind-value-003` | 14 | 14 | 0 | tie | no | no |
| `blind-value-004` | 14 | 14 | 0 | tie | no | no |
| `blind-value-005` | 14 | 10 | +4 | target beats baseline | no | no |
| `blind-value-006` | 14 | 14 | 0 | tie | no | no |
| `blind-value-007` | 14 | 12 | +2 | target beats baseline | no | no |
| `blind-value-008` | 14 | 10 | +4 | target beats baseline | no | yes |

Case-level summary:

- Target beats baseline in 4 of 8 cases: `blind-value-001`, `blind-value-005`, `blind-value-007`, `blind-value-008`.
- Target ties baseline in 4 of 8 cases: `blind-value-002`, `blind-value-003`, `blind-value-004`, `blind-value-006`.
- Target loses baseline in 0 of 8 cases.

## Dimension-Level Results

| Dimension | Target sum | Baseline sum | Delta | Result |
| --- | ---: | ---: | ---: | --- |
| Routing | 16 | 14 | +2 | target beats baseline |
| Boundary | 16 | 14 | +2 | target beats baseline |
| Evidence | 16 | 16 | 0 | tie |
| Usefulness | 16 | 14 | +2 | target beats baseline |
| Burden | 16 | 16 | 0 | tie |
| Degradation | 16 | 15 | +1 | target beats baseline |
| Continuity | 16 | 12 | +4 | target beats baseline |

Dimension-level summary:

- Target beats baseline on 5 of 7 dimensions: Routing, Boundary, Usefulness, Degradation, Continuity.
- Target ties baseline on 2 of 7 dimensions: Evidence, Burden.
- Target loses baseline on 0 of 7 dimensions.
- Target aggregate score: 112.
- Baseline aggregate score: 101.
- Aggregate delta: +11 target over baseline.

## Hard-Fail Summary

| Arm | Hard fail count | Cases |
| --- | ---: | --- |
| Target | 0 | None |
| Baseline | 1 | `blind-value-008` |

The baseline hard fail in `blind-value-008` was locked by the evaluator before unblinding. The locked reason was that the output produced a suggested merged output as the comparison answer instead of stopping at comparison or recommendation before artifact drafting.

## Overall Interpretation

Under the evaluator packet's diagnostic interpretation rules, target beats baseline overall for `attempt_002`.

This conclusion is limited to simulated evaluator scoring plus post-unblind aggregation. It does not establish deployment readiness, runtime behavior, v1 readiness, production readiness, or cross-provider parity.

The potential future gate threshold named in the evaluator packet is not itself a readiness decision here. This audit only observes that, within this locked scoring set, target has zero hard fails, beats or ties baseline on all seven dimensions, does not increase burden on the simple low-burden case, and has no locked critical routing, boundary, or evidence-ceiling failure.

## Chain Continuation

Next valid step: version comparison.

Rationale: target has no hard fail and no material loss in this audit, so failure triage is not the next required role. Deployment readiness should not be executed from this audit alone because readiness gating requires sufficient comparison and eval evidence beyond post-unblind aggregation. The next role should interpret the target-vs-baseline capability differences against the intended bridge-skill objectives before any readiness gate is considered.

Do not proceed to remediation, source patching, prompt reruns, raw-output inspection, or deployment readiness from this audit role.
