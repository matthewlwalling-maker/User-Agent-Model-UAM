# UAM Source Intake and Context Map

**Artifact ID:** `UAM-SOURCE-CONTEXT-MAP`  
**Status:** candidate intake aid  
**Parent:** `UAM-ARCHITECT-INSTRUCTIONS`  
**Canonical filename:** `UAM_Source_Intake_and_Context_Map.md`  
**Artifact index:** `UAM_Artifact_Index.yaml`  
**Naming authority:** `UAM_Artifact_Naming_and_Archive_Convention.md`

<!-- UAM:ARTIFACT-STAMP-BEGIN -->
**Artifact stamp**

```yaml
artifact_revision: 2
revision_date: 2026-06-20
content_sha256: 6a296c658cc5f27a0262a7e6e86ebb906d9f218281dbd7bb96394a09f0127c39
hash_profile: UAM-CANONICAL-TEXT-SHA256-1
```
<!-- UAM:ARTIFACT-STAMP-END -->

## 1. Intake and naming rule

Provide source **content**, not filenames alone. A source may be supplied as an exact file, a raw archive, or a reference guaranteed loadable in the assigned context. Do not rewrite or clean the archive before intake.

`AGENTS.md` is already placed in project source material and is the sole active path for the Architect instructions. Do not create or request a second active `UAM_Architect_Project_Instructions.md`; classify any such file as a displaced snapshot.

Project-controlled active artifacts use stable versionless names and self-describing stamps. `UAM_Artifact_Index.yaml` records canonical paths, current stamps, status, parents, and archive pointers. Acting references pin the updater-recorded stamp and attach exact content or a guaranteed-loadable immutable reference; they never use a mutable active path as a frozen input. Active replacement is single-writer and serialized. A parent mismatch is flag-and-block unless an explicit compatibility check passes.

Donor and legacy filenames are preserved exactly as received so provenance is not destroyed. The Source Authority Register maps them to stable project identities; only earlier snapshots actually supplied are archived, while unavailable historical snapshots are recorded as gaps.

## 2. First package to provide

| Priority | Source group | Why it is needed now |
|---:|---|---|
| 1 | `project-state.md`, adoption/decision records, checksums, sentinel records | Establish current authority, hashes/archive lineage, and unresolved decisions |
| 2 | Full project directory tree or artifact inventory | Detect duplicates, supersession, missing dependencies, and bottoms-up clusters |
| 3 | `AB_Runtime_Authority_Reference_v1.1.md` | AB routing, authority, evidence stages, reach, stopping |
| 4 | `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` | Requirement tiers, capability derivation, scaling, E1-E12/sentinels |
| 5 | `OMR_Operator_Prototype_Runtime_v0.2.md` | OMR ownership, sequencing, branch/freshness, packets |
| 6 | `P2_State_Schemas_v0.1.json` | Exact current OMR state schemas and metadata donor |
| 7 | `OMR_Evidence_Capture_Protocol_v0.1.md` | Evidence, packet, reconstruction, context-isolation discipline |
| 8 | `P5_Executor_View_v0.1.yaml` | Adversarial and executor-facing fixtures |
| 9 | Current AB1-AB9 wrappers/macros and router tests | Actual operational surface to preserve/refactor |
| 10 | Current deployment-readiness plan and revisions | Reconcile build/test/deployment ordering with the active framework |

## 3. Second package

- `Codex conversation for AB Rethink.md`
- `Branch Conversation_UAM Architecture.txt`
- prompt and skill production templates/patterns
- Agent Builder quality model and failure catalog
- historical build/evaluation tasks and baseline outputs
- current runtime/profile/repository layout
- handoff/package artifacts and platform adapter material
- user operating profile sources and privacy rules

## 4. Third package: donor lens library

Provide exact source definitions, not names alone, for:

- `blind-grader`
- `spec-builder`
- `steelman-premortem`
- `variant-reconciliation`
- `gold-standard-comparison`
- `narrative-substance-review`
- `safe-shrink`
- `consistency-review`
- `break-it-tester`
- `model-vs-consensus`
- `prompt-refiner`
- `prediction-log`

## 5. Source register fields

For every artifact, record:

```yaml
artifact_id: <stable versionless id or unknown>
canonical_name: <stable human-readable name or unknown>
observed_filename: <exact supplied filename>
active_filename: <versionless canonical filename or null for archive-only source>
artifact_stamp:
  artifact_revision: <integer | legacy-label | unknown>
  revision_date: <ISO-8601-date | unknown>
  content_sha256: <authoritative-canonical-hash | unknown>
  hash_profile: <UAM-CANONICAL-TEXT-SHA256-1 | legacy | unknown>
content_ref: <attached | guaranteed-loadable | immutable-archive-path | null>
archive_filename: <path or null while active>
created_at: <timestamp or unknown>
modified_at: <timestamp or unknown>
status: authoritative-current-scope | adopted | candidate | implemented | validated | superseded | archive | unknown
system_scope: UAM | AB | OMR | runtime | evaluation | donor | user-profile | other
owned_subjects: []
predecessor_archive_refs: []
successor_active_ref: <stable id or null>
parent_refs: []
compatible_with: []
conflicts_with: []
source_type: contract | schema | implementation | evidence | fixture | conversation | decision | template | archive
evidence_stage: design-time | simulated | live-runtime | post-implementation | production-observed | not-applicable
loadability: attached | guaranteed-loadable | citation-only | missing
load_bearing_for: []
dimensions: []
operations: []
privacy_class: public-project | internal | sensitive | secret-prohibited
notes: <text>
```

## 6. Context loading matrix

| Context | Required sources | Deliberately excluded |
|---|---|---|
| C0 Architecture Control | project-state, source register, decision/conflict registers, framework, high-level artifact map | full donor library, raw runtime logs unless decision-relevant |
| C1 Primary Component | universal framework sections, assigned dimension/operation sections, exact local donor sources, frozen brief | unrelated dimensions and archives |
| C2 Independent Challenge | same requirements and load-bearing sources; primary candidate withheld during independent derivation | author rationale and previous comparison verdicts |
| C3 Evaluation | frozen candidate, rubric, fixtures, stable identities, pinned artifact stamps, loadable immutable content refs, evidence ceiling | mutation authority, repair instructions |
| C4 Implementation | adopted spec, repository state, change boundary, tests, tool authority, rollback | unresolved alternative architectures unless explicitly reopened |
| C5 Integration | frozen component specs, Spine contracts, interface maps, conflict register | all original conversations and donor sources by default |

## 7. Dimension-specific minimums

| Dimension | Minimum additional content |
|---|---|
| D1 Intent & Collaboration | Goal Completeness procedure, OMR O1 contract, user operating profile sources |
| D2 Governance & Control | AB Runtime Authority, OMR selector/ownership/invalidation, Evidence Capture prohibitions |
| D3 Operational Skill Fabric | AB registry/routing, broad-skill consolidation analysis, current AB wrappers |
| D4 Reasoning Intelligence | exact donor skill definitions and baseline/ablation tasks |
| D5 Agent Builder Domain Brain | AB authority and completeness sources, production grammar, quality/failure sources |
| D6 State/Evidence/Continuity | P2 schemas, OMR runtime, Evidence Capture, AB8/AB9 donor behavior |
| D7 Runtime/Transport/Delivery | packet/manifest evidence rules, AB9 packaging, adapters, executor fixtures |
| D8 Evaluation/Evolution | P5 fixtures, Goal Completeness evals, Evidence Capture, prediction-log |

## 8. Immediate classification of supplied artifacts

| Artifact | Current treatment |
|---|---|
| `UAM_Artifact_Naming_and_Archive_Convention.md` | adopted project identity rule |
| `AGENTS.md` | active UAM Architect project instructions in source material; sole active path for `UAM-ARCHITECT-INSTRUCTIONS` |
| `UAM_Artifact_Index.yaml` | active shared identity/index register; exact full-file hash is detached in `SHA256SUMS` |
| `UAM_Model_Framework.md` | active versionless candidate common framework; not adopted; actionable use pins its pinned artifact stamp and loadable immutable content reference |
| `UAM_Model_Participation_and_Assurance_Plan.md` | active versionless candidate donor; naming is normalized, but semantic compatibility and bootstrap ordering still require reconciliation before adoption |

## 9. Intake completion condition

The intake stage is sufficient for buildout planning when:

- every load-bearing artifact is present or explicitly missing;
- active/current-scope authority is distinguishable from candidate and immutable archived history;
- pinned artifact stamps, loadable immutable content refs, and parent/supersession links exist for critical sources;
- the participation-plan conflicts are recorded;
- the Phase-1 Spine contract inputs and bootstrap-pair source packages can be assembled without relying on conversation memory.
