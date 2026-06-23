---
name: design-solution
description: "Use when explicitly invoked with /design, or when the user asks what should exist: architecture, plan, specification, candidate designs, workflow, or implementation contract. Do not use for artifact mutation unless the user separately authorizes /build."
---

# Design Solution

Command: `/design`  
ID: `uam.design-solution`  
Version: `0.1.0`  
Evidence ceiling: `design-time`

## Purpose

Determine what should exist before or apart from creating the substantive artifact.

## Use When

- The user asks for architecture, specification, plan, candidate designs, workflow design, or target state.
- Material requirements should be derived before anchoring on an existing artifact.
- Competing design branches need reconciliation.

## Do Not Use When

- The user only wants an authorized artifact edit or file materialization.
- The user asks only for evaluation, comparison, diagnosis, research, or handoff.
- The design is already committed and the next required operation is implementation.

## Reads

- `work_intent`
- `relevant_state`
- `source_artifact`
- `evidence`
- `provider_capability_profile`

## Writes

- `artifact`: design artifact, specification, plan, or architecture.
- `state`: selected design choices and open branches.

## Chain Router Entry/Exit Check

After identifying the current request, explicit command, intended work object, action authority, likely scope, and whether a next route may be proposed or entered, but before final mode selection or substantive action, run a local route-sensitivity check.

Do not load router reference material for ordinary same-command work that can complete, stop, or merely recommend a next command within this skill's boundary without deciding route authority, `next_allowed`, auto-continuation, stop-gate status, or evidence upgrade.

The check trips when the route involves bounded continuation, next-step authority or `next_allowed`, stop gates, review/research/verification/reference work owed as a condition of continuation, artifact acting references, evidence-stage upgrade risk, context handoff or fresh-context routing, or material changes to routing, autonomy, chain policy, stop gates, object boundaries, evidence ceilings, eval gates, or stateful workflow behavior.

When the check trips, load only the relevant section bundle from package-relative `docs/chain-router-reference.md`:

- next-route execution: Route Envelope, Chain Authority, Auto-Continue Rule, Command Continuation Matrix, Stop Gates;
- mutation, readiness, evidence upgrade, or material work-object boundary: Route Envelope, Chain Authority, Stop Gates, Closeout Discipline;
- review/research/support-operation owed as a continuation condition: Chain Authority, Command Continuation Matrix, Support Operations, Stop Gates;
- handoff or fresh-context routing: Route Envelope, Chain Authority, Auto-Continue Rule, Stop Gates, Closeout Discipline;
- governed artifact acting references: Route Envelope, Artifact Acting References, Chain Authority, Stop Gates;
- router, autonomy, stop-gate, evidence, eval-gate, stateful-workflow, or object-boundary policy changes: full reference.

Loading router reference material never grants action authority. If explicit authority is missing, stop, ask, or downgrade to a non-executing recommendation.

Before closeout, if the response would authorize, block, execute, auto-continue, package, or make owed work a condition for a next route and the required section bundle has not been loaded, either load it or downgrade the output to a non-executing recommendation.

If section-specific loading is unavailable but the full reference is available, use `KERNEL.md` for simple non-material cases and load the full reference when a material route decision depends on it. If the reference itself is unavailable, continue only within `KERNEL.md` and record the reference gap in closeout.

## Modes

| Mode | Use when | Required operations | Reasoning and context to apply | Output focus |
|---|---|---|---|---|
| `explore` | The user wants design space, options, or materially different approaches before commitment. | Derive goals and constraints, generate distinct candidates, name tradeoffs, keep optional opportunities separate. | Use capability-first reasoning, then premortem lightly on high-risk candidates. Do not inspect an existing artifact as the frame until required capabilities are stated. | Candidate set, tradeoffs, and selection criteria. |
| `architect` | The user needs target structure, component boundaries, workflow, or system design. | Build a required capability model, assign capabilities to components or stages, define interfaces, authority, evidence, validation, and stop points. | Use capability-first, evidence-ceiling, and boundary reasoning. Load current artifacts only after the goal-derived capability model for material work. | Architecture and design decisions. |
| `specify` | The user needs an implementation-ready contract, agent spec, skill spec, prompt spec, or role instructions. | Emit the scaled governing skeleton, define authority and action gates, identify verbatim-critical sections, state design intent. | Use spec-builder grammar, ambiguity-gate context, provider capability profile, and source authority. | Implementation-ready specification. |
| `plan` | The user needs sequencing, rollout, milestones, dependencies, or validation path. | Identify phases, dependencies, decision gates, verification owed, rollback/revisit triggers, and next owner. | Use smallest-sufficient-process reasoning and evidence-ceiling discipline. Preserve optional future work as optional. | Plan, phases, gates, and verification sequence. |
| `reconcile` | Multiple designs, drafts, branches, or model outputs must become one target design or decision basis. | Align sections, compare behavior per divergence, preserve load-bearing differences, choose or preserve branches, produce a rationale ledger. | Use variant-reconciliation, verbatim-critical protection, and branch identity. Do not blend incompatible designs for elegance. | Reconciled design or unresolved conflict ledger. |
| `refine` | A design exists and needs bounded improvement without reopening the whole architecture. | Confirm the existing decision basis, identify the local improvement target, preserve settled choices, update only affected design elements. | Use preservation mapping, evidence ceiling, and no-material-change stopping. Route to `architect` if the requested change reopens system structure. | Bounded revised design and preservation note. |

## Lenses

- `capability-first`
- `gold-standard`
- `narrative-substance`
- `premortem`
- `variant-reconciliation`
- `evidence-ceiling`

## Context Loading

Load context progressively by selected mode:

- Always load the current request, explicit constraints, evidence stage, authority, provider capability profile, and relevant manifest command boundaries.
- For `explore`, load goals, constraints, known alternatives, and any decision criteria. Avoid deep artifact reading until the option space is framed.
- For `architect`, load source artifacts, prior state, existing interfaces, dependencies, validation expectations, and any deployment constraints after the independent capability model is formed.
- For `specify`, load target host/provider constraints, authority surface, action surface, source hierarchy, output requirements, and any sibling spec or house grammar that should be matched.
- For `plan`, load dependencies, sequencing constraints, verification gates, rollout limits, and rollback requirements.
- For `reconcile`, load all candidate versions, their source identity, known strengths, verbatim-critical sections, and criteria for selection.
- For `refine`, load the settled design basis and only the affected neighboring design context unless a broader dependency is exposed.

If a mode needs current external information and retrieval is unavailable, route to `/research` or label the assumption as unverified rather than presenting it as evidence.

## Scaling And Authority Gate

Before material design work, identify or infer:

- target asset, system, workflow, or decision;
- objective and lifecycle stage;
- material constraints;
- evidence stage;
- authorized action;
- whether open architecture is authorized.

Proceed on a bounded assumption when a wrong assumption would be reversible and would not materially change the design. Ask one focused question when the ambiguity would select a different architecture, authorize a hard-to-reverse action, or collapse two incompatible branches.

Use the `fast` path when the design target is local, reversible, low-coupling, and unlikely to hide a material omission. Use the `material` path when success depends on multiple components, state, authority, validation, deployment, provider capability, or branch-sensitive decisions.

For material work that evaluates or revises an existing artifact, derive and state the independent required capability model before using the existing artifact as the frame. Keep Tier 1 and Tier 2 requirements separate from optional Tier 3 opportunities and speculative Tier 4 possibilities.

## Procedure

1. Select exactly one primary mode from the mode table. Add a supporting mode only when necessary and state why.
2. Apply the scaling and authority gate.
3. Confirm objective, constraints, authority, and evidence stage.
4. Separate explicit, entailed, optional, and speculative requirements.
5. Load only the context required by the selected mode.
6. For material work, derive the required capability model before evaluating the current artifact.
7. Produce candidate designs or a single target design as the request warrants.
8. Identify selected choices, rejected alternatives, optional opportunities, and preserved strengths.
9. State verification owed and handoff needs.
10. Stop before implementation unless `/build` is separately authorized.

## Mode Procedures

Use only the mode procedure needed for the request. Do not run every procedure by default.

### `specify`

When designing an agent, skill, role, workflow, or governing instruction set, emit a scaled contract that covers:

- role, scope, and boundaries;
- precedence or conflict-resolution order;
- execution and authority modes;
- evidence and provenance expectations;
- output discipline;
- classification or scaling rules;
- governance and action gates;
- ambiguity handling;
- accuracy over agreement;
- known edge cases;
- pre-output checks;
- optional resources and design intent.

Flag `verbatim-critical` sections whose wording carries behavior, such as ambiguity gates, injection defenses, safety/legal constraints, and action-confirmation gates.

### `architect`

Derive the required capability model before mapping any current artifact. For material architecture, make selected choices traceable to explicit or entailed requirements and keep optional opportunities separate.

When alternatives expose a real decision, provide materially different candidates rather than wording variants.

For material architecture based on an existing artifact, use this output order:

1. Path, evidence stage, goal basis, and assumptions.
2. Independent required capability model with requirement traces.
3. Visible seal that the independent model is complete.
4. Current artifact mapping, coverage, and gap assessment.
5. Target architecture, fix layer, verification owed, and stop decision.

### `reconcile`

When reconciling drafts, branches, or model outputs:

1. Align sections or behavioral units.
2. For each divergence, decide whether it is same intent with different wording or different behavior.
3. Preserve behavior-bearing wording over nicer prose.
4. Select verbatim-critical sections whole instead of blending clause by clause.
5. Produce a rationale ledger and residual conflicts.

### `premortem`

When a material design choice is about to be committed, add:

- the decision and key premises;
- the strongest opposing case;
- likely failure causes;
- the simpler version and what it sacrifices;
- an observable kill condition or tripwire.

For low-stakes reversible choices, keep this to a short tripwire.

### `gold-standard`

Use only when a relevant reference basis exists or can be gathered. State the corpus or standard, selection criterion, coverage limits, and whether the comparison is legible or illustrative.

Classify frontier omissions as `close` or `correct-omission`. Classify deltas as scoped novelty, prior art missed, or different-not-better. Never make unqualified novelty claims.

If live retrieval is required but unavailable, name the needed sources and downgrade the result to supplied-source or design-time illustration.

### `narrative-substance`

For strategy, explanatory, or persuasive design artifacts, test whether each major section does logical work or merely restates context. Preserve necessary context, but prefer proof over paraphrase.

## Required Output

- Scaling path and authority assumption, when material.
- Required design.
- Independent capability model, when material.
- Selected design choices.
- Optional opportunities.
- Rejected alternatives.
- Verbatim-critical sections, when applicable.
- Rationale ledger, when reconciling variants.
- Premortem tripwire or kill condition, when commitment risk warrants it.
- Corpus and claim scope, when using gold-standard comparison.
- Verification still required.
- Recommended move, route options when real, and approval shorthand when safe.
- `No material change needed`, when the current design is sufficient at the available evidence stage.

## Stop Conditions

- The design is sufficient for commitment or implementation.
- Missing authority blocks selecting a design.
- Evidence is insufficient for the requested claim.
- Implementation would begin without `/build` authority.

## Boundary

`/design` may create design artifacts, but it must not silently create or change the production artifact.
