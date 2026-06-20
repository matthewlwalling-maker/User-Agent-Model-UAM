# UAM Model Participation and Assurance Plan

**Artifact ID:** `UAM-MODEL-PARTICIPATION`  
**Parent framework:** `UAM-FRAMEWORK`  
**Framework compatibility:** unresolved; this candidate derives from a pre-convention parent and requires semantic and sequencing reconciliation before adoption  
**Canonical filename:** `UAM_Model_Participation_and_Assurance_Plan.md`  
**Artifact index:** `UAM_Artifact_Index.yaml`  
**Naming authority:** `UAM_Artifact_Naming_and_Archive_Convention.md`  
**Related candidate:** `UAM-DEPLOY-READINESS`  
**Status:** candidate participation and assurance architecture; not active runtime authority  
**Evidence ceiling:** design-time architectural synthesis  
**Initial primary provider set:** OpenAI and Anthropic  
**Optional specialist pool:** Google and xAI, activated only by explicit need or test condition  
**Canonical runtime bootstrap:** Codex / OpenAI environment  
**Canonical authority:** deterministic UAM control and state infrastructure under user/Gatekeeper authority  
**Promotion authority:** user/principal through the UAM Gatekeeper

<!-- UAM:ARTIFACT-STAMP-BEGIN -->
**Artifact stamp**

```yaml
artifact_revision: 2
revision_date: 2026-06-20
content_sha256: 6d579196285b1be3beb1258fe2e8d3dd820aac39d8d9ccaadf305b6b11a8bb7d
hash_profile: UAM-CANONICAL-TEXT-SHA256-1
```
<!-- UAM:ARTIFACT-STAMP-END -->

**Active-artifact rule:** use the bare plan name in explanatory prose. Runs, assignments, contracts, adoptions, handoffs, and evidence MUST pin the stamp and loadable immutable content reference.

---

## 1. Purpose

This document defines how core LLMs, provider APIs, coding runtimes, and evaluators may participate in designing, building, testing, and operating the UAM Framework.

It replaces the earlier assumption that every material UAM component should be developed through a standing cross-provider committee of primary architect, counter-architect, reconciler, evaluator, and multiple native adapter owners.

The revised objective is narrower and more deployable:

1. preserve one coherent and reconstructable UAM;
2. keep ordinary runtime execution on one canonical path;
3. use independent models where they add demonstrable design or assurance value;
4. keep governance, canonical state, evidence, and promotion outside model authority;
5. avoid cross-provider consensus as an execution prerequisite;
6. allow additional providers without placing them permanently in the critical path;
7. expand participation only when evidence shows that the added model improves the relevant component.

The UAM retains all eight dimensions and its provider-neutral architecture. This revision narrows **who participates, when, and with what authority**. It does not narrow the UAM's conceptual scope.

---

## 2. Normative Language and Scope

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` are normative within this candidate artifact.

This document inherits the UAM Model Framework document-identity contract: **bare stable name for explanation; pinned artifact stamp and loadable immutable content reference for action**.

This document governs:

- model participation roles;
- initial provider topology;
- component-revision stewardship;
- provider-neutral packet boundaries;
- API adapter sequencing;
- independent assurance and escalation;
- disagreement handling;
- exact model/runtime identity records;
- participation tests and promotion conditions.

This document does not:

- assign permanent ownership of any UAM dimension to a vendor;
- make an LLM authoritative for D2 Governance and Control or D6 State, Evidence, and Continuity;
- authorize API calls, installation, deployment, profile mutation, or repository mutation;
- select exact model IDs before a run freeze;
- replace the UAM Model Framework;
- modify AB1-AB9 or OMR O1-O4 authority;
- promote evidence beyond design-time.

---

## 3. Archived-Lineage Decision Summary

| Topic | v0.1 posture | v0.2 posture |
|---|---|---|
| Runtime topology | Broad multi-seat, cross-provider participation | One canonical runtime for ordinary execution |
| Default provider set | Claude, Gemini, and ChatGPT as standing participants | ChatGPT/Codex primary; Claude default counterpart; Gemini/Grok optional |
| D2 and D6 ownership | Model-led dimensional allocation | Deterministic UAM infrastructure is authoritative |
| Reconciliation | LLM reconciler compares and proposes a unified result | Deterministic validation and selection; no forced consensus |
| Disagreement | Material branches routed through reconciliation | Preserve incumbent or branch; escalate only decision-material conflicts |
| API adapters | Native adapters for all providers before broad testing | OpenAI canonical adapter first; narrow Anthropic assurance adapter second; others deferred |
| Provider failover | Early deployment requirement | Later resilience experiment, not an initial production gate |
| Runtime latency | Multiple providers may participate in a workflow | Cross-provider work is normally off the critical runtime path |
| Model ownership | Multi-seat component ownership | Bounded, revision-scoped participation and stewardship |
| Promotion | User/Gatekeeper | Unchanged: user/Gatekeeper only |

The retained strengths from v0.1 are:

- precise model, host, API, and runtime identity;
- provider-neutral semantic contracts;
- exact packets, stable state references, content hashes, and archive refs;
- preservation of independent branches;
- separation of authoring, evaluation, and promotion;
- evidence ceilings and reversible adoption;
- provider-specific adapter conformance rather than assumed compatibility.

---

## 4. Architectural Commitment

> **Models participate in UAM work; they do not own UAM truth. Canonical governance and state are deterministic, ordinary execution uses one runtime path, and additional models enter only through bounded design or assurance roles.**

### 4.1 One canonical execution path

During the current UAM buildout, ordinary user-facing execution MUST use one canonical runtime path unless a specific, tested decomposition authorizes otherwise.

The bootstrap runtime is:

```text
ChatGPT / GPT / Codex / OpenAI API
```

This is a practical starting point based on project implementation continuity. It is not permanent vendor ownership.

### 4.2 Deterministic authority for control and state

D2 and D6 MUST be controlled by application-owned mechanisms, including schemas, validators, exact references, transition rules, evidence records, freshness checks, branch rules, and rollback records.

A model MAY propose a transition or candidate state. A model MUST NOT make an otherwise illegal transition valid.

### 4.3 Cross-provider participation is normally off the critical path

Claude, Gemini, Grok, or any future provider SHOULD participate through frozen, bounded packets for:

- design-time candidate generation;
- independent challenge;
- adversarial evaluation;
- portability testing;
- specialist capability testing;
- release assurance.

They MUST NOT be required for routine runtime completion unless that dependency has been deliberately tested, adopted, and recorded.

### 4.4 No cross-provider consensus requirement

The UAM MUST NOT require models to debate until they agree.

A valid process may:

- select the incumbent;
- select a challenger;
- import named donor elements and revalidate;
- preserve live branches;
- conclude `No material change needed`;
- or block only when the unresolved difference changes an authorized, load-bearing decision.

### 4.5 Revision-scoped stewardship

A model or provider may serve as the primary architect, implementer, challenger, or evaluator for a named component revision. That role does not create permanent ownership of the dimension or component family.

### 4.6 Smallest sufficient participation

The UAM SHOULD use the fewest providers needed to detect a material error or produce a measurable quality gain.

More models are not automatically more reliable. Participation burden, latency, cost, privacy exposure, and reconciliation risk are architectural costs that require justification.

---

## 5. Initial Topology: 1 + 1 + N

```text
                         USER / GATEKEEPER
                    commitment · promotion · stop
                                │
             ┌──────────────────▼──────────────────┐
             │ Deterministic UAM control/state     │
             │ schemas · validators · evidence     │
             │ branches · freshness · rollback     │
             └──────────────────┬──────────────────┘
                                │
             ┌──────────────────▼──────────────────┐
             │ 1 — Canonical runtime executor      │
             │ ChatGPT / GPT / Codex / OpenAI      │
             └──────────────────┬──────────────────┘
                                │
        ┌───────────────────────┴───────────────────────┐
        │                                               │
┌───────▼────────────────┐                    ┌─────────▼──────────────┐
│ +1 — Default           │                    │ +N — Optional          │
│ counterpart            │                    │ specialist auditors    │
│ Claude / Anthropic     │                    │ Gemini · Grok · future │
└────────────────────────┘                    └────────────────────────┘
```

### 5.1 The `1`: canonical runtime executor

The canonical runtime performs:

- ordinary operation routing;
- user-facing execution;
- authorized artifact production;
- file and tool operations;
- interaction with deterministic UAM state services;
- execution of promoted UAM skills and Domain Brains;
- baseline evaluation and trace capture;
- rollback to the known-good runtime.

The canonical runtime is not the canonical authority. It consumes and proposes state through deterministic contracts.

### 5.2 The `+1`: default design and assurance counterpart

Claude is the initial default counterpart for material work where independent generative or adversarial review is likely to add value.

Typical uses include:

- material UAM architecture revisions;
- D4 reasoning-library design;
- specification and narrative-substance review;
- steelman-premortem analysis;
- independent evaluation of OpenAI-authored components;
- alternative design branches for high-consequence changes.

Claude normally operates asynchronously from the canonical runtime and receives only the narrowest sufficient packet.

### 5.3 The `+N`: optional specialists

Gemini, Grok, local models, or future providers MAY be activated for a specific purpose.

Default specialist hypotheses are:

| Provider family | Candidate specialist use | Activation examples |
|---|---|---|
| Gemini / Google | multimodal review, very-long-context stress testing, high-volume batch evaluation, portability review | multimodal Domain Brain, state reconstruction at scale, Google adapter conformance |
| Grok / xAI | load-bearing dissent, unusual-assumption challenge, fourth-provider audit, xAI adapter conformance, resilience experiment | unresolved OpenAI/Claude disagreement, UAM Spine revision, provider-diversity stress test |
| Future or local model | privacy, offline execution, cost, narrow domain specialization, provider independence | sensitive packet, local-only requirement, validated specialist benchmark |

Specialist participation MUST have a named purpose. A provider is not activated merely because it exists.

---

## 6. Roles and Authority

### 6.1 Role definitions

| Role | Primary function |
|---|---|
| User/principal | Commits material intent and adopts or rejects architecture |
| Gatekeeper | Validates authority, state, evidence, transition, and promotion eligibility |
| Deterministic control/state plane | Owns legal transitions, exact state, evidence, branches, freshness, and rollback |
| Canonical runtime executor | Performs ordinary authorized work through the promoted runtime |
| Primary component architect | Produces a candidate design for one named revision |
| Default counterpart | Independently challenges or derives a material candidate |
| Specialist auditor | Tests a specific capability, assumption, portability concern, or failure mode |
| Adapter implementer | Translates committed semantics into one provider/runtime surface |
| Independent evaluator | Executes frozen tests and records evidence without repairing the candidate in place |

### 6.2 Authority matrix

| Role | May | Must not |
|---|---|---|
| User/Gatekeeper | commit, adopt, branch, reject, reopen, authorize | treat model consensus as sufficient evidence |
| Deterministic plane | validate, reject, commit pre-authorized routine transitions, mark stale, retain branches | invent domain content or silently rewrite decisions |
| Canonical executor | reason, author, evaluate, use tools, propose state changes | bypass schemas, self-promote architecture, overwrite canonical state directly |
| Primary architect | create a bounded candidate design | claim permanent ownership or certify its own superiority |
| Default counterpart | challenge, derive an independent branch, identify omissions | mutate canonical state or force a debate loop |
| Specialist auditor | test the named specialist question | broaden itself into a standing reviewer |
| Adapter implementer | realize committed semantics on a platform | redefine UAM authority, evidence, operation ownership, or stopping |
| Independent evaluator | score, diagnose, preserve limitations and dissent | repair the candidate and then score the repaired version as first-pass evidence |

### 6.3 Separation rules

For material components:

- the author and sole promotion evaluator SHOULD differ;
- load-bearing D2, D6, and Spine changes MUST receive independent challenge;
- the model that authored a candidate MAY run self-tests but MUST NOT be its only source of promotion evidence;
- exact role, provider, host, model, context condition, and packet hash MUST be recorded.

---

## 7. Initial Provider Participation Allocation

These are bootstrap defaults, not comparative verdicts or permanent assignments.

### 7.1 OpenAI / ChatGPT / GPT / Codex

**Initial posture:** canonical runtime and primary implementation environment.

Default responsibilities:

- routine operation execution;
- D3 routing and skill integration;
- Agent Builder Domain Brain implementation;
- file, package, and repository work through Codex where authorized;
- initial OpenAI runtime adapter;
- deterministic-validator and state-service integration;
- trace, fixture, and evaluation-harness implementation;
- integration of promoted designs from other model participants.

Restrictions:

- OpenAI model output is candidate reasoning, not canonical state by itself;
- the canonical executor MUST NOT self-promote a material architecture;
- provider-side conversation state, compaction, cache, or memory MUST remain non-authoritative.

### 7.2 Anthropic / Claude

**Initial posture:** default non-critical-path design and assurance counterpart.

Default responsibilities:

- generative architecture challenge;
- reasoning-lens and recipe design;
- narrative and specification quality review;
- premortem, steelman, and adversarial analysis;
- independent evaluation of material OpenAI-authored components;
- primary design candidate for selected D4 revisions when explicitly assigned.

Restrictions:

- Claude is not required for routine runtime completion;
- Claude does not own canonical state;
- its outputs remain candidates until deterministic validation and Gatekeeper promotion;
- the initial Anthropic adapter MAY be assurance-only rather than a full production runtime adapter.

### 7.3 Google / Gemini

**Initial posture:** optional specialist auditor.

Candidate responsibilities when activated:

- multimodal input and output evaluation;
- long-context state-reconstruction stress testing;
- high-volume or batch evaluation;
- provider-neutral portability review;
- Google-native adapter conformance when such an adapter becomes necessary.

Restrictions:

- Gemini is not a standing participant in every component build;
- no Google production adapter is required for the initial UAM pilot;
- activation must name the specialist question and stop condition.

### 7.4 xAI / Grok

**Initial posture:** optional load-bearing challenger and diversity auditor.

Candidate responsibilities when activated:

- independently testing assumptions shared by OpenAI and Anthropic;
- fourth-provider review of a UAM Spine, D2, D6, or release decision;
- adversarial branch generation;
- xAI adapter conformance;
- controlled resilience or provider-failover experiments.

Restrictions:

- Grok is not a permanent dimension owner;
- Grok is not required for ordinary runtime or every material review;
- beta or preview surfaces remain exploratory until separately validated.

### 7.5 Exact model identity

Provider-family names are insufficient for evidence.

Every executed role MUST record:

```yaml
model_owner: <provider>
inference_host: <direct provider or named cloud host>
model_id_requested: <exact id>
model_id_served: <returned id when available>
release_channel: stable | snapshot | preview | beta | experimental
surface: chat | direct-api | agent-sdk | coding-runtime | managed-agent
api_or_sdk_version: <exact version or date>
reasoning_configuration: <exact settings>
tools_enabled: []
storage_and_tracing_configuration: <record>
context_condition: parent-thread | packet-boundary | separate-context
source_packet_ref:
  stable_id: <packet-id>
  stamp_or_packet_hash: <exact-content-identity>
  content_ref: <loadable-ref>
run_date: <timestamp>
evidence_stage: design-time | simulated | live-runtime | post-implementation | production-observed
```

A model served through a different inference host is a distinct runtime candidate unless conformance has been established.

---

## 8. Participation Tiers

The tier is selected by consequence, coupling, omission risk, and need for independent assurance—not by prestige or task length.

| Tier | Name | Required participation | Typical use | Runtime effect |
|---|---|---|---|---|
| MP0 | Routine execution | Canonical runtime only | ordinary authoring, bounded analysis, routine handoff | no external provider call |
| MP1 | Test-backed single-runtime change | Canonical runtime + deterministic/local tests | local skill fix, adapter patch, bounded artifact change | no external provider call unless test fails materially |
| MP2 | Material dual-provider design | Canonical runtime + Claude in separate or packet-bounded context | material architecture, reasoning recipe, Domain Brain revision | asynchronous design/evaluation; not required for each live task |
| MP3 | Load-bearing assurance | Canonical runtime + Claude + deterministic validation; optional one specialist | UAM Spine, D2, D6, promotion schema, irreversible runtime boundary | Gatekeeper only if a decision-material conflict remains |
| MP4 | Specialist audit | MP1-MP3 plus a named Gemini, Grok, local, or future-model role | multimodal, long-context, portability, diversity, resilience | bounded to the specialist question |
| MP5 | Controlled provider bakeoff | Frozen multi-provider evaluation campaign | determining whether another provider earns a role or adapter investment | design/evaluation environment only |

### 8.1 Tier defaults

- MP0 is the default for ordinary runtime work.
- MP1 is the default for implementation refinements that can be validated locally.
- MP2 is the default for material architecture and D4 reasoning changes.
- MP3 is required for load-bearing control, state, evidence, promotion, or irreversible integration changes.
- MP4 and MP5 require an explicit activation rationale.

### 8.2 Fallback behavior

- Failure or unavailability of Claude MUST NOT block MP0 or MP1 work.
- Failure of an optional specialist MUST NOT corrupt or alter canonical state.
- For MP2, an unavailable counterpart normally defers promotion rather than blocking unrelated runtime work.
- For MP3, the incumbent valid contract remains active unless the Gatekeeper authorizes a different disposition.

---

## 9. Revised UAM Dimensional Mapping

No provider owns a whole dimension. The table defines the initial authority and participation posture.

| Dimension | Canonical authority | Initial build/integration lead | Default independent assurance | Optional specialist role |
|---|---|---|---|---|
| D1 Intent and Collaboration | User/Gatekeeper intent contract and deterministic commitment records | OpenAI runtime integration | Claude tests over-interpretation, burden, and collaboration quality | Gemini portability across long or multimodal context |
| D2 Governance and Control | Deterministic selector, authority matrix, schemas, validators, rejection rules | OpenAI/Codex implements initial services | Claude attacks loopholes and hidden authority expansion | Grok diversity review; Gemini large-case consistency testing |
| D3 Operational Skill Fabric | UAM operation registry and routing contracts | OpenAI/Codex implements canonical skill surface | Claude challenges skill topology, invocation ergonomics, and generative depth | Gemini portability review when another runtime is targeted |
| D4 Reasoning Intelligence | UAM lens and recipe contracts plus D8 evidence | Claude may lead selected design candidates; OpenAI integrates and ablates | Reciprocal OpenAI/Claude review depending on author | Gemini alternative generation; Grok non-consensus branch |
| D5 Domain Brains | Domain-specific source authority and UAM Spine | Per domain; Agent Builder begins in OpenAI/Codex | Claude challenges generative and specification completeness | Specialist chosen by domain need |
| D6 State, Evidence, and Continuity | Deterministic state store, evidence ledger, exact refs, freshness, branch rules | OpenAI/Codex implements initial services | Claude tests semantic loss and ownership loopholes | Gemini long-context reconstruction; Grok independent state challenge |
| D7 Runtime, Transport, and Delivery | Provider-neutral runtime contract and environment authority | OpenAI/Codex canonical adapter first | Claude reviews semantic translation for Anthropic assurance lane | Google/xAI adapters only when activated |
| D8 Evaluation and Evolution | Frozen eval package, evidence protocol, Gatekeeper promotion | OpenAI/Codex builds harness and trace capture | Claude provides independent qualitative/adversarial evaluation | Gemini batch/multimodal; Grok load-bearing fourth-provider audit |

### 9.1 D4 reciprocal authorship rule

Claude may be the primary design author for a D4 component revision. In that case:

- OpenAI/Codex becomes the integration and executability reviewer;
- Claude does not evaluate its own superiority;
- the canonical UAM component is the promoted provider-neutral artifact, not Claude's native prompt form.

### 9.2 D5 domain-specific allocation

A future Domain Brain MUST receive its own assignment. The Agent Builder allocation does not automatically determine ownership for research, planning, product design, or other domains.

---

## 10. D2 and D6 Deterministic Authority Contract

### 10.1 Required deterministic components

The initial UAM control and state plane MUST include, at minimum:

1. canonical state storage;
2. stable schema IDs with frozen content hashes;
3. exact object and artifact references;
4. content hashes;
5. transition eligibility validation;
6. role and field-write authority;
7. evidence-stage enforcement;
8. branch and conflict preservation;
9. freshness and invalidation;
10. append/supersede evidence behavior;
11. rollback and supersession records;
12. immutable audit records for rejected transitions.

### 10.2 Model proposal boundary

A model may return:

- a proposed state object;
- a proposed transition;
- a candidate evidence record;
- a candidate architecture;
- a candidate artifact revision;
- a recommendation to block, branch, or stop.

The deterministic plane decides whether that proposal is structurally eligible. The Gatekeeper decides material architectural promotion when required.

### 10.3 Pre-authorized routine transitions

The deterministic plane MAY commit a routine transition without repeated user approval only when:

- the user or governing contract already authorized the operation class;
- every schema and authority condition passes;
- no material branch conflict exists;
- no evidence promotion is attempted;
- no irreversible or destructive boundary is crossed;
- rollback or supersession is defined.

### 10.4 Provider session state

Provider-native conversation history, cache, memory, compaction, stored response, or session continuation MUST be treated as:

```text
non-authoritative runtime convenience
```

Canonical UAM state MUST remain reconstructable without provider session history.

### 10.5 Cross-provider continuity

Cross-provider work does not require identical hidden context retention. It requires identical declared inputs and auditable projections.

Every model participant receives a provider-neutral packet that contains exact current state and artifact references. Any omitted content is explicit and MUST NOT be inferred as authoritative.

---

## 11. Provider-Neutral Model Participation Packet

Every nontrivial model role MUST receive a frozen packet.

Minimum packet fields:

```yaml
packet_id: UAM-MPP-<component>-<candidate>-<role>-<run>
packet_schema_ref:
  stable_artifact_id: UAM-MODEL-PARTICIPATION-PACKET
  pinned_stamp:
    artifact_revision: <monotonic-integer>
    revision_date: <ISO-8601-date>
    content_sha256: <authoritative-content-sha256>
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: <attached-or-guaranteed-loadable-immutable-ref>
parent_framework_ref:
  artifact_id: UAM-FRAMEWORK
  canonical_filename: UAM_Model_Framework.md
  pinned_stamp:
    artifact_revision: <exact-adopted-integer>
    revision_date: <exact-adopted-ISO-date>
    content_sha256: <exact-adopted-content-sha256>
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: <attached-or-guaranteed-loadable-immutable-ref>
  adoption_ref: <record-ref>
component_id: <stable-component-id>
component_candidate_stamp: <pinned-stamp-or-candidate-content-hash>
participation_tier: MP0 | MP1 | MP2 | MP3 | MP4 | MP5
assigned_role: canonical-executor | primary-architect | counterpart | specialist-auditor | adapter-implementer | evaluator
committed_outcome: <statement>
required_obligations: []
material_constraints: []
authorized_decisions: []
prohibited_decisions: []
state_refs: []
artifact_refs: []
evidence_projection:
  ledger_ref: <ref>
  included_entry_ids: []
  omitted_entry_count: <integer>
  evidence_ceiling: <stage>
branch_and_conflict_state: []
permitted_reads: []
forbidden_reads: []
required_outputs: []
output_schema_ref: <ref>
stop_conditions: []
context_condition: packet-boundary | separate-context | parent-thread
storage_and_data_policy: <policy ref>
model_identity_requirements: <record ref>
packet_hash: <sha256>
```

### 11.1 Output minimum

A participant output MUST include or be wrapped with:

- stable candidate ID and complete candidate stamp;
- source packet ID and hash;
- assigned role;
- decisions made within authority;
- assumptions and branches;
- evidence ceiling;
- unresolved conflicts;
- artifact or state proposal references;
- validation owed;
- terminal disposition.

### 11.2 Packet limitations

A packet is a transport projection, not canonical state. Receiving a packet does not authorize the model to revise its parent state.

---

## 12. Selection, Disagreement, and Escalation

### 12.1 No reconciler seat by default

The standing LLM reconciler from v0.1 is retired.

A deterministic selection procedure and bounded Gatekeeper escalation replace open-ended reconciliation.

### 12.2 Selection procedure

```text
1. Validate candidate identity, packet, schema, authority, freshness, and evidence.
2. Reject every candidate that fails a deterministic condition.
3. Establish the current valid incumbent or baseline.
4. Score remaining candidates against the frozen, dimension-specific rubric.
5. Select a challenger only when it clears the predeclared material-improvement threshold.
6. If results are close or evidence is insufficient, preserve the incumbent.
7. Import donor elements only by name and revalidate the resulting candidate.
8. Preserve material dissent and branch identity.
9. If the decision is invariant across live branches, proceed without forcing agreement.
10. Escalate only when the unresolved difference changes authority, canonical state, evidence semantics, irreversible behavior, or another declared load-bearing decision.
```

### 12.3 Valid disagreement outcomes

| Condition | Outcome |
|---|---|
| Challenger fails deterministic validity | Reject challenger |
| Challenger is valid but not materially better | Retain incumbent; `No material change needed` |
| Challenger materially improves the component | Select challenger or import named donor elements |
| Candidates differ but imply the same authorized decision | Preserve dissent and proceed |
| Difference is material but reversible | Preserve separate branches and continue branch-specific work |
| Difference changes authority, state, evidence, or irreversible action | Block promotion and present a Gatekeeper decision card |
| Evaluator or specialist is unavailable | Preserve incumbent; do not corrupt or stall unrelated runtime work |

### 12.4 Gatekeeper decision card

A decision card MUST be concise and include:

- exact decision to be made;
- incumbent and challenger references;
- deterministic validity result;
- decision-material differences only;
- evidence and limitations;
- reversible default;
- consequences of each choice;
- recommendation and confidence;
- stop or revisit trigger.

Raw multi-model transcripts SHOULD NOT be the primary user decision interface.

### 12.5 Anti-deadlock rule

The system MUST NOT initiate repeated provider-to-provider debate merely because disagreement exists.

The default fallback is the current valid incumbent, a preserved branch, or a blocked material decision—not an unbounded consensus loop.

---

## 13. API and Runtime Adapter Strategy

### 13.1 Adapter order

The initial adapter sequence is:

1. **OpenAI canonical runtime adapter** — required for the first pilot.
2. **Anthropic assurance adapter** — required only for frozen design/evaluation packets used in MP2-MP3.
3. **Google specialist adapter** — deferred until a Gemini-specific test is authorized.
4. **xAI specialist adapter** — deferred until a Grok-specific test is authorized.
5. **Full alternate-runtime and failover adapters** — later resilience phase after the canonical slice is stable.

### 13.2 Assurance adapter versus production adapter

An assurance adapter may support only:

- bounded prompt and packet translation;
- structured candidate output;
- model identity capture;
- raw response retention;
- data/storage policy enforcement;
- retry and timeout handling.

It need not initially support:

- canonical state mutation;
- file or shell execution;
- full UAM skill runtime;
- provider-side orchestration;
- production handoff routing;
- automatic runtime failover.

### 13.3 Native API evidence

Promoted claims about a provider adapter SHOULD come from the provider's native API or SDK. Compatibility wrappers MAY be used for exploratory work but MUST NOT establish semantic equivalence by themselves.

### 13.4 Adapter invariants

Every adapter MUST preserve:

- operation identity;
- authorized decision scope;
- state and packet distinctions;
- exact state/artifact/evidence references;
- evidence ceiling;
- branch identity;
- required output structure;
- stopping and rejection behavior;
- tool and file authority;
- storage, tracing, and privacy configuration.

### 13.5 Provider feature facts

Model names, API behavior, limits, tool support, retention, pricing, and release status are mutable dependencies. They MUST be recorded in a dated Model Capability Registry from official documentation or observed runs at execution time.

This planning artifact intentionally avoids hard-coding current model aliases or feature claims.

---

## 14. Model Capability Registry

Create a registry only for models or runtimes that are authorized for a planned role.

Minimum record:

```yaml
registry_schema_ref: UAM-MODEL-CAPABILITY-REGISTRY
registry_schema_pinned_stamp:
  artifact_revision: <monotonic-integer>
  revision_date: <ISO-8601-date>
  content_sha256: <authoritative-content-sha256>
  hash_profile: UAM-CANONICAL-TEXT-SHA256-1
registry_schema_content_ref: <attached-or-guaranteed-loadable-immutable-ref>
record_id: MCR-<provider>-<model>-<host>-<date>
model_owner: <provider>
inference_host: <host>
model_display_name: <name>
model_id_requested: <exact id>
model_id_served: <exact id or unknown>
release_channel: stable | snapshot | preview | beta | experimental
surface: chat | direct-api | agent-sdk | coding-runtime | managed-agent
api_or_sdk_version: <version/date>
authorized_uam_roles: []
prohibited_uam_roles: []
input_modalities: []
output_modalities: []
structured_output_status: supported | conditional | unsupported | unverified
tool_calling_status: supported | conditional | unsupported | unverified
state_and_storage_mechanisms: []
tracing_and_observability: []
data_retention_and_residency: []
security_and_approval_controls: []
context_and_output_limits: <dated facts or unknown>
cost_basis: <dated reference or unknown>
latency_profile: <observed or unknown>
tested_uam_components: []
known_limitations: []
source_refs: []
source_checked_at: <timestamp>
retest_triggers: []
```

Model reputation or conversational impression may be recorded as a hypothesis, not as a verified capability.

---

## 15. Model Participation Record

Each material component revision receives a participation record rather than a permanent ownership record.

```yaml
participation_record_id: UAM-MPR-<component>-<record-id>
component_id: <stable-component-id>
component_candidate_stamp: <pinned-stamp-or-candidate-content-hash>
parent_framework_ref:
  artifact_id: UAM-FRAMEWORK
  canonical_filename: UAM_Model_Framework.md
  pinned_stamp:
    artifact_revision: <exact-adopted-integer>
    revision_date: <exact-adopted-ISO-date>
    content_sha256: <exact-adopted-content-sha256>
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: <attached-or-guaranteed-loadable-immutable-ref>
  adoption_ref: <record-ref>
status: proposed | active | contested | superseded | retired
participation_tier: MP0 | MP1 | MP2 | MP3 | MP4 | MP5
canonical_authority:
  control_contract_ref: <ref>
  state_contract_ref: <ref>
  promotion_authority: user-gatekeeper
canonical_runtime:
  provider: OpenAI
  model_record_ref: <MCR ref>
  adapter_ref: <adapter ref>
primary_architect:
  provider: <provider>
  model_record_ref: <ref>
  packet_ref: <ref/hash>
default_counterpart:
  provider: Anthropic | none
  model_record_ref: <ref or none>
  packet_ref: <ref/hash or none>
specialist_participants: []
independent_evaluator:
  provider_or_role: <identity>
  packet_ref: <ref/hash>
owned_decisions: []
prohibited_decisions: []
candidate_refs: []
branch_and_conflict_refs: []
deterministic_validation_ref: <ref>
eval_package_ref: <ref>
evidence_ceiling: <stage>
disagreement_disposition: none | incumbent-retained | challenger-selected | donor-import | branch-preserved | gatekeeper-block
verdict: pending | adopt | revise | branch | reject | no-material-change
adopted_artifact_ref: <ref or null>
rollback_ref: <ref or null>
review_date: <date>
revisit_triggers: []
```

There is no mandatory `reconciler` field.

---

## 16. Controlled Component Build and Assurance Procedure

### Phase 0 — Freeze the assignment

Freeze:

- parent UAM Framework stable identity, pinned adopted artifact stamp, adoption record, and loadable immutable content reference;
- stable component identity and candidate stamp;
- participation tier;
- committed goal and required subdimensions;
- owned and prohibited decisions;
- exact state, artifact, and evidence inputs;
- output contract;
- evaluation rubric and material-improvement threshold;
- context condition;
- data policy;
- model and adapter records;
- stop and fallback conditions.

### Phase 1 — Produce the primary candidate

The assigned primary architect creates one candidate from the frozen packet.

For MP0-MP1, the canonical runtime is normally the only model participant.

For MP2-MP3, the primary architect may be OpenAI or Claude depending on the component revision.

### Phase 2 — Generate independent challenge only when required

For MP2-MP3, the default counterpart receives its own frozen packet in a separate or auditable packet-bounded context.

Gemini or Grok is not added unless an MP4 specialist purpose is recorded.

### Phase 3 — Deterministic validation

Reject any candidate that fails:

- schema validity;
- authority;
- state freshness;
- exact parent references;
- branch preservation;
- evidence ceiling;
- required output completeness;
- prohibited-decision constraints;
- stop and terminal requirements.

Generative quality cannot override deterministic failure.

### Phase 4 — Independent evaluation

Evaluate valid candidates against the frozen rubric. Use anonymization where practical and preserve raw first-pass outputs.

The evaluation MUST distinguish:

- behavioral or architectural quality;
- state and packet completeness;
- authority correctness;
- evidence sufficiency;
- implementation executability;
- complexity and burden;
- provider limitations;
- evaluator confidence.

### Phase 5 — Deterministic selection or Gatekeeper escalation

Apply the selection procedure in Section 12.

Do not merge candidates by default. Named donor imports create a new candidate revision that must be revalidated.

### Phase 6 — Canonical implementation

The canonical runtime implements the promoted provider-neutral design unless another implementation runtime was explicitly authorized.

### Phase 7 — Post-implementation validation

Run local, contract, system-ring, and regression tests. Preserve first-pass failures and repairs separately. Promote only the exact tested revision.

---

## 17. Testing Requirements for the Participation Architecture

### 17.1 Critical deterministic tests

These MUST pass at 100% for the tested scope:

- illegal transition rejected;
- unauthorized field/object write rejected;
- stale parent rejected;
- evidence overclaim rejected;
- silent branch union rejected;
- provider output cannot directly overwrite canonical state;
- provider session state cannot substitute for required UAM state;
- packet/state/artifact/evidence distinctions remain intact;
- model or adapter substitution is recorded;
- rollback metadata is complete.

### 17.2 Single-runtime baseline tests

The canonical runtime MUST demonstrate that:

- MP0 and MP1 work completes without Claude, Gemini, or Grok;
- ordinary routing and artifact work does not stall on external-provider availability;
- canonical state remains reconstructable without provider chat history;
- the known-good runtime can be restored.

### 17.3 Selective-participation ablations

For representative material tasks compare:

1. canonical runtime alone;
2. canonical runtime plus targeted Claude counterpart;
3. canonical runtime plus an optional specialist when justified;
4. all available models, only as an experimental burden/control condition.

The targeted counterpart or specialist earns continued use only when it produces repeatable material uplift or detects failures the baseline misses at acceptable cost, latency, and privacy burden.

### 17.4 Deadlock and fallback tests

Test:

- OpenAI and Claude disagree but the runtime decision is invariant;
- OpenAI and Claude disagree on a D2/D6 load-bearing rule;
- Claude is unavailable;
- an optional specialist is unavailable;
- a challenger is valid but only marginally different;
- a challenger is superior on one criterion but violates authority;
- a donor import creates a new unvalidated candidate;
- the Gatekeeper declines to choose between reversible branches.

The system passes only when it preserves the incumbent, branch, or block state without entering an unbounded debate loop.

### 17.5 Packet and continuity tests

Each participating provider must be able to:

- consume the exact declared packet;
- return the packet hash and assigned role;
- avoid inferring omitted authoritative content;
- preserve branch and evidence limitations;
- produce a result that another consumer can audit without conversation reconstruction.

### 17.6 API conformance tests

For each enabled adapter test:

- model identity and alias resolution;
- structured-output behavior;
- tool and approval semantics;
- storage, retention, and tracing settings;
- retries, timeouts, and rate limits;
- malformed packet handling;
- contaminated context labels;
- provider outage behavior;
- model retirement or substitution;
- cost and latency capture;
- data-boundary enforcement.

### 17.7 Promotion conditions

A model role or adapter may be promoted only when:

- deterministic critical tests pass;
- no canonical-state corruption, unauthorized mutation, evidence laundering, or silent branch merge occurred;
- its exact identity and configuration are recorded;
- its contribution is distinguishable from the baseline;
- limitations and fallback behavior are explicit;
- the Gatekeeper adopts the exact tested revision.

No universal numerical claim about multi-agent reliability may be used without scoped evidence from the actual UAM test package.

---

## 18. Data, Privacy, Cost, and Latency Controls

### 18.1 Data minimization

External model participants receive the narrowest sufficient packet.

The default is:

- no unrestricted UAM state export;
- no complete user model unless explicitly required and authorized;
- redact or abstract sensitive examples;
- include exact references rather than unrelated source dumps;
- retain provider-specific data-policy decisions in the run record.

### 18.2 Secrets

API credentials, tokens, and secrets MUST remain in the user's environment or secret manager. They MUST NOT appear in prompts, packets, artifacts, or chat transcripts.

### 18.3 Latency boundary

MP2-MP5 cross-provider work is normally asynchronous design or assurance work. It SHOULD NOT block ordinary runtime requests.

### 18.4 Cost boundary

Every external model campaign MUST have:

- a fixed task count;
- provider-specific spend limits;
- retry ceilings;
- stop conditions;
- captured token, cost, and latency data where available.

### 18.5 Provider-side state and retention

Provider-side storage, tracing, caching, and conversation retention MUST be explicitly configured and recorded. They remain non-authoritative even when enabled.

---

## 19. Bootstrap Sequence

### Bootstrap 0 — Freeze the revised participation contract

Freeze this artifact, the provider/data policy, initial provider pool, and first vertical-slice scope.

### Bootstrap 1 — Build the deterministic D2/D6 minimum

Create:

- authority and transition validator;
- canonical state and artifact registry;
- evidence and branch controls;
- exact packet and reference rules;
- rejection and rollback records.

This minimum is infrastructure, not an LLM-owned design seat.

### Bootstrap 2 — Build the minimal D8 assurance kernel

Create:

- frozen packet generator;
- Model Capability Registry;
- Model Participation Record;
- deterministic candidate validator;
- scorecard and ablation structure;
- raw-run and limitation capture;
- Gatekeeper decision card;
- adoption and rollback record.

### Bootstrap 3 — Build the OpenAI canonical runtime vertical slice

Implement:

- `architect-solution`;
- `evaluate-artifact`;
- initial reasoning lenses;
- Agent Builder Domain Brain minimum;
- canonical OpenAI runtime adapter;
- local and simulated tests.

### Bootstrap 4 — Add the Anthropic assurance lane

Build only the bounded capabilities required for:

- independent material design candidate;
- adversarial challenge;
- structured evaluation response;
- identity, packet, privacy, and raw-run capture.

Do not require a full Claude production runtime at this stage.

### Bootstrap 5 — Run selective-participation tests

Use representative historical and holdout tasks to determine:

- where Claude materially improves results;
- where the single-runtime baseline is sufficient;
- where added participation causes excess burden;
- which activation rules should become default.

### Bootstrap 6 — Activate optional specialists only by trigger

Add Gemini or Grok only for a named MP4/MP5 experiment. Do not build production-grade adapters preemptively.

### Bootstrap 7 — Defer cross-provider runtime failover

Cross-provider failover becomes a later resilience project after:

- the canonical runtime is stable;
- provider-neutral packets and state contracts are proven;
- a specific continuity requirement justifies the added adapter and test burden.

---

## 20. Required First Artifacts

The first implementation package should contain:

1. `UAM_Deterministic_Control_and_State_Contract`
2. `UAM_Provider_Neutral_Model_Participation_Packet`
3. `UAM_Model_Capability_Registry`
4. `UAM_Model_Participation_Record_Schema`
5. `UAM_Selective_Assurance_Eval_Package`
6. `UAM_Gatekeeper_Decision_Card_Schema`
7. `UAM_OpenAI_Canonical_Runtime_Adapter`
8. `UAM_Anthropic_Assurance_Adapter`
9. `UAM_Participation_Adoption_and_Rollback_Record`

Not required for the first pilot:

- production-grade Google adapter;
- production-grade xAI adapter;
- automatic cross-provider failover;
- a standing LLM reconciler;
- full provider parity;
- all-provider participation in every bakeoff.

---

## 21. Key Risks and Controls

| Risk | Control |
|---|---|
| Canonical runtime becomes de facto truth | Separate model output from deterministic state and Gatekeeper promotion |
| External reviewer blocks ordinary work | Keep MP0-MP1 single-runtime and use asynchronous assurance |
| Cross-provider state fragmentation | Use exact provider-neutral packets and application-owned state |
| Reconciliation deadlock | No consensus loop; preserve incumbent, branch, or block |
| One model authors and certifies itself | Independent evaluation for material promotion |
| Provider stereotypes drive allocation | Treat provider roles as hypotheses and run ablations |
| Specialist participation becomes permanent clutter | Require named activation purpose, stop condition, and evidence of value |
| API feature drift | Dated capability registry and retest triggers |
| Compatibility wrapper hides semantic difference | Native adapter evidence for promoted claims |
| Provider session state becomes canonical | Explicit non-authoritative classification and reconstruction tests |
| Privacy exposure multiplies across vendors | Minimized packets, allowlists, redaction, per-provider data policy |
| Cost and latency expand without gain | Fixed campaigns, quotas, single-runtime baseline, selective activation |
| Incumbent survives despite clear improvement | Frozen material-improvement rule and exact challenger evidence |
| Model consensus overrides user intent | User/Gatekeeper retains promotion authority |

---

## 22. Migration from v0.1

### 22.1 Retired requirements

The following v0.1 requirements are retired:

- mandatory multi-seat participation for every material component;
- three-provider independent candidate generation by default;
- standing LLM reconciler role;
- native production adapters for all providers before the first pilot;
- broad cross-provider conformance as a prerequisite for initial deployment;
- mandatory provider failover in the first production gate;
- provisional dimensional allocations that resemble permanent vendor ownership.

### 22.2 Preserved requirements

The following v0.1 requirements remain:

- one named accountable primary architect per material component revision;
- exact model/provider/host/API/runtime identity;
- provider-neutral semantic contracts;
- separate candidate branches;
- no silent union;
- author/evaluator separation for material promotion;
- provider-native adapter validation when an adapter is promoted;
- user/Gatekeeper promotion authority;
- exact evidence, limitation, adoption, and rollback records.

### 22.3 Renamed concepts

| v0.1 term | v0.2 term |
|---|---|
| Multi-model ownership | Model participation and assurance |
| Model Ownership Record | Model Participation Record |
| Counter-architect required for every material component | Default counterpart activated by MP2-MP3 |
| Reconciler | Deterministic selection plus bounded Gatekeeper escalation |
| Multi-provider adapter baseline | Staged adapter strategy |
| Provider failover gate | Later resilience experiment |

---

## 23. Relationship to Other UAM Artifacts

### 23.1 UAM Model Framework

The UAM Model Framework remains the parent architecture. This revision is consistent with its requirements that:

- the UAM Spine preserves authority, state, evidence, provenance, and stopping;
- each dimension can be independently refined;
- D2 governs eligibility and authority;
- D6 owns canonical state and continuity semantics;
- D7 owns platform adapters and runtime realization;
- D8 governs evidence, promotion, monitoring, and rollback.

### 23.2 UAM Deployment Readiness and Test Plan

This artifact supersedes the provider-participation assumptions in the deployment plan where that plan requires:

- native Anthropic, Google, and xAI adapters before the first live pilot;
- all-provider participation in ordinary bakeoffs;
- provider failover as an initial production-readiness condition;
- a standing multi-model reconciliation record.

The deployment plan remains useful for vertical-slice, shadow, canary, evidence, and rollback structure, but it MUST be revised before being treated as fully coherent with this active participation plan.

### 23.3 AB and OMR

This artifact does not change AB1-AB9 or OMR O1-O4.

Their existing distinctions remain useful foundations:

- AB supplies lifecycle routing and action boundaries;
- OMR supplies state-sequenced ownership, exact references, branch preservation, and deterministic selector principles;
- neither becomes a model-voting protocol.

---

## 24. Candidate Commitment

The planning thesis proposed for adoption is:

> **The current UAM buildout will operate through one canonical ChatGPT/GPT/Codex/OpenAI runtime backed by deterministic control and state infrastructure. Claude will serve as the default non-critical-path design and assurance counterpart for material work. Gemini and Grok will be optional specialist auditors activated only by named requirements or evaluation triggers. Cross-provider consensus will never be required for normal runtime completion, and no model will own canonical governance, state, evidence, or promotion.**

This thesis remains design-time until frozen, implemented, and tested.

---

## 25. Terminal Record

**Task class:** architecture-change  
**Terminal state:** active candidate normalized; predecessor snapshots remain preserved as immutable history  
**Do not do next:** do not build all-provider production adapters, require cross-provider consensus, or assign permanent dimensional ownership from this design-time plan  
**Only valid next step:** none required; optional next work is to revise the deployment-readiness plan for consistency and then freeze the first participation test package  
**Recommended context window:** current context for a narrow consistency revision; new contexts for independent MP2-MP5 model runs  
**Next role_class:** architecture-change  
**Next assignee_runtime:** Codex for artifact implementation; user/Gatekeeper for adoption
