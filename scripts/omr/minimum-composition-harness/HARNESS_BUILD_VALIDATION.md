# Harness Build Validation Record v0.3-current

Date: 2026-06-19

## Scope

Current-authority smoke refresh for the Codex CLI executor harness.

## Construction Checks

- Active smoke config points at `authorities_current/`.
- Active smoke config uses `auth_mode: auto` and does not pass `--ignore-user-config` by default.
- `authorities_current/HARNESS_SOURCE_LOCK.json` freezes the adopted compressed runtime source set.
- Source verification checks the lock file dynamically and requires current adopted AB/OMR sources.
- Operator prompt loading uses `OMR_Operator_Prototype_Runtime_v0.2.md` and `OMR_Evidence_Capture_Protocol_v0.1.md`.
- Legacy prompt loading uses `AB_Runtime_Authority_Reference_v1.1.md` and `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md`.
- Stale v0.2 split authorities, smoke variants, planned-smoke output, and handoffs are archived under `archive/outdated_2026-06-19/`.
- O2 prompt now explicitly forbids `CT-*` constraint IDs in `CapabilityModel.capabilities[*].obligation_refs` and `CapabilityModel.obligation_coverage[*].obligation_ref`; constraints may only inform behavior/rationale text.
- O3 prompt now explicitly requires every non-unknown coverage entry, including `absent`, to cite at least one concrete `asset_behavior_ref`; if no concrete behavior or explicit absence reference is available, the entry must be `unknown-insufficient-evidence`.
- O4 prompt now explicitly requires non-empty `ChangeDecision.stop_reason` and non-empty wrapper `stop.code` / `stop.reason`.

## Tests

- Python compilation: pass.
- Pytest deterministic suite: 16/16 pass after O2 reference patch.
- Source verification for `configs/api_smoke.yaml`: pass, 7/7 frozen source records matched.
- `mch doctor --config configs\api_smoke.yaml`: pass for source/config/schema checks.
- `mch plan --config configs\api_smoke.yaml`: pass; 3 fixture cells, 4 condition/replicate cells, 8 system attempts.
- `mch doctor --config configs\api_smoke.yaml --require-provider-auth`: pass after durable Codex ChatGPT login was reused.
- `mch run --config configs\api_smoke.yaml`: complete; 8/8 attempts present.
- `mch validate-run --config configs\api_smoke.yaml`: complete; 1 failed system attempt retained as evidence, 0 invalid/missing comparative cells.
- `mch recover --config configs\api_smoke.yaml --attempt-id api-smoke-current-20260619-C01-C08__C08B__standard__r1__operator`: completed targeted recovery attempt after O2 reference patch.
- `mch recover --config configs\api_smoke_r2.yaml --attempt-id api-smoke-current-20260619-r2-C01-C08__C01__PB__r1__operator`: completed targeted recovery attempt after O3 coverage-reference patch.
- `mch recover --config configs\api_smoke_r2.yaml --attempt-id api-smoke-current-20260619-r2-C01-C08__C01__SC__r1__operator`: completed targeted recovery attempt after O4 stop-field patch.

## Live Smoke Result

Run folder:

`scripts/executor/runs/api-smoke-current-20260619-C01-C08/`

Observed result:

- Complete: true.
- Expected attempts: 8.
- Present attempts: 8.
- Failed attempts: 1.
- Invalid comparative cells: 0.
- Failed attempt: `C08B / standard / operator`.
- Failure source: `state-schema-or-reference`.

The failed C08B operator attempt did not indicate a CLI/login or harness-execution failure. O1 produced a valid `GoalContract`; O2 produced an invalid `CapabilityModel` because it placed `CT-*` constraint IDs in fields whose schema accepts only `OB-*` obligation references.

## Targeted Recovery Result

Recovery attempt:

`scripts/executor/runs/api-smoke-current-20260619-C01-C08/attempts/api-smoke-current-20260619-C01-C08__C08B__standard__r1__operator__recovery01/`

Observed result:

- Status: completed.
- Recovered success: true.
- Trace completeness: 1.0.
- O2 local validation: valid.
- O2 `obligation_refs`: only `OB-1` and `OB-2`.
- O2 `obligation_coverage.obligation_ref`: only `OB-1` and `OB-2`.
- Terminal O4 visible answer: blocked by insufficient impact/dependency evidence at design-time ceiling.

The recovery does not erase or upgrade the original first-pass failure. It verifies the targeted O2 prompt patch under a separate retained recovery attempt.

## Fresh R2 Smoke Result

Run folder:

`scripts/executor/runs/api-smoke-current-20260619-r2-C01-C08/`

Observed result:

- Complete: true.
- Expected attempts: 8.
- Present attempts: 8.
- Failed attempts: 2.
- Invalid comparative cells: 0.
- Failed attempt: `C01 / PB / operator`; failure source `operator-O3-coverage`.
- Failed attempt: `C01 / SC / operator`; failure source `state-schema-or-reference`.
- `C08B / standard / operator`: completed first-pass; O2 local validation passed.

The r2 smoke confirms the C08B O2 constraint/reference defect did not recur, but it is not a clean first-pass smoke pass because two C01 operator attempts failed.

## Targeted R2 Recovery Result

Recovery attempts:

- `scripts/executor/runs/api-smoke-current-20260619-r2-C01-C08/attempts/api-smoke-current-20260619-r2-C01-C08__C01__PB__r1__operator__recovery01/`
- `scripts/executor/runs/api-smoke-current-20260619-r2-C01-C08/attempts/api-smoke-current-20260619-r2-C01-C08__C01__SC__r1__operator__recovery01/`

Observed result:

- `C01 / PB / operator` recovery: completed; recovered success true; trace completeness 1.0; O3 local validation valid.
- `C01 / SC / operator` recovery: completed; recovered success true; trace completeness 1.0; O4 local validation valid.

The recoveries do not erase or upgrade the original r2 first-pass failures. They verify the targeted O3/O4 prompt/schema-facing patches under separate retained recovery attempts.

## Limitations

- Direct sandboxed `codex login status` checks can still fail because the restricted shell cannot access the durable CLI login state; the escalated provider/auth check passed.
- The live smoke is a harness/provider execution result, not independent evaluator scoring, holdout selection, official run certification, or comparative verdict.
- The original C08B first-pass operator failure remains retained evidence. The targeted recovery passed after patching O2 prompt/reference instructions.
- The fresh r2 smoke produced two new first-pass operator failures in C01 and should not be treated as a clean pass.
- Targeted retained recoveries for both C01 operator failures passed after O3/O4 prompt/schema-facing patches; the original r2 first-pass failures remain retained evidence.

## Disposition

`R2 CURRENT-AUTHORITY SMOKE COMPLETE; C08B O2 PATCH HELD; C01 TARGETED RECOVERIES PASSED; FIRST-PASS FAILURES RETAINED`
