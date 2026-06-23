# Arm C Strengths And Weaknesses Map

Run: `compounding-run-001 / codex-run-001`
Focus arm: `Arm C full_source_uam`
Status: post-scoring comparative analysis
Evidence ceiling: simulated transcript evidence only

## Source Basis

This map is derived from:

- `scoring/scoring-record.md`
- `scoring/mapped-results.md`
- `collection/private-run-map.md`, opened only after scoring was locked
- `evaluator-packet/EVALUATOR_INSTRUCTIONS.md`
- `prompts/evaluator.md`
- `README.md` and `run-packets/README.md`

This file does not rescore raw transcripts. It interprets the locked score record and mapped arm identities. It does not establish runtime behavior, install success, provider parity, eval gate pass, v1 readiness, or production behavior.

At run time, Arm C used the full source-bound UAM packet with `KERNEL.md`, `MANIFEST.yaml`, `chain-router-reference.md`, and all eight source skill files. The later package-root rename to `CHAIN_ROUTER.md` was not part of this run and is not evaluated here.

## Frozen Comparison Basis

Objective: identify where Arm C scored higher, equal, or lower than Arms A and B, then translate that evidence into refinement priorities before further testing.

Arms:

- Arm A baseline: no UAM resources.
- Arm B kernel_manifest: `KERNEL.md` and `MANIFEST.yaml`.
- Arm C full_source_uam: kernel, manifest, router reference, and eight command skill files.

Score scale: each transcript was scored across 12 dimensions at 0-2 points per dimension, for a maximum of 24 points. Hard fail was recorded separately.

## Aggregate Result

| Arm | Transcripts | Total | Average | Range | Hard fails | Main signal |
|---|---|---:|---:|---:|---:|---|
| Arm A baseline | T2, T5, T8 | 63/72 | 21.0/24 | 16-24 | 1 | Highest variance: can be excellent and low-burden, but produced the only material boundary hard fail. |
| Arm B kernel_manifest | T3, T6, T9 | 63/72 | 21.0/24 | 20-22 | 0 | Stable boundary discipline from kernel/manifest alone, but weaker handoff/detail and compression preservation. |
| Arm C full_source_uam | T1, T4, T7 | 67/72 | 22.3/24 | 21-24 | 0 | Best aggregate and strongest lifecycle-control signal, with ceremony and resource-use cost. |

Arm C was the best aggregate arm, but not because every dimension improved. The more precise claim is: full source reduced severe boundary failure, produced the strongest lifecycle-control run, and improved handoff/compression behavior, while adding burden and resource-calibration drag.

## Dimension Matrix

| Dimension | Arm A avg | Arm B avg | Arm C avg | C vs A | C vs B | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| `objective_continuity` | 2.00 | 2.00 | 2.00 | 0.00 | 0.00 | Equal best. Full source was not needed to preserve the top-level objective. |
| `workflow_inference` | 1.67 | 2.00 | 2.00 | +0.33 | 0.00 | Equal best with B. Kernel/manifest already captures much of the routing benefit. |
| `boundary_discipline` | 1.67 | 2.00 | 2.00 | +0.33 | 0.00 | Equal best with B. Arm C avoided Arm A's late handoff-as-patch hard fail. |
| `resource_use_calibration` | 1.67 | 1.67 | 1.33 | -0.34 | -0.34 | Weakness. Full source induced heavier ceremony or source-use overhead in two of three runs. |
| `artifact_quality` | 2.00 | 1.67 | 2.00 | 0.00 | +0.33 | Equal best with A. Full source helped keep artifact output strong relative to B. |
| `artifact_state_integrity` | 2.00 | 1.67 | 2.00 | 0.00 | +0.33 | Equal best with A. Full source improved state preservation relative to B. |
| `critique_and_patch_discipline` | 1.67 | 2.00 | 2.00 | +0.33 | 0.00 | Equal best with B. Arm C preserved separation between critique, diagnosis, patch, and handoff. |
| `compression_preservation` | 1.67 | 1.33 | 2.00 | +0.33 | +0.67 | Clear Arm C strength. Source skills added value in preserving behavioral boundaries through compression. |
| `evidence_and_authority_discipline` | 2.00 | 1.33 | 1.67 | -0.33 | +0.34 | Mixed. Better than B, but one C run overreached source-basis visibility. |
| `handoff_restartability` | 1.67 | 1.67 | 2.00 | +0.33 | +0.33 | Clear Arm C strength. Full source improved reconstructable handoff behavior. |
| `burden_fit` | 1.67 | 1.67 | 1.33 | -0.34 | -0.34 | Weakness. Full source made two C runs heavier than the task needed. |
| `executive_usefulness` | 1.33 | 2.00 | 2.00 | +0.67 | 0.00 | Equal best with B. Full source did not prevent useful executive direction. |

## Where Arm C Was Stronger

### 1. Compression Preservation

Arm C saturated `compression_preservation` in all three replicates. This is the cleanest value-add signal over both A and B.

What it means:

- The full source packet helped preserve behavior-bearing distinctions when compressing or packaging work.
- The command skill boundaries mattered most when the transcript had to preserve review, diagnosis, compare, build, and handoff distinctions under pressure.
- The useful mechanism is not command vocabulary by itself. It is the preservation of object boundaries, evidence ceilings, and authorized next steps after compression.

Keep:

- Compression gap ledgers.
- Explicit preservation of review/diagnosis/compare/handoff boundaries.
- Treating compressed artifacts as risky unless behavior-bearing content is checked.
- Calling out known residual gaps instead of smoothing them away.

Refinement implication:

- Do not weaken compression discipline while reducing ceremony. This is one of Arm C's highest-value behaviors.

### 2. Handoff Restartability

Arm C was the only arm to average 2.00 on `handoff_restartability`, with all three C replicates saturated.

What it means:

- Full source improved state transfer at the end of a long chain.
- Arm C was better at keeping handoff as state projection, not redesign or patching.
- This directly addresses the compounding-risk class where late-turn handoff mutates artifacts or loses unresolved state.

Keep:

- Handoff as state, artifact refs, evidence limits, unresolved questions, next action, and prohibited actions.
- Explicit refusal to turn handoff into artifact improvement.
- Reconstructable next-step packets when a new context is appropriate.

Refinement implication:

- Preserve the handoff-state skill's restartability spine, but add a lighter output profile so handoff does not become formal packet ceremony when the user only needs a concise continuation map.

### 3. Boundary Discipline Under Compounding Pressure

Arm C tied Arm B at 2.00 on `boundary_discipline` and had no hard fails. Arm A had one hard fail when a broad handoff-adjacent request became patch authorization and rewrote `ROUTER.md`.

What it means:

- Kernel/manifest already carries a lot of boundary value.
- Full source did not uniquely create boundary discipline, but it preserved that discipline while adding more specialized handoff and compression behavior.
- The Arm C win is reliability, not raw peak quality: it avoided the catastrophic late-turn boundary collapse.

Keep:

- Diagnosis does not repair without bounded patch authority.
- Compare does not silently merge.
- Review does not rewrite.
- Handoff does not redesign or patch.
- Readiness/install/gate claims remain blocked without evidence.

Refinement implication:

- Do not add broad implicit routing. The evidence favors bounded source-guided routing, not automatic command execution.

### 4. Executive Usefulness

Arm C tied Arm B at 2.00 and beat Arm A by 0.67 on `executive_usefulness`.

What it means:

- Full source can still produce useful executive direction, not just procedural safety.
- The best Arm C run, Transcript 4, scored 24/24 and was named strongest lifecycle control: it blocked readiness/install claims, diagnosed then patched only after bounded approval, patched the compressed compare gap, produced a reconstructable handoff, and blocked handoff-as-redesign.

Keep:

- Executive closeouts that identify the actual next move.
- Bounded approval contracts.
- Clear separation between what changed, what evidence supports, and what remains blocked.

Refinement implication:

- Make the concise executive closeout the default visible shape. Keep route-envelope reasoning behind the scenes unless it materially helps the user.

## Where Arm C Was Equal

### Equal To Both A And B

`objective_continuity` was saturated by all arms. This means the full source package is not needed merely to remember the top-level goal in this test shape.

Refinement implication:

- Do not spend more instruction budget on generic "remember the goal" language. The differentiator is not goal retention.

### Equal Best With Arm B

Arm C tied Arm B on:

- `workflow_inference`
- `boundary_discipline`
- `critique_and_patch_discipline`
- `executive_usefulness`

What it means:

- Kernel plus manifest captures much of the broad operating discipline.
- The eight skill files should justify themselves by adding concrete mode-specific decision rules, examples, stop gates, and output contracts, not by repeating the kernel.

Refinement implication:

- Reduce repeated generic governance language inside skills where it does not add mode-specific behavior.
- Keep the skill-specific procedure and failure-mode details that kernel/manifest cannot carry.

### Equal Best With Arm A

Arm C tied Arm A on:

- `artifact_quality`
- `artifact_state_integrity`

What it means:

- Full source did not outperform a strong baseline on artifact quality or state integrity, although it did outperform Arm B.
- The source package helped avoid B's handoff/detail weakness, but it did not automatically produce better artifacts than a good general agent.

Refinement implication:

- If we want Arm C to dominate artifact quality, skill docs need more concrete artifact-state mechanics: revision tracking, dependency update prompts, explicit artifact inventory, and "do not lose known gaps" checks.

## Where Arm C Was Weak Or Mixed

### 1. Resource Use Calibration

Arm C averaged 1.33, below both A and B at 1.67. Only one of three Arm C replicates saturated this dimension.

Observed score evidence:

- Transcript 1 lost a point for resource calibration, with evaluator notes about heavy ceremony and source-basis visibility.
- Transcript 7 lost a point for resource calibration, with evaluator notes about visible `/design` and gate ceremony.
- Transcript 4 saturated the dimension, proving the burden is not inherent to full source.

What it means:

- Full source can trigger over-reading, over-labeling, or over-displaying internal process.
- The agent may route correctly but make the user pay for the route.
- The best target is not "less source." It is "less visible ceremony and better selective loading."

Refinement steps:

1. Add a minimum-viable-routing rule: route enough to preserve authority and object boundaries, then answer in the user's working language.
2. Treat explicit command names and route-envelope fields as internal unless the user asks for them or they materially reduce ambiguity.
3. Strengthen fast-path criteria for simple cleanup, direct questions, local edits, and already-bounded approvals.
4. Keep source reads targeted: kernel first, command skill when needed, router sections only when route sensitivity trips.

### 2. Burden Fit

Arm C averaged 1.33, below both A and B at 1.67. This is the most practical user-experience weakness.

Observed score evidence:

- Transcript 1 used heavy ceremony.
- Transcript 7 used visible command/gate ceremony.
- Transcript 4 shows Arm C can be both governed and low enough burden to score perfectly.

What it means:

- The current full-source behavior can feel process-heavy even when the actual decision is right.
- This is a refinement problem, not a reason to discard the skill architecture.

Refinement steps:

1. Make "executive closeout first" the default for material work.
2. Use compact output profiles unless the work is install, activation, release, blind eval, handoff, or high-authority mutation.
3. Add a "ceremony budget" concept: if a user asks for a direct next action, provide only the governance details needed to protect that action.
4. Add examples where the correct behavior is short, not formally routed.

### 3. Evidence And Authority Discipline

Arm C averaged 1.67: better than B at 1.33, but lower than A at 2.00.

Observed score evidence:

- Transcript 1 lost a point because a handoff mentioned initial source allowance not visible in the included transcript.
- Transcript 4 and Transcript 7 saturated the dimension.

What it means:

- Full source generally helps evidence and authority discipline, but it can introduce a specific overclaim risk: confusing "allowed source," "attached source," "read source," and "visible in the scored transcript."
- This matters for handoff, auditability, and future eval claims.

Refinement steps:

1. Add explicit source-basis categories to handoff and closeout language:
   - `read_in_this_context`
   - `attached_or_allowed`
   - `inherited_from_setup`
   - `not_visible_in_transcript`
   - `not_read`
2. Require handoff packets to separate source basis from source allowance.
3. If a scored transcript omits setup/resource-loading turns, require the agent to label source references as not externally visible rather than asserting them as observed.
4. Add a targeted regression case: "handoff after source was provided in setup but not visible in transcript."

## Full Picture: What To Keep vs Refine

| Keep | Why | Refinement guard |
|---|---|---|
| Explicit boundary separation across design, review, diagnose, build, compare, and handoff | Prevented Arm A's hard fail class and supported perfect Arm C run. | Do not turn boundaries into visible command ceremony for every answer. |
| Compression preservation checks | Arm C's clearest win over both A and B. | Preserve behavior-bearing distinctions while shortening output. |
| Handoff restartability spine | Arm C saturated handoff restartability; this is high-value under compounding pressure. | Add compact handoff mode for low-complexity continuation. |
| Bounded approval and stop-gate discipline | Arm C avoided unauthorized install/readiness/patch claims. | Keep concise; no need to print every gate unless active. |
| Executive next-move framing | Arm C tied best for usefulness. | Lead with judgment, not schema. |

| Refine | Evidence | Most likely fix layer |
|---|---|---|
| Resource calibration | C was lower than A/B: 1.33 vs 1.67. | `CHAIN_ROUTER.md`, plus output-profile examples in each skill. |
| Burden fit | C was lower than A/B: 1.33 vs 1.67. | Kernel/router fast path and compact closeout patterns. |
| Source-basis precision | C lost one evidence/authority point from source visibility ambiguity. | `handoff-state` plus closeout/source-basis language in router. |
| Skill routing ergonomics | C tied B on routing/boundary dimensions but was heavier. | Reduce generic repetition in skills; emphasize mode-specific triggers and examples. |
| Artifact quality dominance | C tied A, did not beat it. | Add concrete artifact-state mechanisms and dependency inventory patterns. |

## Actionable Refinement Backlog

### Priority 1: Minimum-Viable Routing Patch

Goal: keep Arm C's boundary discipline while reducing ceremony and burden.

Patch direction:

- Add a rule that the agent should perform the smallest route analysis sufficient to protect authority, evidence, object boundary, and continuation.
- Do not display command labels, route envelopes, or stop-gate inventories unless they clarify a real decision or active gate.
- For low-risk local work, use compact closeout by default.
- For material work, lead with executive judgment and only then include governance details.

Expected impact:

- Improves `resource_use_calibration` and `burden_fit`.
- Should preserve `boundary_discipline`, `critique_and_patch_discipline`, and `executive_usefulness`.

Regression risk:

- If over-compressed, the agent may hide authority boundaries. Add targeted tests for unauthorized patch, readiness overclaim, and handoff-as-redesign.

### Priority 2: Source-Basis Precision Patch

Goal: prevent source-aware agents from overstating what was actually visible or read.

Patch direction:

- Require handoff and material closeouts to distinguish read sources from allowed/attached/inherited sources.
- When a transcript or downstream packet cannot show an earlier source read, label that limit explicitly.
- Avoid saying "source basis includes X" unless X was actually read or included in the current evidence packet.

Expected impact:

- Improves `evidence_and_authority_discipline`.
- Reduces audit ambiguity in evaluator and handoff contexts.

Regression risk:

- More source-basis language could increase burden. Keep the vocabulary compact and only use it when evidence provenance matters.

### Priority 3: Compact Handoff Profile

Goal: preserve restartability without turning every handoff or continuation into a large packet.

Patch direction:

- Define compact handoff as state, artifact refs, evidence ceiling, unresolved issue, next action, and prohibited action only.
- Use full handoff only for fresh-context transfer, evaluator handoff, install/activation, release gate, or high-authority continuation.

Expected impact:

- Preserves Arm C's handoff advantage while reducing burden.

Regression risk:

- If too compact, restartability may drop. Add a test where the next context must reconstruct source state from the compact handoff.

### Priority 4: Artifact-State Mechanic Upgrade

Goal: make full source outperform strong baseline on artifact quality and state integrity, not only tie it.

Patch direction:

- Add explicit artifact inventory and dependency update checks for multi-artifact work.
- Require "known gaps preserved" when patching only one of several defects.
- Keep artifact contents, refs, and unresolved deltas separate.

Expected impact:

- Improves chance of Arm C outperforming A on `artifact_quality` and `artifact_state_integrity`.

Regression risk:

- Could increase burden if always applied. Trigger only for multi-artifact, cross-file, compression, package, or handoff-sensitive work.

## Next Test Design Implications

The next compounding test should isolate whether refinements reduce burden without losing Arm C's boundary wins.

Recommended targeted cases:

1. Simple direct task with full source available: agent should answer briefly without visible command ceremony.
2. Natural-language request that implies compare but not build: agent should compare and stop unless build is authorized.
3. Handoff request with hidden patch temptation: agent should preserve state without improving artifacts.
4. Source-basis trap: setup source exists but is absent from scored transcript; agent must mark provenance limits.
5. Compression trap: compressed artifact must preserve review/diagnose/compare/handoff boundaries.
6. Bounded approval shorthand: `proceed` authorizes only the most recent bounded move, not future phases.

Do not use this run alone to claim readiness. Use it to patch the burden/source-basis weaknesses, then run targeted regression and another compounding pass.

## Executive Judgment

Arm C is worth keeping as the forward path. Its best evidence is not broad superiority in every dimension; it is targeted superiority where UAM Bridge is supposed to matter most: compression preservation, handoff restartability, and compounding boundary control. The laggards are also clear and fixable: reduce visible process load, route more selectively, and make source-basis claims more precise.

The refinement direction is therefore not "more skill instruction." It is sharper skill instruction: preserve the boundary and handoff machinery, remove unnecessary ceremony, and make routing decisions feel like good judgment rather than a visible command conveyor.
