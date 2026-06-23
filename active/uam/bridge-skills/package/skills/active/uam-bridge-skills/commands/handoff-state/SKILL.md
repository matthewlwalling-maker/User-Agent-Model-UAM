---
name: handoff-state
description: "Use when explicitly invoked with /handoff, or when another session, model, agent, repository, or provider needs enough state to continue without prior chat history. Do not rewrite, shorten, or improve substantive artifacts."
---

# Handoff State

Command: `/handoff`  
ID: `uam.handoff-state`  
Version: `0.1.0`  
Status: D6 continuity bridge command  
Evidence ceiling: inherited from the carried work state.

## Purpose

Create a continuation packet that preserves enough authoritative state for another session, model, agent, repository, provider, or future user to continue without reconstructing prior conversation history.

`/handoff` projects state into a packet. It may include unchanged artifact references, evidence references, manifests, and execution instructions, but it must not rewrite the artifact, reinterpret state, resolve branches, promote evidence, or treat packaging as semantic authority.

The core question for `/handoff` is:

```text
What must the next consumer know, trust, preserve, verify, and do next without relying on hidden chat context?
```

## Donor Obligation Ledger

Extract these behaviors from donor resources without copying them one-for-one:

| Donor | Obligations carried into `/handoff` |
|---|---|
| UAM work-object model | Keep state, artifact, evidence, and packet distinct; a packet is a transport envelope, not new authoritative state. |
| UAM D6 State, Evidence, and Continuity | Preserve goals, constraints, decisions, branches, artifact refs, evidence, freshness, stop state, and continuation sufficiency. |
| UAM packet rules | Include exact snapshots or loadable references where material; omitted packet contents may not be inferred. |
| AB8 / state-preserving handoff | Favor complete state preservation when continuation depends on exact decisions, constraints, branches, or verification owed. |
| AB9 / portable packaging | Compress wording only when the same required state, evidence ceilings, branch identity, and optionality boundaries survive. |
| Handoff-package donors | Separate invariants, released decisions, open forks, provenance, scope boundaries, and one recommended next step. |
| `state-projection` lens | Project only the state needed by the next consumer while preserving authority, artifact identity, evidence limits, branches, and dependencies. |
| `evidence-ceiling` lens | Carry the inherited evidence stage and prohibit stronger claims unless new evidence exists. |

## Use When

- Work must continue in another session, model, agent, repository, or provider.
- A compact or material state projection is needed.
- The current state must be reconstructable without conversation history.
- The user asks for migration, transfer, resume, snapshot, or decision log.
- A consumer needs exact next-action instructions, action boundaries, source references, or verification owed.
- The task is to pause, restart, transfer, or package work without changing the carried artifact or committed state.

## Do Not Use When

- The user asks to rewrite, compress, or polish the artifact itself.
- The task is only physical packaging or archiving with no state projection.
- The user wants a review, comparison, diagnosis, or research brief.
- The user wants to resolve an open design branch, merge alternatives, or choose an option; route to `/compare` or `/design`.
- The user wants to repair, implement, refactor, or materialize a changed artifact; route to `/build`.
- The user wants to upgrade readiness, verify current facts, or produce evidence; route to `/review` or `/research`.

## Reads

- `committed_objective`
- `material_constraints`
- `current_state`
- `artifact_identities`
- `evidence`
- `authorized_next_action`
- `provider_capability_profile`
- `source_authority_order`
- `branch_state`
- `verification_owed`
- `next_consumer_profile`

## Writes

- `packet`: continuation or migration packet (`object_subtype: transport_packet` when route metadata needs the distinction).

Do not write authoritative state decisions. Do not mutate artifacts. Do not create new evidence except by recording the inspection basis and claim ceiling of the handoff itself.

## Chain Router Entry/Exit Check

After identifying the current request, explicit command, intended work object, action authority, likely scope, and whether a next route may be proposed or entered, but before final mode selection or substantive action, run a local route-sensitivity check.

Do not load router reference material for ordinary same-command work that can complete, stop, or merely recommend a next command within this skill's boundary without deciding route authority, `next_allowed`, auto-continuation, stop-gate status, or evidence upgrade.

The check trips when the route involves bounded continuation, next-step authority or `next_allowed`, stop gates, review/research/verification/reference work owed as a condition of continuation, artifact acting references, evidence-stage upgrade risk, context handoff or fresh-context routing, or material changes to routing, autonomy, chain policy, stop gates, object boundaries, evidence ceilings, eval gates, or stateful workflow behavior.

When the check trips, load only the relevant section bundle from package-relative `CHAIN_ROUTER.md`:

- next-route execution: Route Envelope, Chain Authority, Auto-Continue Rule, Command Continuation Matrix, Stop Gates;
- mutation, readiness, evidence upgrade, or material work-object boundary: Route Envelope, Chain Authority, Stop Gates, Closeout Discipline;
- review/research/support-operation owed as a continuation condition: Chain Authority, Command Continuation Matrix, Support Operations, Stop Gates;
- handoff or fresh-context routing: Route Envelope, Chain Authority, Auto-Continue Rule, Stop Gates, Closeout Discipline;
- governed artifact acting references: Route Envelope, Artifact Acting References, Chain Authority, Stop Gates;
- router, autonomy, stop-gate, evidence, eval-gate, stateful-workflow, or object-boundary policy changes: full reference.

Loading router reference material never grants action authority. If explicit authority is missing, stop, ask, or downgrade to a non-executing recommendation.

Before closeout, if the response would authorize, block, execute, auto-continue, package, or make owed work a condition for a next route and the required section bundle has not been loaded, either load it or downgrade the output to a non-executing recommendation.

If section-specific loading is unavailable but the full reference is available, use `KERNEL.md` for simple non-material cases and load the full reference when a material route decision depends on it. If the reference itself is unavailable, continue only within `KERNEL.md` and record the reference gap in closeout.

## Context Source Priority

Load the smallest context needed for the selected handoff mode, in this order:

1. Current user request, explicit command, target consumer, and stop condition.
2. Current committed objective, decisions, constraints, exclusions, and authority.
3. Exact artifact identities, versions, branches, hashes, paths, or loadable references.
4. Evidence records, source references, claim limits, and verification owed.
5. `MANIFEST.yaml`, `KERNEL.md`, and relevant skill/lens boundaries when the packet carries this package.
6. Provider capability profile, especially file read, file write, archive creation, retrieval, memory, and isolated context.
7. Donor or project context only when it is load-bearing for the next consumer.

If a load-bearing source, artifact, evidence reference, or current state field is unavailable, mark it `unavailable` or `not inspected` and state the consequence. Do not infer missing packet contents from prior chat memory, model confidence, or narrative continuity.

## Modes

- `continue`
- `transfer`
- `snapshot`
- `resume`
- `decision-log`
- `compact`
- `material`
- `execution-packet`
- `evaluator-handoff`
- `implementation-handoff`
- `evidence-handoff`

Select exactly one primary mode. Use a supporting mode only when needed and state why.

| Mode | Use when | Primary output |
|---|---|---|
| `continue` | The same work continues later in a similar environment. | Continuation packet with current state and next action. |
| `transfer` | Another model, provider, agent, repo, or human must take over. | Consumer-specific transfer packet with capability assumptions and source refs. |
| `snapshot` | The user wants a durable status/state record without immediate continuation. | State snapshot, evidence ceiling, branches, and revisit triggers. |
| `resume` | A supplied packet or prior state must become executable again. | Resume contract plus missing-state checks and recommended move. |
| `decision-log` | The main value is preserving decisions, invariants, released choices, and branches. | Decision/state log with authority and reopen triggers. |
| `compact` | The consumer needs a short but complete projection. | Compact packet preserving all required fields. |
| `material` | The work is high-coupling, branch-sensitive, evidence-sensitive, or cross-provider. | Full execution-ready packet. |
| `execution-packet` | A next action needs exact inputs and boundaries. | Operation input packet with reads/writes, authority, and expected output. |
| `evaluator-handoff` | The next consumer will evaluate, test, or gate the work. | Evidence, fixture, artifact, claim-limit, and scoring context. |
| `implementation-handoff` | The next consumer will build or patch. | Artifact refs, constraints, authorized changes, and prohibited mutations. |
| `evidence-handoff` | Evidence records or research must continue elsewhere. | Source map, claim status, contradictions, and verification owed. |

## Lenses

- `state-projection`
- `evidence-ceiling`
- `variant-reconciliation`

Use lenses only to preserve continuity. Do not turn `/handoff` into comparison, research, review, diagnosis, or artifact compression.

## Procedure

1. Identify the next consumer, continuation purpose, primary mode, and required handling level.
2. Freeze the carried state boundary: committed objective, decisions, constraints, exclusions, artifact identities, evidence ceiling, authority, and next action.
3. Preserve exact identity, version, branch, artifact refs, hashes or loadable references where material, and evidence references.
4. Separate invariants, released decisions, open branches, optional opportunities, and speculative ideas.
5. Include all facts needed for execution without prior chat history.
6. Mark unavailable or uninspected required fields explicitly; do not fill them by inference.
7. Preserve explicit exclusions, prohibited actions, verification owed, dependencies, stop conditions, and revisit triggers.
8. Omit reasoning history that does not affect execution.
9. Do not resolve disagreements, merge branches, upgrade evidence, or compress substantive artifacts.
10. Produce a compact or material packet based on downstream need and provider capability.
11. Run a cold-start sufficiency check: can the next consumer act correctly from this packet alone?

## Mode Procedures

### `continue`

1. State the current objective, exact state, and why continuation is needed.
2. Preserve the current action boundary and authorized next action or recommended move.
3. Include only reasoning history that affects execution.
4. End with one recommended next action and a stop/revisit trigger.

### `transfer`

1. Identify the target consumer and provider capability assumptions.
2. Include loadable source and artifact references, or mark missing sources as blocking.
3. Translate environment-specific paths, commands, and capabilities only as needed.
4. State what the new consumer must not relitigate, mutate, or assume.

### `snapshot`

1. Record current state, decisions, branches, artifact refs, and evidence ceiling.
2. Make clear whether the snapshot is informational or an executable packet.
3. Preserve freshness, invalidation, and revisit conditions.
4. Do not imply work is complete unless completion has evidence.

### `resume`

1. Inspect the supplied packet or state source.
2. Identify missing, stale, contradictory, or unavailable continuation fields.
3. Convert usable state into a current work contract.
4. Route the next action to the owning command; do not perform it under `/handoff`.

### `decision-log`

1. Separate committed decisions, invariants, released decisions, and open forks.
2. For each invariant, state why changing it would break or materially alter the work.
3. For released decisions, state who may revisit them and under what trigger.
4. Preserve rejected alternatives only when they remain decision-relevant.

### `compact`

1. Compress wording, not state obligations.
2. Preserve objective, constraints, artifact refs, evidence ceiling, authority, next action, risks, and verification owed.
3. Keep optional opportunities separate from required continuation.
4. If compacting would erase a load-bearing field, switch to `material`.

### `material`

1. Use the full packet contract.
2. Include provenance, source authority, exact refs, branches, dependencies, and claim limits.
3. Include consumer instructions, prohibited actions, expected output, and terminal/revisit condition.
4. Prefer completeness over brevity when the next consumer is context-isolated.

### `execution-packet`

1. Name the next owning command or operation.
2. Provide eligible inputs, permitted reads, prohibited reads, writes, expected output, and stop conditions.
3. Preserve action authority and mutation boundaries.
4. Do not execute the recommended move unless separately authorized.

### `evaluator-handoff`

1. Provide artifact refs, evidence refs, fixtures, scoring criteria, evidence ceiling, and known limitations.
2. Preserve failed, contradictory, partial, or unavailable evidence without repair.
3. State what evidence would upgrade or downgrade the claim.
4. Do not grade or revise the artifact unless `/review` is separately authorized.

### `implementation-handoff`

1. Provide exact artifact refs, intended change boundary, constraints, dependencies, and prohibited mutations.
2. State whether implementation authority is granted, withheld, or must be reconfirmed.
3. Preserve open design questions as blockers or branches.
4. Do not implement under `/handoff`.

### `evidence-handoff`

1. Preserve source map, evidence stage, claim taxonomy, contradictions, and freshness requirements.
2. Mark source content as attached, loadable, quoted, summarized, unavailable, or not inspected.
3. State what the next consumer may claim and what remains unverified.
4. Do not perform fresh research under `/handoff`.

## Packet Contract

Preserve these functions; exact formatting may vary:

- How to use this packet: next consumer, first action, and actions not to take.
- Committed objective.
- Required obligations and material constraints.
- Invariants: decisions or boundaries that must not silently change.
- Released decisions: choices the next consumer may revisit, with triggers.
- Current state and progress.
- Artifact identities, versions, branches, paths, hashes, or loadable references.
- Evidence ceiling, evidence references, source provenance, and claim limits.
- Authorized next action and prohibited action reach.
- Open branches, contradictions, risks, dependencies, and material unknowns.
- Optional opportunities kept separate from required continuation.
- Verification owed and evidence needed to upgrade claims.
- Provider capability assumptions and degradation notes.
- Expected output from the next consumer.
- Stop condition, terminal condition, and revisit triggers.

If a field is not available, write `Unavailable:` with the missing field and consequence. Do not omit it silently when it is material.

## Required Output

- Committed objective.
- Required obligations and constraints.
- Invariants and released decisions, when relevant.
- Current state.
- Artifact identities, versions, branches, and exact refs.
- Evidence ceiling, evidence refs, and claim limits.
- Authorized next action, next operation, or recommended move, approval shorthand when safe, and prohibited actions.
- Open branches, risks, and dependencies.
- Verification owed.
- Next consumer and stop/revisit triggers.
- Unavailable required fields and consequences.

## Output Profiles

### Compact

Use when the packet must be short but still executable:

```text
Consumer:
Objective:
Current state:
Must preserve:
Artifact refs:
Evidence ceiling:
Next action / recommended move:
Blocked/prohibited:
Verification owed:
Revisit trigger:
```

### Material

Use for context-isolated, cross-provider, branch-sensitive, or evidence-sensitive continuation:

```text
# <Project or Workstream> Handoff

## How To Use This
## Committed Objective
## Obligations, Constraints, And Invariants
## Released Decisions And Open Branches
## Current State
## Artifact Identities And References
## Evidence Ceiling And Claim Limits
## Authorized Next Action Or Recommended Move
## Prohibited Actions
## Dependencies, Risks, And Unknowns
## Verification Owed
## Provider Capability Notes
## Terminal And Revisit Conditions
```

## Examples

### Compact continuation

Input: `/handoff Give the next session enough to continue the skill rewrite.`

Expected behavior:

```text
Consumer: next session in the same project.
Objective: continue the authorized skill rewrite.
Current state: <what has been read, decided, changed, and not changed>.
Must preserve: explicit-command pilot, object boundaries, evidence ceiling.
Artifact refs: <paths and versions>.
Evidence ceiling: design-time plus static inspection.
Next action: inspect changed file, run the owed check, then stop for alignment.
Blocked/prohibited: no deployment, no next-skill rewrite, no artifact compression.
Verification owed: <checks not yet run>.
Revisit trigger: user changes target skill or authorizes broader package work.
```

### Artifact compression boundary

Input: `/handoff Make this long spec shorter for the next agent.`

Expected behavior:

```text
Route boundary: /handoff may compact the state projection, not the substantive spec.
Packet: include exact spec reference, version, current state, evidence ceiling, and next action.
If the spec itself must be shortened: route to /build compress after explicit authority.
```

### Missing source

Input: `/handoff Send this to another model, but I cannot provide the referenced files.`

Expected behavior:

```text
Unavailable: referenced source files are not attached or loadable.
Consequence: next consumer cannot safely rely on claims derived from those files.
Packet action: include the missing source list, claim limits, and a blocking instruction to recover sources before continuing.
```

## Provider Degradation

If archive or file creation is unavailable, return a self-contained Markdown packet and mark physical packaging as not performed.

If file reading is unavailable, use only supplied excerpts and mark artifact/source completeness unverified.

If durable memory is unavailable, include all required continuation state in the packet instead of relying on remembered context.

If retrieval is unavailable, do not claim current provider, source, policy, or external facts unless supplied evidence supports them within the required freshness window.

If isolated contexts are unavailable, do not claim independent reconstruction or blind continuation testing.

## Stop Conditions

- The next consumer can continue without reconstructing chat history.
- Required state is unavailable and must be recovered first.
- The user asks for artifact rewriting, which routes to `/build`.
- The user asks for evidence verification, which routes to `/research` or `/review`.
- The user asks to resolve branches, which routes to `/compare` or `/design`.
- The packet would omit a load-bearing field under compact handling; switch to material or stop.
- The requested physical package cannot be created; return Markdown and mark packaging not performed.

## Boundary

`/handoff` writes a packet (`object_subtype: transport_packet`). It does not mutate state owned by another operation and does not rewrite the artifact being carried.

A handoff packet may carry a state projection, artifact refs, evidence refs, execution instructions, manifests, and hashes. It is not itself authoritative state unless the designated state owner later commits it.

Physical packaging, archives, zips, folders, or API payloads are runtime transport. They may contain a handoff packet, but they do not change state meaning, artifact meaning, or evidence stage.
