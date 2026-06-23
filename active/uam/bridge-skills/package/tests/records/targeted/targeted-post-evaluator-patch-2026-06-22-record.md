# Targeted Static Evaluation Record

Run timestamp: `2026-06-22 18:44:54 UTC`

Target package: `uam-bridge-skills` v0.1.0

Runner: `evals/run_static_eval.py`

Run scope: `selected cases`

Selected case IDs:

- `evc-001`
- `evc-002`
- `evc-003`
- `evc-004`
- `evc-005`
- `evc-006`
- `evc-007`
- `handoff-compact-001`
- `obj-001`
- `obj-002`
- `obj-003`
- `obj-004`
- `obj-006`
- `obj-007`
- `obj-008`
- `over-001`
- `over-002`
- `over-003`
- `over-004`
- `over-005`
- `over-006`
- `over-007`
- `over-008`
- `route-006`
- `route-007`

Evidence stage: static validation over design-time fixtures. This is not live-runtime, independent, or cross-model parity evidence.

## Aggregate

- Suites checked: 5
- Assertions checked: 25
- Passed: 25
- Failed: 0

## Results

| Suite | Case | Result | Notes |
|---|---|---|---|
| handoff_state | handoff-compact-001 | PASS | required contract coverage present |
| routing | route-006 | PASS | required contract coverage present |
| routing | route-007 | PASS | required contract coverage present |
| object-integrity | obj-001 | PASS | required contract coverage present |
| object-integrity | obj-002 | PASS | required contract coverage present |
| object-integrity | obj-003 | PASS | required contract coverage present |
| object-integrity | obj-004 | PASS | required contract coverage present |
| object-integrity | obj-006 | PASS | required contract coverage present |
| object-integrity | obj-007 | PASS | required contract coverage present |
| object-integrity | obj-008 | PASS | required contract coverage present |
| evidence-ceiling | evc-001 | PASS | required contract coverage present |
| evidence-ceiling | evc-002 | PASS | required contract coverage present |
| evidence-ceiling | evc-003 | PASS | required contract coverage present |
| evidence-ceiling | evc-004 | PASS | required contract coverage present |
| evidence-ceiling | evc-005 | PASS | required contract coverage present |
| evidence-ceiling | evc-006 | PASS | required contract coverage present |
| evidence-ceiling | evc-007 | PASS | required contract coverage present |
| overactivation | over-001 | PASS | required contract coverage present |
| overactivation | over-002 | PASS | required contract coverage present |
| overactivation | over-003 | PASS | required contract coverage present |
| overactivation | over-004 | PASS | required contract coverage present |
| overactivation | over-005 | PASS | required contract coverage present |
| overactivation | over-006 | PASS | required contract coverage present |
| overactivation | over-007 | PASS | required contract coverage present |
| overactivation | over-008 | PASS | required contract coverage present |

## Claim Limits

- Passing assertions mean the source package text contains the required contract coverage for the fixture.
- Passing assertions do not prove that any provider will follow the contract in live use.
- Cross-model parity remains unproven until provider adapters are run against the parity prompts and outputs are compared.

## Next Action

Diagnose any failed assertions by fix layer before treating the explicit-command pilot as eval-gated.
