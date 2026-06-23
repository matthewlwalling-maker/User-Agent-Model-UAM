# Blind Run 001 Attempt 002 Orchestration

Run id: `blind-run-001`
Attempt id: `attempt_002`
Status: `prepared_not_run`
Purpose: patch the runtime orchestration gap that made `attempt_001` non-blind simulated.
Evidence ceiling before execution: `design-time orchestration plan`

## Why Attempt 002 Is Needed

`attempt_001` produced useful dry-run artifacts, but it was not blind evidence. The target and baseline arms were generated in one already-informed runner context after the UAM Bridge package had been loaded. That contaminates the baseline condition.

The material gap is not in the frozen UAM Bridge package. The gap is in runtime orchestration: the run must create separate fresh arm contexts before prompt generation.

## Required Execution Topology

Use three role surfaces:

1. `runner_coordinator`
   - May read `runner-packet.md`, `freeze-record.md`, and this orchestration file.
   - May assign prompts to fresh arm contexts.
   - May collect raw outputs, randomize labels, create anonymized outputs, and preserve the mapping key.
   - Must not score, diagnose, or read evaluator materials.
   - Must not generate both arm outputs itself after loading target materials.

2. `target_arm_context`
   - Fresh context.
   - May read the frozen UAM Bridge package files identified by `freeze-record.md`.
   - Receives one case prompt and supplied context at a time, or all cases if the context remains target-only.
   - Must not read evaluator packet, hidden traps, scoring criteria, baseline outputs, anonymized outputs, or mapping key.

3. `baseline_arm_context`
   - Fresh context.
   - Receives only this neutral instruction:

```text
You are a helpful assistant. Answer the user's request directly and carefully. Do not use UAM Bridge Skills, command routing rules, or the UAM package.
```

   - Receives the same case prompt and supplied context as the target arm.
   - Must not read UAM Bridge package files, UAM command routing rules, target outputs, evaluator packet, hidden traps, scoring criteria, anonymized outputs, or mapping key.

## Context Granularity

Preferred: one fresh target context and one fresh baseline context per case.

Acceptable: one fresh target context for all target outputs and one fresh baseline context for all baseline outputs, provided each remains arm-pure and no target material enters the baseline context.

Not acceptable: one context generates both target and baseline outputs after reading UAM Bridge files or target-arm behavior.

## Attempt 002 Output Files

Create only these attempt-specific run artifacts:

- `raw-outputs-attempt_002.md`
- `anonymized-outputs-attempt_002.md`
- `mapping-key-attempt_002.local.md`
- optional `orchestration-log-attempt_002.md` if context ids, tool outputs, or manual interventions need a separate record.

Do not overwrite `attempt_001` artifacts.

## Preflight Checklist

Before generating outputs:

- `freeze-record.md` source hashes still pass.
- `runner_coordinator` has not read `evaluator-packet.md`.
- `target_arm_context` is fresh and target-only.
- `baseline_arm_context` is fresh and baseline-only.
- the baseline context receives no UAM Bridge source, command routing rules, target output, mapping key, hidden traps, or scoring criteria.
- the target context receives no evaluator packet, hidden traps, scoring criteria, or mapping key.
- provider, model, date, tool access, and capability profile are recorded for each arm context.
- any unavailable isolation requirement causes a stop with status `blocked_orchestration`.

## Pressure Test: Can This Thread Still Run Attempt 002?

Assumption under test: the current Codex thread can still run `attempt_002` as blind evidence.

Result: `conditionally false as stated`.

Reason: this current thread is already contaminated for arm generation. It has read the UAM Bridge package, `attempt_001` outputs, mapping material, and orchestration discussion. It may coordinate a rerun, but it cannot itself generate both fresh target and baseline outputs and still claim blind isolation.

Repaired assumption: this thread can coordinate `attempt_002` only if it is explicitly allowed to create or use fresh isolated execution contexts for the target and baseline arms, and if those contexts receive only their permitted materials.

Blocking condition: if fresh context creation is unavailable or not authorized, do not run `attempt_002`; record `blocked_orchestration`.

## Go/No-Go Decision

Go only if:

- fresh isolated target and baseline contexts are available;
- the baseline context can be kept free of UAM Bridge package content and prior run outputs;
- the target context can be kept free of evaluator/scoring/mapping content;
- the runner can preserve mapping separately and give the evaluator only anonymized outputs.

No-go if:

- the same context must generate both arms;
- the baseline context has already seen UAM Bridge package content;
- evaluator materials or scoring criteria have been read by any arm-generation context;
- arm mapping is exposed before scoring.

## Stop Condition

Stop after producing `attempt_002` raw outputs, anonymized outputs, and the separate local mapping key. Do not score, diagnose, patch, or proceed to evaluator handoff in the same operation.
