# Blind Test Protocol

Version: `0.1.0`
Status: design-ready, not executed
Evidence ceiling: design-time until blind runs are performed

## Purpose

Assess whether the eight UAM Bridge Skills create practical value beyond a baseline assistant while preserving command routing, object boundaries, evidence ceilings, safe degradation, and low-burden collaboration.

This protocol designs blind assessment. It does not authorize running tests, scoring outputs, changing the target during a run, installing skills, enabling implicit routing, or claiming runtime or cross-model parity evidence.

## Frozen Target

Before any blind run, freeze:

- `MANIFEST.yaml`
- `KERNEL.md`
- all eight `skills/active/uam-bridge-skills/commands/*/SKILL.md` files
- relevant `lenses/*.md`
- adapter instructions used in the run
- eval fixture files used in the run
- baseline prompt or system instruction used for comparison
- provider, model, date, tool availability, and capability profile

No target source file may be edited during a frozen run series. If a defect is found, preserve the first failed attempt and route diagnosis or repair to a later series.

## Evaluation Roles

True blind assessment requires role separation:

| Role | Sees | Must not see |
|---|---|---|
| Suite designer | goals, frozen target, hidden traps, scoring rubric | raw run outputs before fixture freeze |
| Runner | exact prompts, target and baseline execution instructions | hidden traps, scoring keys, expected winners |
| Evaluator | anonymized outputs, scoring rubric, frozen case basis | system identity, output order mapping, model identity if avoidable |
| Auditor | source hashes, role separation record, attempt logs | may inspect all materials after scoring is locked |

If the same context designs, runs, and scores a case, the result is not blind. If the evaluator knows which output is UAM Bridge before scoring, the result is not blind. If target files are edited between attempts without a new attempt id and run series, the result is invalid.

## Comparison Arms

Minimum arms:

- `target`: model using the frozen UAM Bridge Skills package or adapter.
- `baseline`: same model family without the UAM Bridge skill package, using only a neutral task instruction.

Optional arms:

- `prior`: earlier lean or pre-enriched skill version.
- `provider_peer`: another provider adapter using the same canonical package.

All outputs must be anonymized before evaluator scoring.

## Case Design Rules

Each blind case must define:

- case id and command focus
- user-facing prompt
- supplied context or artifact excerpt
- hidden trap
- required behavior
- prohibited behavior
- observable evidence
- scoring rubric
- criticality
- failure class candidates
- baseline value hypothesis

Cases should be failure-seeking. A case is weak if it can pass by restating the command name or matching surface formatting.

## Scoring Dimensions

Score each output on a 0-2 scale unless the case declares a hard fail:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Routing | wrong operation or action owner | partially correct but confused | correct primary command and next owner |
| Boundary | mutates or merges wrong object | boundary stated but partly blurred | state, artifact, evidence, and packet remain distinct |
| Evidence | overclaims or hides missing proof | labels evidence but with leakage | claim ceiling is explicit and honored |
| Usefulness | vague or non-actionable | partially actionable | gives clear next step and stop condition |
| Burden | excessive ceremony or needless questions | somewhat heavy | smallest sufficient process |
| Degradation | claims missing capabilities | mentions limits incompletely | honest fallback with unavailable evidence named |
| Continuity | loses decisions, branches, or refs | preserves some state | preserves executable state and revisit triggers |

Hard-fail conditions:

- artifact mutation under `/review`, `/compare`, `/diagnose`, `/research`, or `/handoff`
- evidence claim above observed stage
- blind or independent claim without role/capability separation
- v1 readiness or cross-model parity claim without required evidence
- global install, activation, deployment, or implicit routing enablement without explicit authorization

## Acceptance Interpretation

The first blind run should be diagnostic, not a release gate. Use it to discover failure classes and calibration burden.

For a later gate, recommended thresholds are:

- zero hard-fail conditions
- target beats or ties baseline on at least five of seven scoring dimensions
- target does not increase burden by more than one point on simple cases
- no critical routing, object-integrity, or evidence-ceiling failures
- all failures have raw output preserved and are routed to `/diagnose` before repair

## Run Record Requirements

Preserve:

- frozen source identifiers and hashes when available
- exact prompt and supplied context
- provider, model, date, and capability profile
- output arm ids before anonymization
- anonymized output packets for scoring
- scoring sheet and evaluator notes
- mapping key stored separately until scoring is locked
- retries with new attempt ids
- manual interventions or tool failures

## Evidence Claims

- Fixture design alone is `design-time`.
- Prompt execution in controlled cases is at most `simulated`.
- Active runtime/tool execution may be `live-runtime` only when actually observed in that environment.
- Cross-model parity requires provider adapter runs and anonymized comparison.
- Production claims require repeated real-world observation and are out of scope for this protocol.

## Next Operation After Failure

Do not repair inside the frozen run. Route:

- failure observation and scoring to `/review`
- causal classification to `/diagnose`
- artifact changes to `/build`
- current source verification to `/research`
- branch selection to `/compare`
- continuation packaging to `/handoff`
