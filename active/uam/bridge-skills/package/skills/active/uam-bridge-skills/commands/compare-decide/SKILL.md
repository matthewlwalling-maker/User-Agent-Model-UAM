---
name: compare-decide
description: "Use when explicitly invoked with /compare, or when the user asks to compare versions, candidates, donor components, model outputs, or options against a frozen basis. Do not silently merge candidates or rewrite artifacts."
---

# Compare Decide

Command: `/compare`  
ID: `uam.compare-decide`  
Version: `0.1.0`  
Evidence ceiling: `design-time` unless comparative tests are supplied.

## Purpose

Make relative judgment explicit while preserving branch identity, decision criteria, tradeoffs, and evidence limits.

`/compare` decides among alternatives or explains why a single winner is not defensible. It may recommend donor components or a later synthesis, but it must not silently merge, rewrite, or select on vibes.

## Donor Obligation Ledger

Extract these behaviors from donor resources without copying them one-for-one:

| Donor | Obligations carried into `/compare` |
|---|---|
| UAM compare-options placement | Keep comparison distinct from review, diagnosis, build, and handoff; write decision support and evidence, not artifact changes. |
| `version-comparison` | Freeze one objective and criteria before scoring; compare behavioral support, gains, regressions, duplicated behavior, and new risks; preserve non-ranking when the basis is insufficient. |
| `option-ranker` | Use a shared weighted rubric when ranking; enforce hard constraints before preferences; guard against order, recency, and salience bias; name the decisive criterion. |
| `variant-reconciliation` | Align sections or behavioral units; choose load-bearing content per divergence; protect verbatim-critical sections from clause-by-clause blending; produce a rationale ledger. |
| `model-vs-consensus` | Build an independent model before looking at consensus when consensus itself is being judged; state falsifiers, kill conditions, and what would change the decision. |
| `gold-standard` lens | Use a scoped reference basis only when one exists or can be gathered; avoid unqualified frontier or novelty claims. |
| `evidence-ceiling` lens | Keep confidence tied to supplied evidence, tests, retrieval status, and provider capabilities. |

## Use When

- The user provides two or more candidates, versions, options, drafts, models, or donor components.
- A ranking, selection, reconciliation recommendation, or decision matrix is needed.
- The user wants to know what improved, regressed, or should be borrowed.
- The user asks whether a candidate differs from consensus, a baseline, or a gold standard.
- The user needs to preserve branch tradeoffs before choosing a recommended move.

## Do Not Use When

- Criteria are unresolved and cannot be derived without inspecting candidates.
- The user asks to directly implement a merge.
- Only one artifact is being evaluated.
- The task is causal failure diagnosis rather than comparison.
- The user asks for source discovery, live verification, or current facts before a comparison basis exists.
- The user asks for a handoff packet or artifact compression rather than a decision.

## Reads

- `work_intent`
- `candidate_artifacts`
- `frozen_objective`
- `decision_criteria`
- `evidence`
- `provider_capability_profile`
- `baseline_or_consensus`
- `hard_constraints`

## Writes

- `evidence`: comparison basis, scores, tradeoffs, confidence.
- `state`: decision support, selected branch if authorized.

Do not write or revise the candidate artifacts. Do not create a merged artifact. If the user authorizes synthesis or file mutation, route the selected comparison result to `/build`.

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

## Modes

Select exactly one primary mode. Use a supporting mode only when needed and state why.

| Mode | Use when | Primary output |
|---|---|---|
| `delta` | Versions or revisions must be compared against a frozen objective or prior baseline. | Gains, regressions, duplicated behavior, new risks, and rank or non-rank. |
| `rank` | Multiple options must be ordered against shared criteria. | Weighted matrix, ranking, decisive criterion, call. |
| `select` | The user needs one chosen path, candidate, or donor source. | Selection with confidence, decision changers, and excluded alternatives. |
| `reconcile` | Multiple drafts or model outputs should inform one future artifact. | Branch-preserving merge recommendation and rationale ledger. |
| `baseline` | Candidates are being compared to a standard, reference corpus, rubric, or required capability model. | Baseline fit, gaps, correct omissions, and scoped claim. |
| `consensus-check` | An independent view must be compared to consensus, market, majority opinion, or another aggregate. | Independent model, consensus gap, falsifier, and verdict boundary. |

## Lenses

- `gold-standard`
- `variant-reconciliation`
- `evidence-ceiling`
- `capability-first`

## Context Loading

Load the smallest context needed for the selected mode:

1. Current request, exact command, candidate identities, and user-stated goal.
2. Frozen objective, hard constraints, decision criteria, and authorized action.
3. Candidate artifacts or relevant excerpts, preserving source identity and order received.
4. Baseline, consensus, reference corpus, or capability model when the mode requires one.
5. Evidence stage, supplied tests, retrieval status, and provider capability limits.
6. Relevant lenses and donor obligations only after the comparison basis is fixed.

If candidate identity, objective, or decision criteria are missing and cannot be derived safely, stop with the smallest blocking question. If criteria can be derived from the stated objective, state and freeze them before scoring.

## Procedure

1. Select the primary mode and confirm whether comparison, ranking, selection, reconciliation, or non-ranking is the requested outcome.
2. Freeze the objective, criteria, hard constraints, evidence stage, and authority before scoring.
   In compact phrasing: freeze criteria and compare before any merge.
3. Separate hard constraints from preferences. Exclude infeasible candidates before ranking, but do not describe constraint exclusion as merit failure.
4. Evaluate every candidate on the same basis. Compare behavioral support and load-bearing differences, not prose polish or presentation order.
5. Run an anti-anchoring pass: check whether first-seen, most recent, longest, most vivid, or user-favored candidates are being advantaged without evidence.
6. Identify gains, regressions, duplicated behavior, tradeoffs, missing data, and newly introduced risks.
7. Preserve ties, branch-specific winners, and unresolved tradeoffs when one universal winner is not defensible.
8. Name the decisive criterion when a ranking or call is made.
9. Recommend donor components only when compatibility and structural reach are clear.
10. State confidence, falsifiers or decision changers, and what evidence would alter the result.
11. Recommend `/build` for any authorized merge, synthesis, or artifact change.

## Mode Procedures

### `delta`

Use when comparing revisions, proposals, components, or model outputs against a frozen objective.

1. State the frozen objective and required capabilities.
2. Compare each candidate against the same objective, capability by capability.
3. Mark coverage as stronger, weaker, equal, missing, duplicated, incompatible, or unknown.
4. Name meaningful gains and regressions.
5. Rank only when the objective supports a global ranking; otherwise return branch-specific winners.

### `rank`

Use when the user needs an ordered choice among options.

1. Define weighted criteria before scoring.
2. Apply hard constraints first.
3. Score every feasible option on the same scale.
4. Break ties by the highest-weight criterion, then downside risk. If still tied, say so.
5. End with a call such as `select`, `defer`, `reject`, or the user's requested decision frame.

### `select`

Use when the user needs one candidate or path chosen.

1. Confirm selection authority and whether the choice is advisory or committed state.
2. State the minimum acceptable threshold.
3. Choose only if one candidate clears the threshold better than the alternatives.
4. If no candidate clears the threshold, return `defer` or `none selected` with the missing evidence.
5. State what would reopen the decision.

### `reconcile`

Use when variants should inform a later canonical artifact.

1. Align sections, claims, or behavioral units.
2. For each divergence, classify it as same intent/different wording, different behavior, missing coverage, or incompatible premise.
3. Select behavior-bearing content over nicer prose.
4. Select verbatim-critical sections whole rather than blending clause by clause.
5. Emit a rationale ledger and residual conflicts.
6. Stop before writing the merged artifact unless `/build` is separately authorized.

### `baseline`

Use when comparing to a rubric, corpus, gold standard, or required capability model.

1. State the baseline and its source.
2. Label the corpus or standard as supplied, retrieved, or assumed.
3. Compare on frontier dimensions or required capabilities.
4. Separate true gaps from correct omissions.
5. Scope any novelty, readiness, superiority, or parity claim to the evidence checked.

### `consensus-check`

Use when a candidate, model, price, or position is being compared to consensus or an aggregate view.

1. Build or state the independent model before using consensus as an anchor.
2. Compare independent view and consensus on the same terms.
3. Decompose the gap as likely overreaction, real information update, model error, or insufficient evidence.
4. State a falsifier and kill condition for the decision.
5. Avoid financial, legal, medical, or other regulated advice beyond evidence-bounded analysis.

## Required Output

Preserve these functions; exact formatting may vary:

- Frozen comparison basis: objective, criteria, hard constraints, candidates, evidence stage.
- Candidate-by-candidate assessment on the same basis.
- Gains, regressions, tradeoffs, missing data, and risks.
- Ranking, selected branch, reconciliation recommendation, or explicit non-ranking.
- Decisive criterion, when a call is made.
- Donor-component recommendations, when warranted.
- Rationale ledger, when reconciling variants.
- Confidence and evidence limits.
- Falsifier, kill condition, or what would change the decision when commitment risk warrants it.
- Recommended move, route options when real, and approval shorthand when safe.

## Output Profiles

### Compact

Use for low-coupling choices:

```text
Basis: <objective, criteria, evidence stage>
Candidates: <A, B, C>
Decision: <winner, ranking, tie, or defer>
Decisive criterion: <criterion>
Tradeoff: <main cost of the recommendation>
Confidence: <low|medium|high within evidence ceiling>
Recommended move: </build, /research, stop, route option, or other>
```

### Material

Use for consequential, branch-sensitive, or multi-candidate decisions:

```text
Frozen basis
Hard constraints
Criteria and weights
Candidate matrix
Gains and regressions
Tradeoffs and risks
Anti-anchoring check
Decision or non-ranking
Donor components or reconciliation ledger
Evidence limits and confidence
Decision changers
Recommended move
```

## Examples

### Rank options with hard constraints

Input: `/compare Pick the best rollout path: Codex-first, canonical-first, or ChatGPT-first. Do not install anything yet.`

Expected behavior:

```text
Basis: choose a rollout path for source-package work only; no installation authorized.
Hard constraint: path must preserve canonical-source authority and explicit-command pilot posture.
Decision: Codex-first with canonical-source discipline.
Decisive criterion: fastest verifiable local iteration without losing manifest authority.
Tradeoff: cross-model parity evidence arrives later.
Confidence: medium, design-time.
Recommended move: /design or /build for the chosen source-package path, not install.
```

### Reconcile variants without merging

Input: `/compare Reconcile these two skill drafts and tell me what to borrow.`

Expected behavior:

```text
Frozen basis: preserve command boundary, writes, evidence ceiling, and user-facing usability.
Ledger:
- Trigger section: choose Draft B; clearer do-not-use boundary.
- Procedure: hybrid; Draft A has stronger sequencing, Draft B has better stop conditions.
- Authority gate: choose Draft A whole; verbatim-critical.
Residual conflicts: Draft B allows artifact mutation, which violates /compare.
Recommended move: /build can apply the ledger if authorized.
```

## Provider Degradation

If independent or blind contexts are unavailable, do not claim blind or independent comparison.

If retrieval is unavailable, use supplied sources only and label baseline or consensus claims as unverified. If code execution or test access is unavailable, do not claim measured parity or performance. If candidate artifacts cannot be read, compare only provided excerpts and state the resulting ceiling.

## Stop Conditions

- A defensible comparison or non-ranking is complete.
- Missing criteria or candidate identity blocks scoring.
- User authority is needed to select or merge.
- Evidence is insufficient for the requested confidence or consensus claim.
- The next step would mutate artifacts, publish a decision, or collapse branches without authorization.

## Boundary

`/compare` may recommend a synthesis but must not silently create a best-of-both artifact.

It may write decision support and selected state when authorized. It must not rewrite candidate artifacts, perform root-cause diagnosis, gather new external evidence as the main task, or create handoff packets.
