# GitHub Master Repo Automation

Status: prepare-not-push process
Evidence ceiling: static validation until run against a local clone
Master repo URL: `https://github.com/matthewlwalling-maker/User-Agent-Model-UAM.git`

## Purpose

Publish the local UAM Bridge Skills active source package into the master UAM GitHub repository without mixing active source, generated exports, private test material, or runtime claims.

The automation is implemented by:

```text
uam-bridge-skills/tools/active/publish_bridge_skills_to_master_repo.ps1
```

## Default Publication Target

The script publishes into a local clone of the master repo at:

```text
active/uam/bridge-skills/
  AGENTS.md
  README.md
  PACKAGE_STAMP.yaml
  SOURCE_MANIFEST.yaml
  PUBLICATION_RECORD.md
  authority/
  package/
```

`AGENTS.md` is placed at the Bridge active root so future agents working inside `active/uam/bridge-skills/` receive the Bridge-specific operating contract without replacing the master repository's root `AGENTS.md`.

`authority/` contains workspace authority and source-context snapshots that travel with the Bridge package:

```text
authority/
  UAM_Artifact_Index.yaml
  UAM_Artifact_Naming_and_Archive_Convention.md
  UAM_Model_Framework.md
  UAM_Model_Participation_and_Assurance_Plan.md
  UAM_Source_Intake_and_Context_Map.md
  UAM_Bootstrap_Pair_Brief.md
```

The local package copied into `package/` preserves the current hierarchy, including:

```text
package/skills/active/uam-bridge-skills/
  MANIFEST.yaml
  KERNEL.md
  CHAIN_ROUTER.md
  commands/*/SKILL.md
```

## Default Exclusions

The publisher excludes generated or private material by default:

- `exports/generated/`
- generated cache folders and `*.pyc`
- `.local.*` files
- `private.local/`
- `scoring-keys.local/`
- `raw/` and `raw-private/`
- `raw-outputs.*`
- private run maps and private hashes
- mapping keys
- scoring keys
- test response folders

## Prepare Or Publish

Prepare/update a local clone without staging:

```powershell
.\uam-bridge-skills\tools\active\publish_bridge_skills_to_master_repo.ps1 `
  -TargetRepoPath "C:\path\to\User-Agent-Model-UAM"
```

Prepare and stage the active package:

```powershell
.\uam-bridge-skills\tools\active\publish_bridge_skills_to_master_repo.ps1 `
  -TargetRepoPath "C:\path\to\User-Agent-Model-UAM" `
  -Stage
```

Prepare, stage, and commit:

```powershell
.\uam-bridge-skills\tools\active\publish_bridge_skills_to_master_repo.ps1 `
  -TargetRepoPath "C:\path\to\User-Agent-Model-UAM" `
  -Stage `
  -Commit `
  -CommitMessage "Publish UAM Bridge Skills active set"
```

Push requires an explicit confirmation phrase:

```powershell
.\uam-bridge-skills\tools\active\publish_bridge_skills_to_master_repo.ps1 `
  -TargetRepoPath "C:\path\to\User-Agent-Model-UAM" `
  -Stage `
  -Commit `
  -Push `
  -PushConfirmation "PUSH UAM BRIDGE SKILLS TO MASTER"
```

## Safety Rules

- The script requires `-TargetRepoPath`; it does not assume the current workspace is a usable Git repo.
- The script refuses dirty target repos unless `-AllowDirtyTarget` is supplied.
- The script warns when the local clone remote does not match the master repo URL.
- The script does not checkout branches automatically.
- The script only pushes when `-Push`, `-Commit`, and the exact push confirmation phrase are supplied.
- The script does not install, activate, deploy, or claim readiness.
- The script runs workspace governance QC and YAML validation before publication unless `-SkipValidation` is explicitly supplied.
- The script publishes Bridge authority files under `active/uam/bridge-skills/`, not over the master repository root authority files.

## Current Stop Gate

This process is built and statically validated, and it has been shaped against the observed GitHub repository layout where `active/uam/` currently contains only `.gitkeep`. First live use should run without `-Stage`, inspect the generated `active/uam/bridge-skills/` root, then rerun with `-Stage` or `-Commit` only after review.
