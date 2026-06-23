# Master Git Export Automation

Status: superseded narrow export helper note
Evidence ceiling: static file export and hash verification only

Supersession note: `docs/publication/bridge-skills-master-repo-publication-plan.md` is the governing plan for project-wide, active-set-based publication into the master UAM repository. This document remains as a record of the earlier ChatGPT architecture audit export helper and should not be treated as the full publication workflow.

## Purpose

Use `tools/active/export_relevant_files.ps1` to copy a curated UAM Bridge packet into a local export folder or into a separate master Git repository clone for ChatGPT, API, or other external-review access.

The automation exists because not every important working artifact lives inside the canonical package tree when it is first created. For example, fresh-context and architecture-audit packets may be created under the workspace-level `handoff-packets/` folder before they are ready to be shared through a Git-backed source bundle.

## Current Export Profile

The default profile exports the ChatGPT architecture audit packet plus the source files it tells ChatGPT to inspect:

- `handoff-packets/open/chatgpt-architecture-audit-packet-2026-06-22.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md`
- `uam-bridge-skills/adapters/chatgpt/README.md`
- `uam-bridge-skills/tests/runs/compounding-run-001/README.md`
- `uam-bridge-skills/tests/runs/compounding-run-001/codex-run-001/scoring/mapped-results.md`
- the eight `uam-bridge-skills/skills/active/uam-bridge-skills/commands/*/SKILL.md` files

The export intentionally excludes:

- `AGENTS.md`
- raw private transcripts
- private run maps
- global installed Codex skills
- evaluator scoring keys
- prior conversation exports

## Local Export

Run from the workspace root:

```powershell
.\uam-bridge-skills\tools\active\export_relevant_files.ps1
```

Default output:

```text
uam-bridge-skills/exports/generated/chatgpt-architecture-audit-2026-06-22/
```

The script writes:

- `EXPORT_MANIFEST.md`
- `HASHES.sha256`
- `CHATGPT_ARCHITECTURE_AUDIT_PACKET.md`
- `source-snapshot/`

## Export To Master Git Repo

When the local master Git clone path is known, run:

```powershell
.\uam-bridge-skills\tools\active\export_relevant_files.ps1 -TargetRepoPath "C:\path\to\master-repo"
```

By default, the target path inside the repo is:

```text
uam-bridge-skills/exports/generated/chatgpt-architecture-audit-2026-06-22/
```

To choose another repo subfolder:

```powershell
.\uam-bridge-skills\tools\active\export_relevant_files.ps1 `
  -TargetRepoPath "C:\path\to\master-repo" `
  -TargetSubdir "exports"
```

## Optional Git Staging

To copy and stage the exported bundle without committing or pushing:

```powershell
.\uam-bridge-skills\tools\active\export_relevant_files.ps1 `
  -TargetRepoPath "C:\path\to\master-repo" `
  -Stage
```

The script never commits, pushes, installs, activates, deploys, or updates release status.

## Integrity Behavior

The script:

- verifies that each required source file exists;
- copies only the curated export files;
- compares SHA-256 hashes before and after each copy;
- writes `EXPORT_MANIFEST.md`;
- writes `HASHES.sha256`;
- refuses `-Stage` unless `-TargetRepoPath` points to a usable Git repository;
- preserves stale files in an existing export folder and warns instead of deleting them.

## Claim Limits

An exported packet is a sharing artifact, not runtime proof.

Do not claim:

- global installation;
- activation;
- v1 readiness;
- provider parity;
- gate passage;
- production behavior;
- broad implicit routing readiness.
