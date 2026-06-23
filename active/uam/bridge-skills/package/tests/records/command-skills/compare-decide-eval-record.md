# Compare Decide Evaluation Record

Run timestamp: `2026-06-20 03:04:12 UTC`

Target revision: `uam.compare-decide` v0.1.0

Fixture: `evals/compare-decide-cases.yaml`

Runner: `evals/run_compare_decide_eval.py`

Evidence stage: static validation over design-time fixtures. This is not live-runtime, independent, or cross-model parity evidence.

## Aggregate

- Assertions checked: 17
- Passed: 17
- Failed: 0

## Results

| Case | Result | Notes |
|---|---|---|
| structure-skill-file | PASS | present |
| structure-fixture-file | PASS | present |
| structure-manifest-registration | PASS | present |
| structure-command | PASS | present |
| structure-skill-id | PASS | present |
| structure-writes | PASS | present |
| structure-boundary | PASS | present |
| compare-delta-001 | PASS | required compare contract coverage present |
| compare-rank-001 | PASS | required compare contract coverage present |
| compare-select-001 | PASS | required compare contract coverage present |
| compare-reconcile-001 | PASS | required compare contract coverage present |
| compare-baseline-001 | PASS | required compare contract coverage present |
| compare-consensus-001 | PASS | required compare contract coverage present |
| compare-boundary-001 | PASS | required compare contract coverage present |
| compare-degrade-001 | PASS | required compare contract coverage present |
| compare-research-001 | PASS | required compare contract coverage present |
| compare-stop-001 | PASS | required compare contract coverage present |

## Claim Limits

- Passing assertions mean the compare skill text contains the required controls for the compare fixture.
- This does not prove actual prompt behavior, model compliance, provider parity, or readiness for implicit routing.

## Next Owed

Forward-test actual `/compare` outputs for delta, rank, select, reconcile, baseline, consensus-check, degradation, and missing-criteria cases.
