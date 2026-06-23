# Bridge Skills Master Repo Publication Plan

Status: governing publication plan for UAM Bridge Skills; not yet executed in the master repo
Evidence ceiling: design-time source and repository-structure inspection
Master repository: `matthewlwalling-maker/User-Agent-Model-UAM`
Default branch observed: `main`

## Purpose

This plan defines how UAM Bridge Skills should be published into the master UAM GitHub repository as a scalable active set with archive lineage, package stamps, file manifests, evidence separation, and future automation paths for staging, committing, and pushing.

The plan replaces the earlier narrow "export a ChatGPT audit packet" framing. That packet remains one possible export profile, but the publication system must govern the whole Bridge Skills source package and its supporting evidence, packets, handoffs, and generated export bundles.

## Source Basis

This plan is based on:

- `UAM_Artifact_Naming_and_Archive_Convention.md`
- `UAM_Artifact_Index.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md`
- observed master repo tree containing `active/uam/`, `archive/uam/`, `evidence/`, `handoffs/`, `packets/`, and `registers/`

The master repo artifact convention controls publication identity and archive lineage. The Bridge Skills manifest controls the internal package source layout. Neither one should silently override the other.

## Core Decision

UAM Bridge Skills should be published as a package-level active artifact family:

```yaml
stable_artifact_id: UAM-BRIDGE-SKILLS
stable_name: UAM Bridge Skills
active_root: active/uam/bridge-skills
status: rollout-lab-candidate
evidence_ceiling: design-time
active_write_owner: UAM Architect under user/Gatekeeper authority
```

The active root is versionless. Versions, dates, hashes, and prior states live in stamps, manifests, evidence records, archive paths, and commit history.

## Master Repo Placement

Use object type to decide placement:

| Object type | Master repo path | Rule |
|---|---|---|
| Active Bridge Skills package | `active/uam/bridge-skills/` | Latest governed active set. Versionless path only. |
| Archived active-set snapshots | `archive/uam/bridge-skills/` | Immutable outgoing active package snapshots. |
| Eval records, audit records, run results | `evidence/uam/bridge-skills/` | Evidence only; never active package authority. |
| Handoff packets | `handoffs/uam/bridge-skills/` | Transfer material; not active source. |
| Runnable/shareable packets | `packets/uam/bridge-skills/` | Operator, evaluator, install, test, or provider packets. |
| Registers or publication records | `registers/` or `active/uam/bridge-skills/registers/` | Root registers for cross-UAM authority; local registers for Bridge-only operational records. |

Recommended active root structure:

```text
active/uam/bridge-skills/
  AGENTS.md
  README.md
  PACKAGE_STAMP.yaml
  SOURCE_MANIFEST.yaml
  PUBLICATION_RECORD.md
  authority/
    UAM_Artifact_Index.yaml
    UAM_Artifact_Naming_and_Archive_Convention.md
    UAM_Model_Framework.md
    UAM_Model_Participation_and_Assurance_Plan.md
    UAM_Source_Intake_and_Context_Map.md
    UAM_Bootstrap_Pair_Brief.md
  package/
    adapters/
    docs/
    tests/
    lenses/
    skills/
      active/
        uam-bridge-skills/
          KERNEL.md
          MANIFEST.yaml
          CHAIN_ROUTER.md
          commands/
    tools/
  exports/
    <generated export profile>/
```

`package/` is the published source package root. The active skill package anchors remain grouped under `package/skills/active/uam-bridge-skills/`, and paths inside that `MANIFEST.yaml` remain package-relative.

`AGENTS.md` belongs at `active/uam/bridge-skills/AGENTS.md` so future agents operating inside the Bridge subtree receive the Bridge-specific contract without overwriting the master repository root `AGENTS.md`.

`authority/` carries the Bridge workspace authority and source-context snapshots needed to understand why the package exists and how it was governed. These are source-context copies for the Bridge active set; they do not replace the master repository's root authority files unless a separate master-repo authority transaction explicitly updates those root files.

## Active Set Rule

Only `active/uam/bridge-skills/` is the current Bridge Skills active package in the master repo.

Files under `evidence/`, `handoffs/`, `packets/`, `archive/`, or local development exports are not active source, even when they contain snapshots of source files. Consumers must not treat a packet, evidence bundle, or archive snapshot as the current package unless an acting reference explicitly pins that immutable state.

## Version And Dating Policy

Use active-set revisions, not versioned active paths.

Rules:

- The active path never includes `latest`, `current`, `final`, dates, semantic versions, or status labels.
- `artifact_revision` increments only when the active Bridge Skills package is published or replaced in the master repo.
- `revision_date` is the date of that publication/replacement transaction.
- Prior local work can be recorded as lineage, but its dates must be observed or described as unknown.
- Do not "backdate" a publication date to make history look cleaner.
- Use "backfilled lineage" for reconstructed history, with exact observed dates and hashes when available.
- If exact prior bytes are unavailable, record a predecessor gap rather than fabricating an archive snapshot.

Initial publication should be revision `1` for the master repo Bridge Skills active set, even if the internal package version remains `0.1.0`.

The internal package version and the master active-set revision are separate:

| Field | Scope | Example |
|---|---|---|
| `package_id` / `version` in `package/skills/active/uam-bridge-skills/MANIFEST.yaml` | Bridge Skills package semantics | `uam-bridge-skills` / `0.1.0` |
| `artifact_revision` in `PACKAGE_STAMP.yaml` | Master repo active-set publication | `1`, `2`, `3` |
| Git commit SHA | Repository change identity | produced by Git |

## Stamp Files

Every active Bridge Skills publication must include `PACKAGE_STAMP.yaml`.

Required shape:

```yaml
stable_artifact_id: UAM-BRIDGE-SKILLS
stable_name: UAM Bridge Skills
artifact_revision: 1
revision_date: YYYY-MM-DD
package_manifest_path: package/skills/active/uam-bridge-skills/MANIFEST.yaml
workspace_agents_path: AGENTS.md
workspace_authority_root: authority
source_manifest_path: SOURCE_MANIFEST.yaml
content_sha256: <deterministic package manifest hash>
hash_profile: UAM-PACKAGE-TREE-SHA256-1
evidence_ceiling: design-time
release_status: rollout-lab-candidate
install_status: not-installed
activation_status: not-activated
published_from:
  local_workspace_root: <path recorded by publisher>
  source_package_root: uam-bridge-skills
  source_package_version: 0.1.0
```

`PACKAGE_STAMP.yaml` is the package-level counterpart to a document stamp. It records package identity, not runtime readiness.

## Package Hash Profile

Use `UAM-PACKAGE-TREE-SHA256-1` for the Bridge Skills package active set.

Profile:

1. Include all files listed in `SOURCE_MANIFEST.yaml`.
2. Decode file bytes exactly as stored; do not normalize binary or archive bytes.
3. For text files, record their file SHA-256 as bytes on disk.
4. Sort manifest entries by repository-relative path using `/`.
5. Build canonical manifest lines:

```text
<sha256><two spaces><repo-relative-path><LF>
```

6. SHA-256 hash the UTF-8 bytes of the sorted canonical manifest lines.

The package hash is a hash of the source manifest, not a tarball hash. This makes it deterministic across machines without relying on archive metadata.

## Source Manifest

Every active publication must include `SOURCE_MANIFEST.yaml`.

Required shape:

```yaml
manifest_profile: UAM-BRIDGE-SKILLS-SOURCE-MANIFEST-1
generated_at: YYYY-MM-DDTHH:MM:SSZ
active_root: active/uam/bridge-skills
package_root: active/uam/bridge-skills/package
package_content_sha256: <same value as PACKAGE_STAMP.yaml content_sha256>
entries:
  - path: package/skills/active/uam-bridge-skills/KERNEL.md
    sha256: <file sha256>
    object_type: source
    source_origin: uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md
  - path: evidence/...
    sha256: <file sha256>
    object_type: evidence
    source_origin: ...
```

The first implementation should keep active source entries separate from evidence entries. If evidence is copied into `evidence/uam/bridge-skills/`, it should have its own evidence manifest rather than being mixed into the active source package hash unless explicitly selected as part of the active package.

## Backfilled Lineage

Initial publication should include a backfilled lineage section in `PUBLICATION_RECORD.md`, not fabricated historical active revisions.

Recommended shape:

```yaml
backfilled_lineage:
  - label: local-rollout-lab-candidate-before-master-publication
    observed_source: local workspace
    observed_date_range: 2026-06-20 to 2026-06-22
    materialization_status: exact local bytes available at publication time
    note: first master repo publication; not a prior master active revision
```

If previous exact bytes are later recovered, they can be archived as truthful predecessor snapshots with observed filenames and hashes.

## Archive Transaction

Every replacement after revision `1` must follow a single-writer archive-replace-restamp-reindex transaction:

1. Resolve current active root from `UAM_Artifact_Index.yaml`.
2. Verify `PACKAGE_STAMP.yaml` matches the index entry.
3. Copy the outgoing active root unchanged to `archive/uam/bridge-skills/`.
4. Name the archive snapshot using the master repo archive convention.
5. Generate an archive manifest and file hashes.
6. Prepare the replacement active root in a temporary work path.
7. Generate `SOURCE_MANIFEST.yaml`.
8. Generate `PACKAGE_STAMP.yaml`.
9. Replace the active root.
10. Update `UAM_Artifact_Index.yaml` in the same transaction.
11. Revalidate active stamp/index agreement.
12. Stage the exact changed paths.

The publisher must not delete outgoing active bytes until the archive snapshot has been written and hash-verified.

## Artifact Index Entry

When the first active package is published, add an entry to `UAM_Artifact_Index.yaml` under `active_artifacts`.

Proposed entry shape:

```yaml
- stable_artifact_id: UAM-BRIDGE-SKILLS
  stable_name: UAM Bridge Skills
  canonical_filename: active/uam/bridge-skills/PACKAGE_STAMP.yaml
  status: rollout-lab-candidate; source package active set
  current_stamp:
    artifact_revision: 1
    revision_date: YYYY-MM-DD
    content_sha256: <package content sha256>
    hash_profile: UAM-PACKAGE-TREE-SHA256-1
  content_ref: active/uam/bridge-skills/
  source_manifest_ref: active/uam/bridge-skills/SOURCE_MANIFEST.yaml
  current_stamp_authority: active package stamp
  active_write_owner: UAM Architect under user/Gatekeeper authority
  parent_artifacts:
    - UAM-FRAMEWORK
    - UAM-ARTIFACT-NAMING
  archive_pointers: []
```

The `canonical_filename` points to the package stamp because a folder cannot carry a document header.

## Evidence Placement

Evidence should not be mixed into the active package by default.

Recommended evidence paths:

```text
evidence/uam/bridge-skills/compounding-run-001/
evidence/uam/bridge-skills/static-validation/
evidence/uam/bridge-skills/architecture-audits/
evidence/uam/bridge-skills/publication/
```

Evidence records must retain their claim ceiling:

- design-time
- static validation
- simulated transcript evidence
- live-runtime
- post-implementation
- production-observed

Publishing evidence to the master repo does not upgrade its evidence stage.

## Packet And Handoff Placement

Use packets for executable or shareable bundles:

```text
packets/uam/bridge-skills/chatgpt-architecture-audit/
packets/uam/bridge-skills/stage-2-codex-dogfood/
packets/uam/bridge-skills/evaluator/
```

Use handoffs for state transfer:

```text
handoffs/uam/bridge-skills/
```

Packets and handoffs may include source snapshots, but they are not active source unless copied into `active/uam/bridge-skills/` and indexed.

## Publisher Automation Requirements

The project-wide publisher should replace the narrow one-profile exporter.

Recommended tool:

```text
uam-bridge-skills/tools/active/publish_bridge_skills_to_master_repo.ps1
```

Required modes:

| Mode | Behavior |
|---|---|
| `-Plan` | Print planned source, target paths, archive action, index action, and stop gates. No writes. |
| `-PrepareLocal` | Build a local publication tree under `uam-bridge-skills/exports/master-repo-publication/<run-id>/`. |
| `-TargetRepoPath <path>` | Publish into a local clone of the master repo. |
| `-ArchivePrevious` | Archive the outgoing active root before replacement. Required after revision 1. |
| `-UpdateIndex` | Update `UAM_Artifact_Index.yaml` with the package stamp and archive pointer. |
| `-StageGit` | Run `git add` for changed paths only. |
| `-Commit` | Optional future mode; requires explicit flag, clean generated summary, and user confirmation. |
| `-Push` | Optional future mode; requires explicit flag and confirmation after commit SHA is known. |

The initial implementation supports `-TargetRepoPath`, `-CloneIfMissing`, `-ReplaceActiveRoot`, `-Stage`, `-Commit`, and `-Push`. Push is guarded by an exact `-PushConfirmation` phrase. First live use should run without `-Stage`, inspect the generated active root, then stage or commit only after review.

## Export Profiles

The publisher should read an export/publication registry rather than hard-code one packet.

Recommended registry:

```text
uam-bridge-skills/publication-profiles.yaml
```

Initial profiles:

| Profile | Target | Purpose |
|---|---|---|
| `active-source-package` | `active/uam/bridge-skills/` | Current Bridge Skills active source package. |
| `compounding-run-evidence` | `evidence/uam/bridge-skills/compounding-run-001/` | Simulated transcript evidence and audit records. |
| `chatgpt-architecture-audit-packet` | `packets/uam/bridge-skills/chatgpt-architecture-audit/` | ChatGPT architecture audit packet and source snapshot. |
| `stage-2-dogfood-packet` | `packets/uam/bridge-skills/stage-2-codex-dogfood/` | No-install isolated Codex dogfood packet. |
| `handoff-packets` | `handoffs/uam/bridge-skills/` | Transfer packets for external or fresh-context continuation. |

Each profile must declare:

```yaml
profile_id: string
target_root: string
object_type: source | evidence | packet | handoff | archive | register
include:
  - path patterns
exclude:
  - path patterns
claim_ceiling: string
requires_private_exclusion: true | false
requires_index_update: true | false
requires_archive_transaction: true | false
```

## Private And Exclusion Rules

The publisher must exclude by default:

- raw private transcripts unless a profile explicitly includes them for private audit;
- private run maps before scoring is locked;
- local `.git`, `.venv`, caches, and `__pycache__`;
- global installed skills from `.codex/skills`;
- user-private temp files and screenshots;
- unreviewed conversation history;
- generated export folders unless a profile intentionally republishes them as packets.

Private audit exports require a separate profile and must not be mixed with public evaluator or ChatGPT packets.

## Commit And Push Gates

Commit and push are high-authority actions.

Before commit:

- publisher plan must be reviewed;
- workspace governance QC and YAML validation must pass unless explicitly marked blocked;
- file manifest must be generated;
- package hash must be computed;
- index update must be included when active source changes;
- archive snapshot must exist for replacement revisions;
- static checks must run or be explicitly marked blocked;
- commit message must state evidence ceiling and no-readiness claim;
- user must explicitly authorize commit.

Before push:

- commit SHA must be known;
- branch must be confirmed;
- remote must be confirmed;
- user must explicitly authorize push;
- no install, activation, deployment, or release status claim may be bundled into the push.

Default branch commits are allowed only if the user explicitly chooses that route. Safer default is a branch such as:

```text
bridge-skills/publication-r1
```

## Stop Gates

Stop before publishing or staging when:

- master repo path is unresolved;
- target repo is not a Git repo;
- active root exists and `-ArchivePrevious` was not supplied for replacement;
- package stamp and index disagree;
- generated manifest hash does not match copied files;
- private files would enter a public profile;
- evidence would be promoted as active source;
- current action would imply install, activation, v1 readiness, provider parity, or runtime proof;
- user has not explicitly authorized commit or push.

## First Implementation Sequence

Recommended next implementation steps:

1. Build `publication-profiles.yaml`.
2. Use `tools/active/publish_bridge_skills_to_master_repo.ps1` as the guarded publisher; keep `tools/active/export_relevant_files.ps1` for narrow packet exports.
3. Add `-Plan` and `-PrepareLocal` modes first.
4. Generate a local publication tree for `active-source-package`.
5. Review the generated `PACKAGE_STAMP.yaml`, `SOURCE_MANIFEST.yaml`, and `PUBLICATION_RECORD.md`.
6. Add `-TargetRepoPath` support for a local clone of `matthewlwalling-maker/User-Agent-Model-UAM`.
7. Add archive/index update support.
8. Run static validation.
9. Only after review, stage changes in Git.
10. Commit and push only after explicit authorization.

## Claim Limits

Publishing Bridge Skills to the master repo establishes source availability and traceable package identity only.

It does not establish:

- global installation;
- runtime activation;
- provider parity;
- v1 readiness;
- release readiness;
- eval gate passage;
- production behavior;
- broad implicit routing readiness.

Those claims require their own evidence and gates.
