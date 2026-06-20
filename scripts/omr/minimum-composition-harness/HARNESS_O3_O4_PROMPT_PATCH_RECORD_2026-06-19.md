# O3/O4 Prompt Patch Record - 2026-06-19

## Scope

Patched the operator prompt/schema-facing instructions for the two retained C01 operator failures observed in `api-smoke-current-20260619-r2-C01-C08`.

## Source Failures

- `api-smoke-current-20260619-r2-C01-C08__C01__PB__r1__operator`: failed at O3 local validation with `MCP-E330_COVERAGE_WITHOUT_BEHAVIOR_REF: CAP-4`.
- `api-smoke-current-20260619-r2-C01-C08__C01__SC__r1__operator`: failed at O4 local validation with `stop_reason: '' should be non-empty`.

## Patch

Changed `scripts/executor/src/mcp_harness/prompts.py`:

- O3 now requires every non-unknown coverage entry, including `absent`, to cite at least one concrete `asset_behavior_ref`.
- O3 now instructs the operator to use `unknown-insufficient-evidence` instead of `absent` when no concrete behavior or explicit absence reference can be cited.
- O4 now requires non-empty `ChangeDecision.stop_reason` and wrapper `stop.code` / `stop.reason`.

Changed `scripts/executor/tests/test_harness.py`:

- Added regression assertions that the operator prompt contains the O3 absent/unknown guardrail and O4 non-empty stop-field guardrail.

## Validation

- `python -m pytest tests --basetemp .pytest_tmp`: 16 passed, 1 pytest cache warning.
- `mch doctor --config configs\api_smoke_r2.yaml`: pass.

## Targeted Retained Recoveries

- `api-smoke-current-20260619-r2-C01-C08__C01__PB__r1__operator__recovery01`: completed; recovered_success true; trace completeness 1.0; O3 local validation valid.
- `api-smoke-current-20260619-r2-C01-C08__C01__SC__r1__operator__recovery01`: completed; recovered_success true; trace completeness 1.0; O4 local validation valid.

## Evidence Boundary

This is live harness execution in the active Codex CLI environment for targeted retained recoveries. It is not independent evaluator scoring, a clean first-pass r2 smoke pass, holdout selection, comparative verdict, official run certification, or OMR architecture promotion.

The original r2 first-pass failures remain retained evidence. The recovery attempts separately verify the targeted prompt/schema-facing patches.
