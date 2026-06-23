# Chain Router Reference

Status: design-time reference
Scope: expanded routing policy for `uam-bridge-skills/KERNEL.md`
Evidence ceiling: design-time unless eval, static validation, or runtime evidence is recorded elsewhere

This reference expands the kernel Chain Router policy. It is load-triggered by `KERNEL.md`; it is not a ninth command, registry, artifact system, provider orchestrator, or substitute for any skill's `SKILL.md`.

## Load Triggers

Load this reference before acting when a route involves any of the following:

- bounded continuation across commands;
- next-step authority or `next_allowed`;
- stop gates;
- review, research, verification, or reference work owed;
- artifact acting references;
- evidence-stage upgrade risk;
- context handoff or fresh-context routing;
- material changes to routing, autonomy, chain policy, stop gates, object boundaries, evidence ceilings, eval gates, or stateful workflow behavior.

If this reference is unavailable, continue only within `KERNEL.md` and record the missing reference in closeout.

## Route Envelope

For material work, keep a compact route envelope:

```yaml
route_envelope:
  command: /align | /design | /build | /review | /compare | /diagnose | /research | /handoff
  mode_hint: string | null
  scope: string
  evidence_stage: design-time | simulated | live-runtime | post-implementation | production-observed
  action_authority: assess-only | recommend | patch | augment | rewrite | implement | retest | package | gate
  work_object: state | artifact | evidence | packet
  object_subtype: design_artifact | production_artifact | source_artifact | transport_packet | null
  source_basis: supplied | local-files | donor-reference | eval-record | external-source | runtime-observation | unavailable
  artifact_ref: object | null
  chain_state: complete | next-step-known | alignment-needed | blocked | no-material-change-needed
  recommended_move: string | null
  route_options: list
  approval_contract: string | null
  stop_gates: list
  next_allowed: true | false
```

`mode_hint` is advisory. The receiving skill owns final mode resolution from its own `SKILL.md`. If `mode_used` materially differs from `mode_hint`, closeout should name the reason.

`next_allowed` is not action authority. It means the router may present or enter the next route only when Chain Authority and stop gates permit it.

`recommended_move` is the user-facing executive direction for the next movement in the work. It may be an executable action, a decision, a stop condition, or a real fork. `route_options` records materially different next paths when they exist. `approval_contract` records the short approval reply, if any, that would authorize the recommended move without restating the full prompt.

`object_subtype` preserves authority distinctions that `work_object` alone cannot carry. Use `design_artifact` for design-owned specifications, plans, architectures, or decision artifacts; `production_artifact` for substantive deliverables whose mutation belongs to `/build`; `source_artifact` for package, adapter, fixture, or repository source files whose mutation belongs to `/build`; and `transport_packet` only when `work_object: packet`. `transport_packet` must not be treated as an artifact or as authoritative state.

## Artifact Acting References

Use `artifact_ref` when a governed UAM artifact or context-isolated downstream action depends on exact artifact state.

```yaml
artifact_ref:
  stable_artifact_id: string | null
  stable_name: string | null
  canonical_filename: string | null
  artifact_revision: integer | null
  revision_date: date | null
  content_sha256: string | null
  loadable_ref: path | packet-ref | archive-ref | null
  reference_status:
    - planning-only
    - active-resolved
    - pinned-resolved
    - unindexed-local
    - stale-pin
    - index-mismatch
    - loadable-content-missing
    - unresolved
  reference_requirement:
    - planning-ok
    - acting-reference-required
    - archive-transaction-required
```

Bare stable artifact names are sufficient for planning and discussion. Downstream machine action, build, handoff, adoption, compatibility record, evaluation, or evidence claim on a governed UAM artifact requires a stable identity, recorded stamp, and loadable content reference when available.

Ordinary local package paths remain usable for local planning and bounded package edits unless promoted into governed artifact flow. The router must not compute hashes, mint stamps, update artifact indexes, or perform archive transactions. If a governed active artifact requires replacement, route through the owning single-writer archive-replace-restamp-reindex process.

## Chain Authority

Authority states:

- `role_only`: execute the requested role and stop.
- `analysis_chain`: continue only among read-only or state/evidence-writing operations within the same bounded objective.
- `packet_chain`: produce a packet or continuation prompt, then stop before executing it.
- `bounded_build`: mutate the named artifact only within explicit target, action, and scope authority.
- `verification_chain`: verify the artifact or claim explicitly named by the prior step.
- `blocked`: no meaningful continuation without missing authority, source, capability, or user decision.

The current route may propose a next route, but proposal is not authority. The router may downgrade or stop by inference; it must not upgrade authority by inference.

Artifact mutation, install, activation, deployment, release status changes, readiness claims, artifact stamping, archive transactions, broad implicit routing, and replacement of external canonical artifacts require explicit user authority and any required governing transaction.

Short approval replies such as `proceed`, `approved`, `yes`, `do it`, `execute`, `go`, or `continue` may authorize only the most recent recommended move when that move is bounded, unambiguous, and still current. Shorthand approval inherits the prior source basis, evidence ceiling, context decision, route option, and authority boundary. It does not authorize blocked actions, alternate route options, future phases, evidence upgrades, or high-authority actions unless those were explicitly named and permitted.

## Auto-Continue Rule

Continuation decisions:

- `continue_same_role`
- `continue_readonly_support`
- `continue_verification`
- `stop_with_recommended_move`
- `stop_with_operator_prompt`
- `ask_for_authority`
- `require_fresh_context`
- `blocked`

Auto-continuation may proceed only when all are true:

- the current route is explicit or part of an explicitly authorized chain;
- `chain_state` is `next-step-known`;
- exactly one primary next route is identified;
- the next route is same-scope or narrower;
- the authority state covers the next action;
- no stop gate is active;
- work-object boundaries remain intact;
- evidence stage is not upgraded by inference;
- required sources and acting references are available;
- fresh context is not required;
- mutation is not performed unless `bounded_build` authority exists.

If any condition fails, stop with the recommended move, provide an operator prompt only when it materially helps, ask for authority, require fresh context, or mark blocked.

## Command Continuation Matrix

| Command | May continue to | Must stop before |
|---|---|---|
| `/align` | Same-role clarification; scoped `/design`, `/review`, `/research`, or stop when authority is clear | Downstream material execution without explicit command authority |
| `/design` | Scoped `/align`, `/research`, `/review`, `/compare`, `/handoff`, or stop with `/build` recommendation | File creation, implementation, readiness claims, or action beyond design authority |
| `/build` | Same-role verification; `/review`, `/diagnose`, `/handoff`, or stop | Unauthorized mutation, rewrite/N+2 expansion, install, deploy, delete, readiness claims |
| `/review` | `/diagnose`, `/build` recommendation, `/research`, `/handoff`, or stop | Artifact edits, full root-cause repair, readiness Green without evidence |
| `/compare` | `/design`, `/build` recommendation, `/review`, or stop | Silent merge, synthesis, or missing criteria/candidates |
| `/diagnose` | `/build` recommendation, `/review`, `/research`, `/handoff`, or stop | Repair, retest, permanent-prevention claim |
| `/research` | `/review`, `/design`, `/build` recommendation, or stop | Artifact edits, current/latest claims without retrieval, plan updates without authority |
| `/handoff` | Usually stop after packet; may name any next command as packet instruction | Executing the packet's next role, rewriting artifacts, compression of substantive artifacts |

## Support Operations

For material design and other high-coupling routes:

- `/align` is orientation: scope, authority, constraints, success criteria.
- `/research` is external draw: donor sources, current facts, provenance, provider facts, external evidence.
- `/design` is synthesis: target architecture, specification, plan, or workflow.
- `/review` is internal assessment: completeness, consistency, evidence limits, risk, build-readiness.
- `/build` is materialization: authorized artifact mutation only.

The router coordinates these operations. It does not turn them into agent roles or absorb their internal procedures.

## Stop Gates

Stop gates override `next_allowed`, Chain Authority, and auto-continuation.

Global gates:

- `authority_missing`
- `mutation_without_bounded_build`
- `irreversible_or_external_action`
- `evidence_upgrade`
- `readiness_or_release_claim`
- `context_separation_required`
- `source_basis_missing`
- `work_object_crossing`
- `completion_integrity`
- `scope_drift`
- `review_owed`
- `research_owed`
- `multiple_next_routes`
- `artifact_reference_unresolved`
- `acting_reference_required`
- `stale_pin`
- `active_index_mismatch`
- `loadable_content_missing`
- `archive_transaction_required`
- `concurrent_writer_detected`
- `unindexed_governed_artifact`

Command-specific gates should preserve each command boundary:

- `/align`: stop before downstream role execution unless separately authorized.
- `/design`: stop before file creation, implementation, or readiness claims.
- `/build`: stop on missing path/scope/overwrite authority; verify before claiming written or complete.
- `/review`: stop before edits or root-cause repair; block readiness Green without required evidence.
- `/compare`: stop before merge or synthesis unless `/build` is authorized.
- `/diagnose`: stop before repair, retest, or permanent-prevention claims.
- `/research`: stop before artifact or plan updates unless `/build` or `/design` is separately authorized.
- `/handoff`: stop before executing the packet's next role.

## Closeout Discipline

Material routes should close with enough information to support continuation control:

```yaml
router_closeout:
  status: complete | next-step-known | alignment-needed | blocked | no-material-change-needed
  command_completed: /align | /design | /build | /review | /compare | /diagnose | /research | /handoff
  mode_used: string | null
  work_object_written: state | artifact | evidence | packet | none
  object_subtype_written: design_artifact | production_artifact | source_artifact | transport_packet | null
  evidence_stage: design-time | simulated | live-runtime | post-implementation | production-observed
  claim_scope: string
  action_authority_used: string
  source_basis_used: list
  acting_reference_status: planning-only | resolved | unresolved | stale | mismatch | not-applicable
  stop_gates_active_or_checked: list
  review_owed: none | before-build | before-gate | after-build | independent
  research_owed: none | source-map | current-fact-check | donor-gap | provider-capability-check
  verification_owed: string | none
  reference_owed: none | chain-router-reference | artifact-reference | skill-local-reference
  recommended_move: string | null
  route_options: list
  approval_contract: string | null
  operator_prompt: string | null
  next_route: object | null
  next_allowed: true | false
  prohibited_next_actions: list
```

Evidence stage must be scoped to the exact claim and object. Verification of one edit does not establish package readiness, runtime behavior, cross-model parity, or production-observed behavior.

User-facing closeout should lead with executive judgment and recommended movement. `next_route` remains internal routing metadata; do not make a command snippet the center of gravity when the user needs judgment, a fork, a decision, or a stop condition.

## Adversarial Review

Adversarial review is required by default before building material changes to:

- routing or command selection;
- authority or mutation gates;
- object-boundary rules;
- evidence ceilings;
- stop gates;
- artifact identity or acting-reference semantics;
- eval gates;
- stateful workflow behavior;
- autonomy or continuation policy.

A low-risk local edit may waive adversarial review only when closeout records why it was not material.

Adversarial cases should test overactivation, unauthorized mutation, stale artifact references, evidence upgrades, review/research owed handling, mode-boundary leakage, broad implicit routing, completion-integrity failures, and handoff/artifact compression confusion.

## Reference Evolution

This reference is expected to grow as evals, adversarial reviews, and runtime observations expose new traps. Prefer adding detailed schemas, matrices, examples, and failure cases here before increasing the size of `KERNEL.md`.

Promote a rule from this reference into `KERNEL.md` only when it must be always visible to preserve authority, evidence, object boundaries, stop behavior, or explicit invocation.
