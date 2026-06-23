# Dogfood Install Protocol

Version: `0.1.0`
Status: rollout lab candidate
Evidence ceiling: design-time unless specific static, simulated, live-runtime, or post-implementation evidence is recorded.

## Purpose

Define how UAM Bridge Skills may move from source-only development into controlled dogfood use without collapsing into unauthorized global installation, broad implicit routing, v1 release, or readiness claims.

This protocol does not authorize installation, activation, deployment, release-status changes, provider-profile replacement, or global skill registration. It defines the gates that must be satisfied before those actions can be separately authorized.

## Governing Limits

The manifest remains controlling:

- `global_install_authorized: false`
- `activation_authorized: false`
- v0.1 permitted use is source review, adapter drafting, and eval fixture expansion.
- v0.1 prohibited use includes global installation, v1 deployment, broad implicit routing, and production readiness claims.
- v1 remains `blocked_until_gates_pass`.

The kernel remains controlling:

- Explicit command invocation comes first.
- Broad implicit routing is disabled for v0.1.
- Artifact mutation requires explicit bounded `/build` authority.
- `next_allowed` is not action authority.
- Evidence stage must be scoped to the exact claim and object.

## Evidence Labels

Use the narrowest accurate evidence label.

| Label | Meaning |
|---|---|
| `design-time` | Reasoned from source review, architecture, fixture design, or static inspection. |
| `static validation` | Parsed, schema-checked, or otherwise validated without running prompts or observing model behavior. |
| `simulated` | Behavior observed under controlled prompts, fixtures, dry runs, or non-live evaluator scoring. |
| `live-runtime` | Behavior observed in an active provider/runtime environment. |
| `post-implementation` | Verification after a specific implemented adapter or source change. |
| `production-observed` | Repeated real-world behavior after approved deployment. |

Do not convert one label into another by implication. A successful source patch, static validator pass, or local dry run does not establish package readiness, cross-model parity, production behavior, or v1 release eligibility.

## Stage 0: Source-Only Lab

Current default state.

Prerequisites:

- Canonical package remains under `uam-bridge-skills/`.
- Manifest, kernel, skills, lenses, evals, and docs remain source artifacts.
- Static validation can be run without changing provider profiles.

Allowed:

- Build, review, patch, and expand source files.
- Draft adapters from canonical source.
- Expand routing, object-integrity, evidence-ceiling, degradation, overactivation, blind value proposition, and cross-model parity fixtures.
- Run static validators and design/simulated checks.

Not allowed:

- Copy files into global or provider profile skill locations.
- Activate provider adapters.
- Enable broad implicit routing.
- Claim v1, runtime reliability, cross-model parity, or readiness.

Rollback:

1. Identify changed source files and the last known good revision.
2. Revert only affected source package files.
3. Preserve unrelated user changes.
4. Re-run manifest consistency and design-time/static checks.
5. Record the failure and fix layer before retrying.

## Stage 1: Local Dry-Run Dogfood

Use the skills as local source references during UAM Bridge skill-building, without installing them into a provider skill directory.

Prerequisites:

- Stage 0 is intact.
- Static validator passes for relevant YAML fixtures.
- Known gaps are recorded.
- The task remains within source-package development or bounded skill-building.

Allowed:

- Invoke `/align`, `/design`, `/build`, `/review`, `/compare`, `/diagnose`, `/research`, and `/handoff` explicitly while reading from source.
- Record friction, missed routing, overactivation, boundary drift, and evidence overclaims.
- Use dry-run outputs as simulated evidence only when prompts, outputs, scoring criteria, and environment notes are preserved.

Not allowed:

- Treat local source use as installed behavior.
- Claim runtime behavior or provider compatibility.
- Use dry-run convenience as a readiness gate.

Rollback:

1. Stop using the source package as the operating reference.
2. Preserve the observation as evidence if useful.
3. Route any remedy to `/diagnose` or authorized `/build`.

## Stage 2: Isolated Codex Dogfood Profile

Install only into a separate sandbox or profile-specific Codex environment. This is not global installation.

Prerequisites:

- Explicit user authorization names the target profile or install path.
- Current provider profile or configuration is backed up.
- Exact source version, installed paths, and source hashes are recorded.
- Smoke checks are defined before installation.
- No critical static review findings remain open for routing, authority, object boundaries, evidence ceilings, stop gates, or rollback.

Allowed:

- Explicit-command use only.
- Bounded UAM Bridge skill-building tasks.
- Runtime observation in the isolated profile.
- Post-install smoke checks for routing, object integrity, evidence ceiling, degradation, and overactivation.

Not allowed:

- Default/global profile installation.
- Broad implicit routing.
- v1 release or readiness claims.
- Cross-provider claims from Codex-only evidence.

Rollback:

1. Disable any implicit routing first.
2. Remove or deactivate installed sandbox adapter files.
3. Restore the backed-up provider profile or configuration.
4. Confirm the old profile behavior is active.
5. Record residual files or settings that still need cleanup.

## Stage 3: Limited Explicit-Command Pilot

Use the isolated dogfood profile for real work, still explicit-command first.

Prerequisites:

- Stage 2 smoke checks pass or limitations are accepted explicitly.
- Runtime notes show no critical authority, object-boundary, evidence-ceiling, degradation, or overactivation failures.
- Rollback path is documented and available.
- Known limitations and non-goals are recorded.

Allowed:

- Pilot use for UAM Bridge skill-building and governed package work.
- Collection of runtime observations, failures, and improvement opportunities.
- Targeted patching only through authorized `/build`.

Not allowed:

- Broad implicit routing.
- Provider-wide activation.
- Production, v1, or cross-model claims.
- Release-status updates without a separate gate operation.

Rollback:

Use the Stage 2 rollback path. If any critical failure appears, pause pilot use before patching so the failure can be placed at the correct layer.

## Stage 4: Adapter Expansion

Draft and test other provider adapters from the canonical manifest after Codex dogfood has produced useful evidence without critical failures.

Prerequisites:

- Canonical source remains the authority.
- Provider capability profiles are rechecked against current official docs before adapter release.
- Adapter-specific degradation paths are specified.
- Cross-model parity cases are available for target providers.

Allowed:

- Provider-specific adapters derived from `MANIFEST.yaml`, `KERNEL.md`, and skill contracts.
- Provider-limited simulated or runtime checks.
- Capability-specific degradation notes.

Not allowed:

- Adapter behavior that redefines command ownership, writes, evidence ceilings, or stop gates.
- Capability claims without dated verification.
- Cross-model parity claims unless target providers have actually been tested.

Rollback:

1. Remove or deactivate the selected adapter only.
2. Restore provider-specific backup.
3. Keep canonical source unchanged unless a separately authorized source fix is needed.
4. Record adapter-specific failure and fix layer.

## Stage 5: Global Install Candidate

This stage is only a candidate state. It is not authorized by this protocol.

Prerequisites:

- v1 gates pass at the required evidence stage:
  - routing;
  - object integrity;
  - evidence ceiling;
  - degradation;
  - overactivation;
  - blind value proposition;
  - cross-model parity.
- Raw prompts, outputs, scoring, environment notes, and limitations are preserved.
- Rollback path is proven.
- User explicitly authorizes global install and names the target provider/profile.
- Release-status update is separately authorized through a gate/release operation.

Allowed only after explicit authorization:

- Candidate global install.
- Conservative activation under documented limitations.

Still not automatic:

- Broad implicit routing.
- Production readiness.
- Replacement or supersession of existing AB, OMR, Codex, Claude, ChatGPT, Gemini, or API artifacts.

Rollback:

Use the provider-install rollback path from `docs/governance/rollback.md`, then record the failure, affected version, source hashes, and restored profile state.

## Global Promotion Blockers

Do not promote any of the following globally:

- Source changes with only design-time or static-validation evidence.
- Chain Router Entry/Exit behavior that has not been tested beyond fixture review or manual simulation.
- Provider adapters with placeholder, stale, or unverified capability profiles.
- Broad implicit routing.
- Skills or adapters that overactivate on simple reversible tasks.
- Any behavior that treats `next_allowed` as mutation or execution authority.
- Any behavior that lets `/review` mutate artifacts, `/handoff` rewrite artifacts, `/compare` merge branches silently, or `/diagnose` repair without `/build`.
- Cross-model parity claims without target-provider evidence.
- Readiness, v1, production, or runtime claims beyond the available evidence stage.

## Critical Tripwires

Pause dogfood or roll back if any of these occur:

- Unauthorized mutation.
- Review/build boundary collapse.
- Handoff rewrites or compresses a substantive artifact.
- Evidence overclaim.
- Simple-task overactivation.
- Missing-capability fallback is hidden or misrepresented.
- `next_allowed` is treated as action authority.
- Adapter behavior diverges from canonical source ownership.
- Rollback cannot restore the prior profile.

## Minimum Dogfood Record

Each dogfood run or pilot change should record:

- source revision or hash when available;
- provider/profile used;
- installed paths, if any;
- command or scenario exercised;
- evidence label;
- observed behavior;
- failures or limitations;
- rollback status;
- next authorized operation, if any.

## Next Valid Operations

- `/review` this protocol against `MANIFEST.yaml`, `KERNEL.md`, `docs/governance/rollout-plan.md`, `docs/governance/rollback.md`, and `docs/governance/v1-release-gate.md`.
- `/build` add this document to any docs index or manifest only if separate source-indexing authority is granted.
- `/diagnose` any failed dogfood run before patching.

Do not proceed from this protocol directly to installation, activation, broad implicit routing, release-status update, or v1 readiness claim.
