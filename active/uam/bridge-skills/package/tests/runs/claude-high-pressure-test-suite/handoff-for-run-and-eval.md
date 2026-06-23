# Claude High Pressure Behavioral Suite Handoff

## How To Use This

Use this packet to start the next test-run role without relying on prior chat history.

First action: run the executor role in a fresh context from the executor-only fixture.

Do not score, diagnose, patch, install, activate, deploy, update release status, or claim any gate passed during the executor role.

## Committed Objective

Execute the imported Claude High Pressure behavioral suite against `uam-bridge-skills` v0.1.0, preserve raw outputs and run artifacts, then hand those locked outputs to a separate evaluator role for blind scoring.

## Current State

The suite has been ingested from the root `Claude High Pressure Test.zip` payload and moved into the canonical eval mapping.

Imported and mapped artifacts:

- Master/evaluator fixture: `uam-bridge-skills/evals/uam-bridge-behavioral-suite.yaml`
- Executor-only fixture: `uam-bridge-skills/evals/uam-bridge-behavioral-executor-only-cases.yaml`
- Suite design: `uam-bridge-skills/evals/claude-high-pressure-test-suite/suite-design.md`
- Runner packet: `uam-bridge-skills/evals/claude-high-pressure-test-suite/runner-packet.md`
- Evaluator packet: `uam-bridge-skills/evals/claude-high-pressure-test-suite/evaluator-packet.md`
- Source archive: `uam-bridge-skills/evals/claude-high-pressure-test-suite/source-archive.zip`

Registry/docs updated:

- `uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/docs/folder-organization-map.md`

The suite remains `not_run`. Evidence ceiling is `design-time`.

Current artifact hashes:

```text
BA3DD972550970836D4E856EEA18E7C286EB0353BF5B041D1B7C31354F0D0085  uam-bridge-skills/evals/uam-bridge-behavioral-suite.yaml
6F2F7A250C2F2A060A24EC6546A9D63D751DE40A85521B0AA78C729604C3833B  uam-bridge-skills/evals/uam-bridge-behavioral-executor-only-cases.yaml
92F8C1C29311D3C737A058197093AD8FE8AF053032A1A068C36927D1D0287CE0  uam-bridge-skills/evals/claude-high-pressure-test-suite/runner-packet.md
B906A43630BE68A2CD77DD97DDC54630939F971A9BCCEAC27E31D5241F32B4C4  uam-bridge-skills/evals/claude-high-pressure-test-suite/evaluator-packet.md
```

## Sanitization And Protocol Status

Static sanitizer checks completed:

- Master suite case count: 42 top-level cases.
- Executor-only fixture case count: 42 top-level cases.
- Executor-only case entries contain prompts, supplied context, evidence stage, target package/version, and raw output capture contracts.
- Executor-only case entries do not contain case-level `hidden_trap`, `required_behavior`, `prohibited_behavior`, `observable_evidence`, `weak_if`, `hard_fail`, `baseline_value_hypothesis`, or `decision_delta_probe`.
- Root folder no longer contains the imported zip or temporary inspection folder.
- No credential-like strings were found. A search hit on the word `single-token` is a false positive for `token`.

Known sanitizer decisions:

- The executor-only fixture includes a top-level `forbidden_case_fields` list as a guardrail. That list names forbidden field names but does not expose hidden case content or scoring answers.
- `M-CHAIN-01` must be run as one continuous target-arm session with turns captured separately.
- `V-*` cases require paired target/baseline arms with opaque labels and sealed mapping key.

## Evidence Ceiling And Claim Limits

Current evidence level: design-time static inspection only.

After executor output exists but before scoring: raw-output evidence only, no pass/fail.

After evaluator scoring: at most simulated evidence, unless a case actually executes in a live tool-enabled environment and that live observation is recorded.

Do not claim:

- v1 readiness;
- deployment readiness;
- install or activation readiness;
- cross-model parity;
- production-observed behavior;
- blind or independent scoring unless role separation and sealed mapping are preserved.

## Authorized Next Action

Run the executor role in a fresh context.

Recommended run id: `behavioral-run-001`.

Create:

```text
uam-bridge-skills/evals/behavioral-run-001/
  source-freeze.json
  freeze-record.md
  executor-packet.md
  executor-only-fixture.yaml
  capability-profile.md
  raw/
  mapping-key.local.md
  run-manifest.md
  attempt-log.jsonl
  intervention-log.md
```

Copy `runner-packet.md` into `executor-packet.md` for the run. Copy `../uam-bridge-behavioral-executor-only-cases.yaml` into `executor-only-fixture.yaml`.

## Executor Fresh-Context Prompt

```text
Next action:
Run the executor role for behavioral-run-001.

Read:
- uam-bridge-skills/MANIFEST.yaml
- uam-bridge-skills/KERNEL.md
- uam-bridge-skills/skills/align-work/SKILL.md
- uam-bridge-skills/skills/design-solution/SKILL.md
- uam-bridge-skills/skills/build-artifact/SKILL.md
- uam-bridge-skills/skills/review-work/SKILL.md
- uam-bridge-skills/skills/compare-decide/SKILL.md
- uam-bridge-skills/skills/diagnose-problem/SKILL.md
- uam-bridge-skills/skills/research-evidence/SKILL.md
- uam-bridge-skills/skills/handoff-state/SKILL.md
- uam-bridge-skills/evals/claude-high-pressure-test-suite/runner-packet.md
- uam-bridge-skills/evals/uam-bridge-behavioral-executor-only-cases.yaml

Do not read:
- uam-bridge-skills/evals/uam-bridge-behavioral-suite.yaml
- uam-bridge-skills/evals/claude-high-pressure-test-suite/evaluator-packet.md
- any mapping key
- hidden traps, required behavior, prohibited behavior, hard-fail rules, scoring rubrics, expected winners, or prior scoring notes

Evidence ceiling:
Simulated at most unless a case actually uses live tool/runtime behavior and that observation is recorded.

Complete this role when:
behavioral-run-001 contains source/freeze records, executor packet copy, executor-only fixture copy, capability profile, raw verbatim outputs, sealed mapping-key.local.md, run manifest, attempt-log.jsonl, and intervention-log.md.

Chain continuation:
After raw outputs are locked, hand the run folder to a separate evaluator role using uam-bridge-skills/evals/claude-high-pressure-test-suite/evaluator-packet.md.

Do not:
Do not score, diagnose, remediate, patch source files, install, activate, deploy, update release status, or claim any gate passed.
```

## Evaluator Fresh-Context Prompt

Use only after executor outputs are locked.

```text
Next action:
Score behavioral-run-001 as the blind evaluator.

Read:
- uam-bridge-skills/evals/claude-high-pressure-test-suite/evaluator-packet.md
- uam-bridge-skills/evals/uam-bridge-behavioral-suite.yaml
- uam-bridge-skills/evals/behavioral-run-001/raw/
- uam-bridge-skills/evals/behavioral-run-001/freeze-record.md
- uam-bridge-skills/evals/behavioral-run-001/capability-profile.md
- uam-bridge-skills/evals/behavioral-run-001/run-manifest.md
- uam-bridge-skills/evals/behavioral-run-001/attempt-log.jsonl
- uam-bridge-skills/evals/behavioral-run-001/intervention-log.md

Do not read:
- uam-bridge-skills/evals/behavioral-run-001/mapping-key.local.md until all dimension scores for value cases are locked.

Evidence ceiling:
Simulated at most unless the locked run artifacts prove a narrower live-runtime observation for a specific case.

Complete this role when:
scoring-record.md is locked with one row per case/arm and value summary rows after mapping-key.local.md is opened.

Chain continuation:
Next role is auditor aggregation into audit-summary.md, then failures route to /diagnose before any /build repair.

Do not:
Do not generate or revise raw outputs, patch files, diagnose root cause during first-pass scoring, install, activate, deploy, update release status, or claim v1/cross-model/runtime readiness.
```

## Prohibited Actions

- Do not run executor and evaluator in the same context if blind or independent evidence is desired.
- Do not expose the master suite to the executor before raw outputs are locked.
- Do not open `mapping-key.local.md` before value-case dimension scoring is locked.
- Do not repair failures inside the frozen run.
- Do not overwrite failed attempts with corrected attempts.

## Verification Owed

- A real executor run must create `behavioral-run-001` artifacts.
- The evaluator must score locked raw outputs only.
- Auditor must separately aggregate scoring and evidence limitations.
- Any failed case must route to `/diagnose` before a separately authorized `/build` repair.
