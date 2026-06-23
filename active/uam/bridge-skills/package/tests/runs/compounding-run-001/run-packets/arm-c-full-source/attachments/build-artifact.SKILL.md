---
name: build-artifact
description: "Use when explicitly invoked with /build, or when the user authorizes creating, editing, implementing, compressing, or materializing the substantive artifact. Do not use when the user only asks for review, comparison, diagnosis, research, or state handoff."
---

# Build Artifact

Command: `/build`  
ID: `uam.build-artifact`  
Version: `0.1.0`  
Status: interim artifact-authoring bridge command  
Evidence ceiling: `design-time` unless post-change verification is run.

## Purpose

Create or change the substantive artifact within the authorized boundary.

`/build` is the artifact-mutation command. It may create, patch, augment, rewrite, implement, shape, compress, or materialize artifacts, but only after the target and action boundary are committed. It must not use artifact creation as a back door for unresolved design, evaluation, comparison, diagnosis, research, or handoff work.

The core question for `/build` is:

```text
What artifact change is authorized, how far may it propagate, what must be preserved, and how will completion be distinguished from verification?
```

## Donor Obligation Ledger

Extract these behaviors from donor resources without copying them one-for-one:

| Donor | Obligations carried into `/build` |
|---|---|
| UAM authoring / artifact boundary | `/build` writes artifacts only; it may record change notes but must not claim review, readiness, diagnosis, comparison, or handoff ownership. |
| `artifact-change` | Proceed only when the target and action boundary are committed or narrowly explicit; apply the smallest sufficient reach; preserve verified strengths; distinguish implementation completion from verification completion. |
| Common governance contract | Do not silently broaden authorized action; classify explicit, entailed, optional, and speculative requirements; treat `No material change needed` as valid. |
| Source authority | Resolve conflicts at the owning source; do not let donor files or adapters override canonical package contracts. |
| Change record template | Report target revision, authorized action, boundary, changed components, preserved elements, tests, residual risk, and next authorized operation. |
| `safe-shrink` / safe-compression lens | Classify load-bearing and ornamental content before cutting; protect verbatim-critical sections; emit a dropped-element ledger and budget status. |
| `house-style-checker` | When matching a standard, derive or load a concrete checkable grammar before applying style; do not replace user standards with generic polish. |
| `spec-builder` | When creating governing specs, include the behavioral spine and flag verbatim-critical sections whose wording must survive compression or later edits. |
| `variant-reconciliation` | When building from multiple drafts, align sections, preserve behavior-bearing wording, do not blend verbatim-critical passages, and keep a rationale ledger. |

## Use When

- The user requests a new artifact.
- The user authorizes modifying an existing artifact.
- A committed design or explicit instruction is ready to implement.
- The user requests safe compression, shaping, patching, augmentation, rewrite, or file materialization.
- The user supplies a target standard and asks to apply it to an artifact.

## Do Not Use When

- The user only wants evaluation.
- Material architecture remains unresolved.
- The task is only to transfer or preserve work state.
- The requested action would overwrite, delete, publish, install, or activate without explicit authorization.
- The user asks to choose between alternatives without authorizing a merged artifact.
- The user asks for current external evidence and the needed evidence has not been gathered.

## Reads

- `work_intent`
- `user_constraints`
- `selected_design`
- `source_artifact`
- `evidence`
- `preservation_requirements`
- `provider_capability_profile`
- `manifest_command_boundaries`

## Writes

- `artifact`: substantive content or files.

Change summaries, validation notes, and residual risks may accompany the artifact, but they do not become independent evidence claims unless verification has actually been performed.

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

Select exactly one primary mode. Use a supporting mode only when required to complete the authorized artifact change, and state why.

| Mode | Use when | Required operations | Output focus |
|---|---|---|---|
| `create` | A new artifact is requested and no existing artifact controls the structure. | Confirm target, audience, constraints, source authority, required skeleton, and deliverable format. | New artifact plus assumptions and verification owed. |
| `patch` | A local defect or named section must change while unnamed components stay stable. | Read the affected section and first-degree dependencies; edit only the named scope; avoid unrelated cleanup. | Minimal corrected artifact or diff. |
| `augment` | The base artifact is sound but needs a new capability or section integrated. | Add the capability and revise only directly connected interfaces; preserve settled architecture. | Integrated addition plus dependency note. |
| `rewrite` | Whole-asset replacement is explicitly authorized or the base is materially defective. | Confirm rewrite authority, preserve load-bearing requirements, rebuild the artifact, and name what was intentionally replaced. | Replacement artifact plus preservation ledger. |
| `implement` | A committed design, specification, or plan must be materialized. | Apply the authorized design without reopening architecture; map design choices to artifact changes. | Implemented artifact plus design-trace note. |
| `shape` | The artifact needs formatting, house style, tone, structure, or presentation changes without changing substance. | Derive or load the target standard, protect meaning, and report governed dimensions touched. | Shaped artifact plus conformance note. |
| `compress` | The artifact must be shorter or fit a budget. | Classify load-bearing versus ornamental content, protect verbatim-critical text, cut to budget when possible, and emit a dropped ledger. | Compressed artifact plus budget and risk ledger. |
| `materialize` | Content must become files or file changes in the workspace. | Confirm intended paths, overwrite authority, provider capability, and verification commands before writing. | Written files or complete not-written fallback contents. |

## Lenses

- `safe-compression`
- `narrative-substance`
- `variant-reconciliation`
- `evidence-ceiling`

## Context Source Priority

Load the smallest context needed for the selected mode, in this order:

1. Current user request and exact explicit `/build` instruction, if any.
2. Target artifact path, current revision, desired output format, and authorized action.
3. User constraints, preservation requirements, exclusions, budget, house style, and stop condition.
4. Selected design, prior work contract, or committed state when implementation depends on it.
5. Current source artifact and directly connected dependencies.
6. `MANIFEST.yaml`, `KERNEL.md`, and command boundaries when editing this package or another governed package.
7. Donor resources or exemplars relevant to the selected mode.
8. Provider capability profile and available verification tools.

If a load-bearing source is unavailable, either ask, proceed with a labeled bounded assumption, or produce a prepare-not-execute artifact. Do not fabricate source authority, tests, or file writes.

## Procedure

1. Confirm target artifact, action, scope, preservation requirements, and authority.
2. Select one primary mode and state any supporting mode.
3. Classify origin posture: `greenfield`, `existing-artifact`, `design-to-implement`, or `multi-source`.
4. Classify transformation reach: `local-correction`, `bounded-addition`, `whole-reconstruction`, `style-only`, or `budget-compression`.
5. Classify realization depth: `compose-content`, `materialize-files`, or `integrate-runtime`.
6. Separate explicit, entailed, optional, and speculative requirements.
7. Load only the context needed for the mode and direct dependencies.
8. Apply the smallest sufficient reach and avoid unrelated cleanup.
9. Preserve verified strengths unless the user authorizes replacement.
10. Protect verbatim-critical sections and behavior-bearing wording.
11. Materialize files only when path, overwrite authority, and provider capability are clear.
12. Run available targeted verification, or label verification as owed.
13. Record what changed, what was preserved, and what verification was performed.

## Mode Procedures

Use only the mode procedure needed for the request. Do not run every procedure by default.

### `create`

Use when the user wants a new artifact and there is no controlling draft.

1. Confirm artifact type, audience, authority, constraints, and success condition.
2. Load any required house grammar, exemplar, source hierarchy, or committed design.
3. Choose the smallest skeleton that carries the required behavior.
4. Create the artifact with optional future ideas clearly separated from required content.
5. Name assumptions and verification still owed.

### `patch`

Use when a named section, file, field, test, or component needs a local correction.

1. Read the target and directly affected neighboring context.
2. Confirm unnamed components must remain stable.
3. Edit only the minimum necessary surface.
4. Do not reformat, rename, reorder, or simplify unrelated material.
5. Verify the changed surface when a targeted check exists.

### `augment`

Use when the artifact is basically sound but missing a capability.

1. Identify the missing capability and why it belongs in the artifact.
2. Add the capability at the owning location.
3. Update only direct first-degree dependencies needed for coherence.
4. Stop if integration requires broader propagation that would amount to rewrite.
5. Report dependency reach and preserved elements.

### `rewrite`

Use only with explicit rewrite authority or when the user has accepted a whole-asset replacement.

1. Confirm rewrite authority and replacement scope.
2. Extract load-bearing requirements, constraints, source authority, and preserved decisions.
3. Rebuild the artifact without preserving accidental structure.
4. Keep intentional safety redundancy and verbatim-critical rules intact unless replacement is authorized.
5. Report what was replaced, what was preserved, and what regression risk remains.

Never hide a rewrite inside a sequence of patches or augments.

### `implement`

Use when a design, plan, or specification has already been committed.

1. Load the committed design and implementation boundary.
2. Map each load-bearing design decision to the target artifact.
3. Apply the design without reopening architecture unless a blocker is exposed.
4. If implementation reveals a design conflict, stop or route back to `/design`.
5. Distinguish implementation completion from post-change verification.

### `shape`

Use for tone, format, house style, presentation, or structural conformance.

1. Derive or load the target standard as a concrete, checkable grammar.
2. Determine whether the change is substance-preserving or substance-changing.
3. Apply style only within the authorized surface.
4. Preserve claims, logic, and user voice unless the user asked to change them.
5. Report governed dimensions confirmed or any standard gaps.

### `compress`

Use when the user gives a size limit, says to shorten, or asks to fit an artifact into a field.

1. Confirm budget type and hard limit, if any.
2. Classify content as load-bearing, ornamental, duplicated, or verbatim-critical.
3. Preserve verbatim-critical sections exactly unless the user authorizes behavioral change.
4. Cut ornamental and duplicated material first.
5. Tighten non-critical load-bearing wording only when meaning remains stable.
6. If the budget is impossible without dropping load-bearing content, stop and offer options with behavioral costs.
7. Emit a dropped-element ledger and residual risk.

### `materialize`

Use when the artifact must be written to files, folders, configs, or generated outputs.

1. Confirm target paths and whether creating, modifying, or overwriting is authorized.
2. Inspect existing files before editing.
3. Use the provider's safe file-editing mechanism.
4. Avoid unrelated filesystem churn.
5. Verify that files were written and content matches the intended artifact.
6. If file writing is unavailable, return complete file contents with intended paths and mark them `not written`.

## Action Gates

Stop or prepare without executing when the requested build would:

- overwrite, delete, publish, install, activate, submit, send, or deploy without action-specific confirmation;
- broaden from patch or augment into rewrite without explicit authority;
- change source authority, manifest ownership, adapter behavior, eval gates, or rollout status beyond the authorized target;
- require current external evidence that has not been gathered;
- claim readiness, correctness, or runtime behavior without verification.

Use this compact gate when needed:

```text
GATE: PREPARE-NOT-EXECUTE
PREVIEW: <artifact or intended change>
BLOCKED ACTION: <overwrite/delete/publish/install/activate/etc.>
CONFIRMATION NEEDED: <specific confirmation required>
```

## Required Output

- Completed artifact or change summary.
- Authorized action and boundary.
- Preservation note.
- Validation performed.
- Unresolved risks.
- Recommended move, route options when real, and approval shorthand when safe.

For material builds, include enough of a change record that a later `/review` or `/handoff` can continue without reconstructing the conversation.

## Output Profiles

### Compact

Use for small, reversible changes:

```text
Changed: <artifact/section>
Boundary: <authorized action and scope>
Preserved: <key stable elements>
Validation: <check run or not run>
Risk: <if any>
Recommended move: <recommended move, route option, approval shorthand, or stop>
```

### Material

Use for multi-file, high-coupling, compression, rewrite, implementation, or file-materialization work:

```text
Artifact
Authorized action and boundary
Change record
Preservation ledger
Verification performed
Verification still owed
Residual risks
Recommended move or separately authorized operation
```

### Compression

Use when the primary mode is `compress`:

```text
COMPRESSED: <artifact>
BUDGET: <count>/<limit> or <not measured>
VERBATIM-CRITICAL: <preserved sections>
DROPPED: <ledger>
RISK: <load-bearing tightening to spot-check>
```

## Provider Degradation

If file writing is unavailable, return complete file contents with intended paths and mark them `not written`.

If code execution or tests are unavailable, complete the artifact change when authorized but label validation as `not run`.

If retrieval is unavailable and the build depends on current external information, route to `/research` or mark the relevant material as unverified.

If durable memory is unavailable, include the preservation and change record in the response rather than relying on session memory.

## Examples

### Patch

Input: `/build Patch the manifest status for build-artifact only.`

Expected behavior:

```text
Changed: MANIFEST.yaml command entry for /build.
Boundary: patch; one manifest field only.
Preserved: other commands, provider profiles, release gates.
Validation: manifest re-read.
Recommended move: stop or /review if readiness is in question.
```

### Augment

Input: `/build Add degradation behavior to this skill, but keep the current mode structure.`

Expected behavior:

```text
Artifact: revised SKILL.md section.
Authorized action: augment.
Dependency reach: provider degradation section and directly related stop conditions.
Preserved: mode names and command boundary.
Verification still owed: run object-integrity/evidence-ceiling cases if available.
```

### Compress

Input: `/build Compress this 9,000-character instruction set to 6,000 characters.`

Expected behavior:

```text
COMPRESSED: <under-budget artifact>
BUDGET: 5,700/6,000 when countable
VERBATIM-CRITICAL: ambiguity gate; action-confirmation gate
DROPPED: redundant examples; restated rationale
RISK: shortened provenance wording should be spot-checked.
```

### Prepare, Do Not Execute

Input: `/build Install these skills globally.`

Expected behavior:

```text
GATE: PREPARE-NOT-EXECUTE
PREVIEW: source package is ready for installation review.
BLOCKED ACTION: global install / activation
CONFIRMATION NEEDED: explicit install authorization and target provider/profile.
```

## Stop Conditions

- Requested artifact is complete.
- Missing authority prevents mutation.
- Unresolved architecture materially changes the build.
- Provider capability prevents materialization and the user has not approved a fallback.
- The safe result is `No material change needed`.
- The next useful step is evaluation, comparison, diagnosis, research, or handoff rather than further artifact mutation.

## Boundary

`/build` owns production artifact and source artifact creation or mutation (`object_subtype: production_artifact` or `source_artifact`). It does not claim readiness, runtime behavior, cross-model parity, diagnose root cause, compare alternatives, gather research evidence, or create handoff packets except as supporting notes.

When `/build` exposes a need for another operation, recommend that operation as the next separately authorized step rather than silently chaining it.
