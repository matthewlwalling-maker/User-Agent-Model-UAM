# Final Workspace Cleanup Record

Date: 2026-06-22
Evidence ceiling: static validation
Deletion policy: no files deleted in this batch

## Executed Batches

- Normalized top-level handoff packets into `handoff-packets/open/` and `handoff-packets/archive/`.
- Organized package docs into `docs/governance/`, `docs/cleanup/`, `docs/protocols/`, `docs/publication/`, and `docs/install/`.
- Moved active command skills into `skills/active/`.
- Moved active tools into `tools/active/`.
- Moved active lenses into `lenses/active/`.
- Moved generated exports into `exports/generated/`.
- Created package packet homes under `packets/` for future operator, evaluator, install, and external-review packets.

## Integrity Records

- Pre-move hashes: `tests/integrity/final-cleanup-2026-06-22-pre-move.sha256`
- Post-state hashes: `tests/integrity/final-cleanup-2026-06-22-post-state.sha256`
- Relocation map: `tests/integrity/final-cleanup-2026-06-22-relocation-map.tsv`
- Prior evals-to-tests relocation map: `tests/integrity/evals-to-tests-relocation-map-2026-06-22.tsv`
- Active skill package relocation map: `tests/integrity/active-skill-package-relocation-2026-06-23-relocation-map.tsv`
- Active skill package post-state hashes: `tests/integrity/active-skill-package-relocation-2026-06-23-post-state.sha256`

## Source-Control Alignment

Follow-up alignment on 2026-06-23 patched the governing controls so future source-bound work uses the new map:

- The active skill package now lives at `skills/active/uam-bridge-skills/`, containing `MANIFEST.yaml`, `KERNEL.md`, `CHAIN_ROUTER.md`, and `commands/*/SKILL.md`.
- `AGENTS.md` points canonical command loading to `skills/active/uam-bridge-skills/commands/<command-skill>/SKILL.md` and the active package anchors.
- `SKILL_REGISTRY.yaml` treats `skills/active/uam-bridge-skills/commands/` as the active manifest-controlled command root and keeps candidate/archive lanes non-loadable by default.
- `folder-organization-map.md`, `workspace-taxonomy-v2.md`, and `workspace-taxonomy-v2-migration-ledger.md` now describe the executed `docs/<category>/`, `tools/active/`, `lenses/active/`, `skills/active/`, and `exports/generated/` homes.
- The active `AGENTS.md` artifact was archived, restamped, and mirrored in `UAM_Artifact_Index.yaml`.
- Follow-up governance alignment created `docs/governance/source-authority-change-log.md` so future agent-instruction and source-authority changes have a single narrative record in addition to stamps, archives, ledgers, and source control commits.

## Intentional Stop Gates

- `.agents/` remains because deletion requires explicit delete authority.
- `.git/` remains because deletion requires explicit delete authority and it may affect tooling expectations.
- Empty `uam-bridge-skills/evals/` remains as an inert compatibility placeholder unless deletion is explicitly authorized.
- Generated cache archives remain under `tests/archive/generated-cache/` because this batch was no-delete.
- Donor vault cleanup under `FOR CONTEXT/` remains separate because donor byte-fidelity may matter.

## Rollback

Use `tests/integrity/final-cleanup-2026-06-22-relocation-map.tsv` to move paths back if needed. For files patched after relocation, restore from source control or from the relevant pre-move hash reference plus prior package snapshots where available.
