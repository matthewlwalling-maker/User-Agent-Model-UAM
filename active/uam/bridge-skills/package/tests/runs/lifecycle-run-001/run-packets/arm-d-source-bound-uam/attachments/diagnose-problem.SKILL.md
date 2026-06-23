---
name: diagnose-problem
description: "Use when explicitly invoked with /diagnose, or when the user provides an observed failure, recurring miss, suspicious behavior, premortem request, or asks where the remedy belongs. Do not silently implement the remedy."
---

# Diagnose Problem

Command: `/diagnose`  
ID: `uam.diagnose-problem`  
Version: `0.1.0`  
Evidence ceiling: `design-time` for hypotheses; higher only with supplied observations, eval results, tests, logs, or runtime evidence.

## Purpose

Explain why something failed or is likely to fail, then place the remedy at the correct layer without silently applying it.

`/diagnose` writes causal evidence and recovery state. It may identify a patch target, regression test, or build route, but it must not repair the artifact, rewrite a skill, rerun a test suite, install anything, or change deployment posture unless the user separately authorizes another operation.

The core question for `/diagnose` is:

```text
What was expected, what was observed, what failure mechanism best explains the gap, and where must the smallest remedy live?
```

## Donor Obligation Ledger

Extract these behaviors from donor resources without copying them one-for-one:

| Donor | Obligations carried into `/diagnose` |
|---|---|
| UAM diagnose-failure boundary | Diagnose the failure mechanism and fix layer; write evidence and recovery state, not repairs. |
| `failure-triage` | Require or mark missing observed behavior, exact invocation, raw output/error, target revision, evidence stage, and authorized action; separate observation from interpretation. |
| Agent Builder assessment contract | State severity and confidence separately; place the remedy at the originating layer; choose the smallest sufficient structural reach. |
| AB6 failure-triage registry | Treat anchoring, over-expansion, incorrect tiering, false coverage, evidence overclaim, action misrouting, wrong-layer remedy, regression, and failure to stop as first-class diagnostic classes. |
| AB7 calibration boundary | Diagnose clarification burden, interface friction, and stop-condition burden only when actual burden or interaction evidence is supplied. |
| `break-it-tester` / adversarial eval | Use failure-seeking reproduction cases when needed; preserve hidden trap, required behavior, prohibited behavior, and scoring rule. |
| `steelman-premortem` | For likely future failures, state the decision, strongest opposing case, likely failure causes, simpler version, and observable kill condition. |
| Evidence-ceiling lens | Do not claim systemic, runtime, parity, or production behavior from one ambiguous miss or design-time review. |

## Use When

- The user explicitly invokes `/diagnose`.
- The user provides an observed failure, raw output, error, misfire, regression, or repeated behavior.
- The user asks for root cause, fix layer, impact, recovery plan, regression verification, or "why did this happen?"
- A review, eval, test, or runtime run found a failure that needs causal classification.
- The user requests a premortem or asks how a plan, artifact, skill, workflow, or deployment is most likely to fail.
- The user asks whether a remedy belongs in kernel/router, skill procedure, lens, resource, adapter, eval, governance, interface, runtime/tooling, or artifact content.

## Do Not Use When

- The user asks only to edit, implement, compress, or materialize the artifact.
- The issue is choosing among alternatives rather than explaining a failure mechanism.
- The user wants an ordinary quality/readiness review and no failure mechanism is in question.
- The user asks only for current source-backed research.
- The user needs an eval suite designed or run as the primary deliverable.
- The user has not supplied observations and wants a runtime or systemic diagnosis rather than a design-time hypothesis.
- The safe next step is a simple direct answer with no material causal uncertainty.

## Reads

- `work_intent`
- `user_constraints`
- `observed_behavior`
- `expected_behavior`
- `exact_prompt_or_invocation`
- `target_revision`
- `raw_output_or_error`
- `evidence`
- `eval_or_test_result`
- `provider_capability_profile`
- `manifest_command_boundaries`

## Writes

- `evidence`: observed symptom, expected behavior, causal model, confidence, uncertainty, severity, and verification owed.
- `state`: recovery recommendation, fix-layer placement, structural reach, and recommended move.

Do not write or revise artifacts. Do not create a merged decision, research brief, eval record, or handoff packet except as a separately authorized operation.

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

Select exactly one primary mode. Use a supporting mode only when needed to complete the diagnosis and state why.

| Mode | Use when | Required operations | Output focus |
|---|---|---|---|
| `triage` | The failure is fresh, incomplete, or needs initial classification. | Reconstruct expected behavior, separate observation from interpretation, classify likely mechanism. | Symptom, likely class, evidence gaps, next observation. |
| `root-cause` | Enough evidence exists to explain why the failure happened. | Compare expected vs observed behavior, test alternatives, choose cause with confidence. | Most likely cause, alternatives, supporting evidence. |
| `premortem` | The failure has not happened but a consequential choice needs disconfirmation. | Steelman the opposing case, rank likely future failures, define kill condition. | Failure forecast and tripwire. |
| `fix-layer` | The main risk is applying the remedy in the wrong place. | Trace origin across kernel/router, skill, lens, resource, adapter, eval, governance, interface, runtime, or artifact. | Correct owner and smallest structural reach. |
| `impact` | The user needs consequence, severity, blast radius, or release impact. | Separate local from systemic evidence, scope affected objects and claims. | Severity, affected surfaces, advancement limits. |
| `recovery` | The user needs a repair path but has not authorized mutation. | Name smallest remedy, regression verification, owner, and recommended move. | Recovery plan without implementation. |
| `calibration` | The observed issue is clarification burden, overactivation, interface friction, or failure to stop. | Require actual interaction/burden evidence; distinguish usability friction from procedural failure. | Calibration fix layer and burden reduction check. |

## Lenses

- `premortem`
- `break-it-testing`
- `evidence-ceiling`
- `capability-first`

Use lenses only when they add expected value. `/diagnose` may borrow adversarial cases to reproduce a failure or premortem logic to forecast one, but it must not become `/review` eval design, `/build` implementation, `/compare` selection, or `/research` source discovery.

## Context Source Priority

Load the smallest context needed for the selected mode, in this order:

1. Current user request and exact explicit `/diagnose` instruction, if any.
2. Observed behavior, expected behavior, raw output/error, exact prompt/invocation, target revision, and supplied evidence.
3. User constraints, authorized action, stop condition, and requested claim.
4. Relevant governing contract: `MANIFEST.yaml`, `KERNEL.md`, current skill/lens boundaries, eval fixture, test expectation, or artifact spec.
5. Prior version or baseline when diagnosing regression.
6. Provider capability profile and known degradation limits.
7. Donor resources or lenses relevant to the selected diagnostic mode.

If the expected behavior or observation is unavailable and guessing would materially change the diagnosis, ask for the missing source or return a bounded hypothesis. Do not turn missing observation into a confident cause.

## Procedure

1. Confirm target, expected behavior, observed behavior, evidence stage, authorized action, and object boundary.
2. Select one primary mode and the smallest diagnostic depth that can prevent the wrong remedy.
3. Reconstruct expected behavior from the governing contract, stated goal, eval case, or target spec.
4. Separate observation from interpretation. Quote or summarize raw behavior separately from inferred cause.
5. Identify the gap between expected and observed behavior.
6. Classify the likely failure mechanism.
7. Test alternative causes and state what evidence would distinguish them.
8. Identify the originating fix layer: kernel/router, skill procedure, lens, resource/source map, adapter/provider profile, eval harness, governance/deployment, interface/output, runtime/tooling, or artifact content.
9. State severity and confidence separately.
10. Distinguish local evidence from systemic evidence. One ambiguous miss is not systemic.
11. Recommend the smallest sufficient recovery and structural reach: no change, patch, augment, rewrite, retest, reroute, or collect more evidence.
12. Name the exact verification owed after any implementation.
13. Hand implementation to `/build`, source gathering to `/research`, eval design or readiness judgment to `/review`, or option selection to `/compare` when needed.

## Mode Procedures

### `triage`

Use when the available evidence is messy, partial, or fresh.

1. State the observed symptom in neutral terms.
2. State the expected behavior and source of that expectation.
3. List missing diagnostic inputs only if they materially affect cause or remedy.
4. Classify the initial failure class with low, medium, or high confidence.
5. Name the next observation that would confirm or reject the diagnosis.
6. Stop before prescribing a broad fix when the evidence only supports triage.

### `root-cause`

Use when the user needs the most likely cause.

1. Build a cause map with the most likely cause and plausible alternatives.
2. For each cause, tie evidence to the specific observed behavior.
3. Reject causes that do not explain the symptom or require unsupported assumptions.
4. Avoid defaulting to the core prompt, kernel, or user error when the origin is elsewhere.
5. State confidence and uncertainty without false precision.
6. Recommend the smallest fix layer and verification owed.

### `premortem`

Use when the failure is prospective rather than observed.

1. Restate the decision, plan, artifact, or deployment being committed.
2. Steelman the strongest case that it is wrong or premature.
3. Assume it failed and rank the likely failure causes.
4. Identify the premise most likely to be false.
5. Name the simpler version and what it sacrifices.
6. Define an observable kill condition or revisit trigger.
7. Label the output as design-time forecast, not observed failure evidence.

### `fix-layer`

Use when the main diagnostic value is preventing a wrong-layer remedy.

1. Trace where the failure originates, not where it was discovered.
2. Check each plausible layer: kernel/router, skill procedure, lens, resource/source map, adapter/provider profile, eval harness, governance/deployment, interface/output, runtime/tooling, and artifact content.
3. Place the fix at the first layer that can remove the cause without broader drift.
4. Preserve verified strengths and avoid rewriting unaffected layers.
5. State structural reach and why a broader rewrite is not yet warranted, when applicable.

### `impact`

Use when the user needs consequence or blast radius.

1. Identify affected command, artifact, adapter, eval, claim, or user workflow.
2. Separate local failure from systemic pattern.
3. State severity as consequence if unaddressed.
4. State release, readiness, evidence, or rollout implications within the available evidence.
5. Name what additional failures would upgrade the diagnosis from local to systemic.

### `recovery`

Use when the user needs the next repair path but mutation is not authorized.

1. State the smallest sufficient recovery.
2. Name the owner and recommended move, usually `/build` for artifact mutation or `/review` for eval verification.
3. Include a regression check that would catch the same failure again.
4. Include a stop condition if no material change is needed.
5. Do not apply the remedy under `/diagnose`.

### `calibration`

Use when the problem is burden, friction, overactivation, excessive clarification, or stop behavior.

1. Require actual burden, clarification, interface, or stop-condition evidence.
2. Distinguish a procedural failure from user-experience friction.
3. Identify whether the fix belongs in kernel scaling, skill trigger text, output profile, interface, or provider adapter.
4. State the burden reduction expected and the regression risk.
5. Verify later with overactivation, degradation, or interaction cases.

## Failure Class Reference

Use these classes when they fit, and name a more specific class when they do not:

- `anchoring`: the response overfit the supplied artifact, first option, or visible section labels.
- `over-expansion`: the response added speculative requirements or unnecessary process.
- `incorrect-tiering`: optional, speculative, or adjacent ideas were treated as required.
- `false-coverage`: a heading, label, or mention was treated as effective behavior.
- `evidence-overclaim`: the response claimed beyond the evidence stage.
- `action-misrouting`: the wrong command, owner, or recommended move was selected.
- `wrong-layer-remedy`: the fix was placed where the issue surfaced rather than where it originates.
- `regression`: prior required behavior was lost or weakened.
- `overactivation`: a heavy process ran for a simple, reversible request.
- `excessive-clarification`: the agent asked when a bounded assumption would suffice.
- `interface-friction`: output shape, prompt surface, or tool flow created avoidable burden.
- `failure-to-stop`: the agent manufactured work after a sufficient answer or no-material-change result.
- `tooling-or-runtime`: the observed issue depends on unavailable, failing, or misused tools.
- `artifact-content`: the source artifact itself lacks or contradicts required behavior.

## Action Gates

Stop or route instead of diagnosing when:

- the target or observed behavior is missing and cannot be inferred safely;
- the user asks for a fix but mutation authority is not present;
- the user asks for current external facts needed to explain the failure;
- the requested diagnosis requires runtime, logs, tests, or provider observations that are unavailable;
- the diagnosis would require changing manifest authority, rollout status, adapter behavior, eval gates, or deployment posture beyond the authorized target.

Use this compact gate when needed:

```text
GATE: ASK
ASK: <one focused question about observation, expected behavior, target revision, or authority>
```

Use this for hypothesis-only work:

```text
GATE: HYPOTHESIS
AVAILABLE EVIDENCE: <stage and sources>
HYPOTHESIS: <bounded causal model>
OBSERVATION NEEDED: <exact evidence that would confirm or reject it>
```

Use this for unauthorized repair:

```text
GATE: ROUTE
DIAGNOSIS: <cause and fix layer>
BLOCKED ACTION: patch / rewrite / retest / install / deploy
RECOMMENDED MOVE: /build, /review, /research, or /compare after authorization
```

## Required Output

Preserve these functions; exact formatting may vary:

- Observed symptom.
- Expected behavior and source.
- Most likely cause.
- Alternative causes.
- Root-cause class.
- Evidence and uncertainty.
- Severity and confidence, stated separately.
- Correct remedy layer and structural reach.
- Smallest sufficient recovery.
- Verification or regression check owed.
- Recommended move, route options when real, and approval shorthand when safe.
- Stop, revisit, or missing-observation condition.

For material diagnoses, include enough of the frozen basis, raw observation, evidence limit, and remedy layer that a later `/build`, `/review`, or `/handoff` can continue without reconstructing the conversation.

## Output Profiles

### Compact

Use for low-coupling or single-symptom diagnoses:

```text
Symptom: <observed behavior>
Expected: <source of expected behavior>
Cause: <most likely class and reason>
Fix layer: <owning layer>
Severity: <low|medium|high>; Confidence: <low|medium|high>
Recovery: <smallest sufficient next step>
Verification: <check owed>
```

### Material

Use for repeated failures, release-impacting failures, regressions, or wrong-layer risk:

```text
Frozen basis
Observed vs expected behavior
Cause map
Failure class
Severity and confidence
Local vs systemic evidence
Correct fix layer and structural reach
Recovery plan
Regression verification
Evidence limits
Recommended move
Stop or revisit trigger
```

### Premortem

Use when the failure has not happened:

```text
Decision
Steelman against
Likely failure causes
False-premise candidate
Simpler version
Kill condition
Net: proceed / proceed-with-tripwire / reconsider
Evidence limit: design-time forecast
```

## Provider Degradation

If logs, test output, or raw runtime traces are unavailable, limit the result to design-time or supplied-evidence hypotheses and name the observation needed.

If file reading is unavailable, diagnose only supplied excerpts and mark source coverage as unknown outside those excerpts.

If code execution is unavailable, do not claim reproduction or retest; provide a static reproduction plan or expected regression check.

If retrieval is unavailable and current external facts are needed, route to `/research` or state the exact sources required.

If provider capability is uncertain, treat capability-caused failures as hypotheses until the profile is verified.

If durable memory is unavailable, restate the frozen basis and evidence limit in the response rather than relying on session memory.

## Examples

### Observed Object-Boundary Failure

Input: `/diagnose The review found a defect and rewrote the file immediately. What failed?`

Expected behavior:

```text
Symptom: `/review` mutated the artifact after identifying a defect.
Expected: `/review` writes evidence only and routes fixes to `/build`.
Cause: action-misrouting with object-boundary drift.
Fix layer: review skill procedure or router boundary text, not the artifact content.
Severity: high for governed package integrity; Confidence: medium if only one output is supplied.
Recovery: patch the owning boundary text after authorization.
Verification: object-integrity case where "review and fix" does not mutate under `/review`.
```

### Wrong-Layer Remedy

Input: `/diagnose This skill failed a missing-resource case. Should we change the kernel?`

Expected behavior:

```text
Cause: likely wrong-layer risk.
Fix layer: resource/source map if the procedure is sound but lacks a required reference; not kernel by default.
Recovery: add or route the missing resource through `/build` after confirming the target path.
Verification: rerun the missing-resource case and a kernel-boundary regression.
```

### Premortem

Input: `/diagnose premortem: enabling broad implicit routing after these design docs.`

Expected behavior:

```text
Decision: enable broad implicit routing from design-time docs.
Steelman against: routing behavior is unobserved across providers; false positives could add ceremony and boundary drift.
Likely failure causes: overactivation, action misrouting, evidence overclaim, adapter capability drift.
Kill condition: any critical routing/object-integrity failure in simulated or live pilot evals.
Net: reconsider or proceed only with explicit-command pilot.
Evidence limit: design-time forecast.
```

### Hypothesis Only

Input: `/diagnose Why did the model ignore the handoff packet?`

Expected behavior:

```text
GATE: HYPOTHESIS
AVAILABLE EVIDENCE: no raw prompt, packet, target model, or output supplied.
HYPOTHESIS: possible context placement, instruction conflict, packet incompleteness, or provider capability mismatch.
OBSERVATION NEEDED: exact packet, invocation, model/provider, and raw output.
```

## Stop Conditions

- The failure mechanism, fix layer, recovery plan, and verification owed are clear.
- Evidence is insufficient and the required observations are named.
- User authority is required to apply a remedy.
- The safe result is `No material change needed`.
- The next useful step is artifact mutation, source gathering, eval design, comparison, or handoff rather than further diagnosis.

## Boundary

`/diagnose` can recommend fixes. It does not patch, rewrite, retest, install, deploy, update manifest status, mutate adapters, or claim readiness unless the user explicitly authorizes another operation.

Hand implementation to `/build` when mutation is needed. Hand eval design or readiness judgment to `/review`, current source gathering to `/research`, and alternative selection to `/compare`.

When `/diagnose` identifies a likely fix, it should identify the smallest correct fix layer and stop before changing the artifact.
