# Research Evidence Evaluation Record

Target revision: `uam.research-evidence` v0.1.0 enriched draft with dedicated fixture suite

Fixtures: `evals/research-evidence-cases.yaml`, `evals/routing-cases.yaml`, `evals/object-integrity-cases.yaml`, `evals/evidence-ceiling-cases.yaml`, `evals/degradation-cases.yaml`, and static structure checks

Evidence stage: design-time plus static validation

Evaluator independence: same-session design-time evaluation; not blind, not independent, not runtime model validated.

## Frozen Basis

- `/research` writes evidence only.
- `/research` may gather, verify, source-map, fact-check, synthesize, discover, and update evidence status.
- `/research` must preserve source authority, source scope, source dates, retrieval status, and claim limits.
- `/research` must separate direct source claims, observations, model inference, and implications for the current work.
- `/research` must preserve contradictory or uncertain findings rather than averaging them into unsupported certainty.
- Current, latest, official, provider-capability, legal, market, schedule, and other unstable claims require live retrieval or fresh enough supplied evidence.
- Without live retrieval, `/research` must assess only supplied evidence, label unsupported claims as unverified, and list sources needed to upgrade.
- `/research` must not update plans, mutate artifacts, choose options, diagnose failures, create handoff packets, or claim readiness beyond available evidence.

## Static Evaluation Results

| Case | Result | Notes |
|---|---|---|
| structure | PASS | Skill defines use/do-not-use, reads, writes, modes, lenses, required output, degradation, stop conditions, and boundary. |
| manifest-status | PASS | Manifest marks `/research` as `v0.1-enriched`. |
| research-discover-001 | PASS | Skill defines discover mode, source authority, freshness, and must-have source handling before adapter changes. |
| research-verify-001 | PASS | Skill requires checkable subclaims, support status, scope mismatch handling, and `not inspected` labels. |
| research-synthesize-001 | PASS | Skill separates authority/date/scope/agreement, direct source claims, model inference, and implications. |
| research-source-map-001 | PASS | Skill requires source identity, type, date, scope, inspected status, loadable reference, and no bare-citation reliance. |
| research-fact-check-001 | PASS | Skill defines atomic claims and supported, partially supported, contradicted, uncertain, unverified, and out-of-scope labels. |
| research-update-001 | PASS | Skill requires fresh-enough evidence, stale assumption handling, and absolute dates when relative dates matter. |
| research-contradiction-001 | PASS | Skill requires contradiction preservation, authority by subclaim, and claim limits. |
| research-degrade-001 | PASS | Skill requires `No live retrieval available`, supplied-evidence-only assessment, exact sources needed, and no latest/current overclaim. |
| research-boundary-001 | PASS | Skill forbids artifact writes and requires separate authorization for downstream operations. |
| research-high-stakes-001 | PASS | Skill treats insufficient high-stakes evidence as insufficient or out of scope rather than settled advice. |
| route-004 | PASS | Current provider capability verification routes to `/research` before adapter plan changes. |
| obj-005 | PASS | Skill requires contradictory or uncertain findings and forbids unsupported averaging. |
| evc-003 | PASS | Skill treats stale provider-doc checks as unverified unless current retrieval or fresh supplied evidence supports them. |
| deg-002 | PASS | Skill states `No live retrieval available`, assesses only supplied evidence, and labels unsupported claims as unverified. |

## Aggregate

Static/design-time pass: included in package static eval, 94 / 94.

No material skill patch required after the passing static run.

## Evidence Limits

This result proves only that the enriched `/research` skill text and existing fixtures contain the required controls. It does not prove that a provider will reliably retrieve, cite, preserve contradictions, or obey claim ceilings in live use.

Before pilot readiness, forward-test `/research` with actual prompt outputs for discover, verify, synthesize, source-map, fact-check, update, supplied-source-only degradation, contradictory evidence, boundary protection, and high-stakes insufficient-source prompts.

## Recommended Next Operation

Proceed to the next target skill only after user alignment. If continuing the established build order, the next un-enriched skill is `/review` or whichever target the user selects.
