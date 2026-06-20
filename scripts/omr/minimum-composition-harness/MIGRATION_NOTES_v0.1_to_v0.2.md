# Migration Notes — v0.1 Anthropic API to v0.2 Codex CLI

## Required user change

Use the v0.2 folder as a new harness installation. Do not overwrite an already-started v0.1 run series.

## Provider change

```yaml
provider:
  type: codex_cli
  binary: codex
  auth_mode: chatgpt
  model: gpt-5.5
  reasoning_effort: high
  model_verbosity: low
```

No `ANTHROPIC_API_KEY` is used. The harness calls the user's existing authenticated Codex CLI.

## Experiment content unchanged

The five governing authorities, P1–P7, executor fixture view, selector logic, state schemas, evidence rules, Case 8 boundary, blinding, and evaluator handoff are unchanged.

## New operational behavior

- JSONL Codex trace capture;
- exact Codex thread ID and token usage;
- safe automatic pause on usage-window exhaustion;
- archived partial attempts;
- continuation without rerunning complete attempts;
- immutable run config/source check on resume;
- `mch usage-summary`;
- batch helper scripts.

## Do not merge old run evidence

A v0.1 Anthropic run and a v0.2 Codex run are different provider series. They may later be compared as separate replications, but their raw attempts must not be combined into one run series.
