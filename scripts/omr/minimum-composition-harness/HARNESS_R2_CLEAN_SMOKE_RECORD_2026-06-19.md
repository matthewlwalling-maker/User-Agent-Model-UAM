# Evaluation Record

- Run ID: `api-smoke-current-20260619-r2-C01-C08`
- Target revision: current-authority executor harness after O2 reference prompt patch.
- Evidence stage: live harness execution in the active Codex CLI environment; not independent evaluator scoring.
- Frozen goal/capability basis: `scripts/executor/configs/api_smoke_r2.yaml`, `scripts/executor/authorities_current/HARNESS_SOURCE_LOCK.json`, and `scripts/executor/authorities_current/P5_Executor_View_v0.1.yaml`.
- Fixtures and commands:
  - `mch doctor --config configs\api_smoke_r2.yaml`
  - `mch plan --config configs\api_smoke_r2.yaml`
  - `mch run --config configs\api_smoke_r2.yaml`
  - `mch validate-run --config configs\api_smoke_r2.yaml`
  - `mch usage-summary --config configs\api_smoke_r2.yaml`
- Raw output location: `scripts/executor/runs/api-smoke-current-20260619-r2-C01-C08/`

## Case Results

- `C01 / PB / operator`: failed. Failure source: `operator-O3-coverage`. O3 local validation reported `MCP-E330_COVERAGE_WITHOUT_BEHAVIOR_REF: CAP-4`.
- `C01 / PB / legacy`: completed.
- `C01 / SC / operator`: failed. Failure source: `state-schema-or-reference`. O4 local validation reported `stop_reason: '' should be non-empty`.
- `C01 / SC / legacy`: completed.
- `C08A / standard / operator`: completed.
- `C08A / standard / legacy`: completed.
- `C08B / standard / operator`: completed. O2 local validation passed; the prior `CT-*` in `obligation_refs` failure did not recur.
- `C08B / standard / legacy`: completed.

## Threshold Result

- Complete: true.
- Expected attempts: 8.
- Present attempts: 8.
- Failed attempts: 2.
- Invalid cells: 0.
- Remaining attempts: 0.

This is not a clean first-pass smoke pass because two operator attempts failed.

## Failure Classifications

- Observed O3 coverage artifact defect: an absent coverage entry for `CAP-4` used an empty `asset_behavior_refs` array, while local semantic validation requires every non-unknown coverage entry to cite at least one concrete asset behavior reference.
- Observed O4 schema/reference artifact defect: O4 emitted an empty `stop_reason`, violating the non-empty schema requirement.
- The earlier C08B O2 constraint/reference defect was not reproduced in r2.

## Evidence Limitations

- Same-context executor run; not blind, independent, or evaluator-scored.
- No holdouts were selected.
- No comparative verdict or OMR architecture promotion decision was produced.
- The original r1 first-pass failure and recovery remain separate evidence and are not pooled into this r2 result.

## Recommended Next Operation

Patch the operator prompt/schema-facing instructions for:

1. O3 absent coverage entries: require a concrete asset behavior reference for every non-unknown coverage classification, including `absent`, or require `unknown-insufficient-evidence` when no concrete behavior reference can be cited.
2. O4 stop fields: require non-empty `ChangeDecision.stop_reason` and wrapper `stop.code` / `stop.reason`.

Then run targeted retained recoveries for the two failed C01 operator attempts before considering another fresh full smoke.

## Targeted Recovery Result After O3/O4 Prompt Patch

Prompt patch:

- O3 now instructs every non-unknown coverage entry, including `absent`, to cite at least one concrete `asset_behavior_ref`; if no concrete behavior or explicit absence reference is available, the entry must be `unknown-insufficient-evidence`.
- O4 now instructs `ChangeDecision.stop_reason` and wrapper `stop.code` / `stop.reason` to be non-empty strings.

Commands:

- `mch recover --config configs\api_smoke_r2.yaml --attempt-id api-smoke-current-20260619-r2-C01-C08__C01__PB__r1__operator`
- `mch recover --config configs\api_smoke_r2.yaml --attempt-id api-smoke-current-20260619-r2-C01-C08__C01__SC__r1__operator`

Recovery attempts:

- `api-smoke-current-20260619-r2-C01-C08__C01__PB__r1__operator__recovery01`: completed; recovered_success true; trace completeness 1.0; O3 local validation valid.
- `api-smoke-current-20260619-r2-C01-C08__C01__SC__r1__operator__recovery01`: completed; recovered_success true; trace completeness 1.0; O4 local validation valid.

These recoveries do not erase or upgrade the original r2 first-pass failures. They verify the targeted O3/O4 prompt/schema-facing patches under separate retained recovery attempts.
