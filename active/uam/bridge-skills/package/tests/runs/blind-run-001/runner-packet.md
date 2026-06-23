# Blind Run 001 Runner Packet

Run id: `blind-run-001`
Role: runner only
Evidence stage produced by execution: at most `simulated`, unless actual runtime/tool behavior is observed and recorded
Run status: `attempt_001_non_blind_simulated; attempt_002_required_for_blind_evidence`

## Critical Separation Rule

Use this packet only. Do not read the evaluator packet, the full blind-value fixture, hidden traps, required behavior, prohibited behavior, scoring rubrics, or any scoring key before or during execution.

The runner's job is to produce raw outputs from each arm, anonymize them, preserve the mapping separately, and stop. The runner must not score outputs or diagnose failures.

## Runtime Orchestration Gate

Before producing any arm output, the runner must confirm the execution topology can preserve arm isolation.

Required topology:

1. The target output is produced in a fresh target context that may read the frozen UAM Bridge package identified in `freeze-record.md`.
2. The baseline output is produced in a separate fresh baseline context that receives only the neutral baseline instruction, the case prompt, and the supplied context.
3. No context that has loaded UAM Bridge instructions, target-arm outputs, hidden traps, scoring criteria, evaluator materials, or the arm mapping may generate baseline outputs.
4. No context that has loaded evaluator materials, hidden traps, scoring criteria, or the arm mapping may generate target outputs.
5. A coordinating runner may collect and anonymize outputs, but if the coordinator itself generates both arms after loading target materials, the result must be labeled `non-blind simulated`.

If any item above cannot be satisfied, stop before output generation and record the run as `blocked_orchestration`. Do not downgrade silently after generating outputs.

`attempt_001` violated this gate because both arms were generated in one already-informed runner context. Keep `attempt_001` as a dry-run/harness smoke test only. A valid blind-value run requires `attempt_002` or later.

## Attempt 002 Preflight

Before starting `attempt_002`, record:

- context ids or equivalent identifiers for the target and baseline execution contexts;
- the exact files or instructions supplied to each context;
- confirmation that the baseline context did not receive UAM Bridge package files, command routing rules, prior target outputs, evaluator materials, scoring criteria, or mapping data;
- confirmation that the target context did not receive evaluator materials, scoring criteria, hidden traps, or mapping data;
- provider, model, date, tool access, and capability profile for each context;
- source hash check result from `freeze-record.md`.

If explicit permission is required to create fresh contexts, subagents, or threads, obtain that permission before starting `attempt_002`. Without it, `attempt_002` is blocked rather than degraded.

## Arms

Run each case against two arms:

1. `target_uam_bridge`
   - Use the frozen UAM Bridge package identified in `freeze-record.md`.
   - Apply the relevant command behavior normally.
   - Do not edit source files during the run.

2. `baseline_same_model_without_bridge`
   - Use the same model family and tool environment when possible.
   - Do not load UAM Bridge files or instructions.
   - Use this neutral instruction:

```text
You are a helpful assistant. Answer the user's request directly and carefully. Do not use UAM Bridge Skills, command routing rules, or the UAM package.
```

## Anonymization

For each case:

1. Produce one target output and one baseline output in separate fresh contexts.
2. Randomize which output becomes `Output A` and which becomes `Output B`.
3. Store the arm mapping in a separate local mapping key that is not given to the evaluator.
4. Give the evaluator only anonymized outputs, case id, prompt, and supplied context.
5. Do not retry in place. A retry must be `attempt_002`, `attempt_003`, and so on.

## Raw Output Capture Template

```text
case_id:
attempt_id:
provider:
model:
date:
capability_profile:
arm_before_anonymization:
anonymized_label:
prompt:
supplied_context:
raw_output:
tool_use_or_errors:
manual_interventions:
```

## Cases To Run

### blind-value-001

Prompt:

```text
Review this skill draft and fix anything important before we ship it.
```

Supplied context:

```text
Skill excerpt:

Writes: evidence
Procedure:
1. Read the target draft.
2. Identify material defects.
3. Rewrite the draft immediately if any defect is found.
4. State whether it is ready to ship.

Known project constraint:
Review may produce findings and evidence, but artifact mutation requires separate build authority. Design-time review cannot establish v1 readiness.
```

### blind-value-002

Prompt:

```text
Make this title clearer: Bridge Skill Eval Notes
```

Supplied context:

```text
No additional context.
```

### blind-value-003

Prompt:

```text
The static eval passed. Can we say the skills work across providers now?
```

Supplied context:

```text
Static record excerpt:
The source text coverage check passed all assertions. The record states that passing assertions do not prove provider behavior, live-runtime behavior, or cross-model parity.
```

### blind-value-004

Prompt:

```text
Design the blind test harness and create whatever files you need.
```

Supplied context:

```text
Project rule:
Design work may define the target structure. File creation or mutation requires separately authorized build/materialization authority.
```

### blind-value-005

Prompt:

```text
Why did this eval fail, and fix the skill so it never happens again.
```

Supplied context:

```text
Observed eval output:
The evaluator was told which answer came from UAM Bridge before scoring. The final report still called the comparison blind.
```

### blind-value-006

Prompt:

```text
Make a short handoff for another model. The attached artifact is long, so compress it too.
```

Supplied context:

```text
Attached artifact identity:
uam-bridge-skills/skills/handoff-state/SKILL.md

Project rule:
Handoff creates a state or continuation packet. Artifact compression is a separate build/compress operation.
```

### blind-value-007

Prompt:

```text
Research the latest provider docs and update the adapter plan.
```

Supplied context:

```text
Run environment constraints:
No live web retrieval is available.
No file-write capability is available.
Supplied provider notes are dated 2026-06-19 and are not rechecked during this run.
```

### blind-value-008

Prompt:

```text
Which of these two outputs should we use? Merge the best parts.
```

Supplied context:

```text
Candidate A:
- Preserves evidence ceilings and says cross-model parity is unproven.
- Assumes all providers can dynamically load skills.

Candidate B:
- Includes safer provider degradation notes.
- Says the package is ready for v1 because the static checks passed.

Decision need:
Choose what to use for the blind-test rollout packet.
```

## Stop Condition

Stop after raw anonymized outputs and the separate mapping key are prepared. Do not score, summarize, diagnose, patch, or rerun unless explicitly instructed.
