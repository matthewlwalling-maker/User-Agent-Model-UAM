# Review Work Evaluation Record

Target revision: `uam.review-work` v0.1.0 enriched draft

Fixtures: `evals/review-work-cases.yaml`

Evidence stage: design-time plus static validation

Evaluator independence: same-session design-time evaluation; not blind, not independent, not runtime model validated.

Latest static run: `2026-06-20 03:08:56 UTC`

Runner: `evals/run_static_eval.py`

Suite result: 8 / 8 `review-work` cases passed; full static package run 94 / 94 assertions passed.

## Frozen Basis

- `/review` writes evidence only.
- `/review` may recommend fixes but must not mutate the reviewed artifact.
- `/review` must freeze target, criteria, evidence stage, and claim ceiling before issuing a verdict.
- `/review` must judge behavior against requirements, not headings, prose polish, or intent.
- Readiness decisions must treat absent evidence as unverified and must not issue Green from design-time plausibility when stronger evidence is required.
- Provider degradation must be explicit when runtime tests, retrieval, file reading, isolated evaluation, or durable memory are unavailable.

## Static Evaluation Results

| Case | Result | Notes |
|---|---|---|
| review-object-001 | PASS | Skill defaults ambiguous review-and-fix requests to read-only findings and routes patches to `/build`. |
| review-completeness-001 | PASS | Completeness mode derives a required capability model and classifies coverage behaviorally. |
| review-readiness-001 | PASS | Readiness mode requires exact gate evidence and forbids Green from design-time plausibility when stronger evidence is required. |
| review-adversarial-001 | PASS | Adversarial mode requires hidden traps, required/prohibited behavior, scoring rules, criticality, and evidence-stage labeling. |
| review-regression-001 | PASS | Regression mode freezes prior/current versions, compares behavior-bearing content, and forbids merge or patch during review. |
| review-evidence-001 | PASS | Evidence mode maps claims to evidence stage and names verification needed for stronger claims. |
| review-blind-grade-001 | PASS | Blind-grade mode leads with grade, uses purpose-fit vectors, and guards against invented flaws or grade inflation. |
| review-degrade-001 | PASS | Provider degradation section limits conclusions when tests, retrieval, file reading, isolation, or memory are unavailable. |

## Aggregate

Static/design-time pass: 8 / 8.

No material skill patch required from this static run.

## Evidence Limits

This result proves only that the enriched `/review` skill text and fixtures contain the required controls. It does not prove that a model will reliably execute those controls in live use, under cross-model parity, or in production.

Before pilot readiness, forward-test `/review` with actual prompt outputs for read-only review, completeness, readiness, adversarial eval design, regression, evidence claims, blind grading, and missing-tool degradation.

## Recommended Next Operation

Run a forward-test eval with actual assistant outputs, then route failures to `/diagnose` or patch the owning skill text with `/build`.
