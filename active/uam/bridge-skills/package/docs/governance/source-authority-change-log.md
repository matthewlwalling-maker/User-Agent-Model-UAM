# Source Authority Change Log

Status: active governance record
Evidence ceiling: static validation unless a specific entry names stronger evidence
Scope: source authority, agent instructions, active package controls, file-placement governance, publication controls, install controls, and QC controls for the UAM Bridge Skills workspace

## Purpose

This file is the canonical narrative record for changes to source-authority resources. It answers the question that hashes and archives cannot answer by themselves: why did the authority surface change, what files moved or changed, what validation was run, and what claims remain prohibited?

This log supplements, but does not replace, artifact stamps, archive snapshots, integrity records, migration ledgers, registries, manifests, or source control commits.

## Update Rule

Update this file in the same transaction whenever a change materially affects any of these resources or their authority semantics:

- `AGENTS.md`
- `UAM_Artifact_Index.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/commands/*/SKILL.md`
- `uam-bridge-skills/SKILL_REGISTRY.yaml`
- `uam-bridge-skills/TEST_REGISTRY.yaml`
- `uam-bridge-skills/docs/governance/*`
- `uam-bridge-skills/docs/install/*`
- `uam-bridge-skills/docs/publication/*`
- `uam-bridge-skills/docs/cleanup/folder-organization-map.md`
- `uam-bridge-skills/docs/cleanup/workspace-taxonomy-v2.md`
- `uam-bridge-skills/tools/active/*` when source authority, publication, install, export, validation, or QC semantics change

For indexed root authority artifacts, use the full archive-replace-restamp-reindex transaction and record the archive and hash references here.

## Required Entry Fields

Each entry should include:

- `date`
- `change_id`
- `authority_class`
- `changed_files`
- `reason`
- `summary`
- `archive_ref`
- `hash_or_integrity_ref`
- `validation`
- `evidence_ceiling`
- `prohibited_claims`
- `follow_up`

Use `none` only when a field truly does not apply.

## Entries

### 2026-06-22-root-cleanup-and-agent-instruction-archive

Date: 2026-06-22 through 2026-06-23
Change ID: `2026-06-22-root-cleanup-and-agent-instruction-archive`
Authority class: workspace organization and indexed root authority
Changed files:

- `AGENTS.md`
- `UAM_Artifact_Index.yaml`
- `uam-bridge-skills/docs/cleanup/root-workspace-cleanup-plan.md`
- `uam-bridge-skills/docs/cleanup/workspace-taxonomy-v2.md`
- `uam-bridge-skills/docs/cleanup/final-workspace-cleanup-record-2026-06-22.md`

Reason: the workspace needed a governed cleanup model so active source, donor context, evidence, generated exports, packets, and archives did not remain mixed at the root.
Summary: root cleanup planning and follow-up source-control alignment established the active package map, archived prior agent-instruction snapshots, and mirrored the active `AGENTS.md` stamp in `UAM_Artifact_Index.yaml`.
Archive reference: `archive/UAM Architect Project Instructions/UAM Architect Project Instructions -- r3 pre-source-control-alignment (2026-06-23) [4ea49ec8f037].md`
Hash or integrity reference: `UAM_Artifact_Index.yaml` active entry for `UAM-ARCHITECT-INSTRUCTIONS`; cleanup integrity records under `uam-bridge-skills/tests/integrity/`
Validation: static file inspection and workspace governance QC in later follow-up
Evidence ceiling: static validation
Prohibited claims: no install, activation, publication, deployment, readiness, or runtime-control claim
Follow-up: keep future authority changes recorded in this log

### 2026-06-23-active-skill-package-grouping

Date: 2026-06-23
Change ID: `2026-06-23-active-skill-package-grouping`
Authority class: active package source authority and command path control
Changed files:

- `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/commands/*/SKILL.md`
- `uam-bridge-skills/SKILL_REGISTRY.yaml`
- `uam-bridge-skills/TEST_REGISTRY.yaml`
- `AGENTS.md`
- `UAM_Artifact_Index.yaml`

Reason: the active skills, kernel, manifest, and router needed to live together as one package instead of leaving anchor files separate from command skills.
Summary: the active command package was grouped under `skills/active/uam-bridge-skills/`, and path authorities were updated so active command loading points to `skills/active/uam-bridge-skills/commands`.
Archive reference: `archive/UAM Architect Project Instructions/UAM Architect Project Instructions -- r3 pre-source-control-alignment (2026-06-23) [4ea49ec8f037].md`
Hash or integrity reference: `uam-bridge-skills/tests/integrity/active-skill-package-relocation-2026-06-23-relocation-map.tsv`; `uam-bridge-skills/tests/integrity/active-skill-package-relocation-2026-06-23-post-state.sha256`
Validation: `validate_workspace_governance.py` and `validate_yaml.py` were run in follow-up and passed with the known empty `evals/` warning
Evidence ceiling: static validation
Prohibited claims: no global install, isolated dogfood activation, runtime verification, broad implicit routing, or readiness claim
Follow-up: keep active package anchors and command skills housed together unless a future migration ledger authorizes a different map

### 2026-06-23-workspace-governance-qc-and-master-publisher

Date: 2026-06-23
Change ID: `2026-06-23-workspace-governance-qc-and-master-publisher`
Authority class: validation, export, and publication automation controls
Changed files:

- `uam-bridge-skills/tools/active/validate_workspace_governance.py`
- `uam-bridge-skills/tools/active/publish_bridge_skills_to_master_repo.ps1`
- `uam-bridge-skills/tools/active/export_relevant_files.ps1`
- `uam-bridge-skills/docs/publication/github-master-repo-automation.md`
- `uam-bridge-skills/tests/records/static/workspace-governance-qc-2026-06-23.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`

Reason: future agents needed deterministic QC for the new hierarchy and a guarded path to prepare or publish the active package to the master GitHub repository.
Summary: added workspace governance QC and a guarded master-repo publisher. The publisher includes explicit push confirmation requirements and does not push without `-Push`, `-Commit`, and `-PushConfirmation "PUSH UAM BRIDGE SKILLS TO MASTER"`.
Archive reference: none
Hash or integrity reference: QC record at `uam-bridge-skills/tests/records/static/workspace-governance-qc-2026-06-23.md`
Validation: workspace governance QC passed with one expected warning for the empty `uam-bridge-skills/evals/` compatibility placeholder; YAML validation passed
Evidence ceiling: static validation
Prohibited claims: no commit, push, install, activation, deployment, runtime verification, or readiness claim
Follow-up: run the publisher only with explicit user authorization for the selected target repository action

### 2026-06-23-source-authority-change-log-created

Date: 2026-06-23
Change ID: `2026-06-23-source-authority-change-log-created`
Authority class: source authority change tracking
Changed files:

- `uam-bridge-skills/docs/governance/source-authority-change-log.md`
- `AGENTS.md`
- `UAM_Artifact_Index.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/tools/active/validate_workspace_governance.py`
- `uam-bridge-skills/docs/cleanup/folder-organization-map.md`
- `uam-bridge-skills/docs/cleanup/workspace-taxonomy-v2.md`
- `uam-bridge-skills/docs/cleanup/final-workspace-cleanup-record-2026-06-22.md`

Reason: the existing archive and index trail preserved bytes and current stamps, but did not provide one canonical explanation record for source-authority changes.
Summary: created this changelog, wired it into the workspace operating contract, added a manifest pointer, and extended governance QC so future authority changes must keep this record visible.
Archive reference: `archive/UAM Architect Project Instructions/UAM Architect Project Instructions -- r4 pre-source-authority-change-log (2026-06-23) [b5cf1794a741].md`
Hash or integrity reference: `UAM_Artifact_Index.yaml` active entry for `UAM-ARCHITECT-INSTRUCTIONS` after revision 5 restamp
Validation: post-change `validate_workspace_governance.py`, `validate_yaml.py`, PowerShell parser checks, hash checks, and read-back
Evidence ceiling: static validation
Prohibited claims: no install, activation, commit, push, deployment, runtime verification, or readiness claim
Follow-up: use this file as the first stop when asking why agent instructions or source authority resources changed

### 2026-06-23-master-repo-publication-target-corrected

Date: 2026-06-23
Change ID: `2026-06-23-master-repo-publication-target-corrected`
Authority class: publication automation and source-authority transport
Changed files:

- `uam-bridge-skills/tools/active/publish_bridge_skills_to_master_repo.ps1`
- `uam-bridge-skills/tools/active/validate_workspace_governance.py`
- `uam-bridge-skills/docs/publication/github-master-repo-automation.md`
- `uam-bridge-skills/docs/publication/bridge-skills-master-repo-publication-plan.md`
- `uam-bridge-skills/docs/governance/source-authority-change-log.md`

Reason: the first publisher copied the package tree but did not publish Bridge-specific agent instructions and root authority/source-context files into the target GitHub active set, and the observed GitHub `active/uam/` folder did not yet contain a `bridge-skills/` home.
Summary: updated the publisher to create `active/uam/bridge-skills/`, place Bridge `AGENTS.md` at that root, copy workspace authority and source-context files into `authority/`, generate a human-readable active-root `README.md`, and run source validation before publication.
Archive reference: none
Hash or integrity reference: generated `SOURCE_MANIFEST.yaml` and `PACKAGE_STAMP.yaml` on publication; local static validation before publication
Validation: post-change workspace governance QC, YAML validation, PowerShell parser check, and local dry-run against a disposable Git repository
Evidence ceiling: static validation
Prohibited claims: no GitHub commit, push, install, activation, deployment, runtime verification, or readiness claim
Follow-up: live publication still requires a local clone of `matthewlwalling-maker/User-Agent-Model-UAM`, inspection of generated `active/uam/bridge-skills/`, and explicit commit/push authorization
