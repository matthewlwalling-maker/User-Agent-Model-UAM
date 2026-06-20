# Minimum Composition Current-Authority Harness v0.3-current - Codex CLI

This package runs the four-operator prototype and unchanged legacy Goal-Completeness control through the locally installed Codex CLI.

The active smoke path is refreshed for the adopted compressed runtime source set in `authorities_current/`.

## Current Scope

The harness:

- invokes `codex exec` non-interactively;
- freezes current adopted AB/OMR runtime sources through `authorities_current/HARNESS_SOURCE_LOCK.json`;
- uses GPT-5.5 with one frozen reasoning setting for both systems;
- captures JSONL events, thread IDs, final messages, usage, and latency;
- disables web search, shell tools, project rules, and writable access;
- reuses persisted Codex CLI auth by default (`auth_mode: auto`, `ignore_user_config: false`);
- enforces PB/SC context construction;
- validates operator state against P2;
- retains failures and interrupted attempts;
- supports safe continuation across Codex usage windows while enforcing a frozen config, source set, Codex executable, and CLI version;
- creates blinded evaluator packets only after the full configured series is complete.

The harness does not score either architecture.

## Fast Start

```powershell
cd "C:\Users\Matthew\OneDrive\Documents\Custom Agent Building\Gatekeeper State Protocol\scripts\executor"
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\setup_windows.ps1
.\.venv\Scripts\Activate.ps1

codex login status
mch doctor --config configs\api_smoke.yaml --require-provider-auth
mch plan --config configs\api_smoke.yaml
mch run --config configs\api_smoke.yaml
mch validate-run --config configs\api_smoke.yaml
mch usage-summary --config configs\api_smoke.yaml
```

See [CODEX_QUICKSTART.md](CODEX_QUICKSTART.md) for the beginner workflow.

## Evidence Status

The refreshed harness must pass local deterministic tests and `mch doctor` before a live smoke run. It has not produced an authoritative comparison.
