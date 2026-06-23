---
name: review-work
description: "Use when explicitly invoked with /review, or when the user asks whether an artifact, design, plan, implementation, claim, eval, or handoff is correct, complete, effective, safe, or ready. Default read-only; do not mutate the artifact."
---

# Review Work

Command: `/review`
ID: `uam.review-work`
Version: `0.1.0`
Status: interim evidence-writing bridge command
Evidence ceiling: `design-time` unless supplied tests, evals, or runtime observations support a stronger claim.

## Purpose

Evaluate work without silently changing it.

`/review` is the read-only evaluation command. It may assess completeness, quality, regression risk, adversarial failure modes, evidence limits, or readiness, but it writes findings and evidence only. It must not mutate the reviewed artifact, merge alternatives, diagnose a full root cause beyond the observed review mechanism, gather new external research, or create a handoff packet unless the user separately authorizes another operation.

The core question for `/review` is:

```text
Against what frozen basis does this target succeed or fail, what evidence supports that verdict, and what must change before a stronger claim is allowed?
```

## Donor Obligation Ledger

Extract these behaviors from donor resources without copying them one-for-one:

| Donor | Obligations carried into `/review` |
|---|---|
| UAM evaluate-artifact boundary | `/review` writes evidence only; it recommends fixes but does not implement them. |
| `architecture-assessment` | Derive the required capability model from the target goal; assess behavior, not headings; classify coverage; locate gaps at the owning layer. |
| `adversarial-evaluation` | Freeze target, basis, fixtures, and evidence stage before scoring; separate observed failures from speculative diagnosis; preserve raw evidence when running evals. |
| `deployment-readiness` | Treat absent evidence as unverified; issue Green, Yellow, Red, or Blocked only within the required gate and evidence stage. |
| `blind-grader` | Lead with the binding verdict; grade against purpose and audience; name specific failure modes; do not invent flaws. |
| `break-it-tester` | Seek failure cases, tag criticality, protect against release overclaim, and make pass/fail criteria observable. |
| Common governance contract | Separate explicit, entailed, optional, and speculative requirements; preserve strengths; use smallest sufficient review depth; treat `No material change needed` as valid. |
| Evidence-ceiling lens | Never convert design-time plausibility into runtime, parity, production, or readiness evidence. |

## Use When

- The user explicitly invokes `/review`.
- The user asks to assess, critique, validate, pressure-test, grade, audit, gate, or check readiness.
- The task is to identify gaps, risks, regressions, evidence limits, or verification owed.
- A completed artifact needs review before build, deployment, handoff, or acceptance.
- The user asks whether a claim is supported by the available evidence.

## Do Not Use When

- The user has authorized creating or modifying the artifact as the primary task.
- The task is to choose among multiple candidates rather than assess one target.
- The task is to explain an observed failure mechanism in depth.
- The user needs current source discovery or external evidence gathering before judgment.
- The user wants a state packet for another session or model.
- The right answer is a simple direct confirmation with no material review risk.

## Reads

- `work_intent`
- `user_constraints`
- `target_artifact`
- `goals_or_criteria`
- `evidence`
- `source_revisions`
- `provider_capability_profile`
- `manifest_command_boundaries`

## Writes

- `evidence`: verdict, findings, coverage, limits, verification owed, and recommended move.

Do not write or revise the target artifact. Do not create state commitments except the minimal review basis needed to explain the evidence. Do not create packets.

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

Select exactly one primary mode. Use a supporting mode only when needed to complete the review and state why.

| Mode | Use when | Required operations | Output focus |
|---|---|---|---|
| `completeness` | The target may be missing required capabilities, sections, constraints, or edge cases. | Freeze objective, derive capability model, map coverage, classify gaps. | Coverage verdict and fix layer. |
| `quality` | The target exists but may be weak, unclear, unfit for audience, or below standard. | Select fit-for-purpose vectors, grade binding constraints, preserve strengths. | Verdict-first critique and exact findings. |
| `adversarial` | The user wants pressure-testing, red-team review, or failure-seeking eval design. | Derive traps, criticality, prohibited behavior, scoring rule, and evidence needed. | Failure case bank or adversarial findings. |
| `regression` | A changed artifact may have lost prior behavior or violated preservation requirements. | Compare to frozen prior basis, identify behavior-bearing deltas, separate intentional from accidental changes. | Regression findings and preservation risks. |
| `readiness` | The user asks whether something is ready to ship, deploy, pilot, release, or rely on. | Verify gates, evidence stage, unverified dependencies, residual risks, and advancement conditions. | Green/Yellow/Red/Blocked gate decision. |
| `evidence` | The main question is whether a claim is supported by the available sources, tests, or observations. | Map claims to evidence, assign claim ceilings, name missing verification. | Supported, unsupported, overclaimed, or unresolved claims. |
| `blind-grade` | The user wants a score, grade, independent critique posture, or "how good is this?" | Hide authorship preference, score vectors against purpose, let binding flaw determine grade. | Grade, vector scores, ship/hold line. |

## Lenses

- `blind-grading`
- `break-it-testing`
- `evidence-ceiling`
- `capability-first`
- `premortem`

Use lenses only when they add expected value. Do not let a review become a full eval-suite build, root-cause diagnosis, or implementation plan unless the user separately routes there.

## Context Source Priority

Load the smallest context needed for the selected mode, in this order:

1. Current user request and exact explicit `/review` instruction, if any.
2. Target artifact, source revision, supplied criteria, and requested claim.
3. User constraints, audience, success standard, preservation requirements, and stop condition.
4. Available evidence: tests, eval records, logs, citations, prior review basis, or runtime observations.
5. `MANIFEST.yaml`, `KERNEL.md`, and command boundaries when reviewing this package or another governed package.
6. Relevant prior artifact version when reviewing regressions.
7. Donor resources or lenses relevant to the selected review mode.
8. Provider capability profile and known degradation limits.

If the target, criteria, or evidence basis is unavailable and guessing would materially change the verdict, ask or return `Blocked`. Do not invent a standard, source revision, or test result.

## Procedure

1. Confirm target, source revision if material, authorized action, evidence stage, objective, and criteria.
2. Select one primary mode and the smallest review depth that can detect material error.
3. Freeze the review basis before judging: target, goal, criteria, evidence, constraints, and claim ceiling.
4. Separate explicit, entailed, optional, and speculative requirements.
5. Derive the required behavior or gate model before assessing existing sections.
6. Evaluate behavior against requirements, not headings, polish, intent, or author confidence.
7. Classify coverage as `sufficient`, `partial`, `nominal-but-ineffective`, `absent`, `misplaced`, `duplicated`, or `unknown-insufficient-evidence`.
8. Identify material findings, strengths to preserve, evidence limits, and correct fix location.
9. Separate severity from confidence.
10. Issue a verdict within the evidence ceiling.
11. Recommend the move, route options, or stop condition without applying the fix.
12. Stop when findings are sufficient or the requested claim exceeds available evidence.

## Mode Procedures

Use only the mode procedure needed for the request.

### `completeness`

Use when the target may not cover the job it claims to do.

1. Derive a required capability model from explicit and entailed requirements.
2. Map actual behavior to each capability.
3. Classify every material requirement as sufficient, partial, nominal-but-ineffective, absent, misplaced, duplicated, or unknown.
4. Preserve strengths that carry real behavior.
5. Name only material gaps and the owning fix layer.
6. State whether the target is complete enough for its stage.

### `quality`

Use when the target exists but its fitness is uncertain.

1. Identify artifact class, audience, and purpose.
2. Choose three to five fit-for-purpose review vectors.
3. Score or judge each vector against a named failure mode.
4. Let the binding constraint set the verdict.
5. Provide exact recommended edits or fix targets, but do not perform them.
6. Stop if no material change is needed.

### `adversarial`

Use when the review must seek failure rather than confirmation.

1. Map the target surface: promises, boundaries, claims, and interfaces.
2. Create or apply failure-seeking cases with hidden trap, required behavior, prohibited behavior, and scoring rule.
3. Tag criticality where a failure would block release or use.
4. State whether the cases were only designed, statically checked, simulated, or run.
5. Preserve failed cases and limitations without repairing the target.
6. Recommend `/diagnose` for root-cause analysis or `/build` for authorized fixes.

### `regression`

Use when a new version may have lost old behavior.

1. Freeze the prior version, current version, and preservation requirements.
2. Compare behavior-bearing content before prose polish.
3. Separate intentional changes from accidental losses and unknown deltas.
4. Identify regressions, improvements, neutral changes, and areas needing test evidence.
5. Name the smallest fix layer.
6. Do not merge or patch versions during the review.

### `readiness`

Use when the user asks for a gate decision.

1. Identify required gates and required evidence stage.
2. Verify which gates have evidence at that stage.
3. Treat missing evidence as unverified, not positive.
4. Issue exactly one decision:
   - `Green`: all required gates verified at the required stage.
   - `Yellow`: usable with named limitations and bounded residual risk.
   - `Red`: a material gate failed.
   - `Blocked`: required evidence or dependency is unavailable.
5. State advancement conditions and next responsible operation.
6. Never issue `Green` from design-time plausibility when runtime, parity, production, or post-implementation evidence is required.

### `evidence`

Use when the main question is claim support.

1. List the claims being reviewed.
2. Map each claim to supplied evidence or mark evidence absent.
3. Assign the maximum justified claim stage.
4. Flag unsupported, stale, contradictory, or overclaimed statements.
5. State what verification would upgrade the claim.
6. Avoid new research unless separately routed to `/research`.

### `blind-grade`

Use when the user wants a grade or critique posture.

1. Grade against purpose and audience, not the author's identity or effort.
2. Lead with the grade or verdict.
3. Score the selected vectors with one-line evidence.
4. Do not invent a flaw when the work is sound.
5. Provide ranked exact fix recommendations.
6. End with a ship, ship-with-fixes, hold, or back-to-bench line.

## Action Gates

Stop or route instead of reviewing when:

- the target artifact is missing;
- criteria are required and unavailable;
- the user asks for current external facts that have not been gathered;
- the user asks to review and fix but mutation authority is ambiguous;
- the requested verdict requires tests, runtime observations, independent graders, or cross-model evidence that are unavailable;
- the review would require changing manifest authority, rollout status, adapter behavior, eval gates, or deployment posture beyond the authorized target.

Use this compact gate when needed:

```text
GATE: ASK
ASK: <one focused question about target, criteria, evidence, or authority>
```

Use this for claim overreach:

```text
GATE: BLOCKED
BLOCKED CLAIM: <claim requested>
AVAILABLE EVIDENCE: <stage and source>
VERIFICATION NEEDED: <test, eval, runtime run, source check, or independent review>
```

If the user asks "review and fix," default to read-only review first and recommend `/build` for authorized patches unless they explicitly authorize mutation.

## Required Output

- Verdict.
- Review basis: target, criteria, evidence stage, and assumptions.
- Material findings, ordered by severity.
- Strengths to preserve, when material.
- Failure or value mechanism.
- Evidence limits and claim ceiling.
- Correct fix location.
- Recommended move, route options when real, and approval shorthand when safe.
- Stop or verification condition.

For material reviews, include enough of the frozen basis and evidence limits that a later `/build`, `/diagnose`, or `/handoff` can continue without reconstructing the conversation.

## Output Profiles

### Compact

Use for small, low-coupling reviews:

```text
Verdict: <sufficient / issues found / blocked / no material change needed>
Basis: <target, criteria, evidence stage>
Findings: <ranked material points>
Evidence limit: <claim ceiling>
Recommended move: <stop, /build, /diagnose, /research, /compare, verification, or route option>
```

### Material

Use for high-coupling, readiness, regression, adversarial, or governed artifact reviews:

```text
Verdict
Frozen basis
Coverage or vector assessment
Material findings
Strengths to preserve
Evidence limits
Correct fix layer
Recommended move
Stop or verification condition
```

### Readiness Gate

Use when the primary mode is `readiness`:

```text
DECISION: <Green | Yellow | Red | Blocked>
REQUIRED STAGE: <design-time | simulated | live-runtime | post-implementation | production-observed>
VERIFIED GATES: <gates with evidence>
FAILED OR UNVERIFIED: <gates without sufficient evidence>
LIMITATIONS: <named limits>
ADVANCEMENT CONDITIONS: <exact conditions>
RECOMMENDED MOVE: <usually /build, /diagnose, /research, or stop>
```

## Provider Degradation

If runtime or test execution is unavailable, limit claims to design-time or supplied evidence and name the tests required for stronger evidence.

If code execution is unavailable, do not claim executed validation; report only static review or supplied test evidence.

If retrieval is unavailable and the review depends on current external facts, route to `/research` or return a blocked evidence statement.

If file reading is unavailable, review only supplied excerpts and mark coverage as unknown outside those excerpts.

If isolated or blind evaluation is unavailable, do not claim blind or independent review.

If durable memory is unavailable, include the frozen basis and evidence limits in the response rather than relying on session memory.

## Examples

### Read-Only Review Before Fix

Input: `/review Review this and fix it if needed.`

Expected behavior:

```text
Verdict: issues found, but mutation is not authorized under /review.
Basis: supplied artifact, stated goal, design-time review.
Findings: <ranked findings>
Recommended move: /build patch after explicit authorization.
```

### Readiness Gate

Input: `/review readiness Can we call v1 ready from these design docs?`

Expected behavior:

```text
DECISION: Blocked
REQUIRED STAGE: post-implementation plus eval evidence for v1 gates
FAILED OR UNVERIFIED: routing, object integrity, degradation, overactivation, cross-model parity
LIMITATIONS: design-time documents do not prove runtime behavior.
RECOMMENDED MOVE: run required evals before readiness claim.
```

### No Material Change Needed

Input: `/review This compact handoff packet against the agreed packet fields.`

Expected behavior:

```text
Verdict: no material change needed.
Basis: supplied packet, agreed fields, design-time review.
Strengths: state, artifact refs, evidence, unresolved questions, and next action remain separate.
Evidence limit: content completeness only; no runtime handoff behavior observed.
Recommended move: stop.
```

### Adversarial Eval Design

Input: `/review adversarial Design cases to break this skill.`

Expected behavior:

```text
Verdict: eval cases designed, not run.
Cases: hidden trap, required behavior, prohibited behavior, scoring rule, criticality.
Evidence limit: design-time case quality only.
Recommended move: run cases before claiming behavior.
```

## Stop Conditions

- The verdict and material findings are sufficient for the requested review.
- Missing target, criteria, source revision, or evidence blocks a meaningful verdict.
- The requested claim exceeds available evidence.
- The safe result is `No material change needed`.
- The next useful step is artifact mutation, source gathering, diagnosis, comparison, or handoff rather than further review.

## Boundary

`/review` writes findings and evidence. It may recommend `/build`, `/diagnose`, `/research`, `/compare`, or `/handoff`, but it must not perform those operations unless the user separately continues with clear authority.

It must not modify the reviewed artifact unless the user explicitly converts the work to `/build`.

When `/review` exposes a needed fix, it should identify the smallest correct fix layer and stop before changing the artifact.
