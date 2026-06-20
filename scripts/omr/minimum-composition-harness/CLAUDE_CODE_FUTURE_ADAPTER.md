# Future Cross-Model Adapter — Claude Code

## Answer

Yes. A future cross-model run can use **Claude Code** instead of requiring the Claude Console Messages API.

Claude Code supports a non-interactive/headless command:

```bash
claude -p "prompt" --output-format json
```

It can also return schema-constrained structured output with `--json-schema`, stream JSON events, expose a session ID and usage metadata, and authenticate through an individual Claude.ai Pro or Max account. This is sufficient to build a provider adapter similar to the Codex CLI adapter.

## What would stay frozen

A Claude Code replication must retain:

- P1–P7;
- fixtures and holdouts;
- operator/legacy prompt content;
- state validation;
- context conditions;
- raw capture;
- A/B blinding;
- evaluator procedure.

Only the provider adapter and provider-specific telemetry mapping should change.

## What must not happen

Do not mix Codex and Claude Code inside one architecture comparison cell. Both the operator prototype and legacy control must use the same model/provider configuration within a run series.

A Claude Code series is a **separate replication**, not an extension of the Codex run.

## Authentication choice

Claude Console billing is not mandatory for an individual Claude Code replication when Claude Code is authenticated with a Claude.ai Pro or Max subscription. Console/API, Teams/Enterprise, Bedrock, Vertex, or Foundry may still be preferable when predictable automation billing and organizational control matter.

## Deferred work

The v0.2 package intentionally does not include a Claude Code adapter. Adding it before the Codex smoke test would expand the implementation surface without helping the immediate objective.
