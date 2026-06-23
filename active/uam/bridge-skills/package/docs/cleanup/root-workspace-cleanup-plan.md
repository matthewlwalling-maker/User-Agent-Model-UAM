# Root Workspace Cleanup Plan

Status: proposed cleanup and rehome plan; not executed
Date: 2026-06-22
Evidence level: static filesystem inspection and source-doc review
Workspace root: `C:\Users\Matthew\OneDrive\Documents\UAM MODEL FRAMEWORK\0A. UAM Bridge Skills`

## Purpose

Normalize the entire workspace so every file has an explicit home:

- active root governance;
- canonical Bridge Skills package source;
- donor/reference material;
- handoff and packet material;
- evidence and eval run material;
- generated exports;
- local runtime state;
- archived inactive or displaced material;
- generated/transient cleanup candidates.

This plan does not move, delete, archive, install, publish, stage, commit, or push anything. It defines the cleanup architecture and the candidate actions that require explicit follow-up authorization.

## Source Basis

Read or inspected:

- `AGENTS.md`
- `UAM_Artifact_Naming_and_Archive_Convention.md`
- `UAM_Artifact_Index.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md`
- `uam-bridge-skills/docs/cleanup/folder-organization-map.md`
- `uam-bridge-skills/docs/cleanup/cleanup-operations-protocol.md`
- current root directory listing
- current `uam-bridge-skills/docs/` listing
- current `uam-bridge-skills/tests/` run-folder listing
- current `handoff-packets/` top-level listing

Git state:

- `.git/` exists at the workspace root but is empty.
- `git rev-parse --show-toplevel` failed with "not a git repository".
- Treat this workspace as not currently backed by usable local Git metadata.

Static review update on 2026-06-22:

- `README.md` was confirmed as a displaced framework snapshot candidate and archived on 2026-06-22 as `archive/root-governance/UAM-FRAMEWORK/README__displaced-root-snapshot__observed-2026-06-19__sha256-a5efdd3282d9.md`.
- The earlier active-index/loadable-content mismatch for `UAM_Model_Participation_and_Assurance_Plan.md` and `UAM_Bootstrap_Pair_Brief.md` has been resolved by restoring both files to the workspace root. Static re-check confirmed both files are present and their whole-file SHA-256 values match the index's `integrity_file_sha256` values.
- `requirements-dev.txt` was moved into `uam-bridge-skills/` on 2026-06-22 with the paired `uam-bridge-skills/tools/active/validate_yaml.py` guidance patch.
- Moving `handoff-packets/open/chatgpt-architecture-audit-packet-2026-06-22.md` later requires a paired update to `uam-bridge-skills/tools/active/export_relevant_files.ps1`, which currently hard-codes the packet's top-level `handoff-packets/` path.

## Cleanup Principles

1. Root should carry only active governance/entrypoint material and major workstream roots.
2. Archive folders should preserve inactive or displaced material close to the category it belongs to.
3. Archive moves must be byte-preserving, hash-recorded moves, not semantic rewrites.
4. Empty runtime folders and generated caches are cleanup candidates, not historical artifacts.
5. The canonical package remains `uam-bridge-skills/`; do not move package source roots casually.
6. Evidence, packets, exports, donors, and handoffs are not active package source.
7. Moving an artifact that appears in `UAM_Artifact_Index.yaml` requires active-index and archive-transaction discipline.
8. Moving package files referenced by `MANIFEST.yaml` requires a manifest-aware build and follow-up review.
9. Raw/private evaluator material must not be moved into public-facing packet/export locations without explicit private-audit authorization.
10. Cleanup should be staged so a mistake in one category cannot damage another category.

## Target Category Map

Recommended category homes:

| Category | Primary home | Archive home | Notes |
|---|---|---|---|
| Active root governance | workspace root | `archive/root-governance/` | Keep indexed active artifacts at root unless a formal active-set migration is authorized. |
| Canonical Bridge Skills package | `uam-bridge-skills/` | `uam-bridge-skills/archive/` only for package-level displaced material | Avoid archive folders inside command roots unless specifically needed. |
| Package governance docs | `uam-bridge-skills/docs/` | `uam-bridge-skills/docs/archive/` | Superseded docs can move here after references are updated. |
| Package tools | `uam-bridge-skills/tools/` | `uam-bridge-skills/tools/archive/` | Do not archive a tool while `MANIFEST.yaml` still names it as active. |
| Tests and evidence runs | `uam-bridge-skills/tests/` | `uam-bridge-skills/tests/archive/` | Run folders are evidence/history, not clutter by default. |
| Generated exports | `uam-bridge-skills/exports/` | `uam-bridge-skills/exports/archive/` | Exports are derivatives and should not be treated as canonical source. |
| Handoff packets | `handoff-packets/open/` or `handoff-packets/` | `handoff-packets/archive/` | Use `open/` only if we want top-level handoffs visibly separated from historical packets. |
| Donor material | `FOR CONTEXT/` | `FOR CONTEXT/archive/` | Preserve donor identity; dedupe only with explicit donor cleanup authority. |
| Local runtime state | `.codex/`, `.venv/`, `.agents/` | none by default | Usually keep or delete/recreate, not archive. |
| Invalid/empty runtime shells | `.git/`, `.agents/` when empty | none by default | Verify empty and delete only with explicit authorization. |
| Generated caches | `__pycache__/`, `*.pyc` | none by default | Delete only after path verification; do not archive. |

## Proposed Root Shape

Target root after staged cleanup:

```text
0A. UAM Bridge Skills/
  AGENTS.md
  UAM_Artifact_Index.yaml
  UAM_Artifact_Naming_and_Archive_Convention.md
  UAM_Model_Framework.md
  UAM_Source_Intake_and_Context_Map.md
  archive/
    root-governance/
  FOR CONTEXT/
    archive/
  handoff-packets/
    open/
    archive/
  uam-bridge-skills/
    KERNEL.md
    MANIFEST.yaml
    requirements-dev.txt
    adapters/
    docs/
      archive/
    tests/
      archive/
    exports/
      archive/
    lenses/
    skills/
    tools/
      archive/
```

Local runtime folders may remain at root when needed:

```text
  .codex/
  .venv/
```

Empty `.agents/` and empty invalid `.git/` should be removed only after explicit cleanup authorization and immediate pre-action verification that they are still empty.

## Current Root Inventory And Classification

| Path | Current classification | Proposed disposition | Rationale |
|---|---|---|---|
| `AGENTS.md` | preserve-authority | keep at root | Active workspace operating contract. |
| `UAM_Artifact_Index.yaml` | preserve-authority | keep at root | Active artifact index. |
| `UAM_Artifact_Naming_and_Archive_Convention.md` | preserve-authority | keep at root | Active naming/archive convention. |
| `UAM_Model_Framework.md` | preserve-source / indexed active candidate | keep at root | Indexed active candidate framework. |
| `UAM_Source_Intake_and_Context_Map.md` | preserve-source / indexed active candidate | keep at root | Indexed source intake/context map. |
| `README.md` | displaced/legacy root snapshot | archived under `archive/root-governance/UAM-FRAMEWORK/` on 2026-06-22 | Content identifies canonical filename as `UAM_Model_Framework.md`; appears to be an older or displaced framework snapshot under the wrong active-style name. |
| `requirements-dev.txt` | package support source | moved to `uam-bridge-skills/requirements-dev.txt` on 2026-06-22 | Dev dependency file describes UAM Bridge Skills validation dependency and belongs with package tooling. |
| `FOR CONTEXT/` | preserve-donor | keep at root | Donor vault; not clutter. |
| `handoff-packets/` | preserve-packet | normalize into `open/` and `archive/` subfolders | Top-level packet area is valid but needs internal separation. |
| `uam-bridge-skills/` | preserve-source | keep at root | Canonical source package. |
| `.codex/` | local runtime/dogfood state | keep for now | Contains dogfood records/packages/skills; do not move as cleanup. |
| `.venv/` | local runtime dependency environment | keep for now | May be useful for validation; delete/recreate only with explicit authority. |
| `.agents/` | empty runtime shell | delete after verification | Currently empty; no archive value. |
| `.git/` | empty invalid Git shell | delete after verification | Currently empty and not a usable repo; no archive value. |

## Candidate Relocation Table

Rows marked as executed were completed during the 2026-06-22 root cleanup batch. Remaining rows are proposed actions only and require explicit cleanup authorization.

| Current path | Proposed path/action | Class | Risk | Verification | Rollback/recovery |
|---|---|---|---|---|---|
| `README.md` | `archive/root-governance/UAM-FRAMEWORK/README__displaced-root-snapshot__observed-2026-06-19__sha256-a5efdd3282d9.md` | preserve-history | External habits may expect a root README. | Hash before/after; confirm `UAM_Model_Framework.md` remains root active candidate. | Move the archived file back to `README.md`. |
| `requirements-dev.txt` | `uam-bridge-skills/requirements-dev.txt` plus a paired patch to `uam-bridge-skills/tools/active/validate_yaml.py` install guidance | preserve-source | Scripts or humans may expect the root path. | Executed 2026-06-22; hash before/after recorded in `workspace-taxonomy-v2-migration-ledger.md`; package file exists at target path. | Move back to root and revert reference patches. |
| `.agents/` | delete empty directory | cleanup-candidate | Could become non-empty before execution. | Re-list contents immediately before delete; stop if non-empty. | None needed if empty; recreate directory if a runtime expects it. |
| `.git/` | delete empty invalid directory | cleanup-candidate | A tool may be confused if expecting Git metadata. | Re-list contents and rerun `git rev-parse`; stop if non-empty or valid. | Recreate empty folder only if needed; real Git metadata must come from a proper clone. |
| `handoff-packets/open/automation-folder-maintenance-governance-handoff-2026-06-22.md` | `handoff-packets/open/automation-folder-maintenance-governance-handoff-2026-06-22.md` | preserve-packet | Existing references may point to current path. | Search references; hash before/after. | Move back to root of `handoff-packets/`. |
| `handoff-packets/open/bridge-skills-ideation-refinement-handoff-2026-06-22.md` | `handoff-packets/open/bridge-skills-ideation-refinement-handoff-2026-06-22.md` | preserve-packet | Existing references may point to current path. | Search references; hash before/after. | Move back to root of `handoff-packets/`. |
| `handoff-packets/open/chatgpt-architecture-audit-packet-2026-06-22.md` | `handoff-packets/open/chatgpt-architecture-audit-packet-2026-06-22.md` | preserve-packet | ChatGPT audit packet is referenced by handoffs and hard-coded in `uam-bridge-skills/tools/active/export_relevant_files.ps1`. | Search references; update packet refs and exporter source path if moved. | Move back and restore refs. |
| `handoff-packets/archive/eval-run-control/Compound-Test-Run-Handoff Context Resource.md` | triage before move; likely `uam-bridge-skills/tests/runs/compounding-run-001/run-packets/` or `handoff-packets/archive/eval-run-control/` | needs-triage | Could duplicate or conflict with compounding-run files. | Compare against existing compounding run packet files. | Keep original until duplicate status is known. |
| `handoff-packets/archive/evaluator-source-packets/neutral-evaluator-uam-bridge-v0.1-source-packet-2026-06-22/` | `handoff-packets/archive/evaluator-source-packets/neutral-evaluator-uam-bridge-v0.1-source-packet-2026-06-22/` | preserve-packet/history | May still be useful for eval audit. | Hash manifest before/after; verify file count. | Move folder back. |
| `handoff-packets/archive/evaluator-source-packets/simulated-evaluator-uam-bridge-v2-source-packet-2026-06-22/` | `handoff-packets/archive/evaluator-source-packets/simulated-evaluator-uam-bridge-v2-source-packet-2026-06-22/` | preserve-packet/history | May still be useful for eval audit. | Hash manifest before/after; verify file count. | Move folder back. |
| `handoff-packets/archive/evaluator-source-packets/simulated-evaluator-uam-bridge-v2b-verified-source-packet-2026-06-22/` | `handoff-packets/archive/evaluator-source-packets/simulated-evaluator-uam-bridge-v2b-verified-source-packet-2026-06-22/` | preserve-packet/history | May still be useful for eval audit. | Hash manifest before/after; verify file count. | Move folder back. |
| `uam-bridge-skills/docs/publication/master-git-export.md` | `uam-bridge-skills/docs/archive/master-git-export__superseded-by-publication-plan__2026-06-22.md` | preserve-history | References may still point to it. | Search references; update `folder-organization-map.md` if moved. | Move back and restore refs. |
| `uam-bridge-skills/tools/active/export_relevant_files.ps1` | keep until publisher replacement exists; later archive to `uam-bridge-skills/tools/archive/` | preserve-source / deprecated | Manifest currently names this tool. | Do not move until `MANIFEST.yaml` and docs are updated. | Not applicable until replacement. |
| `uam-bridge-skills/exports/generated/chatgpt-architecture-audit-2026-06-22/` | keep for now; later classify as generated export or archive | preserve-generated-export | It may still support external architecture audit. | Verify `HASHES.sha256` if moved later. | Move folder back. |
| `uam-bridge-skills/tests/archive/generated-cache/evals-pycache-2026-06-22/` | delete after verification | cleanup-candidate | None if regenerated cache only. | Verify path under workspace and generated-only contents. | Regenerate by rerunning scripts if needed. |
| `FOR CONTEXT/**/__pycache__/` | delete only if donor byte-fidelity is not required | cleanup-candidate with donor caution | Donor resources may be expected byte-preserved. | Separate donor cleanup authorization required. | Restore from donor archive if needed. |
| `.venv/**/__pycache__/` and `.venv/**/*.pyc` | leave with `.venv/` or delete `.venv/` as a whole if rebuilding environment | local runtime | Large churn; not meaningful archive. | Confirm user wants env cleanup. | Recreate venv and reinstall deps. |

## Execution Stages

### Stage 0: Preflight Manifest

Actions:

- Generate a pre-cleanup hash manifest for all files outside `.venv/`.
- Record counts for root, handoff, package docs, package evals, package exports, and donor vault.
- Resolve all candidate paths to absolute paths and confirm they are inside the workspace.
- Re-run `git rev-parse --show-toplevel` and record Git state.

Stop if:

- any candidate path is missing;
- any target path exists unexpectedly;
- `.git/` or `.agents/` is no longer empty;
- root indexed active artifacts disagree with `UAM_Artifact_Index.yaml`;
- any active index entry points to loadable content that is not present, unless the user has explicitly authorized a candidate-only cleanup scope that excludes active-index reconciliation;
- private/evaluator material would be exposed to a public packet/export path.

### Stage 1: Create Archive/Open Folders

Create only the category folders needed for approved moves:

```text
archive/root-governance/
handoff-packets/open/
handoff-packets/archive/evaluator-source-packets/
uam-bridge-skills/docs/archive/
uam-bridge-skills/tests/archive/
uam-bridge-skills/exports/archive/
uam-bridge-skills/tools/archive/
```

Do not create unused category archives just for symmetry.

Stage 1 is an execution dependency for any later stage whose target folders do not already exist. For the first root de-mess batch, create only the needed root archive folder, such as `archive/root-governance/UAM-FRAMEWORK/`, before moving `README.md`.

### Stage 2: Root De-Mess

First execution batch:

- Archived `README.md` as a displaced root framework snapshot on 2026-06-22.
- Moved `requirements-dev.txt` into `uam-bridge-skills/` with the paired `validate_yaml.py` guidance patch on 2026-06-22.
- Remove empty `.agents/` and empty invalid `.git/` only if still empty.

Why first:

- This removes the most confusing root-level active-looking duplicate.
- It leaves active root governance intact.
- It moves package dependency metadata into the package.
- It avoids donor, eval, and source package churn.

Execution gate:

- Do not run Stage 2 after Stage 0 reports any active-index/loadable-content mismatch unless the user first authorizes either an index/loadable-content reconciliation or a candidate-only cleanup scope that explicitly excludes indexed active artifact repair.
- Do not run Stage 2 without the needed Stage 1 target folders.

### Stage 3: Handoff Packet Normalization

Recommended second execution batch:

- Create `handoff-packets/open/`.
- Move the three currently useful fresh-context packets into `open/`.
- Move dated evaluator source packet folders into `handoff-packets/archive/evaluator-source-packets/`.
- Triage `Compound-Test-Run-Handoff Context Resource.md` against `uam-bridge-skills/tests/runs/compounding-run-001/` before moving.

Why second:

- Handoff packets are transport packets, so their relocation is less likely to break package source.
- The compounding context resource may overlap with eval run-control material and needs duplicate-aware handling.
- The ChatGPT architecture audit packet is also an exporter input; moving it requires updating `uam-bridge-skills/tools/active/export_relevant_files.ps1` or deferring that packet move until the profile-driven publisher replaces the narrow exporter.

### Stage 4: Superseded Package Docs And Tools

Recommended third execution batch:

- Archive `uam-bridge-skills/docs/publication/master-git-export.md` only after updating references to point to `bridge-skills-master-repo-publication-plan.md`.
- Keep `uam-bridge-skills/tools/active/export_relevant_files.ps1` until a profile-driven publisher replaces it and `MANIFEST.yaml` is updated.

Why third:

- Docs can be archived safely after references are corrected.
- Tools require manifest-aware replacement because the manifest currently names the exporter.

### Stage 5: Generated Cache Cleanup

Recommended fourth execution batch:

- Delete generated `__pycache__/` folders and `.pyc` files outside `.venv/` after explicit approval.
- Treat donor cache cleanup separately from package cache cleanup.
- Leave `.venv/` alone unless the user wants a local environment rebuild.

Why fourth:

- Generated caches are low-value but deletion is still destructive.
- Keeping them separate makes rollback and verification simple.

### Stage 6: Documentation Update And Record

After any approved execution:

- Update `uam-bridge-skills/docs/cleanup/folder-organization-map.md`.
- Create a cleanup execution record, for example:

```text
uam-bridge-skills/docs/root-workspace-cleanup-record-2026-06-22.md
```

The record should include:

- approved scope;
- files/folders moved or deleted;
- pre/post hashes;
- target paths created;
- files not touched;
- verification performed;
- residual risks;
- rollback instructions.

## Explicit Authorization Needed

The following require separate explicit authorization:

- Creating archive/open folders.
- Moving root files.
- Moving packet files or packet folders.
- Moving `requirements-dev.txt`.
- Deleting `.agents/`, `.git/`, `__pycache__/`, or `.pyc` files.
- Archiving superseded docs.
- Moving or archiving donor material.
- Updating `MANIFEST.yaml`.
- Updating `UAM_Artifact_Index.yaml`.
- Any Git operation.
- Any publish, install, activation, deployment, or release-status change.

## Verification Checklist For Execution

Before moves:

- `Resolve-Path` every source and target parent.
- Confirm all resolved paths are inside the workspace root.
- Generate `pre-cleanup-manifest.sha256`.
- Confirm target paths do not already exist unless overwrite is explicitly authorized.
- Confirm no source path is a directory junction or symlink requiring special handling.

After moves:

- Generate `post-cleanup-manifest.sha256`.
- Verify moved file hashes match their pre-cleanup hashes.
- Verify active root files still exist.
- Verify `uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md`, `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`, and `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md` still exist.
- Verify `folder-organization-map.md` matches the new structure.
- Verify no evidence/run-control directory was moved unless explicitly approved.
- Verify no private raw material moved into public packet/export locations.

## Rollback Strategy

Default rollback is path reversal:

- Move archived files back to original paths.
- Move handoff packet files/folders back to original `handoff-packets/` locations.
- Move `uam-bridge-skills/requirements-dev.txt` back to root if scripts expect the old path.
- Restore docs references from the cleanup record.

For deleted empty folders:

- Recreate `.agents/` or `.git/` only if a runtime requires the placeholder.
- Do not attempt to reconstruct real Git metadata from an empty invalid `.git/`; use a proper clone instead.

For generated caches:

- Regenerate by rerunning the relevant scripts if needed.

## Recommended Next Move

Next cleanup review should focus only on remaining unexecuted rows and should check:

- whether the empty `.agents/` and invalid empty `.git/` shells should be deleted now;
- whether `handoff-packets/open/` is the right shape or whether packets should move into a package-local `packets/` root;
- whether `master-git-export.md` can be archived safely now;
- whether the proposed stages avoid manifest/index breakage.

If the review passes and Stage 0 reconfirms no active-index/loadable-content mismatch, the first executable cleanup should be Stage 0, the needed Stage 1 target folders, and Stage 2 only. That removes the most confusing root clutter with the smallest blast radius while preserving the plan's own stop gates.

Do not execute cleanup from this plan without explicit user authorization naming the stage or target paths.
