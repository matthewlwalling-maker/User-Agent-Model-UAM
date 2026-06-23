# Test Suite Evaluation Record

Run timestamp: `2026-06-22 16:33:54 UTC`

Target package: `uam-bridge-skills` v0.1.0

Runner: `evals/run_static_eval.py`

Run scope: `full static suite`

Evidence stage: static validation over design-time fixtures. This is not live-runtime, independent, or cross-model parity evidence.

## Aggregate

- Suites checked: 15
- Assertions checked: 144
- Passed: 144
- Failed: 0

## Results

| Suite | Case | Result | Notes |
|---|---|---|---|
| structure | /align | PASS | contract sections and manifest entry present |
| structure | /design | PASS | contract sections and manifest entry present |
| structure | /build | PASS | contract sections and manifest entry present |
| structure | /review | PASS | contract sections and manifest entry present |
| structure | /compare | PASS | contract sections and manifest entry present |
| structure | /diagnose | PASS | contract sections and manifest entry present |
| structure | /research | PASS | contract sections and manifest entry present |
| structure | /handoff | PASS | contract sections and manifest entry present |
| structure | align-work-cases.yaml | PASS | fixture present |
| structure | build-artifact-cases.yaml | PASS | fixture present |
| structure | design-solution-cases.yaml | PASS | fixture present |
| structure | diagnose-problem-cases.yaml | PASS | fixture present |
| structure | handoff-state-cases.yaml | PASS | fixture present |
| structure | research-evidence-cases.yaml | PASS | fixture present |
| structure | review-work-cases.yaml | PASS | fixture present |
| structure | blind-value-proposition-cases.yaml | PASS | fixture present |
| structure | pressure-red-cases.yaml | PASS | fixture present |
| structure | pressure-red-executor-only-cases.yaml | PASS | fixture present |
| structure | routing-cases.yaml | PASS | fixture present |
| structure | object-integrity-cases.yaml | PASS | fixture present |
| structure | evidence-ceiling-cases.yaml | PASS | fixture present |
| structure | degradation-cases.yaml | PASS | fixture present |
| structure | overactivation-cases.yaml | PASS | fixture present |
| structure | cross-model-parity.yaml | PASS | fixture present |
| manifest-status | /align | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| manifest-status | /design | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| manifest-status | /build | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| manifest-status | /review | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| manifest-status | /compare | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| manifest-status | /diagnose | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| manifest-status | /research | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| manifest-status | /handoff | PASS | release_status v0.1-enriched; expected v0.1-enriched |
| align_work | align-clarify-001 | PASS | required contract coverage present |
| align_work | align-clarify-002 | PASS | required contract coverage present |
| align_work | align-frame-001 | PASS | required contract coverage present |
| align_work | align-contract-001 | PASS | required contract coverage present |
| align_work | align-branch-001 | PASS | required contract coverage present |
| align_work | align-prioritize-001 | PASS | required contract coverage present |
| align_work | align-scope-001 | PASS | required contract coverage present |
| align_work | align-routing-001 | PASS | required contract coverage present |
| align_work | align-routing-002 | PASS | required contract coverage present |
| align_work | align-object-001 | PASS | required contract coverage present |
| align_work | align-stop-001 | PASS | required contract coverage present |
| align_work | align-degrade-001 | PASS | required contract coverage present |
| build_artifact | build-patch-001 | PASS | required contract coverage present |
| build_artifact | build-augment-001 | PASS | required contract coverage present |
| build_artifact | build-rewrite-001 | PASS | required contract coverage present |
| build_artifact | build-implement-001 | PASS | required contract coverage present |
| build_artifact | build-shape-001 | PASS | required contract coverage present |
| build_artifact | build-compress-001 | PASS | required contract coverage present |
| build_artifact | build-materialize-001 | PASS | required contract coverage present |
| build_artifact | build-gate-001 | PASS | required contract coverage present |
| build_artifact | build-degrade-001 | PASS | required contract coverage present |
| build_artifact | build-evidence-001 | PASS | required contract coverage present |
| design_solution | design-explore-001 | PASS | required contract coverage present |
| design_solution | design-architect-001 | PASS | required contract coverage present |
| design_solution | design-specify-001 | PASS | required contract coverage present |
| design_solution | design-plan-001 | PASS | required contract coverage present |
| design_solution | design-reconcile-001 | PASS | required contract coverage present |
| design_solution | design-refine-001 | PASS | required contract coverage present |
| design_solution | design-premortem-001 | PASS | required contract coverage present |
| design_solution | design-boundary-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-triage-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-root-cause-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-premortem-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-fix-layer-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-impact-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-recovery-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-calibration-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-hypothesis-001 | PASS | required contract coverage present |
| diagnose_problem | diagnose-boundary-001 | PASS | required contract coverage present |
| handoff_state | handoff-align-001 | PASS | required contract coverage present |
| handoff_state | handoff-design-001 | PASS | required contract coverage present |
| handoff_state | handoff-build-001 | PASS | required contract coverage present |
| handoff_state | handoff-review-001 | PASS | required contract coverage present |
| handoff_state | handoff-compare-001 | PASS | required contract coverage present |
| handoff_state | handoff-diagnose-001 | PASS | required contract coverage present |
| handoff_state | handoff-research-001 | PASS | required contract coverage present |
| handoff_state | handoff-compact-001 | PASS | required contract coverage present |
| handoff_state | handoff-missing-source-001 | PASS | required contract coverage present |
| handoff_state | handoff-degrade-001 | PASS | required contract coverage present |
| handoff_state | handoff-resume-001 | PASS | required contract coverage present |
| handoff_state | handoff-parity-001 | PASS | required contract coverage present |
| research_evidence | research-discover-001 | PASS | required contract coverage present |
| research_evidence | research-verify-001 | PASS | required contract coverage present |
| research_evidence | research-synthesize-001 | PASS | required contract coverage present |
| research_evidence | research-source-map-001 | PASS | required contract coverage present |
| research_evidence | research-fact-check-001 | PASS | required contract coverage present |
| research_evidence | research-update-001 | PASS | required contract coverage present |
| research_evidence | research-contradiction-001 | PASS | required contract coverage present |
| research_evidence | research-degrade-001 | PASS | required contract coverage present |
| research_evidence | research-boundary-001 | PASS | required contract coverage present |
| research_evidence | research-high-stakes-001 | PASS | required contract coverage present |
| review-work | review-object-001 | PASS | required contract coverage present |
| review-work | review-completeness-001 | PASS | required contract coverage present |
| review-work | review-readiness-001 | PASS | required contract coverage present |
| review-work | review-adversarial-001 | PASS | required contract coverage present |
| review-work | review-regression-001 | PASS | required contract coverage present |
| review-work | review-evidence-001 | PASS | required contract coverage present |
| review-work | review-blind-grade-001 | PASS | required contract coverage present |
| review-work | review-degrade-001 | PASS | required contract coverage present |
| routing | route-001 | PASS | required contract coverage present |
| routing | route-002 | PASS | required contract coverage present |
| routing | route-003 | PASS | required contract coverage present |
| routing | route-004 | PASS | required contract coverage present |
| routing | route-005 | PASS | required contract coverage present |
| routing | route-006 | PASS | required contract coverage present |
| routing | route-007 | PASS | required contract coverage present |
| routing | route-008 | PASS | required contract coverage present |
| object-integrity | obj-001 | PASS | required contract coverage present |
| object-integrity | obj-002 | PASS | required contract coverage present |
| object-integrity | obj-003 | PASS | required contract coverage present |
| object-integrity | obj-004 | PASS | required contract coverage present |
| object-integrity | obj-005 | PASS | required contract coverage present |
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
| degradation | deg-001 | PASS | required contract coverage present |
| degradation | deg-002 | PASS | required contract coverage present |
| degradation | deg-003 | PASS | required contract coverage present |
| degradation | deg-004 | PASS | required contract coverage present |
| degradation | deg-005 | PASS | required contract coverage present |
| degradation | deg-006 | PASS | required contract coverage present |
| degradation | deg-007 | PASS | required contract coverage present |
| degradation | deg-008 | PASS | required contract coverage present |
| overactivation | over-001 | PASS | required contract coverage present |
| overactivation | over-002 | PASS | required contract coverage present |
| overactivation | over-003 | PASS | required contract coverage present |
| overactivation | over-004 | PASS | required contract coverage present |
| overactivation | over-005 | PASS | required contract coverage present |
| overactivation | over-006 | PASS | required contract coverage present |
| overactivation | over-007 | PASS | required contract coverage present |
| overactivation | over-008 | PASS | required contract coverage present |
| cross-model-parity | parity-001 | PASS | required contract coverage present |
| cross-model-parity | parity-002 | PASS | required contract coverage present |
| cross-model-parity | parity-003 | PASS | required contract coverage present |
| cross-model-parity | parity-004 | PASS | required contract coverage present |

## Claim Limits

- Passing assertions mean the source package text contains the required contract coverage for the fixture.
- Passing assertions do not prove that any provider will follow the contract in live use.
- Cross-model parity remains unproven until provider adapters are run against the parity prompts and outputs are compared.

## Next Action

Diagnose any failed assertions by fix layer before treating the explicit-command pilot as eval-gated.
