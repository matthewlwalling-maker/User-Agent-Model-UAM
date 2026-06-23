---
name: research-evidence
description: "Use when explicitly invoked with /research, or when current, external, primary-source, or supplied-evidence verification is required. Degrade honestly when retrieval is unavailable. Do not make unsupported truth claims."
---

# Research Evidence

Command: `/research`  
ID: `uam.research-evidence`  
Version: `0.1.0`  
Status: interim evidence-plane bridge command  
Evidence ceiling: source-dependent; default is `design-time` for synthesis over supplied sources.

## Purpose

Gather, verify, and synthesize evidence while distinguishing source claims, observations, inference, and uncertainty.

`/research` exists because bridge users often need current or source-grounded facts before design, build, review, comparison, or diagnosis can proceed safely. It produces evidence records and claim limits. It does not update plans, mutate artifacts, choose between options, diagnose failures, or create continuation packets unless the user separately authorizes the owning command.

The core question for `/research` is:

```text
What claim needs support, which sources can support it, what is actually verified, and what remains unverified?
```

## Donor Obligation Ledger

Extract these behaviors from donor resources without copying them one-for-one:

| Donor | Obligations carried into `/research` |
|---|---|
| UAM evidence contract | Evidence is a scoped record supporting, contradicting, or limiting claims; model inference is not observed evidence. |
| UAM source-provisioning rule | A bare citation is not enough when the next consumer must rely on source content; provide source content, loadable references, or label the gap. |
| Source authority reference | Resolve conflicts at the owning source and distinguish deployed authority, experimental material, and design-time evidence. |
| Deployment readiness | Treat absent evidence as unverified, not positive; never upgrade readiness or capability claims from plausibility alone. |
| Adversarial evaluation | Preserve exact evidence stage, inputs, raw observations, errors, retries, and limitations when research supports tests or evals. |
| `model-vs-consensus` | For current markets, future events, or consensus-dependent facts, fetch or require current data; do not assert settled outcomes from stale data. |
| `variant-reconciliation` | When sources disagree, preserve the contradiction and decide only at the proper authority layer; do not average disagreement into false certainty. |
| `evidence-ceiling` lens | State permitted claims, prohibited claims, and verification needed to upgrade. |

## Use When

- The user asks to find, verify, update, fact-check, or source-map information.
- Current information may change the answer.
- Provider capability assumptions, platform docs, laws, prices, schedules, or other unstable facts matter.
- Supplied evidence must be assessed without live retrieval.
- A downstream design, build, review, comparison, diagnosis, or handoff depends on source authority or claim support.
- Sources disagree and the work needs a contradiction-preserving evidence brief.

## Do Not Use When

- The user only wants artifact creation from already-supplied facts.
- The task is a design decision that does not require external evidence.
- The task is review, comparison, diagnosis, or handoff with no research need.
- The user asks for legal, medical, financial, safety, or policy advice and the available sources are insufficient for the requested claim.
- The next step is to change a plan, file, artifact, adapter, or release status; route that result to the owning command after the evidence brief.

## Reads

- `research_question`
- `supplied_sources`
- `work_intent`
- `evidence`
- `provider_capability_profile`
- `source_authority_order`
- `freshness_requirement`
- `downstream_claim_or_decision`

## Writes

- `evidence`: research brief, source map, claim limits.

Do not write artifacts, state decisions, plans, provider adapters, release gates, or handoff packets. Research may recommend a move or route options, but the next operation must be separately authorized.

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
| `discover` | The needed sources are unknown or incomplete. | Source candidates, authority ranking, search gaps. |
| `verify` | A specific claim, source, or assumption must be checked. | Claim status, supporting evidence, contradictions, and limits. |
| `synthesize` | Multiple sources must answer one research question. | Evidence brief with source claims, inference, confidence, and uncertainty. |
| `source-map` | The user needs provenance, authority order, or source coverage. | Source inventory, authority map, freshness, and loadability. |
| `fact-check` | A statement may be inaccurate, stale, exaggerated, or unsupported. | Verdict by claim with corrections and evidence ceiling. |
| `update` | Time-sensitive facts may have changed since a prior answer or packet. | Current-status check, dated source map, stale assumptions, upgrade/downgrade note. |

## Lenses

- `gold-standard`
- `evidence-ceiling`
- `variant-reconciliation`

## Source Authority

Use the narrowest source set that can support the requested claim.

Prefer, in order, sources that are:

1. Primary or official for the claim domain.
2. Current enough for the claim's freshness requirement.
3. Directly scoped to the jurisdiction, provider, product, version, artifact, event, or period at issue.
4. Loadable by the current or next consumer, not merely cited.
5. Corroborated by independent sources when the claim is contested, high-stakes, or non-official.

Treat supplied sources as evidence, not automatic truth. When supplied sources conflict with official or newer sources, preserve the conflict and state which source has authority for which claim.

Do not cite unavailable, remembered, or inferred sources as if they were checked. If a source is named but not read, label it `not inspected`.

## Claim Taxonomy

Classify material claims before concluding:

| Label | Meaning |
|---|---|
| `supported` | Directly supported by inspected evidence within scope and freshness needs. |
| `partially supported` | Supported for some scope, period, version, or condition, but not all of the requested claim. |
| `contradicted` | Inspected evidence conflicts with the claim. |
| `uncertain` | Evidence is mixed, indirect, ambiguous, or source authority is unresolved. |
| `unverified` | No adequate inspected evidence supports the claim. |
| `out of scope` | The requested claim requires sources, authority, or professional judgment outside the current research boundary. |

Separate:

- direct source claim;
- observed fact from current retrieval, file inspection, command output, or supplied source;
- model inference from the evidence;
- implication for the user's work.

Only observations from actual retrieval, file inspection, commands, tests, or supplied documents can raise a claim above pure design-time synthesis.

## Freshness Rules

Use retrieval or require current supplied sources when the claim concerns:

- latest, current, today, recently, or newly changed information;
- laws, regulations, policies, platform capabilities, pricing, schedules, availability, market data, or public roles;
- provider adapter capabilities or release readiness;
- future events or live/settled outcomes.

If retrieval is unavailable or not performed, do not claim latest, current, official, settled, or still-valid status unless a supplied source directly supports that claim and is fresh enough for the requested use.

Use absolute dates when relative dates matter. Record source publication, retrieval, access, or inspection dates when available.

## Context Loading

Load the smallest context needed for the selected mode:

1. Current research question, explicit command, and downstream decision or claim.
2. User-supplied sources, dates, artifacts, and constraints.
3. Provider capability profile, especially retrieval, file-read, code-execution, and citation limits.
4. Source authority rules and freshness requirement.
5. Primary or official sources, then corroborating or dissenting sources.
6. Relevant lenses only after the claim and source need are clear.

If a load-bearing source is unavailable, return a blocking or degraded evidence brief rather than filling the gap with memory.

## Procedure

1. Define the research question, downstream claim, and why evidence is needed.
2. Select the primary mode and freshness requirement.
3. Determine whether live retrieval, file inspection, code execution, or supplied-source review is required and available.
4. Freeze the evidence boundary: sources to inspect, date or version scope, provider capabilities, and claim ceiling.
5. Prefer primary, official, authoritative, or otherwise best-fit sources; add corroborating sources when the claim is contested or consequential.
6. Record source identity, authority, date, scope, retrieval or inspection status, and loadability.
7. Extract source claims separately from observations and model inference.
8. Classify each material claim as supported, partially supported, contradicted, uncertain, unverified, or out of scope.
9. Preserve contradictions and explain which source has authority for which subclaim.
10. State permitted claims, prohibited claims, and verification needed to upgrade.
11. State implications for the current work and recommend the next owning command without performing it.

## Mode Procedures

Use only the mode procedure needed for the request. Do not run every procedure by default.

### `discover`

1. Define the claim domain, source authority need, and freshness window.
2. Identify likely primary, official, canonical, or directly authoritative sources.
3. Separate must-have sources from useful corroboration.
4. If retrieval is available, inspect the highest-authority sources first.
5. If retrieval is unavailable, list exact source needs and expected authority role.

### `verify`

1. Restate the claim in checkable subclaims.
2. Inspect the source that can directly support or refute each subclaim.
3. Mark support status by subclaim.
4. Name any scope mismatch, stale date, version mismatch, missing jurisdiction, or unsupported leap.
5. Return the strongest claim that is actually supported.

### `synthesize`

1. Group sources by authority, date, scope, and agreement.
2. Summarize source claims without overstating consensus.
3. Reconcile compatible sources and preserve incompatible claims as contradictions.
4. Distinguish conclusion from inference and state confidence within the evidence ceiling.

### `source-map`

1. Inventory sources with identity, source type, date, scope, inspected status, and loadable reference.
2. Rank authority for the current claim.
3. Flag stale, missing, inaccessible, secondary, or experimental sources.
4. Identify which claims each source can and cannot support.

### `fact-check`

1. Break the target statement into atomic claims.
2. Check each claim against the best available source.
3. Assign a claim label and correction when needed.
4. Preserve `uncertain` and `unverified` instead of forcing true/false.
5. Report the correction boundary and any stronger verification owed.

### `update`

1. Identify the prior assumption, source date, or packet being refreshed.
2. Check current or fresh-enough primary sources when retrieval is available.
3. Compare the prior assumption to inspected current evidence.
4. Mark unchanged, changed, contradicted, stale, or still unverified.
5. Route any plan, adapter, artifact, or release-gate update to the owning command.

## Required Output

Preserve these functions; exact formatting may vary:

- Question and mode.
- Evidence boundary: source set, freshness requirement, retrieval or inspection status, evidence stage.
- Supported findings.
- Contradictory or uncertain findings.
- Partially supported, contradicted, uncertain, unverified, or out-of-scope findings.
- Source map with authority, date, scope, and loadability.
- Claim limits: permitted claims, prohibited claims, verification needed to upgrade.
- Implications for the current work.
- Recommended move, route options when real, and approval shorthand when safe.

## Output Profiles

### Compact

Use for low-coupling claim checks:

```text
Question: <claim to check>
Mode: <verify|fact-check|update|other>
Evidence boundary: <sources inspected or not inspected; retrieval status; date scope>
Finding: <supported|partially supported|contradicted|uncertain|unverified>
Sources: <source map or needed sources>
Claim limit: <what can and cannot be said>
Recommended move: <stop, /design, /build, /review, /compare, /diagnose, /handoff, or route option>
```

### Material

Use for current-information, high-stakes, multi-source, contradiction, or downstream-governing research:

```text
Research question
Mode and evidence boundary
Source authority map
Findings by claim
Contradictions and uncertainty
Inference and implications
Claim limits and verification needed
Recommended move
```

## Examples

### Current Provider Capability Check

Input: `/research Verify the latest provider capabilities and update the adapter plan.`

Expected behavior:

```text
Question: Which provider capabilities are currently supported for the adapter plan?
Mode: update with source-map support.
Evidence boundary: current provider docs required; adapter plan update not authorized under /research.
If retrieval available: inspect official provider docs and record access dates.
If retrieval unavailable: mark capability status unverified and list exact docs needed.
Claim limit: may describe inspected source claims; may not update the adapter plan or claim current status from stale notes.
Recommended move: /design or /build can update the adapter plan after evidence is accepted.
```

### Supplied Sources Disagree

Input: `/research These two sources disagree about the rule. Tell me what we can rely on.`

Expected behavior:

```text
Finding: uncertain unless one source has clear authority for the claim scope.
Contradiction: preserve Source A and Source B claims separately.
Authority: official/current/source-of-record wins only for the subclaims it actually covers.
Claim limit: do not average the disagreement into a single unsupported rule.
Recommended move: stop or /compare if the user needs a decision among interpretations.
```

### No Live Retrieval

Input: `/research Is last week's provider-doc check still current?`

Expected behavior:

```text
No live retrieval available.
Finding: unverified for current status.
Sources needed: current official provider docs with access date.
Claim limit: prior checked docs may support historical assumptions only; they do not prove latest status.
Recommended move: rerun with retrieval or proceed with an explicitly stale assumption if low-risk.
```

## Provider Degradation

When live retrieval is unavailable:

- State `No live retrieval available`.
- Assess only supplied evidence.
- Label unsupported claims as unverified.
- Identify exact sources needed to upgrade the evidence.
- Without retrieval, do not claim latest, current, official, or provider-capability facts beyond the supplied sources.

When file reading is unavailable, assess only user-provided excerpts and label source identity, completeness, and context as unverified unless the excerpt itself establishes them.

When code execution or tests are unavailable, do not claim measured behavior, parsed dataset results, or computed validation. Return the commands, dataset, or inspection needed to upgrade.

When durable memory is unavailable, include the source map and claim limits in the response rather than relying on session memory.

## Stop Conditions

- The evidence brief is sufficient for the recommended move.
- Required retrieval is unavailable and no supplied evidence can support the claim.
- The requested conclusion exceeds the available sources.
- A stronger conclusion would require regulated professional judgment, inaccessible sources, or an unauthorized downstream operation.
- Additional sources would not materially change the next decision.

## Boundary

`/research` produces evidence, not artifacts, designs, repairs, or handoff packets.

It may recommend `/design`, `/build`, `/review`, `/compare`, `/diagnose`, or `/handoff` as a move, but it must not perform those operations under the research command.
