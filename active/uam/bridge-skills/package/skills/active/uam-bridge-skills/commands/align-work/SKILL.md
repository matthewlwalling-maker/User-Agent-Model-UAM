---
name: align-work
description: "Use when explicitly invoked with /align, or as a lightweight pre-pass to clarify intent, constraints, branches, authority, scope, priority, and the recommended move before substantive work. Do not use to produce a final design, artifact, review, comparison, diagnosis, research brief, or handoff packet."
---

# Align Work

Command: `/align`
ID: `uam.align-work`
Version: `0.1.0`
Status: interim D1 / Collaboration Kernel bridge command
Evidence ceiling: `design-time`

## Purpose

Convert messy intent into a compact work contract that lets the recommended move proceed without silently solving the wrong problem.

`/align` is a practical bridge command, not a permanent claim about the final UAM global operation set. It lives in D1 / Spine territory: normalize and commit intent, route the recommended move, and preserve state boundaries. It must not derive domain architecture, mutate artifacts, evaluate quality, merge branches, diagnose failures, perform research, or create handoff packets.

## Donor Obligation Ledger

Extract these behaviors from donor resources without copying them one-for-one:

| Donor | Obligations carried into `/align` |
|---|---|
| UAM D1 Intent and Collaboration | Interpret outcome, classify requirements, handle ambiguity, choose operation, scale compact/material, commit bounded state, define reopen triggers. |
| UAM work-object model | Keep state, artifact, evidence, and packet distinct; `/align` writes state only. |
| `ask-vs-assume` | Ask only when guessing wrong would create a false-premise deliverable or authorize hard-to-reverse action; otherwise use a bounded assumption or preserve branches. |
| `prompt-macro-router` | Preserve exact explicit command text; reject invalid command/action with rule, reason, and smallest correction; never auto-chain downstream. |
| Goal Completeness / governance contract | Separate explicit, entailed, optional, speculative requirements; use the least costly process that can detect a material mistake; treat "No material change needed" as valid. |
| `option-ranker` | In `prioritize`, define criteria before ranking; guard against order, recency, and salience bias. |
| `steelman-premortem` | For consequential choices, test the dominant path against likely failure and name a revisit trigger. |

## Use When

- The user explicitly invokes `/align`.
- The request is ambiguous enough that wrong assumptions would change the work.
- Goals, constraints, branches, priority, authority, or scope need to be sorted before action.
- The next primary command is unclear.
- A prior handoff or packet must be resumed into a current work contract before acting.

## Do Not Use When

- The user has already given a clear, low-risk, reversible task.
- The user requests substantive design, building, review, comparison, diagnosis, research, or handoff as the primary work and the boundary is already clear.
- The only unresolved details are cosmetic.
- The right response is a simple direct answer.

## Reads

- `work_intent`
- `user_constraints`
- `relevant_state`
- `source_artifact`
- `provider_capability_profile`
- `manifest_command_boundaries`

## Writes

- `state`: compact work contract only.

Do not write or revise substantive artifacts. Do not create evaluation evidence beyond noting the design-time basis of the work contract. Do not create a packet.

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

Load the smallest context needed for the selected mode, in this order:

1. Current user request and exact explicit command, if any.
2. User-stated constraints, authority, exclusions, and stop conditions.
3. Current committed state or handoff packet, when supplied for this task.
4. `MANIFEST.yaml` command boundaries and work-object ownership.
5. UAM framework commitments relevant to D1, work objects, evidence ceilings, and stop behavior.
6. Donor resources relevant to the selected mode.
7. Provider capability profile and known degradation limits.

If a load-bearing source is unavailable, say so and choose `ASK`, `ASSUME`, `FORK`, or `PREPARE-NOT-EXECUTE`. Do not reconstruct missing state from vibes or prior chat memory.

## Modes

Select exactly one primary mode. Use a supporting mode only when needed to finish the work contract.

| Mode | Use when | Primary output |
|---|---|---|
| `clarify` | A load-bearing ambiguity could change outcome, authority, or recommended move. | Gate result plus one blocking question or bounded assumption. |
| `frame` | The user has a broad, messy, or exploratory goal. | Stable outcome statement, requirement classes, success conditions. |
| `contract` | Work is ready to proceed but needs a compact execution agreement. | Work contract for the next primary operation. |
| `branch` | Multiple viable interpretations or paths remain materially different. | Branch map, dominant reversible path or user-choice stop. |
| `prioritize` | Goals, constraints, or next steps compete. | Ordered priorities and decisive criterion. |
| `scope` | Task boundary is too broad, too narrow, or risks accidental expansion. | In-scope/out-of-scope boundary and renewed-authorization trigger. |

## Lenses

- `evidence-ceiling`
- `capability-first`
- `premortem`
- `variant-reconciliation`

Use lenses lightly. `/align` may borrow their discipline to frame state, preserve branch identity, avoid overclaiming, and test consequential choices, but it must not turn alignment into design, review, comparison, diagnosis, research, or handoff.

## Procedure

1. Identify the current request, explicit command, authority, and likely object boundary.
2. Detect whether any missing load-bearing state, unavailable packet, or ambiguous mutation authority would change the result.
3. Choose one primary mode and the smallest handling level that can prevent material error.
4. Use `ASK`, `ASSUME`, `FORK`, or `PREPARE-NOT-EXECUTE` only when the gate changes downstream action.
5. Preserve branch identity when live paths differ materially.
6. Route to one recommended move, name real route options, or answer directly when bridge alignment is unnecessary.
7. Stop before creating artifacts, state packets, evidence briefs, comparisons, diagnoses, or implementation.

## Mode Procedures

### `clarify`

Use to prevent false-premise work, not to collect nice-to-have preferences.

1. Name the unresolved premise.
2. Test whether a wrong guess would change the deliverable spine, authority, operation, or a hard-to-reverse action.
3. If yes, ask one focused or batched question and stop.
4. If no and the gap is trivial, proceed with a labeled assumption.
5. If no but two viable paths remain, preserve a fork and proceed only on a reversible dominant path.
6. If the action is clear but hard to reverse, prepare a preview and stop for confirmation instead of asking a generic question.

If missing load-bearing state blocks progress, ask for the missing source, ask for the packet, ask for the path, or ask for the decision. Do not reconstruct the missing state from prior chat memory.

### `frame`

Use to turn exploratory intent into an executable outcome statement.

1. Separate desired outcome from requested method.
2. Classify requirements as explicit, entailed, optional, or speculative.
3. State material constraints, exclusions, and likely success conditions.
4. Keep future ideas optional unless the user explicitly promotes them.
5. Stop before architecture; route architecture needs to `/design`.

### `contract`

Use when the next step is mostly clear and the state needs to be made executable.

1. Identify target, current object, authority, evidence ceiling, and stop condition.
2. Record assumptions and exclusions that the recommended move must preserve.
3. Select one primary next command from the routing table.
4. Name supporting commands only as later recommendations, not automatic chains.
5. End with a compact work contract that can be consumed without replaying the conversation.

### `branch`

Use when multiple paths are live and collapsing them would lose meaning.

1. Name each branch in user-relevant terms.
2. State what differs: goal, scope, artifact, authority, evidence, risk, or next command.
3. Estimate rough fit or likelihood only when useful; do not fabricate precision.
4. Choose a dominant path only if it is reversible and preserves branch identity.
5. Stop for user choice when paths imply different artifact mutations, commitments, or irreversible actions.
6. Name the revisit trigger that would reopen the branch.

### `prioritize`

Use when the user needs a decision about order, not a full comparison artifact.

1. Define ranking criteria before ranking: user priority, hard constraints, dependency order, consequence, reversibility, and omission risk.
2. Separate hard constraints from preferences.
3. Rank the items using the same criteria for each.
4. Check for order, recency, or salience bias.
5. Name the decisive criterion and the recommended move.
6. For consequential commitments, run a short premortem and state a revisit trigger.

### `scope`

Use when the boundary is the main work.

1. Define in scope, out of scope, non-goals, and dependencies.
2. Identify object boundaries: state, artifact, evidence, packet.
3. If the user asks for state projection, route to `/handoff`; if they ask for artifact compression, route to `/build`.
4. State what would require renewed authorization.
5. Prevent hidden expansion into design, build, review, or handoff.
6. Return a boundary that downstream skills must preserve.

## Routing Decision Table

Recommend one primary move when the evidence supports it; name route options when materially different paths remain viable.

| Route to | Use when the committed next job is | Do not route there when |
|---|---|---|
| `/design` | Decide what should exist: architecture, plan, specification, workflow, candidate set. | The artifact change is already specified and authorized. |
| `/build` | Create or modify the substantive artifact within clear authority. | Architecture or mutation authority is unresolved. |
| `/review` | Evaluate correctness, completeness, quality, readiness, or evidence without mutation. | The user mainly wants a new or changed artifact. |
| `/compare` | Judge alternatives against criteria or preserve branch tradeoffs. | There is only one path and no relative decision. |
| `/diagnose` | Explain observed or likely failure and locate fix layer. | The goal is ordinary evaluation without a failure mechanism. |
| `/research` | Gather, verify, or synthesize source-grounded evidence. | The needed evidence is already supplied and current enough. |
| `/handoff` | Project current state to another model, session, agent, or consumer. | The user wants artifact compression or rewriting. |
| stop/direct | No material change needed, or a direct answer/simple edit is sufficient. | A material boundary, authority, or evidence issue remains unresolved. |

## Scaling

Use the least burdensome process that can detect a material mistake.

Compact handling is enough when most are true:

- one bounded outcome;
- low reversibility cost;
- no material artifact mutation;
- no state/evidence/packet ambiguity;
- no conflicting branches;
- likely correction fits in one user turn.

Material handling is required when any combination is material:

- multiple live goals, branches, artifacts, or consumers;
- authority, installation, deletion, publishing, or overwrite risk;
- downstream design/build/review boundary is unclear;
- missing context could create false-premise work;
- state, artifact, evidence, or packet might be confused;
- the work contract must survive handoff or isolated context.

If compact handling reveals hidden coupling, escalate to material and say why. If material handling collapses to a simple direct answer, stop without ceremony.

## Gate Output

When ambiguity or action authority is material, include one of:

```text
GATE: ASK
ASK: <one focused or batched question>
```

Use `ASK` for ambiguous mutation authority, such as "review and improve this specification," when directly modify the artifact is not yet authorized.

```text
GATE: ASSUME
ASSUMPTION: <labeled assumption; override if wrong>
```

```text
GATE: FORK
PATHS: <path A with rough fit> | <path B with rough fit>
PROCEEDING: <dominant reversible path or blocked pending choice>
```

```text
GATE: PREPARE-NOT-EXECUTE
PREVIEW: <safe preparation output>
BLOCKED ACTION: <send/publish/overwrite/delete/install/activate/approve/submit/etc.>
CONFIRMATION NEEDED: <specific confirmation required>
```

Do not use gate labels as ceremony for trivial gaps.

For requests such as "What time is it?", bridge alignment is unnecessary. Answer directly when the environment can support it, and do not produce a material work contract.

## Required Output

Preserve these functions; exact formatting may vary:

- Outcome.
- Required constraints.
- Requirement classes: explicit, entailed, optional, speculative.
- Gate result, when material.
- Bounded assumptions, blocking question, fork, or prepare-not-execute stop.
- Excluded or optional items.
- Primary next operation or recommended move, with route options only when real.
- Fast or material handling recommendation.
- Stop or revisit condition.

For material alignment, include enough state for the recommended move to proceed without reconstructing conversation history.

## Output Profiles

### Compact

Use 4 to 8 short lines:

```text
Outcome: <committed outcome>
Constraints: <must preserve>
Assumption: <if any>
Excluded: <not doing>
Recommended move: </command, direct answer, decision, stop, or fork>
Handling: Compact
```

### Material

Use a work contract:

```text
Outcome
Requirement classes
Constraints and authority
Object boundary
Gate decision
Primary next operation or recommended move
Route options or optional/supporting operations
Evidence ceiling
Approval shorthand, when safe
Stop/revisit trigger
```

## Examples

### Clarify, compact

Input: `/align Make this tighter before I send it.`

Expected behavior:

```text
Outcome: tighten the message draft.
Constraints: preserve meaning and do not send.
GATE: PREPARE-NOT-EXECUTE
PREVIEW: I can revise the draft for review.
BLOCKED ACTION: send
CONFIRMATION NEEDED: explicit instruction to send after review.
Recommended move: /build shape
Handling: Compact
```

### Frame, material

Input: `/align Help me figure out what I am actually trying to build here.`

Expected behavior:

```text
Outcome: define the intended build target before design or implementation.
Explicit: user wants clarification of the build objective.
Entailed: identify constraints, success conditions, and recommended move.
Optional: candidate architectures.
Speculative: provider adapter implementation.
Excluded: creating files or final design in this step.
Recommended move: /design after user accepts the framed outcome.
Handling: Material
```

### Branch

Input: `/align Should this become a Codex-native skill first or a model-neutral package first?`

Expected behavior:

```text
GATE: FORK
PATHS: Codex-first, faster pilot and direct file testing | Canonical-first, stronger parity discipline
PROCEEDING: Codex-first with canonical-source discipline, because it is reversible if manifest boundaries are preserved.
Revisit: if cross-model parity becomes the immediate release target.
Recommended move: /compare if the user wants a formal decision matrix; /design if the branch is accepted.
Handling: Material
```

### Ambiguous Review And Mutation

Input: `/align Review and improve this specification.`

Expected behavior:

```text
GATE: ASK
ASK: Do you want read-only review first, or do you authorize a follow-up /build patch after findings?
Reason: directly modify the artifact is not authorized by a combined review/improve request.
Recommended move: stop until the review/build boundary is clear.
Handling: Compact
```

### Current Evidence Before Update

Input: `/align Find current provider docs and update the adapter plan.`

Expected behavior:

```text
Outcome: verify current provider docs before changing the adapter plan.
Constraint: do not claim current facts from memory.
Recommended move: /research
Reason: source verification routes to `/research` before any plan update; claiming current facts from memory is prohibited.
Handling: Material
```

### Scope

Input: `/align Build the initial rollout, but do not install anything.`

Expected behavior:

```text
Outcome: source package rollout work only.
In scope: canonical source files, skill drafts, eval fixtures, docs.
Out of scope: global install, provider activation, v1 readiness claim.
Object boundary: build may write source artifacts; align writes only this state contract.
Recommended move: /build implement after scope is accepted.
Handling: Material
```

### Direct Answer

Input: `/align What time is it?`

Expected behavior:

```text
Outcome: answer the direct question.
Recommended move: direct
Excluded: material work contract or bridge command chain.
Handling: Compact
```

## Stop Conditions

- The work contract is sufficient for the recommended move.
- One load-bearing question blocks honest progress.
- The safe result is `No material change needed`.
- The user changes the objective or authority.
- The requested move would exceed `/align` ownership.

## Boundary

`/align` may recommend `/design`, `/build`, `/review`, `/compare`, `/diagnose`, `/research`, or `/handoff`, but it does not perform those operations unless the user separately continues with clear authority.

When routing from an explicit command, `/align` must not silently broaden the action, drop a user-supplied constraint, or automatically chain a downstream skill.
