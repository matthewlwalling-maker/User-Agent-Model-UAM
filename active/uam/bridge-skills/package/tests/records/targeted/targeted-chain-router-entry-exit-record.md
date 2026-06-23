# Targeted Static Evaluation Record

Run timestamp: `2026-06-22 16:33:39 UTC`

Target package: `uam-bridge-skills` v0.1.0

Runner: `evals/run_static_eval.py`

Run scope: `selected cases`

Selected case IDs:

- `deg-006`
- `deg-007`
- `deg-008`
- `evc-005`
- `evc-006`
- `evc-007`
- `obj-006`
- `obj-007`
- `obj-008`
- `over-006`
- `over-007`
- `over-008`
- `route-006`
- `route-007`
- `route-008`

Evidence stage: static validation over design-time fixtures. This is not live-runtime, independent, or cross-model parity evidence.

## Aggregate

- Suites checked: 5
- Assertions checked: 15
- Passed: 15
- Failed: 0

## Results

| Suite | Case | Result | Notes |
|---|---|---|---|
| routing | route-006 | PASS | required contract coverage present |
| routing | route-007 | PASS | required contract coverage present |
| routing | route-008 | PASS | required contract coverage present |
| object-integrity | obj-006 | PASS | required contract coverage present |
| object-integrity | obj-007 | PASS | required contract coverage present |
| object-integrity | obj-008 | PASS | required contract coverage present |
| evidence-ceiling | evc-005 | PASS | required contract coverage present |
| evidence-ceiling | evc-006 | PASS | required contract coverage present |
| evidence-ceiling | evc-007 | PASS | required contract coverage present |
| degradation | deg-006 | PASS | required contract coverage present |
| degradation | deg-007 | PASS | required contract coverage present |
| degradation | deg-008 | PASS | required contract coverage present |
| overactivation | over-006 | PASS | required contract coverage present |
| overactivation | over-007 | PASS | required contract coverage present |
| overactivation | over-008 | PASS | required contract coverage present |

## Claim Limits

- Passing assertions mean the source package text contains the required contract coverage for the fixture.
- Passing assertions do not prove that any provider will follow the contract in live use.
- Cross-model parity remains unproven until provider adapters are run against the parity prompts and outputs are compared.

## Next Action

Diagnose any failed assertions by fix layer before treating the explicit-command pilot as eval-gated.
