# Harness Refresh Record - 2026-06-19

## Scope

Refreshed the executor smoke harness/config against the current adopted compressed runtime source set.

## Current Authority Bundle

Active bundle:

`scripts/executor/authorities_current/`

Frozen files:

- `AGENTS.md`
- `AB_Runtime_Authority_Reference_v1.1.md`
- `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md`
- `OMR_Evidence_Capture_Protocol_v0.1.md`
- `OMR_Operator_Prototype_Runtime_v0.2.md`
- `P2_State_Schemas_v0.1.json`
- `P5_Executor_View_v0.1.yaml`
- `HARNESS_SOURCE_LOCK.json`

## Active Smoke Config

`scripts/executor/configs/api_smoke.yaml`

Run series:

`api-smoke-current-20260619-C01-C08`

Auth behavior:

- `auth_mode: auto`
- `ignore_user_config: false`
- `ephemeral: false`
- `history_persistence: none`

This keeps run history nonpersistent while allowing the CLI to reuse durable login state.

## Archived Outdated Materials

Archived under:

`scripts/executor/archive/outdated_2026-06-19/`

Contents include stale v0.2 split-source authorities, old smoke config variants, old planned smoke output, and previous executor handoff packets.

## Evidence Boundary

This is a post-implementation file/config refresh with one live current-authority smoke run executed afterward.

Live smoke run:

- Run folder: `scripts/executor/runs/api-smoke-current-20260619-C01-C08/`
- Expected attempts: 8.
- Present attempts: 8.
- Failed attempts retained as evidence: 1.
- Invalid comparative cells: 0.
- Failed attempt: `C08B / standard / operator`.
- Failure source: `state-schema-or-reference`.

Targeted recovery after O2 reference patch:

- Recovery attempt: `api-smoke-current-20260619-C01-C08__C08B__standard__r1__operator__recovery01`.
- Status: completed.
- Recovered success: true.
- O2 local validation: valid.
- Recovery preserved the original first-pass failure and wrote a separate recovery attempt plus manual-intervention record.

Fresh r2 smoke after O2 reference patch:

- Config: `scripts/executor/configs/api_smoke_r2.yaml`.
- Run folder: `scripts/executor/runs/api-smoke-current-20260619-r2-C01-C08/`.
- Expected attempts: 8.
- Present attempts: 8.
- Failed attempts retained as evidence: 2.
- Invalid comparative cells: 0.
- C08B operator completed first-pass; the O2 constraint/reference defect did not recur.
- Failed attempts: `C01 / PB / operator` and `C01 / SC / operator`.

Targeted retained recoveries after O3/O4 prompt patch:

- Recovery attempt: `api-smoke-current-20260619-r2-C01-C08__C01__PB__r1__operator__recovery01`.
- Status: completed.
- Recovered success: true.
- O3 local validation: valid.
- Recovery attempt: `api-smoke-current-20260619-r2-C01-C08__C01__SC__r1__operator__recovery01`.
- Status: completed.
- Recovered success: true.
- O4 local validation: valid.
- Recoveries preserved the original r2 first-pass failures and wrote separate recovery attempts plus manual-intervention records.

The smoke result is not a comparative score, independent evaluator verdict, holdout selection, official run certification, or OMR architecture verdict.
