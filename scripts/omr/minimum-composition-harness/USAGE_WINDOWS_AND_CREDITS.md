# Usage Windows and Credits Decision Guide

## Decision

The official comparison **can be spread across Codex usage windows**. Credits are not technically required.

For the authoritative run, the recommended rule is:

- use included usage when the smoke-test projection suggests the full run will finish within roughly one or two usage windows;
- add credits when the projection suggests three or more windows, repeated mid-attempt pauses, or a run stretching across multiple days.

Credits do not improve reasoning quality. They reduce interruption and shorten the period in which a CLI or backend model revision could change. The harness now refuses to resume the same run series if the Codex executable path or CLI version changed. A backend revision behind the same model name cannot be cryptographically pinned through ChatGPT-authenticated Codex, so completing the official series in a short period is still preferable.

## Why multi-window execution remains valid

The v0.2 harness preserves the conditions needed for a valid continuation:

- one frozen run-series ID;
- one frozen config checksum;
- one frozen Codex executable path and CLI version;
- one frozen source set;
- one frozen A/B key covering the complete planned series;
- completed attempts are never rerun;
- interrupted attempts are archived;
- each attempt has its own fresh Codex thread;
- both systems for a selected fixture are run by the same harness configuration;
- usage-window pauses are logged as platform events, not scored as architecture failures.

A time gap alone does not invalidate the comparison. A changed model, source, prompt, reasoning setting, fixture, or config does.

## Beginner-safe process

### 1. Do not buy credits before the smoke test

Use included Codex access to run C01/C08. Then inspect:

```powershell
mch usage-summary --config configs\api_smoke.yaml
```

Also check Codex Settings → Usage or `/status` in an interactive Codex session.

### 2. Estimate the official run from observed usage

Use the smoke result as a planning anchor, not a precise forecast:

1. note completed attempts and estimated credits;
2. divide estimated credits by completed attempts;
3. multiply by the official planned attempt count;
4. add a substantial reserve because holdouts and disagreement cases may be longer.

The harness reports an estimate using the June 2026 GPT-5.5 token rate card. Your included plan allowance and account-specific limits are not inferred.

### 3. Choose one of two paths

#### Path A — No added credits

Use case batches and wait for windows to reset.

Recommended batch boundaries:

1. `C01,C02,C03`
2. `C04,C05,C06`
3. `C07,C08A,C08B`
4. `C09A,C09B,C10`
5. `C11,C12,HOLDOUT-MATERIAL-01,HOLDOUT-TRIVIAL-01`

After every batch:

```powershell
mch usage-summary --config configs\run_series.yaml
mch validate-run --config configs\run_series.yaml
```

Do not edit the config between batches.

#### Path B — Add credits

Use credits when the Usage dashboard indicates the included allowance is unlikely to finish the planned series without several pauses. Then run the full frozen config:

```powershell
mch run --config configs\run_series.yaml
```

Credits improve continuity; they do not improve model quality or change scoring.

## Automatic pause behavior

When Codex reports a usage/rate/credit limit:

- the harness stops the series;
- no completed attempt is overwritten;
- the partial attempt directory is preserved;
- the pause is logged as non-contaminating platform evidence;
- rerunning the same command after reset resumes the series.

Do not use `mch recover` for a normal usage-window pause. Recovery is for a retained failed model/platform attempt with a completed failure record.

## When multi-window execution should be abandoned

Start a new run series instead when any of these changes between windows:

- model name;
- reasoning effort;
- Codex CLI version after a material update;
- source or fixture digest;
- holdout content;
- prompt or schema;
- run configuration;
- system ordering or evidence visibility.

## Recommendation

Run the smoke test with included usage first. Spread the official run across complete case batches unless the observed smoke usage suggests more than two or three windows or creates frequent mid-attempt pauses. At that point, credits are the cleaner and more reliable option.
