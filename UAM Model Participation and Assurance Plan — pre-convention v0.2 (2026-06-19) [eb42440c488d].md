# UAM Sub-Architect Brief — Bootstrap Pair

**Artifact ID:** `UAM-BRIEF-BOOTSTRAP-0.1`
**Parent framework:** `UAM-FRAMEWORK-0.21`
**Status:** dispatch-ready, **gated on Phase-0 adoption** (§12.0.1). Until the user adopts or revises UAM-FRAMEWORK-0.21, this packet is a prepared assignment, not an authorization to run a sub-architect.
**Generated:** 2026-06-19
**Evidence ceiling:** design-time → simulated (the validation run is the first artifact that may carry simulated-stage evidence)

---

## 0. Why this brief exists (read first)

This is not an ordinary component assignment. The bootstrap pair is the **validation gate of §12.0.3**: the experiment that tells you whether the Spine + Work-Object Model + Component Spec actually suffice to build a real component *without reopening the framework or inventing a Spine-owned shared encoding*. Its output is therefore two things at once:

1. Two working operation specs — `architect-solution` and `evaluate-artifact` — built **only on contracts already frozen at adoption**.
2. A **validation report** that answers the gate question and either clears the path for parallel dimensional dispatch or sends a shared-encoding decision back to the Spine.

Three hard constraints govern the whole assignment:

- **Build only on frozen contracts.** Permitted inputs: Work-Object Model (§5), the full Spine (§6, including the §6.10 shared-vocabulary contract), the Required Component Specification (§13), and the evidence-stage vocabulary (§3.8). Nothing else is assumed frozen.
- **Do not invent a Spine-owned shared encoding (§6.10.2).** If building either operation requires an error-code scheme, a state-object metadata field, a source-authority precedence, or a packet/manifest format that is **not yet frozen at the Spine**, the sub-architect MUST return a blocking condition naming the missing contract — not define it locally. That block is a *successful* gate outcome (it routes the decision to the Spine owner), not a failure.
- **Keep self-evaluation separate from independent evidence.** `evaluate-artifact` is used to attack what `architect-solution` produces; a self-graded pass is not independent evidence and must be labeled as such (§9.3, §16.4).

---

## Identity

- **Assignment ID:** `UAM-BRIEF-BOOTSTRAP-0.1`
- **Component name:** Bootstrap Operation Pair — `architect-solution` + `evaluate-artifact`
- **Component class:** `skill-family` (two operation families within D3)
- **Assigned dimension(s):** **D3 Operational Skill Fabric** (primary, owns both operation surfaces). Consumes — but does not own — D4 (reasoning lenses), D8 (evaluation), D6 (state references), D2 (authority limits), per the Cross-Dimensional Composition Matrix (§7.9). Cross-dimensional **scope is limited to consumption**; no writes to any other dimension.
- **Authorized role:** design + author the two operation specs to working state (`compose-content`), then exercise them as the §12.0.3 validation experiment. **Not** authorized: runtime install, OMR/AB migration, defining any Spine-owned shared encoding, or building any of the other four operations.
- **Evidence ceiling:** `design-time` for the specs; `simulated` for the validation run, only if a controlled exercise is actually executed and captured per §16.4. No `live-runtime` or higher claim.

## Committed outcome

- **Outcome:** Two complete operation specifications (`architect-solution`, `evaluate-artifact`) conforming to §13, plus a validation report answering the §12.0.3 gate.
- **Success conditions:**
  1. Both specs satisfy the §13 component contract and the §21 completion gate (all 14 questions answerable).
  2. The pair is exercised on **at least one real candidate component** — `architect-solution` designs it; `evaluate-artifact` grades it.
  3. The validation report states **explicitly** whether the build reopened the framework or required an unfrozen Spine-owned shared encoding, and records the kill-condition check (§12.0.3).
- **Material constraints:** build only on frozen contracts; never define a Spine-owned shared encoding; preserve object integrity (architect-solution does not mutate production artifacts; evaluate-artifact does not modify the evaluated artifact in a read-only stage); independent-eval evidence must come from a genuinely separate context, not a new section of the same one (§9.3).

## Requirement classes

### Explicit required
- `architect-solution` operation spec (§13 form).
- `evaluate-artifact` operation spec (§13 form).
- Validation report clearing or escalating the §12.0.3 gate.

### Entailed required
- Routing tests: "design the ideal architecture for X" → `architect-solution`; "does X satisfy its goals / is X ready" → `evaluate-artifact` (outcome-based routing, not keyword match — §16.1 Routing class).
- Neighbor-exclusion enforcement: `architect-solution` must not mutate production artifacts or promote evidence; `evaluate-artifact` must not redefine goals, select architecture, or edit the artifact during a read-only stage (§8.1, §8.3, §16.1 Operation-boundary class).
- Self-eval-vs-independent separation, labeled in every verdict (§9.3).

### Optional
- Additional modes beyond the §8.1 / §8.3 common-mode lists, if the validation exercise shows a recurring need.

### Speculative
- Anything that would require resolving an open question (§20.2) or defining a Spine-owned encoding — **out of scope; block instead.**

## Ownership

- **Owned decisions:** internal structure, procedure, modes, lenses, and recipes of the two operations; their routing logic; their **dimension-local** schemas and naming (§6.10.3).
- **Owned writes:** the two operation specs; design-decision state for these two operations when authorized; the evaluation evidence records produced by the validation run.
- **Prohibited decisions:** defining any Spine-owned shared encoding (§6.10.2); selecting architecture for any other dimension; promoting evidence above the actual stage; adopting or revising the framework.
- **Prohibited writes:** any other operation's spec; any production artifact (architect-solution authors *design* artifacts only; evaluate-artifact writes *evaluation* artifacts/evidence only); the Spine contracts; any other dimension's state.
- **Escalation conditions:** an unfrozen Spine-owned shared encoding is needed → block and name it; a frozen contract appears internally contradictory → block and return to the Spine owner; the assignment cannot be completed without writing outside the owned boundary → block.

## Existing foundations

> **Provisioning rule (§12.0.2): the dispatcher MUST attach the *content* of each source below — full text or a guaranteed-loadable reference in the sub-architect's execution context. Dispatching with these as bare citations violates §12.0.2 and will force a block.** All listed files are present in the project and are guaranteed-loadable references.

- **Attached source content (not citations) + versions:**
  - `AB_Runtime_Authority_Reference_v1.1.md` — AB4 architecture/goal-completeness host; AB2/AB5 evaluation-design vs deployment-gate split; action boundaries and N+1; shared assessment contract (headline-first); evidence stages.
  - `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` — capability-before-asset, four requirement tiers, coverage classes, E1–E12 and sentinel logic.
  - Reasoning-lens donors for `architect-solution`: `spec-builder`, `gold-standard-comparison`, `steelman-premortem`, `narrative-substance-review`.
  - Reasoning-lens donors for `evaluate-artifact`: `blind-grader`, `break-it-tester`, `consistency-review`.
  - The relevant frozen Spine artifacts from Phase 1 (§19), including any shared encodings already frozen.
- **Preserve:** AB4 goal-completeness and open-architecture behavior; AB2/AB5 separation of test-design/execution from readiness-gating; headline-first assessment contract (with the Material goal-completeness exception); evidence-ceiling discipline; `No material change needed` as a valid terminal result.
- **Refactor candidates:** AB4 → `architect-solution`; AB2 + AB5 → `evaluate-artifact` (consolidate the two AB hosts into one operation while keeping the design/execution-vs-gate boundary explicit inside it).
- **Absorb candidates:** the named grading and specification lenses, absorbed as D4 lenses these operations *invoke* — not re-implemented inside the operations.
- **Replace candidates:** none.
- **Retire candidates:** none.
- **Missing capabilities:** the unified UAM operation-spec form itself — this assignment produces it for two operations, and that form becomes the template the other four operations follow.

## Interfaces

- **Upstream inputs:** a committed intent (D1) — for the bootstrap, a **provided test intent** plus a real candidate component to design/grade; the frozen Spine contracts (§6); any frozen shared vocabulary (§6.10.2).
- **Downstream consumers:** the other four operation builds (will copy this spec form and routing pattern); D8 (consumes the validation evidence).
- **Neighboring components:** the `author-artifact`, `compare-options`, `diagnose-failure`, `handoff-state` shells (§8.2/§8.4/§8.5/§8.6) — must not be impersonated or absorbed.
- **Freshness/branch requirements:** build against the frozen Phase-1 Spine revision; if the Spine freeze changes, the specs are stale and the build restarts against the new revision.
- **Compatibility requirements:** compatible Spine version = the adopted `UAM-FRAMEWORK-0.21` Phase-1 freeze.

## Required deliverables

1. `architect-solution` operation specification (§13 YAML, all sections populated).
2. `evaluate-artifact` operation specification (§13 YAML, all sections populated).
3. Routing test deck covering the §16.1 **Routing** and **Operation-boundary** classes for these two operations (including the adversarial "Review and improve this" case from Appendix B that must be intent-classified, not auto-routed).
4. **Validation report** — the §12.0.3 gate answer: did the build run clean on frozen contracts? Did it need any unfrozen Spine-owned shared encoding (and if so, which, escalated to the Spine owner)? Kill-condition check. Evidence captured at the stated stage per §16.4, with the independent-eval context isolation documented.

## Validation

- **Local evals:** each operation performs its own function on positive, negative, adversarial, and no-action cases (architect-solution derives capability-before-asset and generates ≥2 materially different candidates where the problem admits them, §10.3; evaluate-artifact grades completeness/readiness without redefining goals).
- **Spine contract evals:** both operations consume frozen contracts without redefining them; object integrity holds (architect-solution writes design artifacts only; evaluate-artifact does not mutate the evaluated artifact); evidence ceiling respected.
- **Integration evals:** the `architect-solution → evaluate-artifact` handoff — the evaluator consumes the architect's committed design artifact and the committed goal, and produces an independent verdict whose evidence is separated from the architect's self-check.
- **End-to-end evals:** the validation experiment itself — design one real candidate component with `architect-solution`, grade it with `evaluate-artifact`, on representative input.
- **Ablation/baseline:** compare `architect-solution` output with vs. without its reasoning lenses to confirm the lens adds value over the bare operation (§16.3); same for one `evaluate-artifact` lens.
- **Evidence capture (§16.4):** frozen inputs and source versions, exact prompts/contracts, raw first-pass outputs, rejected selections, and the context-isolation evidence for the independent evaluation; first-pass record never overwritten by a repaired run.

## Preservation and stopping

- **Strengths to preserve:** the AB4 / AB2 / AB5 behaviors named above; headline-first output; evidence-ceiling discipline; valid successful stopping.
- **Change boundary:** these two operations only. No other dimension is touched. No Spine-owned encoding is defined.
- **Stop condition:** both specs complete per §21 **and** the validation report is produced answering §12.0.3 → **STOP.** Do not build the other four operations, do not install, do not migrate AB/OMR, do not broaden scope.
- **Revisit triggers:** the Spine Phase-1 freeze changes; the validation run surfaces an unfrozen Spine-owned shared encoding (→ block and return to the Spine owner); a frozen contract is found internally contradictory.

---

## Terminal Record

**Task class:** sub-architect assignment — bootstrap operation pair / validation gate
**Terminal state:** dispatch-ready assignment packet produced; **not yet dispatched** (gated on Phase-0 adoption, §12.0.1)
**Do not do next:** do not run a sub-architect against this packet, and do not treat it as authorization, until the user adopts or revises `UAM-FRAMEWORK-0.21`; do not dispatch any other dimension in parallel until this pair clears the §12.0.3 gate
**Only valid next step:** user adopts/revises the framework (Phase 0), then dispatches this packet with the §12.0.2 source content attached
**Recommended context window:** new context for the sub-architect execution (the build and its independent evaluation each need clean context per §16.4); current context for revising this brief
**Next role_class:** sub-architect execution (D3 operation build) on adoption
**Next assignee_runtime:** user-selected
