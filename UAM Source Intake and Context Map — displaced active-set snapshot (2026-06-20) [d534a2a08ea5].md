# UAM Sub-Architect Brief — Bootstrap Pair

**Artifact ID:** `UAM-BRIEF-BOOTSTRAP`  
**Canonical filename:** `UAM_Bootstrap_Pair_Brief.md`  
**Status:** candidate assignment brief; **not dispatch-ready**  
**Authority:** prepared by the UAM Architect under user/Gatekeeper authority  
**Evidence ceiling:** design-time for this brief; simulated only for a properly frozen and executed validation run  
**Parent framework:** `UAM-FRAMEWORK`  
**Draft basis:** candidate framework snapshot recorded below; an adopted snapshot and adoption record are mandatory at dispatch  
**Legacy source:** immutable pre-convention draft preserved under `archive/UAM_Bootstrap_Pair_Brief/`

<!-- UAM:DOCUMENT-STAMP-BEGIN -->
**Artifact stamp**

```yaml
artifact_revision: 1
updated_at: 2026-06-20T01:06:13Z
payload_sha256: d2cb081e427e2ffb1b7cbccf52326aab508d5456eaf6e9864ddae95a96515e54
hash_scope: full UTF-8 document with this stamp block removed; UTF-8 without BOM; LF line endings
```
<!-- UAM:DOCUMENT-STAMP-END -->

## 0. Disposition and purpose

This brief prepares the first full operation build required by the UAM bootstrap gate: `architect-solution` and `evaluate-artifact`. It is a **prepared assignment family**, not an executable dispatch packet and not authority to begin work.

The bootstrap pair tests a narrow claim:

> Can two real operation specifications be built and exercised from adopted, frozen UAM contracts without reopening a load-bearing framework decision or inventing a cross-dimensional encoding locally?

The output is:

1. two candidate operation specifications;
2. a routing and boundary test deck;
3. a controlled pair exercise on a frozen test target;
4. a validation report that recommends either gate clearance or a precise block.

Gate clearance is only **simulated evidence of bootstrap-contract sufficiency for the tested scope**. It does not adopt the operations, validate production readiness, authorize installation, or promote any claim above the evidence actually captured.

## 1. Draft basis and acting-reference rule

This brief was revised against the following candidate design basis:

```yaml
draft_basis:
  parent_framework:
    stable_artifact_id: UAM-FRAMEWORK
    canonical_filename: UAM_Model_Framework.md
    artifact_revision: 1
    updated_at: 2026-06-20T00:30:20Z
    payload_sha256: 5dc3bd2318333f662af22375ab861e7d5b28ef81d51bd4ce4a6cb9ed8ace83ab
    snapshot_sha256: 3fa0bf77668bcccd1aceddfe0cf90d0f8fcdcb80047fb3a9ad8781c43c73a0e9
    status_at_revision: candidate
  architect_instructions:
    stable_artifact_id: UAM-ARCHITECT-INSTRUCTIONS
    artifact_revision: 1
    payload_sha256: 98e93526d73bd49380d02f48847adc1f2c39560a2a5ab79a25623e26c1039db2
    snapshot_sha256: 5944c8798042f3f2a8d820d79f410cefdf3bcdefd1b9164cc8536712af7fa293
    status_at_revision: candidate
```

These are provenance references, not dispatch authority. The frozen dispatch packet MUST replace them with the exact **adopted** parent stamp, complete-file snapshot hash, adoption record, and loadable content. A bare name, mutable path, numeric legacy label, or locally recomputed hash is insufficient.

## 2. Pre-dispatch eligibility gate

The dispatcher MUST mark every row `PASS` in a frozen dispatch record. Any `FAIL`, `UNKNOWN`, missing hash, or index/header mismatch blocks dispatch.

| Gate | Required condition |
|---|---|
| Framework authority | `UAM-FRAMEWORK` is adopted; exact stamp, complete-file snapshot hash, adoption record, and loadable snapshot are attached. |
| Artifact identity | The framework header, shared artifact index, and detached checksum agree. A mixed or stale active set blocks. |
| Phase 1 — Spine contracts | Frozen, loadable artifacts exist for the error-code vocabulary, state-object metadata convention, source-authority order, and packet/manifest contract. Labels alone do not pass. |
| Phase 2 — operation shells | Thin shells for all six operations are frozen and attached by exact stamp/hash; the two bootstrap shells are the starting contracts, and the other four define neighbor exclusions. |
| Source provisioning | Every load-bearing donor is attached in full or guaranteed loadable in every assigned context, with exact source identity and hash. |
| Test package | A bounded test intent, requirements, frozen rubric, constraints, and target identity are supplied before either operation executes. |
| Role separation | Primary architect, operation executor, independent evaluator, and gate assessor are assigned; required contexts and forbidden reads are frozen. |
| Packet freeze | The acting assignment is serialized through the frozen Spine packet/manifest contract and receives its own immutable packet identity. |
| Freshness | All pins are checked immediately before work starts and again before results are committed. |

### 2.1 Required Phase-1 contract set

The bootstrap pair consumes, but does not define, these cross-boundary contracts:

1. error-code vocabulary and rejection semantics;
2. governed state-object metadata convention;
3. source-authority and conflict-precedence order;
4. packet/manifest format, including acting-reference pins and context restrictions.

If any is absent before dispatch, the assignment is **not eligible to start**. If a novel cross-dimensional encoding need appears during the build, the assignee returns a Spine-contract gap and stops; it does not define the encoding locally.

### 2.2 Required Phase-2 shell set

The packet MUST include frozen thin shells for:

- `architect-solution`;
- `author-artifact`;
- `evaluate-artifact`;
- `compare-options`;
- `diagnose-failure`;
- `handoff-state`.

The bootstrap pair may fully elaborate only `architect-solution` and `evaluate-artifact`. Neighbor shells are read-only boundary contracts.

## 3. Identity, scope, and role topology

### 3.1 Component identity

- **Assignment family:** Bootstrap Operation Pair.
- **Candidate components:** `architect-solution` and `evaluate-artifact`.
- **Component class:** two `skill-family` operation specifications within D3 Operational Skill Fabric.
- **Primary dimension:** D3.
- **Consumed dimensions:** D1 intent, D2 authority, D4 lens interfaces, D5 domain knowledge when the test target requires it, D6 state/evidence references, D7 packet/runtime boundaries, and D8 evaluation criteria.
- **Change boundary:** the two candidate operation specifications and their bootstrap evaluation artifacts only.

### 3.2 Required roles and contexts

| Role | Owns | Context condition | Prohibited behavior |
|---|---|---|---|
| Dispatcher / UAM Architect | eligibility, packet freeze, role assignment, final gate recommendation routing | architecture-control context | author the candidate and then certify it as independent evidence |
| Primary Component Architect | candidate specifications for both operations | fresh build context | write Spine contracts, D4 lens internals, D8 global taxonomy, or canonical state |
| `architect-solution` executor | first-pass execution of the frozen candidate operation on the test intent | fresh execution context | use evaluator findings or post-hoc repairs during first pass |
| Independent Evaluator | execute the frozen `evaluate-artifact` candidate against the frozen design and rubric | genuinely separate context | inspect hidden builder rationale, mutate the artifact, redefine goals, or repair then score as first pass |
| Gate Assessor | inspect frozen run records and issue a bounded clearance/block recommendation | fresh assessment context | promote artifacts or evidence; conceal limitations or failed prerequisites |

Provider choice is not fixed by this brief. Exact runtime, model, host, configuration, tools, and context condition are recorded at dispatch and in evidence. A separate context run by the same authoring model is **context-isolated**, not automatically author-independent; the evidence label must say which independence properties actually hold.

## 4. Committed outcome and success conditions

### 4.1 Outcome

Produce:

- a complete candidate specification for `architect-solution`;
- a complete candidate specification for `evaluate-artifact`;
- a routing and operation-boundary test deck;
- a controlled pair exercise;
- a validation report answering the bootstrap gate.

### 4.2 Success conditions

The assignment succeeds only when all of the following hold:

1. Each operation candidate satisfies the semantic contract in Framework §13 and answers all Framework §21 completion questions.
2. Each candidate declares a stable ID, intended versionless active filename, candidate snapshot hash, parent framework pin, ownership, work-object authority, activation, composition, failure model, validation, and stopping.
3. The pair is exercised on one dispatcher-supplied, frozen, materially representative test intent.
4. The architect run preserves at least two materially different candidates when the problem admits them and records the committed design without mutating production artifacts.
5. The evaluator consumes the committed goal, frozen rubric, and frozen design; it does not redefine the goal or modify the evaluated artifact.
6. Routing, neighbor exclusion, object integrity, authority, evidence ceiling, freshness, vocabulary consistency, and stopping tests pass for the tested scope.
7. The report explicitly records whether any framework decision was reopened, any shared encoding was missing or invented, and whether the kill condition was encountered.
8. Raw first-pass outputs, failures, repairs, model/runtime identity, context isolation, packets, hashes, and limitations are preserved.
9. No claim exceeds `simulated`, and the recommendation states the exact scope that was tested.
10. The assignees stop after producing the required outputs or a valid blocker.

## 5. Requirement trace

### Explicit required

- `architect-solution` candidate operation specification.
- `evaluate-artifact` candidate operation specification.
- routing and operation-boundary test deck.
- frozen pair exercise and evidence package.
- bootstrap validation report with a gate-clearance or blocking recommendation.

### Entailed required

- exact acting-reference pins and freshness checks;
- source-complete, context-loadable packets;
- neighbor exclusions against the other four operation shells;
- D3/D4/D8/D6/Spine ownership separation;
- independent-evaluation context controls and truthful independence labeling;
- first-pass preservation and separate repair records;
- valid no-action and `No material change needed` outcomes;
- rollback/deprecation path for candidate operation artifacts.

### Optional

- additional operation modes shown by repeated evidence to be necessary;
- a second test target when the first target cannot exercise a load-bearing boundary;
- provider-diverse evaluation when separately authorized.

### Speculative and out of scope

- new global operations;
- new Spine-owned schemas or code systems;
- canonical D4 lens definitions or recipe registry;
- canonical D8 scorecard/evidence taxonomy;
- D6 state-store design;
- runtime installation, AB/OMR migration, or production deployment;
- building any of the remaining four operations beyond their frozen shells.

## 6. Ownership and work-object authority

### 6.1 D3-owned decisions

The primary architect may decide, for the two candidate operations only:

- purpose and operation-level required capabilities;
- modes and activation conditions;
- outcome-based routing and neighbor exclusions;
- operation procedure and stopping behavior;
- operation-level input/output and composition hooks;
- local, non-exported implementation vocabulary;
- which already-defined lenses or domain modules the operation may invoke through their frozen interfaces.

### 6.2 Decisions owned elsewhere

- **Spine:** all cross-dimensional encodings, source precedence, packet/manifest form, shared metadata, and error vocabulary.
- **D4:** lens internals, lens contracts, and canonical cross-operation recipe definitions.
- **D8:** global evaluation taxonomy, promotion gates, shared scorecards, and evidence-system policy.
- **D6:** canonical state/evidence semantics, ledger commit, freshness/invalidation implementation, and branch storage.
- **D7:** runtime adapters, physical transport, installation, and delivery mechanics.
- **User/Gatekeeper:** adoption, promotion, material branch resolution, and authority expansion.

The bootstrap candidates may reference or propose requirements to these owners. They may not define those owners' canonical vocabulary.

### 6.3 Permitted and prohibited writes

**Permitted candidate outputs:**

- the two operation specifications in the assignment workspace;
- routing, boundary, and local evaluation fixtures;
- run records, scorecards, and a validation report conforming to frozen shared contracts;
- candidate state/evidence proposals for later commit by the authorized owner.

**Prohibited writes:**

- active canonical operation files;
- the UAM Spine or another dimension's contract;
- canonical state or evidence ledger entries directly;
- production artifacts or runtime installations;
- another operation's full specification;
- an evaluated artifact during a read-only evaluation stage.

Candidate files declare intended active identities but remain branch/workspace artifacts until the Gatekeeper authorizes promotion through the single-writer active-slot transaction.

## 7. Required source package

The draft's prior statement that all sources were present and guaranteed loadable is withdrawn. The dispatcher must prove loadability per context.

| Source group | Minimum required content |
|---|---|
| Adopted framework | Full adopted `UAM-FRAMEWORK` snapshot, stamp, snapshot hash, and adoption record. |
| Phase-1 Spine contracts | Full frozen artifacts for error codes, shared state metadata, source authority, and packet/manifest format. |
| Phase-2 shells | Full frozen shells for all six operations. |
| AB authority donor | `AB_Runtime_Authority_Reference_v1.1.md`, including AB routing, action boundaries, evidence stages, reach, stopping, and AB2/AB4/AB5 distinctions. |
| Goal-completeness donor | `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md`, including requirement classes, capability-before-asset, coverage, E1-E12, and sentinels. |
| D3 consolidation donors | The broad-skill consolidation analysis and current AB1-AB9 wrappers being consolidated. |
| Architect lenses | Exact definitions for `spec-builder`, `gold-standard-comparison`, `steelman-premortem`, and `narrative-substance-review`, or their adopted replacements. |
| Evaluation lenses | Exact definitions for `blind-grader`, `break-it-tester`, and `consistency-review`, or their adopted replacements. |
| Evidence discipline | The applicable OMR Evidence Capture Protocol content, including first-pass preservation, context labels, relabel/repair/pool prohibitions, and reconstruction minimums. |
| Adversarial fixtures | Relevant P5/OMR and AB evaluation fixtures needed for routing, evidence, authority, branch, state, and stopping tests. |
| Test target package | Frozen intent, requirement trace, constraints, target identity, predeclared evaluation rubric, and evidence ceiling. |

Every source record must include its stable or legacy identity, exact snapshot hash, loadable path or attached content, authority scope, and permitted use. A filename alone is not source provisioning.

## 8. Frozen test-target contract

The dispatcher selects the test target before either operation executes. The target must:

- be a bounded but materially representative component-design problem;
- have a committed outcome, requirement classes, constraints, and non-goals;
- admit architectural choice rather than being a trivial formatting task;
- have an evaluation rubric frozen before the architect output is seen;
- not be either bootstrap operation specification, this brief, or one of the four unbuilt canonical operations unless separately authorized;
- remain a fixture/candidate unless independently promoted later;
- carry exact input hashes and an explicit evidence ceiling.

The exercise has two passes:

1. **Architecture pass:** execute the frozen `architect-solution` candidate on the test intent and preserve its raw first-pass design, candidates, selection, branches, and self-check.
2. **Evaluation pass:** in a separate context, first perform a blind outcome/quality assessment from the committed goal, rubric, and frozen design; then perform a contract audit with the permitted trace and packet metadata. The evaluator must distinguish findings from recommendations and must not mutate the design.

## 9. Interfaces and freshness

### Inputs

- adopted parent framework and adoption record;
- frozen Phase-1 contracts;
- frozen Phase-2 operation shells;
- source-complete donor package;
- frozen test target and rubric;
- exact role/context/packet contract.

### Outputs

- two candidate operation specifications;
- routing/boundary test deck;
- frozen run and evidence package;
- bootstrap validation report or precise blocking report.

### Downstream consumers

- UAM Architect and Gatekeeper for the bootstrap gate;
- later operation/component architects after gate clearance;
- D8 evaluation buildout as historical design-time/simulated evidence, not as canonical D8 policy.

### Freshness and invalidation

A change to any pinned parent, Spine contract, operation shell, donor source, rubric, test intent, or candidate operation snapshot invalidates the affected result. The response is flag-and-block pending bounded revalidation; no consumer silently continues on the old pin or silently adopts the new one.

## 10. Required deliverables

1. **`architect-solution` candidate specification**  
   Stable ID and intended canonical filename declared; all Framework §13 fields populated.
2. **`evaluate-artifact` candidate specification**  
   Stable ID and intended canonical filename declared; all Framework §13 fields populated.
3. **Routing and operation-boundary test deck**  
   Includes positive, negative, adversarial, ambiguous, no-action, and stopping cases. It must include “Review and improve this” as an intent-classification case rather than an automatic route.
4. **Bootstrap run package**  
   Serialized through the frozen packet/manifest contract and containing exact inputs, raw outputs, hashes, contexts, runtime/model records, failures, repairs, and limitations.
5. **Bootstrap validation report**  
   States prerequisites, tested scope, results by evaluation ring, vocabulary check, kill-condition result, evidence stage, unresolved limitations, and a bounded recommendation.
6. **Blocking report, when applicable**  
   Names the failed prerequisite or shared-contract gap, the evidence for the block, the owner, and the smallest valid next action. It must not invent a replacement contract.

## 11. Validation requirements

### 11.1 Preflight

- adopted parent pin and adoption record validate;
- every required source loads in its assigned context;
- Phase-1 and Phase-2 contract pins agree with the artifact index;
- packet identity, permitted reads, forbidden reads, and output contract validate;
- test rubric predates architect output;
- evaluator context is isolated as declared.

### 11.2 Local operation tests

Each candidate receives positive, negative, adversarial, ambiguous, and no-action tests.

`architect-solution` must show:

- capability-before-asset reasoning;
- materially distinct candidate generation where the problem admits it;
- explicit requirement trace, branches, selection basis, interfaces, and stopping;
- no production mutation, runtime implementation, or evidence promotion.

`evaluate-artifact` must show:

- assessment against frozen goals and criteria;
- separation of finding, evidence, limitation, and remedy recommendation;
- no goal redefinition, architecture selection without authority, or artifact mutation;
- truthful claim and independence labels;
- `No material change needed` as a valid result.

### 11.3 Spine and vocabulary tests

- shared error, metadata, source-authority, and packet fields are consumed exactly as frozen;
- neither operation defines a competing cross-dimensional encoding;
- state, artifact, evidence, and packet remain distinct;
- authority and evidence ceilings hold;
- any uncertain shared/local classification escalates rather than being localized silently.

### 11.4 Integration and end-to-end tests

- the evaluator consumes the exact committed design artifact and committed goal produced by the architect path;
- branch identity and rejected alternatives remain reconstructable where decision-relevant;
- a downstream consumer can reconstruct the run without originating conversation history;
- evaluator findings do not alter the first-pass design;
- terminal state is explicit and no unauthorized next operation starts.

### 11.5 Baselines and ablations

Compare, where the fixture supports it:

- baseline design behavior without the selected architect lens recipe;
- candidate `architect-solution` behavior with the selected frozen lenses;
- baseline evaluation without the selected evaluator lens;
- candidate `evaluate-artifact` behavior with the selected frozen lens;
- over-composed behavior where too many lenses are activated.

A lens or recipe is not promoted from one run. The result only records whether it added value in the tested case.

### 11.6 Evidence capture

Preserve:

- all acting-reference stamps and complete-file hashes;
- exact packet content and source projections;
- exact runtime/model/tool configuration;
- context condition and isolation evidence;
- raw first-pass outputs;
- candidate branches and rejected selections;
- failures, repairs, and manual interventions as separate records;
- scorecards and assessor rationale;
- limitations and evidence ceiling.

## 12. Bootstrap gate decision

The Gate Assessor may recommend **clearance for the next planned buildout stage** only when:

- every pre-dispatch gate passed;
- both candidate specs and the pair exercise completed without reopening a load-bearing framework decision;
- no Spine-owned shared encoding was invented or contradicted;
- all critical authority, object-integrity, freshness, evidence, and vocabulary tests passed;
- the independent-evaluation claim is accurately scoped;
- the evidence package is reconstructable;
- unresolved limitations do not invalidate the tested bootstrap claim.

Otherwise the assessor recommends a block and names the owner of the missing or contradictory contract. Gate clearance does not adopt the candidate operations. Adoption remains a separate user/Gatekeeper decision on exact candidate snapshots.

The kill condition is encountered when two components independently define the same cross-dimensional encoding incompatibly, or when this build can proceed only by doing so. On the first sign of that condition: preserve evidence, stop the build, and return the decision to the Spine owner.

## 13. Preservation, stopping, and terminal state

### Strengths to preserve

- AB4 goal-completeness and open-architecture behavior;
- AB2/AB5 separation between test design/execution and readiness gating;
- headline-first material assessment behavior where applicable;
- evidence-stage discipline;
- branch preservation;
- smallest-sufficient reach;
- `No material change needed` as a successful terminal result.

### Stop conditions

Stop when either:

1. all required deliverables and the gate report are complete; or
2. a prerequisite, authority, source, freshness, contract, or shared-vocabulary blocker is established.

Do not continue into the other four operations, dimension buildout, implementation, installation, migration, or promotion.

### Current terminal record

```yaml
task_class: sub-architect assignment design and readiness correction
terminal_state: candidate brief patched; not dispatch-ready
blocking_conditions:
  - adopted parent framework pin and adoption record not yet supplied
  - Phase-1 shared contract artifacts not yet supplied in this brief
  - Phase-2 operation shell set not yet supplied in this brief
  - donor source loadability and exact hashes not yet frozen
  - test target, rubric, roles, and contexts not yet frozen
only_valid_next_step: complete the prerequisite set, reconcile artifact identity, and generate an immutable dispatch packet
prohibited_next_step: dispatch the bootstrap pair directly from this mutable brief
next_role_class: UAM Architect / Artifact Custodian for prerequisite and packet freeze
```
