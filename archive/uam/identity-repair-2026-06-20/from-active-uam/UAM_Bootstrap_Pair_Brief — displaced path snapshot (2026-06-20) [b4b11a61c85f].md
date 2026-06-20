# UAM Source Intake and Context Map

**Artifact ID:** `UAM-SOURCE-CONTEXT-MAP`  
**Status:** candidate intake aid  
**Parent:** `UAM-ARCHITECT-INSTRUCTIONS`  
**Last updated:** 2026-06-20  
**Active filename:** `UAM_Source_Intake_and_Context_Map.md`  
**Archive lineage:** `archive/UAM_Source_Intake_and_Context_Map/UAM_Source_Intake_and_Context_Map__legacy-v0.1__superseded-20260620T001210Z__sha256-a126f509e875.md`  
**Naming authority:** `UAM_Artifact_Naming_and_Archive_Convention.md`  

## 1. Intake and naming rule

Provide source **content**, not filenames alone. A source may be supplied as an exact file, a raw archive, or a reference guaranteed loadable in the assigned context. Do not rewrite or clean the archive before intake.

For project-controlled artifacts, the active canonical filename, title, and artifact ID contain no version token. Exact identity is the stable ID/path plus snapshot hash. When a living artifact is replaced, the outgoing snapshot is archived immutably and assigned its archive label retrospectively. Existing donor and legacy filenames are preserved as received during intake so provenance is not destroyed; the Source Authority Register maps them to stable project identities.

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
artifact_id: <stable id or unknown>
filename: <exact filename>
active_filename: <versionless canonical filename or null for archive-only source>
snapshot_sha256: <hash>
archive_label: <retrospective label or null while active>
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
| C3 Evaluation | frozen candidate, rubric, fixtures, exact stable refs, snapshot hashes, and archive refs, evidence ceiling | mutation authority, repair instructions |
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
| `UAM_Model_Framework.md` | active versionless candidate common framework; not adopted; exact snapshot pinned by hash |
| `UAM_Model_Participation_and_Assurance_Plan.md` | active versionless candidate donor; naming is normalized, but semantic compatibility and bootstrap ordering still require reconciliation before adoption |

## 9. Intake completion condition

The intake stage is sufficient for buildout planning when:

- every load-bearing artifact is present or explicitly missing;
- active/current-scope authority is distinguishable from candidate and immutable archived history;
- hashes and parent/supersession links exist for critical sources;
- the participation-plan conflicts are recorded;
- the Phase-1 Spine contract inputs and bootstrap-pair source packages can be assembled without relying on conversation memory.
