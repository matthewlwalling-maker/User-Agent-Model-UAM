# Change Record

- Target revision: `scripts/executor` current-authority smoke harness, run series `api-smoke-current-20260619-C01-C08`.
- Authorized action: patch and targeted retest.
- Authorized boundary: O2/operator prompt or schema-reference handling so constraints are not emitted as `obligation_refs`, then rerun targeted C08B smoke.
- Files/components changed: `src/mcp_harness/prompts.py`, `tests/test_harness.py`, validation/result records.
- Direct dependencies changed: O2 prompt contract and deterministic regression coverage for O2 `CapabilityModel` reference IDs.
- Preserved elements: P2 source schema, OMR authority files, original first-pass smoke artifacts, original failed C08B attempt.
- Prohibited propagation respected: no source-authority rewrite, no schema relaxation, no overwrite of first-pass evidence, no full smoke rerun.
- Tests run: `pytest tests --basetemp .pytest_tmp`; `mch doctor --config configs\api_smoke.yaml`; `mch validate-run --config configs\api_smoke.yaml`; `mch recover --config configs\api_smoke.yaml --attempt-id api-smoke-current-20260619-C01-C08__C08B__standard__r1__operator`.
- Test results: pytest 16/16 pass; doctor pass; validate-run complete with original 1 retained failed first-pass attempt and 0 invalid cells; targeted recovery `api-smoke-current-20260619-C01-C08__C08B__standard__r1__operator__recovery01` completed with `recovered_success: true`.
- Regressions or residual risk: recovery is not a new first-pass comparative result and does not promote the original run to an official verdict. Original C08B first-pass failure remains retained evidence. No independent evaluator scoring or holdout run was produced.
- Next authorized operation: none required for the requested patch/recovery. Optional next operation is a fresh frozen smoke or evaluator package if a clean first-pass comparison is needed.
