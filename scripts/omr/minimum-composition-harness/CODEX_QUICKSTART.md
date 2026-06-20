# Codex Harness Quickstart v0.3-current

This guide assumes:

- Codex CLI is already installed;
- you are already signed in and have used Codex successfully;
- the harness files are organized under `scripts/executor`;
- `authorities_current/` contains the current adopted source freeze;
- you are starting with the non-admissible smoke test, not the official comparison.

## Step 1 - Open PowerShell in the Harness Folder

```powershell
cd "C:\Users\Matthew\OneDrive\Documents\Custom Agent Building\Gatekeeper State Protocol\scripts\executor"
```

## Step 2 - Activate the Python Environment

When the harness Python environment does not exist yet:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\setup_windows.ps1
```

Then activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Step 3 - Confirm Codex is Available

```powershell
codex --version
codex login status
```

The second command must exit successfully.

## Step 4 - Run Local Preflight

The active `configs\api_smoke.yaml` is already refreshed for `authorities_current`.
It uses `auth_mode: auto` so the CLI can reuse your persisted login.

```powershell
mch doctor --config configs\api_smoke.yaml --require-provider-auth
```

Proceed only when the JSON result contains:

```json
"ok": true
```

## Step 5 - Inspect the Plan Before Spending Usage

```powershell
mch plan --config configs\api_smoke.yaml
```

The smoke test covers C01, C08A, and C08B. It is intentionally non-admissible evidence.

## Step 6 - Run the Smoke Test

```powershell
mch run --config configs\api_smoke.yaml
```

Possible exit states:

- exit `0`: the configured run is complete;
- exit `3`: the run is incomplete for a reason other than an automatic usage-window pause;
- exit `4`: Codex usage was exhausted and the harness paused safely.

When exit `4` occurs, do not change the config. Wait for usage to reset or add credits, then run the exact same command again. Completed attempts are skipped. An interrupted partial attempt is archived before being retried.

## Step 7 - Validate and Inspect Usage

```powershell
mch validate-run --config configs\api_smoke.yaml
mch usage-summary --config configs\api_smoke.yaml
Get-Content .\runs\api-smoke-current-20260619-C01-C08\Run_Completeness_Report.md
```

## Step 8 - Smoke-Test Decision

Proceed to a fuller run only when:

- the run is complete;
- no context-isolation proof failed unexpectedly;
- operator state validates;
- raw requests, JSONL events, final messages, and token records exist;
- no source or prompt changed during the smoke series.

A wrong model conclusion is evidence, not a software defect. Fix only harness or packaging defects before freezing the official run.
