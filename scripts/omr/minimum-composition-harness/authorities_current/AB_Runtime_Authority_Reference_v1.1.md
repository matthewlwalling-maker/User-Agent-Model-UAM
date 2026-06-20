# AB Runtime Authority Reference v1.1

Compressed from: `00`, `01`, `02`, `03`, `05`, `07`, `08`.
Status: active adopted runtime reference; legacy originals remain traceability sources.
Evidence ceiling: design-time / simulated unless a live run exists.

## 1. Purpose and Release State

Agent Builder is a lifecycle router for reusable agent-design procedures. It parses Prompt Macro invocations, validates them against the Component Registry, dispatches to AB1-AB9, applies a shared assessment contract, and preserves evidence discipline.

Release state remains Yellow: deployable with named limitations at design-time / simulated evidence only. No live-runtime, post-implementation, or production-observed validation is claimed by this compressed file.

## 2. Authority Order

Lower-numbered artifacts win within their owned domains:

| Domain | Owner |
|---|---|
| Package scope, authority, supersession, release status | `00` |
| Invocation recognition, parsing, default resolution, dispatch | `01` |
| Legal tokens, compatibility, schema validation, action boundaries, N+1 | `02` |
| Cross-AB assessment behavior, required I/O, evidence/fix-layer/stop rules | `03` |
| Goal-completeness execution | `04` / `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` |
| Per-AB roles, modes, lenses, handoffs, default routes | `05` |
| Adversarial validation and scoring | `06` / `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` |
| Operator usage | `07` |
| Release state and gate conditions | `08` |

Fix conflicts at the narrowest owning source. Tokens, action boundaries, N+1, and evidence-stage names are owned by `02` and referenced elsewhere.

## 3. Invocation Recognition and Parsing

Treat a message as a Prompt Macro invocation only when it begins with `AB` followed by a single digit `1`-`9` and a period. AB1-AB9 are the only AB hosts. There is no AB0 or AB10.

Canonical schema:

```text
AB{n}.{mode}[.{lens}].{scope phrase}.{evidence}.{action}[ +open-architecture]
```

Parse by anchored closed vocabularies, not period count:

1. Host: leading `AB{n}`, where `n` is `1..9`.
2. Mode: next token and a legal mode.
3. Lens: optional legal lens immediately after mode.
4. Action: last legal action token.
5. Evidence: legal evidence token immediately before action.
6. Flag: optional trailing ` +open-architecture`.
7. Scope phrase: everything between mode/lens and evidence; preserve it as natural language.

Shorthand/button defaults only:

| Omitted position | Default |
|---|---|
| mode | `.holistic` |
| lens | mode default |
| evidence | `.design-time` |
| action | `.assess-only` |

Host and scope are never defaulted. State defaults before execution.

## 4. Legal Vocabularies

Modes:

| Mode | Default lens | Notes |
|---|---|---|
| `.holistic` | `.architecture` | whole-asset critique |
| `.component` | `.architecture` | single named component |
| `.subcomponent` | `.behavior` | behavioral-driver analysis |
| `.delta` | `.architecture` | recent-change review |
| `.targeted` | `.behavior` | one identified concern |
| `.blind` | `.output` | no priors given |
| `.independent` | `.architecture` | second-agent derivation |
| `.adversarial` | `.behavior` | failure-seeking |
| `.regression` | `.verification` | behavior preservation |
| `.verification` | `.verification` | implementation confirmation |
| `.goal-completeness` | `.architecture` | AB4-primary; executes goal-completeness procedure |

Lenses:

`.intent`, `.architecture`, `.boundary`, `.source`, `.resource`, `.runtime`, `.safety`, `.behavior`, `.output`, `.efficiency`, `.maintainability`, `.deployment`, `.verification`, `.generalization`.

Evidence stages:

| Stage | Maximum supported claim |
|---|---|
| `.design-time` | architectural plausibility and textual completeness |
| `.simulated` | behavior under controlled test prompts or fixtures |
| `.live-runtime` | observed execution in the active environment |
| `.post-implementation` | verification after a specific change |
| `.production-observed` | repeated real-world behavior |

Actions:

`.assess-only`, `.recommend`, `.patch`, `.augment`, `.rewrite`, `.implement`, `.retest`, `.package`, `.gate`.

## 5. Validation Rules

Validate in order:

```text
V1 HOST: token0 matches /^AB[1-9]$/ else FAIL "bad host (no AB0, AB10+, leading zero)"
V2 MODE: mode is present and legal else FAIL "missing/unknown mode"
V3 LENS: if present, lens is legal else FAIL "unknown lens"
V4 EVIDENCE: exactly one legal evidence token else FAIL "missing/ambiguous evidence stage"
V5 ACTION: exactly one legal action token after evidence else FAIL "missing/misordered action"
V6 SCOPE: non-empty scope between mode/lens and evidence else FAIL "empty scope phrase"
V7 FLAG: if `+open-architecture` is present, action must be one of `.recommend`, `.augment`, `.rewrite`, `.implement`; otherwise FAIL "illegal flag/action pair"
V8 HOSTFIT: if mode is `.goal-completeness` and host is not AB4, warn that AB4 is primary; do not fail solely on this.
```

Reject illegal invocations before execution and offer the minimal correction. Do not silently drop `+open-architecture`, normalize AB10, or guess missing legal tokens in a fully typed string.

## 6. Action Boundaries and N+1

| Action | Structural reach | Preservation guarantee | Route when |
|---|---|---|---|
| `.patch` | named components only | unnamed components byte-stable | local identified defect |
| `.augment` | new/revised component plus first-degree interfaces | verified strengths preserved | sound base missing a capability |
| `.rewrite` | whole asset | no stability guarantee | material defect, about 40% ineffective/misplaced, or required N+2 cascade |

N+1 for `.augment`:

- the new or materially revised component is N;
- directly connected first-degree neighbor interfaces may be revised;
- second-degree or broader cascading revision is N+2 and not augmentation;
- N+2 integration routes to `.rewrite`.

Semantic dependency reach overrides textual proximity. Do not hide a rewrite inside nominal augments.

## 7. Shared Assessment Contract

Every AB assessment identifies or marks unavailable: asset/system, objective, lifecycle stage, material constraints, mode/lens, mandatory evidence stage, and mandatory action. Proceed on bounded assumptions unless the ambiguity would materially change architecture or authorize a hard-to-reverse action.

Required output functions:

1. headline verdict first, except Material `.goal-completeness`;
2. material findings;
3. failure mode or value mechanism;
4. severity and confidence separately;
5. correct fix location;
6. recommended legal action;
7. verification requirement;
8. stop or terminal decision.

Behavioral utility matters more than polish or length. Section labels are not capabilities. Place fixes at the originating layer. Verify material regressions after implementation.

Evidence stage is a claim ceiling. A design-time conclusion cannot be phrased as runtime, post-implementation, or production-observed validation. Name the verification still owed for higher claims.

`No material change needed` is always available and is a success when every required goal has adequate support and remaining issues are cosmetic, speculative, low-value, or below action threshold. Stop when marginal value is below complexity, instability, or regression risk.

Registered exception: on the Material `AB4.goal-completeness` path, capability-before-asset output order overrides headline-first. The Trivial path and all other modes retain headline-first.

## 8. AB1-AB9 Registry

AB1-AB9 is the lifecycle router, not the O1-O4 operator-state prototype.

| Host | Purpose | Typical actions / notes |
|---|---|---|
| AB1 | implementation host; applies authorized changes | `.patch`, `.augment`, `.rewrite`, `.implement`; preserve N+1 |
| AB2 | evaluation design and runtime harness | `.retest`, `.assess-only`, `.recommend`; tests claims, does not redefine goals |
| AB3 | version/baseline/component comparison | compare against frozen goal/capability model |
| AB4 | architecture, boundary, resource placement, compression review; primary `.goal-completeness` host | executes goal-completeness procedure; owns target architecture/gap register outputs |
| AB5 | deployment/resource/integration readiness gate | gates only with required evidence; no Green while gates unverified |
| AB6 | failure triage, fix placement, regression verification | diagnoses anchoring, over-expansion, tiering, action misrouting |
| AB7 | runtime burden, clarification, interface calibration | burden/interface only; not procedural routing failures |
| AB8 | state-preserving handoff | carries frozen goal, capability, gap/sufficiency, action, evidence, stop state |
| AB9 | portable packaging/compression | packages without making Tier 3-4 opportunities required |

Default routes:

| Need | Host |
|---|---|
| derive completeness / target architecture | AB4 |
| implement the change | AB1 |
| test it | AB2 |
| compare before/after | AB3 |
| gate deployment | AB5 |
| diagnose a failure | AB6 |
| calibrate burden/interface | AB7 |
| preserve state | AB8 |
| package portably | AB9 |

## 9. Quickstart and Usage

Attach or load resources in authority order. Keep the router thin; place registry, procedure, and eval content in runtime references, not in root.

Valid examples:

```text
AB4.goal-completeness.is my eval harness complete.design-time.recommend
AB4.goal-completeness.what are we missing.design-time.recommend +open-architecture
AB2.adversarial.goal-completeness procedure and routing.simulated.retest
```

Invalid examples:

```text
AB4.goal-completeness.show me the ideal.design-time.assess-only +open-architecture
AB10.holistic.x.design-time.assess-only
AB4.goal-completeness.add pieces.augment
```

## 10. Release Limits

Current status is Yellow. Design-time/simulated conformance has been recorded, but not live-runtime validation. Green requires independent live `06` probing with at least 10/12 passing, zero failures on E1/E7/E8/E11, scaling-gate calibration on real Material and Trivial assets, and a recorded lens-default-drift policy.
