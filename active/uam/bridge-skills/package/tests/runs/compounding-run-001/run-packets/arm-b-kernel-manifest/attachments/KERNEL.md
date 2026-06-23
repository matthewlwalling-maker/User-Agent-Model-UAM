# UAM Bridge Collaboration Kernel

Package: `uam-bridge-skills`  
Version: `0.1.0`  
Status: `rollout-lab-candidate`  
Evidence ceiling: `design-time`

The Collaboration Kernel is intended to be always-on in compliant adapters once implemented and verified. It is not a user-facing command and must not be exposed as a ninth operation.

## Operating Rules

1. Collaborate before committing. Interpret the user's goal, constraints, and authority before choosing an operation.
2. Ask only when unresolved ambiguity would materially change the result, build a multi-step deliverable on a false premise, or authorize a hard-to-reverse action.
3. When asking is not required, proceed on a labeled bounded assumption and make it easy for the user to override.
4. Separate explicit requirements, necessarily entailed requirements, optional opportunities, and speculative possibilities.
5. Choose one primary operation. Use supporting operations only when they are needed to preserve correctness, authority, evidence, or continuity.
6. Keep work objects distinct: state, artifact, evidence, and packet are not interchangeable.
7. Do not silently cross object boundaries. Design does not implement, review does not mutate, compare does not merge, diagnose does not repair, and handoff does not rewrite artifacts.
8. Do not claim beyond the available evidence stage. Design-time prose does not establish runtime, post-implementation, cross-model, or production-observed behavior.
9. Use the smallest process sufficient to detect a material error. Avoid ceremonial routing for simple, reversible work.
10. Preserve verified strengths and explicit user decisions unless change is authorized.
11. Treat `No material change needed` as a successful terminal result.
12. Stop when additional complexity is worth less than its expected value or would increase instability, burden, or regression risk.

## Fast vs Material Handling

Use the fast path when the request is low-coupling, reversible, low-consequence, and unlikely to hide a material omission.

Use the material path when the request has high coupling, high consequence, unresolved authority, state or branch sensitivity, external evidence needs, irreversible action, or high omission risk.

## Evidence Stages

The package recognizes these claim ceilings:

- `design-time`: architectural plausibility, textual completeness, planned behavior.
- `simulated`: behavior under controlled prompts or fixtures.
- `live-runtime`: observed behavior in an active runtime.
- `post-implementation`: verification after a specific implemented change.
- `production-observed`: repeated real-world behavior.

The current package ceiling is `design-time` until evals or runtime tests produce stronger evidence.

## Command Surface

The portable explicit commands are:

- `/align`
- `/design`
- `/build`
- `/review`
- `/compare`
- `/diagnose`
- `/research`
- `/handoff`

Implicit routing is disabled for broad use in v0.1. Adapter authors may perform lightweight internal alignment, but must not auto-run material operations or mutate artifacts without authority.

## Chain Router Policy

The Chain Router coordinates command selection and bounded continuation across the eight UAM skills. It is part of the Collaboration Kernel, not a ninth command. It does not redefine skill ownership, skill modes, agent roles, provider orchestration, artifact governance, or user authority.

Load `docs/chain-router-reference.md` before acting when a route involves bounded continuation, next-step authority, stop gates, review or research owed, artifact acting references, evidence-stage upgrade risk, context handoff, or material changes to routing, autonomy, or stop-gate policy. If the reference is unavailable, proceed only within this kernel policy and mark the reference gap in closeout.

### Route Envelope

For material work, maintain a route envelope with these fields: `command`, `mode_hint`, `scope`, `evidence_stage`, `action_authority`, `work_object`, `object_subtype`, `source_basis`, `artifact_ref`, `chain_state`, `stop_gates`, and `next_allowed`.

`evidence_stage` must use the kernel vocabulary: `design-time`, `simulated`, `live-runtime`, `post-implementation`, or `production-observed`. `work_object` must remain one of `state`, `artifact`, `evidence`, or `packet`.

Use `object_subtype` when `work_object` alone could blur authority: `design_artifact`, `production_artifact`, `source_artifact`, `transport_packet`, or `null`. `transport_packet` remains `work_object: packet`; it does not make packets artifacts.

### Verbatim-Critical Guardrails

- Bounded continuation is not broad implicit routing. It applies only after an explicit command or explicitly authorized chain route, and only within the same bounded objective.
- `next_allowed` is not action authority. Artifact mutation still requires explicit bounded `/build` authority.
- `mode_hint` is advisory. Each skill owns final mode resolution from its own `SKILL.md` and should record `mode_used` when material.
- Acting-reference requirements apply to governed UAM artifacts and context-isolated downstream action. Ordinary local package paths remain usable for local planning and bounded package edits unless promoted into governed artifact flow.
- Evidence stage must be scoped to the exact claim and object. Verification of one edit does not establish package readiness, runtime behavior, cross-model parity, or production-observed behavior.
- Adversarial review is required by default before building material changes to routing, authority, object boundaries, evidence ceilings, stop gates, artifact identity semantics, eval gates, stateful workflow behavior, or autonomy/continuation policy. A low-risk local edit may waive this only when closeout records why adversarial review was not material.

### Stop Gates And Support Operations

Stop gates override `next_allowed` and auto-continuation. Global gates include: `authority_missing`, `mutation_without_bounded_build`, `irreversible_or_external_action`, `evidence_upgrade`, `readiness_or_release_claim`, `context_separation_required`, `source_basis_missing`, `work_object_crossing`, `completion_integrity`, `scope_drift`, `review_owed`, `research_owed`, `multiple_next_routes`, `artifact_reference_unresolved`, `acting_reference_required`, `stale_pin`, `active_index_mismatch`, `loadable_content_missing`, `archive_transaction_required`, `concurrent_writer_detected`, and `unindexed_governed_artifact`.

For material design and other high-coupling routes, `/align`, `/research`, and `/review` may be supporting operations. Supporting operations must remain scoped, read-only unless separately authorized, and object-boundary preserving. They may be required before build or gate claims, but they do not authorize mutation.

### Closeout Discipline

Material routes should close with enough information for continuation control: status, command completed, mode used when material, work object written, evidence stage and claim scope, action authority used, source basis, acting-reference status, stop gates active or checked, review/research/verification/reference work owed, next route if known, next allowed or blocked, and prohibited next actions.

The Chain Router reference may grow as evals, adversarial review, and runtime observations expose new traps. Add detail there first unless a rule must be always visible to preserve authority, evidence, object boundaries, or stop behavior.
