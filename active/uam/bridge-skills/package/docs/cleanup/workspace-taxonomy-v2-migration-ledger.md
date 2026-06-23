# Workspace Taxonomy V2 Migration Ledger

Status: execution ledger; cleanup batches executed 2026-06-22; source-control alignment executed 2026-06-23
Date: 2026-06-22
Evidence ceiling: design-time/static review
Source design: `uam-bridge-skills/docs/cleanup/workspace-taxonomy-v2.md`

## Purpose

Track the planned move from the current workspace shape to Workspace Taxonomy V2 without breaking manifest authority, active artifact identity, test evidence, packet references, export exclusions, or rollback.

This ledger is now an execution record for rows marked `executed-2026-06-22` or `source-control-aligned-2026-06-23`. Rows still marked `pending-execution` remain planned only.

## Active Stop Gates

- `AGENTS.md` active-index mismatch was resolved on 2026-06-22 by archiving old instruction snapshots, stamping the active root file, and updating `UAM_Artifact_Index.yaml`.
- The active skill package now lives at `skills/active/uam-bridge-skills/` and contains `MANIFEST.yaml`, `KERNEL.md`, `CHAIN_ROUTER.md`, and `commands/*/SKILL.md`.
- Candidate skills must not become active through scanner behavior.
- Private test material must not enter generated exports.
- Any row that affects a manifest path requires a paired manifest patch and post-migration path validation.
- Any row that affects a governed UAM artifact requires artifact-index and archive-transaction discipline.

## Ledger Fields

| Field | Meaning |
|---|---|
| `id` | Stable row ID for discussion and execution batching. |
| `current_path` | Current source path or explicit pattern. |
| `target_path` | Proposed V2 destination path or pattern. |
| `class` | Preservation or cleanup class. |
| `manifest_impact` | Whether `MANIFEST.yaml` or adapter derivation changes. |
| `reference_impact` | Known docs, handoffs, exports, scripts, or run packets that may reference the path. |
| `privacy_impact` | Whether private/scoring/evaluator material is in scope. |
| `hash_before` | Filled during execution preflight. |
| `hash_after` | Filled during execution verification. |
| `rollback` | Default rollback action. |

## Migration Batches

| ID | Current path | Target path | Class | Manifest impact | Reference impact | Privacy impact | Hash before | Hash after | Rollback |
|---|---|---|---|---|---|---|---|---|---|
| ROOT-README-ARCHIVE | `README.md` | `archive/root-governance/UAM-FRAMEWORK/README__displaced-root-snapshot__observed-2026-06-19__sha256-a5efdd3282d9.md` | preserve-history | none | possible human entrypoint | none | A5EFDD3282D9746BAFCA93AA00C45CF01F0AD34092EDCCF50AC8F98A79449A82 | A5EFDD3282D9746BAFCA93AA00C45CF01F0AD34092EDCCF50AC8F98A79449A82 | executed-2026-06-22; move back to `README.md` |
| ROOT-REQ-MOVE | `requirements-dev.txt` | `uam-bridge-skills/requirements-dev.txt` | preserve-source | none | `tools/active/validate_yaml.py` guidance | none | 9EAD3AF92574AC9365466A6EA9087E63B41FF107386CDFB25A13911F1365AF8A | 9EAD3AF92574AC9365466A6EA9087E63B41FF107386CDFB25A13911F1365AF8A | executed-2026-06-22; move back to root and restore guidance |
| ROOT-EMPTY-AGENTS | `.agents/` | delete only if still empty | cleanup-candidate | none | runtime placeholder possible | none | not-applicable | not-applicable | recreate empty folder if needed |
| ROOT-EMPTY-GIT | `.git/` | delete only if still empty and invalid | cleanup-candidate | none | Git tooling confusion possible | none | not-applicable | not-applicable | recreate only by proper Git init/clone if needed |
| SKILLS-ACTIVE | `uam-bridge-skills/skills/<skill>/SKILL.md` | `uam-bridge-skills/skills/active/<skill>/SKILL.md` | preserve-authority | high | adapters, exports, run packets, skill refs | none | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move each skill back and restore manifest paths |
| ACTIVE-SKILL-PACKAGE | root anchors plus flat `uam-bridge-skills/skills/active/<skill>/SKILL.md` | `uam-bridge-skills/skills/active/uam-bridge-skills/` with `commands/<skill>/SKILL.md` | preserve-authority | high | AGENTS, manifest, adapters, exports, install docs, publication docs | none | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | see `tests/integrity/active-skill-package-relocation-2026-06-23-post-state.sha256` | move anchors back to package root, move command dirs back to `skills/active/`, and restore manifest/registry paths |
| SKILLS-CANDIDATES | future candidate skills | `uam-bridge-skills/skills/candidates/<lane>/<skill>/SKILL.md` | preserve-source | blocked unless manifest excludes candidates | future registry/export refs | none | pending-execution | pending-execution | remove candidate entry or move back to intake path |
| SKILLS-ARCHIVE | historical skill source | `uam-bridge-skills/skills/archive/backfilled-lineage/<source>/` | preserve-history | none if not manifest-listed | source history refs | none | pending-execution | pending-execution | restore archived source to prior archive/intake path |
| EVAL-SUITES-TO-TESTS | `uam-bridge-skills/evals/*-cases.yaml` | `uam-bridge-skills/tests/suites/<category>/` | preserve-source | high | manifest, validator, exports, docs | none | see `tests/integrity/evals-to-tests-pre-move-2026-06-22.sha256` | see `tests/integrity/evals-to-tests-post-move-2026-06-22.sha256` | executed-2026-06-22; move suites back to `evals/` and restore manifest |
| EVAL-RUNS-TO-TESTS | `uam-bridge-skills/evals/*-run-*` and named run folders | `uam-bridge-skills/tests/runs/<run-id>/` | preserve-evidence | medium | docs, exports, packets | high for raw/private and mapping keys | see `tests/integrity/evals-to-tests-pre-move-2026-06-22.sha256` | see `tests/integrity/evals-to-tests-post-move-2026-06-22.sha256` | executed-2026-06-22; move run folders back to `evals/` |
| EVAL-RECORDS-TO-TESTS | `uam-bridge-skills/evals/*-record.md` | `uam-bridge-skills/tests/records/<record-class>/` | preserve-evidence | medium | docs, exports, release gates | low unless record embeds private material | see `tests/integrity/evals-to-tests-pre-move-2026-06-22.sha256` | see `tests/integrity/evals-to-tests-post-move-2026-06-22.sha256` | executed-2026-06-22; move records back to `evals/` |
| DOCS-GOVERNANCE | selected `uam-bridge-skills/docs/*.md` | `uam-bridge-skills/docs/governance/` | preserve-source | low | internal doc links and handoff refs | none | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move docs back and restore refs |
| DOCS-CLEANUP | cleanup docs | `uam-bridge-skills/docs/cleanup/` | preserve-source | low | cleanup handoffs and maps | none | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move docs back and restore refs |
| DOCS-PROTOCOLS | protocol docs | `uam-bridge-skills/docs/protocols/` | preserve-source | low | eval/test packets and docs | possible if examples embed private refs | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move docs back and restore refs |
| DOCS-PUBLICATION | publication and master repo planning docs | `uam-bridge-skills/docs/publication/` | preserve-source | low | export and repo handoff refs | none | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move docs back and restore refs |
| DOCS-INSTALL | dogfood install and activation packets | `uam-bridge-skills/docs/install/` | preserve-source | low | install/run handoff refs | possible profile details | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move docs back and restore refs |
| PACKETS-PACKAGE | future generated operator/evaluator/install/external-review packets | `uam-bridge-skills/packets/<type>/` | preserve-packet | low | handoff refs, export tooling | possible for evaluator packets | not-applicable | not-applicable | scaffold-created-2026-06-22; remove empty scaffold only with delete authority |
| HANDOFF-OPEN | `handoff-packets/*.md` active/open packets | `handoff-packets/open/` | preserve-packet | none | hard-coded handoff refs, exporter input | possible for evaluator packets | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move packets back to `handoff-packets/` |
| HANDOFF-ARCHIVE | dated evaluator source packet folders | `handoff-packets/archive/evaluator-source-packets/` | preserve-packet | none | eval audit refs | possible evaluator material | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move folders back to `handoff-packets/` |
| EXPORTS-GENERATED | `uam-bridge-skills/exports/<export-id>/` | `uam-bridge-skills/exports/generated/<export-id>/` | preserve-generated-export | medium for `export_profiles` | export manifests and docs | must exclude private material | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move export back and restore manifest profile path |
| TOOLS-ACTIVE | `uam-bridge-skills/tools/*.py`, `uam-bridge-skills/tools/*.ps1` | `uam-bridge-skills/tools/active/` | preserve-source | high for manifest-listed tools | scripts, docs, operator prompts | possible export behavior | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move tools back and restore manifest |
| LENSES-ACTIVE | `uam-bridge-skills/lenses/*.md` | `uam-bridge-skills/lenses/active/` | preserve-source | high for manifest lens paths | skills and exports | none | see `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256` | see `tests/integrity/final-cleanup-2026-06-22-post-state.sha256` | executed-2026-06-22; move lenses back and restore manifest |

## Exact Active Skill Path Ledger

| Skill ID | Command | Current path | Planned V2 path | Status |
|---|---|---|---|---|
| `uam.align-work` | `/align` | `skills/active/uam-bridge-skills/commands/align-work/SKILL.md` | `skills/active/uam-bridge-skills/commands/align-work/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |
| `uam.design-solution` | `/design` | `skills/active/uam-bridge-skills/commands/design-solution/SKILL.md` | `skills/active/uam-bridge-skills/commands/design-solution/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |
| `uam.build-artifact` | `/build` | `skills/active/uam-bridge-skills/commands/build-artifact/SKILL.md` | `skills/active/uam-bridge-skills/commands/build-artifact/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |
| `uam.review-work` | `/review` | `skills/active/uam-bridge-skills/commands/review-work/SKILL.md` | `skills/active/uam-bridge-skills/commands/review-work/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |
| `uam.compare-decide` | `/compare` | `skills/active/uam-bridge-skills/commands/compare-decide/SKILL.md` | `skills/active/uam-bridge-skills/commands/compare-decide/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |
| `uam.diagnose-problem` | `/diagnose` | `skills/active/uam-bridge-skills/commands/diagnose-problem/SKILL.md` | `skills/active/uam-bridge-skills/commands/diagnose-problem/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |
| `uam.research-evidence` | `/research` | `skills/active/uam-bridge-skills/commands/research-evidence/SKILL.md` | `skills/active/uam-bridge-skills/commands/research-evidence/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |
| `uam.handoff-state` | `/handoff` | `skills/active/uam-bridge-skills/commands/handoff-state/SKILL.md` | `skills/active/uam-bridge-skills/commands/handoff-state/SKILL.md` | source-control-aligned-2026-06-23; manifest patched |

## Manifest Eval Suite Path Ledger

| Suite key | Current path | Planned V2 category | Status |
|---|---|---|---|
| `align_work` | `tests/suites/command-skills/align-work-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `build_artifact` | `tests/suites/command-skills/build-artifact-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `compare_decide` | `tests/suites/command-skills/compare-decide-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `design_solution` | `tests/suites/command-skills/design-solution-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `diagnose_problem` | `tests/suites/command-skills/diagnose-problem-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `handoff_state` | `tests/suites/command-skills/handoff-state-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `research_evidence` | `tests/suites/command-skills/research-evidence-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `review_work` | `tests/suites/command-skills/review-work-cases.yaml` | `tests/suites/command-skills/` | executed-2026-06-22; manifest patched |
| `blind_value_proposition` | `tests/suites/behavioral/blind-value-proposition-cases.yaml` | `tests/suites/behavioral/` | executed-2026-06-22; manifest patched |
| `uam_bridge_behavioral` | `tests/suites/behavioral/uam-bridge-behavioral-suite.yaml` | `tests/suites/behavioral/` | executed-2026-06-22; manifest patched |
| `uam_bridge_behavioral_executor_only` | `tests/suites/behavioral/uam-bridge-behavioral-executor-only-cases.yaml` | `tests/suites/behavioral/` | executed-2026-06-22; manifest patched |
| `pressure_red_cases` | `tests/suites/pressure/pressure-red-cases.yaml` | `tests/suites/pressure/` | executed-2026-06-22; manifest patched |
| `pressure_red_executor_only` | `tests/suites/pressure/pressure-red-executor-only-cases.yaml` | `tests/suites/pressure/` | executed-2026-06-22; manifest patched |
| `routing` | `tests/suites/routing/routing-cases.yaml` | `tests/suites/routing/` | executed-2026-06-22; manifest patched |
| `object_integrity` | `tests/suites/object-integrity/object-integrity-cases.yaml` | `tests/suites/object-integrity/` | executed-2026-06-22; manifest patched |
| `evidence_ceiling` | `tests/suites/evidence-ceiling/evidence-ceiling-cases.yaml` | `tests/suites/evidence-ceiling/` | executed-2026-06-22; manifest patched |
| `degradation` | `tests/suites/degradation/degradation-cases.yaml` | `tests/suites/degradation/` | executed-2026-06-22; manifest patched |
| `overactivation` | `tests/suites/overactivation/overactivation-cases.yaml` | `tests/suites/overactivation/` | executed-2026-06-22; manifest patched |
| `cross_model_parity` | `tests/suites/cross-model-parity/cross-model-parity.yaml` | `tests/suites/cross-model-parity/` | executed-2026-06-22; manifest patched |

## Existing Run Folder Ledger

| Run folder | Planned run type | Planned V2 path | Privacy impact | Status |
|---|---|---|---|---|
| `tests/runs/blind-run-001/` | blind | `tests/runs/blind-run-001/` | mapping keys and raw outputs need review before export | migrated-to-tests-root |
| `tests/runs/proof-loop-run-001/` | comparison | `tests/runs/proof-loop-run-001/` | evaluator outputs need review before export | migrated-to-tests-root |
| `tests/runs/pressure-run-001/` | pressure | `tests/runs/pressure-run-001/` | raw outputs need review before export | migrated-to-tests-root |
| `tests/runs/pressure-run-002/` | pressure | `tests/runs/pressure-run-002/` | raw outputs need review before export | migrated-to-tests-root |
| `tests/runs/behavioral-run-001/` | behavioral | `tests/runs/behavioral-run-001/` | raw target files and mapping key need review before export | migrated-to-tests-root |
| `tests/runs/claude-high-pressure-test-suite/` | pressure | `tests/runs/claude-high-pressure-test-suite/` | evaluator packet needs review before export | migrated-to-tests-root |
| `tests/runs/compounding-run-001/` | compounding | `tests/runs/compounding-run-001/` | raw-private and private run map present; do not export by default | migrated-to-tests-root |
| `tests/runs/lifecycle-run-001/` | lifecycle | `tests/runs/lifecycle-run-001/` | responses and attachments need review before export | migrated-to-tests-root |

## Verification Owed Before Any Physical Migration

1. Re-run path inventory immediately before the batch.
2. Search references for every current path in the batch.
3. Compute pre-move hashes for every file, excluding `.venv/` unless explicitly in scope.
4. Verify target paths do not exist unexpectedly.
5. Patch `MANIFEST.yaml` in the same batch for any active package source path move.
6. Patch scripts and docs that reference moved paths.
7. Re-run YAML validation and path-resolution validation.
8. Compute post-move hashes and compare moved files to pre-move hashes.
9. Write an execution record with exact changed paths and rollback instructions.

## Recommended Next Move

Use `skills/active/uam-bridge-skills/MANIFEST.yaml`, `SKILL_REGISTRY.yaml`, `TEST_REGISTRY.yaml`, this ledger, and `folder-organization-map.md` as the active source controls for future file placement. Remaining cleanup is stop-gated to delete-authorized placeholders, donor vault triage, and generated-cache disposition.
