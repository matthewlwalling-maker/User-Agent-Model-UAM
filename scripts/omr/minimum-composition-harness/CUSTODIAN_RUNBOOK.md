# Custodian Runbook v0.2 — Codex CLI

## 1. Confirm the environment

```powershell
codex --version
codex login status
python --version
```

Codex must already be authenticated. The harness uses that saved authentication.

## 2. Install the Python harness

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\setup_windows.ps1
.\.venv\Scripts\Activate.ps1
```

## 3. Smoke test

```powershell
Copy-Item configs\api_smoke.example.yaml configs\api_smoke.yaml
mch doctor --config configs\api_smoke.yaml --require-provider-auth
mch plan --config configs\api_smoke.yaml
mch run --config configs\api_smoke.yaml
mch validate-run --config configs\api_smoke.yaml
mch usage-summary --config configs\api_smoke.yaml
```

Do not treat smoke outputs as comparative evidence.

## 4. Holdouts

After the smoke test passes:

- select one unseen Material asset;
- select one unseen Trivial asset;
- complete one selection record for each;
- calculate and record SHA-256 hashes;
- do not modify the assets afterward.

Use `templates/holdout_selection_record_TEMPLATE.yaml`.

## 5. Freeze the official configuration

```powershell
Copy-Item configs\run_series.example.yaml configs\run_series.yaml
```

Populate the run ID, holdout paths, custodian, evaluator, and replicate count. Then run:

```powershell
mch doctor --config configs\run_series.yaml --require-provider-auth
mch plan --config configs\run_series.yaml > planned_official.json
```

Keep a separate copy of the config. The harness rejects config or source changes after the run series begins.

## 6. Execute continuously or in batches

Continuous:

```powershell
mch run --config configs\run_series.yaml
```

Batched:

```powershell
mch run --config configs\run_series.yaml --cases C01,C02,C03
mch usage-summary --config configs\run_series.yaml
```

Use the same config and run ID for every batch.

## 7. Usage-limit pause

When the run exits with code 4:

1. do not edit the config;
2. inspect `Run_Completeness_Report.md`;
3. wait for the usage window to reset or add Codex credits;
4. rerun the same command.

Do not use `mch recover` for this normal pause.

## 8. Model/platform failure

A completed failed attempt is evidence. Do not silently rerun it.

Only use recovery when an explicit platform failure warrants a separate retained attempt:

```powershell
mch recover --config configs\run_series.yaml --attempt-id "ATTEMPT_ID" --note "Exact reason"
```

The original attempt remains unchanged.

## 9. Completion and export

```powershell
mch validate-run --config configs\run_series.yaml
mch usage-summary --config configs\run_series.yaml
```

Export only when complete:

```powershell
mch export-evaluator `
  --config configs\run_series.yaml `
  --full-fixtures "C:\SECURE\P5_Comparative_Fixture_Pack_v0.1.yaml"
```

Keep the full fixture pack and evaluator companion outside the executor workspace.
