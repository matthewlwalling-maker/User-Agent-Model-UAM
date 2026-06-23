# UAM Artifact Identity, Naming, and Archive Convention

**Artifact ID:** `UAM-ARTIFACT-NAMING`  
**Canonical filename:** `UAM_Artifact_Naming_and_Archive_Convention.md`  
**Status:** adopted project rule  
**Authority:** explicit user decision  
**Effective:** 2026-06-20  
**Scope:** governed UAM artifacts, registers, contracts, packets, handoffs, evidence, and implementation deliverables  
**Artifact index:** `UAM_Artifact_Index.yaml`

<!-- UAM:ARTIFACT-STAMP-BEGIN -->
**Artifact stamp**

```yaml
artifact_revision: 2
revision_date: 2026-06-20
content_sha256: 01a6ea18021702339c406f65cc71b6d86eadc1df8f01194b0b12bdfb6a091403
hash_profile: UAM-CANONICAL-TEXT-SHA256-1
```
<!-- UAM:ARTIFACT-STAMP-END -->

## 1. Governing identity rule

> **Every artifact family has one stable, versionless active identity and immutable retrospectively named history. Use the bare stable name for explanation; pin the recorded stamp and loadable immutable content whenever a machine or downstream agent will act.**

The active title, stable artifact ID, and canonical filename MUST NOT contain a project version, revision, date, status, `latest`, `current`, `final`, or candidate suffix. Status remains metadata.

## 2. Artifact stamp

Every material active document carries one whole-document stamp:

```yaml
artifact_revision: <monotonic integer>
revision_date: <ISO-8601 date>
content_sha256: <authoritative canonical content hash>
hash_profile: UAM-CANONICAL-TEXT-SHA256-1
```

The revision and date aid navigation. `content_sha256` is the authoritative content identity.

### 2.1 Canonical hash profile

`UAM-CANONICAL-TEXT-SHA256-1` is computed once by the designated updater:

1. decode as UTF-8 without BOM;
2. normalize line endings to LF;
3. ensure one terminal LF;
4. remove exactly one complete artifact-stamp block, including its begin/end markers and one immediately following newline when present;
5. SHA-256 hash the remaining UTF-8 bytes.

Markdown uses `<!-- UAM:ARTIFACT-STAMP-BEGIN -->` and `<!-- UAM:ARTIFACT-STAMP-END -->`. YAML uses the same markers as full-line comments. Consumers reference the updater-recorded value. Only a conforming validator may recompute it as an integrity check; verification does not mint a new identity.

## 3. Reference semantics

| Form | Meaning | Permitted use |
|---|---|---|
| Bare stable name or ID | Track the active artifact | prose, navigation, planning |
| Stable identity + full stamp + loadable immutable content reference | Consume one exact state | contracts, assignments, handoffs, builds, adoptions, compatibility records, evidence |
| Immutable archive path + recorded hash | Historical state | reconstruction, rollback, audit |

A mutable active path alone is never a frozen acting reference. A filename, version label, revision counter, date, or hash without loadable content is insufficient for context-isolated execution.

## 4. Single-writer replacement transaction

Updating an active artifact is one serialized operation owned by its designated writer:

1. resolve the active artifact through `UAM_Artifact_Index.yaml`;
2. verify the active header matches the index;
3. copy the outgoing file unchanged to its immutable archive path;
4. verify and record the archive file hash;
5. prepare the replacement on a branch or temporary path;
6. compute and insert the new authoritative content hash;
7. validate structure, references, and monotonic revision;
8. atomically replace the active slot;
9. update the index in the same controlled transaction;
10. revalidate header/index agreement.

A concurrent writer MUST create a candidate branch for reconciliation and MUST NOT overwrite the active file.

## 5. Current resolution and staleness

The active document header is source of truth for its own stamp. The shared index maps stable identity to canonical path, current stamp, status, owner, dependencies, and archive pointers.

Any header/index disagreement or pinned/current mismatch flags and blocks material action until bounded compatibility review and revalidation. A consumer MUST NOT silently continue on the stale pin or silently adopt the new state.

## 6. Archive form

Before replacement, archive the outgoing file unchanged under:

```text
archive/<Stable Name>/<Stable Name> — r<N> (<ISO date>) [<12-char-hash>].<ext>
```

Legacy material keeps the label it actually carried:

```text
archive/<Stable Name>/<Stable Name> — pre-convention <legacy label> (<ISO date>) [<12-char-hash>].<ext>
```

Administrative reconciliation snapshots MAY use a truthful descriptor such as `displaced active-set snapshot` or `displaced identity-migration snapshot`. Archive content is immutable. Missing historical bytes are recorded as gaps and never fabricated.

## 7. Active-set boundary

Only the files named as current in `UAM_Artifact_Index.yaml` are active. Files outside the declared canonical active-set root are source intake, displaced snapshots, or history even when their filenames resemble canonical names. This prevents an attachment directory or package cache from creating a second active artifact accidentally.

Project instructions are currently placed in source material as `AGENTS.md`; therefore `AGENTS.md` is the sole canonical active path for `UAM-ARCHITECT-INSTRUCTIONS`. A second active `UAM_Architect_Project_Instructions.md` is prohibited.

## 8. Machine-schema exception

A protocol, API, or serialized state object MAY retain an internal schema/API version when parsing or compatibility requires it. This exception does not permit version tokens in the project artifact title, stable ID, or active filename.

## 9. Completion gate

A reconciliation passes only when:

- every artifact family has exactly one indexed active path;
- all active headers and index stamps agree;
- every displaced materialized predecessor is preserved byte-for-byte;
- known but unavailable predecessor bytes are recorded as gaps;
- acting references can resolve exact loadable content;
- no concurrent or duplicate active instruction/framework/index path remains inside the canonical set;
- rollback is possible by promoting an archived snapshot through a new serialized replacement transaction.
