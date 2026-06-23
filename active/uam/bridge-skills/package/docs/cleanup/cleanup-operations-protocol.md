# Cleanup Operations Protocol

Version: `0.1.0`
Status: cleanup protocol, not executed
Evidence level: design-time/static inspection

## Purpose

Give future agents a safe procedure for organizing this workspace without damaging source authority, donor resources, evidence records, blind-run materials, or user work.

This protocol authorizes planning and classification. It does not authorize deletion, moving, renaming, archive creation, Git operations, installation, or deployment.

## Required Inputs

Before proposing cleanup, identify or mark unavailable:

- cleanup objective
- target path or scope
- current workspace map
- whether Git metadata is available
- files or folders proposed for move/delete/archive
- preservation class for each target
- evidence stage
- user authorization for destructive or structural actions

Use `docs/cleanup/folder-organization-map.md` as the first routing resource.

## Context Recommendation Gate

Recommend a new context window before cleanup execution when:

- the current context is materially bloated and cleanup has many paths;
- the operation is discrete and can be executed from a packet;
- cleanup involves blind-run evidence or evaluator materials;
- prior discussion could bias classification of evidence or donor material.

Do not require a new context for a small documented patch or a non-destructive inspection.

If recommending a new context, provide a cleanup packet with exact target paths, allowed operations, prohibited operations, evidence ceiling, and stop condition.

## Cleanup Stages

### Stage 1: Inventory

Run non-destructive inspection only:

- list top-level folders and files;
- list candidate generated files such as `__pycache__` and `*.pyc`;
- list ad hoc run folders under `tests/runs/`;
- identify files outside the canonical package and donor vault;
- check whether Git metadata exists.

Do not move or delete during inventory.

### Stage 2: Classify

Assign every proposed cleanup target exactly one class:

- `preserve-authority`
- `preserve-source`
- `preserve-evidence`
- `preserve-donor`
- `cleanup-candidate`
- `needs-triage`

If classification is uncertain, use `needs-triage` and stop before action.

### Stage 3: Propose

Produce a cleanup plan with:

- target path;
- current class;
- proposed action;
- reason;
- risk;
- verification after action;
- rollback or recovery path;
- whether the action is destructive.

Do not bundle unrelated cleanup actions. Keep generated-cache cleanup separate from source reorganization, evidence archiving, and donor deduplication.

### Stage 4: Get Authorization

Ask for explicit approval before any:

- delete;
- move;
- rename;
- archive creation;
- donor-resource deduplication;
- evidence-record rewrite;
- manifest or package authority update;
- Git operation;
- global install or activation.

Approval must name the target paths or the precise action class.

### Stage 5: Execute Safely

Only after approval:

- re-check target paths immediately before action;
- verify resolved absolute paths remain inside the workspace;
- use native PowerShell file operations with `-LiteralPath`;
- avoid shell string construction for file operations;
- do not cross from PowerShell enumeration into another shell for deletion or moving;
- preserve unrelated files;
- stop immediately if an expected file is missing or an unexpected path appears.

For manual file edits, use `apply_patch`.

### Stage 6: Verify And Record

After execution:

- list changed, moved, or deleted paths;
- verify source authority files still exist;
- verify manifest paths still resolve if package paths changed;
- verify evidence/run-control records were not altered unless authorized;
- update `docs/cleanup/folder-organization-map.md` if structure changed;
- report evidence level and residual risk.

## Allowed Without Separate Cleanup Authorization

These are safe as inspection or documentation actions:

- read files;
- list files and directories;
- classify cleanup candidates;
- create or patch cleanup documentation;
- propose a cleanup plan;
- update this protocol after user authorization.

## Requires Explicit Authorization

These are not allowed by default:

- deleting `__pycache__` or `.pyc` files;
- moving donor files;
- deleting duplicate archives;
- moving root handoff or recommendation files;
- moving eval records or blind-run packets;
- renaming skills, adapters, docs, or eval files;
- rewriting `MANIFEST.yaml` paths because of cleanup;
- creating zip archives or delivery bundles;
- running blind tests or evals as part of cleanup.

## Special Rules By Area

### Root Files

Root files are high-context project sources. Do not move them merely for tidiness. If a root-to-docs migration is desired, create a migration plan and preserve loadable references.

### `FOR CONTEXT/`

Treat as a donor vault. Do not delete unpacked donor material or archives without explicit user authorization. Generated `.pyc` files inside donor material are cleanup candidates only if donor byte-fidelity is not required.

### `uam-bridge-skills/`

Treat as the canonical package. Any path change inside this folder may affect manifest authority, adapter derivation, or eval routing. Patch source files only with the owning command boundary.

### `tests/`

Separate reusable fixture source from evidence records and run packets:

- fixtures may be patched with eval-design authority;
- records should be append/versioned, not overwritten casually;
- run folders such as `blind-run-001/` preserve run-control state and must not be folded into reusable fixture files;
- generated caches are cleanup candidates.

### `docs/`

Docs may be added for governance, protocols, maps, and rollout resources. If docs become stale after cleanup, patch the affected docs in the same authorized cleanup series.

## Cleanup Plan Template

```text
Cleanup plan:
Scope:
Evidence level:
Git metadata:

Targets:
- Path:
  Class:
  Proposed action:
  Reason:
  Risk:
  Requires explicit authorization: yes/no
  Verification:
  Rollback/recovery:

Stop conditions:
- unexpected path expansion
- target classification uncertain
- evidence/run-control material in scope without explicit authorization
- manifest path would break
- user authorization does not name the action clearly
```

## Execution Prompt Template For A New Context

Use only when the context recommendation gate says a new context is useful:

```text
You are executing an authorized cleanup operation for the UAM Bridge Skills workspace.

Read:
- AGENTS.md
- uam-bridge-skills/docs/cleanup/folder-organization-map.md
- uam-bridge-skills/docs/cleanup/cleanup-operations-protocol.md
- the user-approved cleanup plan

Action boundary:
- Execute only the approved paths and actions.
- Do not infer additional cleanup.
- Do not run tests unless the plan explicitly authorizes them.
- Do not edit source files except documentation updates named in the plan.

Evidence ceiling: static filesystem verification.

Stop immediately if:
- any resolved target path is outside the workspace;
- any target is missing or unexpectedly different;
- the plan includes donor, evidence, or authority files without explicit approval;
- manifest paths would break.

Return:
- actions performed;
- paths changed;
- verification performed;
- files not touched;
- residual risks;
- next valid step.
```

## Current Recommendation

No structural cleanup should run automatically. The only currently obvious cleanup candidates are generated Python cache files, and even those should wait for explicit approval because two are inside donor material.
