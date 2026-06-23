# Executor/Evaluator Runtime Protocol

Version: `0.1.0`
Status: active design-time runtime requirement for UAM eval runs
Evidence ceiling: design-time until an actual run uses this protocol and preserves the required artifacts

## Purpose

This protocol prevents pressure, red-case, parity, and blind-value evals from collapsing into a same-context self-check.

A run can produce behaviorally plausible answers and still fail evidence validation when executor/evaluator separation, packet visibility, context labels, raw output capture, or score-lock artifacts are missing.

This protocol is UAM-native. It borrows runtime evidence-capture discipline from OMR donor protocols, but it does not import OMR state architecture, O1-O4 operators, or five-object state requirements into the UAM Bridge Skills package.

## Scope

Use this protocol for:

- pressure/red-case runs;
- simulated prompt runs;
- blind or comparative value-proposition runs;
- cross-model parity runs;
- reruns after a fixture, skill, adapter, or runtime-protocol change;
- any eval whose result may later support readiness, parity, runtime, or deployment claims.

Do not use this protocol to authorize skill repair, adapter mutation, installation, activation, release-status changes, or deployment. Failures route to `/diagnose`; authorized artifact changes route to `/build`.

## Source Authority

The UAM canonical package remains the source of truth:

- `MANIFEST.yaml`
- `KERNEL.md`
- `skills/active/uam-bridge-skills/commands/*/SKILL.md`
- `tests/*`
- `docs/*`

Donor OMR and evaluator-companion resources provide evidence-capture patterns only. They do not override UAM command ownership, work-object boundaries, evidence stages, provider profiles, or release gates.

## Required Roles

### Fixture Custodian

The fixture custodian freezes the run basis and prepares role-specific packets.

May read:

- full master fixture;
- hidden traps;
- scoring rules;
- source package;
- prior run limitations;
- protocol files.

Must not:

- score outputs;
- edit frozen fixtures after seeing raw outputs;
- repair the target during the run series;
- relabel flawed evidence as valid.

### Executor

The executor produces raw outputs only.

May read:

- executor packet;
- executor-only fixture;
- permitted target package files for the target arm;
- neutral baseline instruction for baseline arms, when applicable;
- supplied user prompts and context.

Must not read before raw outputs are locked:

- hidden traps;
- required behavior;
- prohibited behavior;
- scoring rules;
- hard-fail rules;
- expected winners;
- evaluator packet;
- anonymized mapping key;
- builder predictions;
- prior scoring notes.

Must not:

- score, grade, diagnose, remediate, summarize pass/fail, or claim readiness;
- rewrite source files during the frozen run;
- treat terminal decisions inside raw outputs as evaluator scores;
- generate both target and baseline arms from one target-informed context when a blind or comparative claim is intended.

### Evaluator

The evaluator scores locked raw outputs against the rubric.

May read:

- evaluator packet;
- master fixture or evaluator-only scoring fields;
- locked raw outputs;
- anonymized outputs when the run is blind or comparative.

Must not:

- generate, revise, or rerun raw outputs;
- inspect arm identity before first-pass scoring is locked in blind/comparative runs;
- diagnose root cause or recommend source edits during first-pass scoring;
- give credit for a correct conclusion when required trace, packet, or evidence artifacts are missing.

### Auditor

The auditor aggregates locked scores and evidence limitations.

May read all materials only after evaluator scoring is locked.

Must not:

- rescore outputs unless a separate rescoring role is explicitly authorized;
- patch skills or fixtures;
- upgrade evidence claims beyond the recorded run conditions.

## Context Labels

Every run row must record both intended and actual context condition:

- `parent-thread-single-context`: one already-informed conversation executes the work.
- `packet-boundary`: the packet forbids contamination, but the broader context may already have seen restricted material.
- `separate-context`: a fresh context has not received forbidden material for that role.

Use `separate-context` only with a recorded context ID or equivalent isolation proof, isolation method, contamination checks, and limitation note.

Same-context, packet-boundary, and true separate-context results must be stratified. Do not pool them for claims affected by context isolation unless the aggregate is explicitly labeled non-comparable for isolation credit.

## Fixture Views

### Master Fixture

The master fixture may contain:

- case id;
- prompt;
- supplied context;
- hidden trap;
- expected primary command;
- required behavior;
- prohibited behavior;
- scoring rule;
- hard-fail rule;
- evidence expected;
- diagnosis route on failure.

### Executor-Only Fixture

The executor-only fixture may contain only:

- case id;
- user-facing prompt;
- supplied context;
- evidence stage;
- target package/revision;
- permitted reads;
- forbidden reads;
- raw output capture contract.

It must not contain hidden traps, scoring rules, hard-fail rules, expected winners, or required/prohibited behavior.

### Evaluator Packet

The evaluator packet may contain:

- locked raw outputs;
- scoring dimensions;
- hidden traps;
- required behavior;
- prohibited behavior;
- scoring and hard-fail rules;
- evidence-stage rules;
- output sheet template.

For blind or comparative runs, evaluator packet staging must prevent arm identity exposure until first-pass scoring is locked.

## Required Run Artifacts

Every governed UAM eval run must retain:

- `source-freeze.json` or equivalent source hash record;
- `executor-packet.md`;
- executor-only fixture used for execution;
- `raw-outputs.md`;
- `attempt-log.jsonl`;
- intervention/recovery log, even when empty;
- `evaluator-packet.md`;
- `scoring-record.md`;
- `audit-summary.md`;
- mapping key stored separately when anonymized arms exist;
- protocol/version record naming this file and the fixture revision used.

Raw outputs, failed attempts, contaminated attempts, and rejected run transitions are evidence. Preserve them; do not overwrite them with repaired results.

## Attempt Records

Each attempt record must include:

- run id;
- attempt id;
- recovery-of attempt id, if applicable;
- case id;
- target package and revision;
- fixture id and revision;
- evidence stage;
- intended context condition;
- actual context condition;
- context id or limitation note;
- provider, model, tool availability, and capability profile when known;
- permitted reads;
- forbidden reads;
- manual interventions;
- output file reference;
- terminal executor decision, if present in the raw output.

Executor terminal decisions are raw outputs. They are not pass/fail labels, evaluator scores, architecture verdicts, promotion evidence, or readiness decisions.

## Scoring Requirements

Scorecards must separate:

- behavior correctness;
- object-boundary correctness;
- authority control;
- evidence-ceiling compliance;
- trace or artifact completeness;
- state/packet completeness;
- isolation validity;
- degradation honesty;
- burden control;
- terminal decision correctness;
- evaluator confidence;
- limitations.

Do not collapse behavior pass and evidence completeness into one score. A correct answer without required evidence artifacts can fail evidence validation.

## Validation Fails If

A run is invalid for the affected claim when:

- executor saw hidden traps, scoring keys, hard-fail rules, or evaluator-only fields before raw outputs were locked;
- evaluator saw arm identity or mapping before score lock in a blind/comparative run;
- `separate-context`, `blind`, `independent`, or `uncontaminated` is claimed without isolation proof;
- required run artifacts are missing;
- source, fixture, or protocol versions are unavailable;
- same-context results are pooled with separate-context results for isolation-sensitive claims;
- old flawed evidence is relabeled, repaired in place, or pooled as corrected evidence;
- a recovery overwrites first-pass failure;
- evaluator scoring includes remediation, source edits, or root-cause diagnosis;
- a readiness, v1, runtime, production, provider-current, or cross-model claim exceeds the run evidence stage.

## Evidence Claims

- Fixture design alone is `design-time`.
- Same-context simulated prompt execution is `simulated`, non-blind, and non-independent.
- Packet-boundary execution is auditable for packet compliance but not cognitive independence.
- Separate-context execution can support isolation claims only for roles with recorded isolation proof.
- Live-runtime evidence requires actual observed provider/tool/runtime execution.
- Cross-model parity requires provider-specific runs and comparison at the appropriate evidence stage.
- Production-observed claims are out of scope for this package until repeated real-world observations exist.

## Run Series Rules

Freeze the run basis before execution:

- canonical package files;
- fixture files;
- protocol file;
- provider/model/capability profile;
- run id;
- permitted and forbidden reads;
- output contract;
- evidence stage.

After execution starts:

- do not edit frozen target files;
- do not edit frozen fixture files;
- do not repair outputs in place;
- give retries new attempt IDs;
- preserve manual interventions and recovery reason;
- report flawed and corrected packages separately.

## UAM Pressure Suite Minimum

For `pressure-red-cases.yaml`, a compliant run requires:

1. an executor-only fixture derived from the master pressure fixture;
2. an executor packet that instructs the executor to produce raw outputs only;
3. locked raw outputs for all cases or execution-failure records;
4. a separate evaluator packet built after raw outputs are locked;
5. a scoring record that separates behavior from evidence completeness and isolation validity;
6. an audit summary that states threshold result and evidence limitations;
7. `/diagnose` routing for failed cases before remediation.

## Stop Conditions

Stop the executor role after raw outputs and attempt logs are complete.

Stop the evaluator role after scoring is locked.

Stop the auditor role after aggregate result and evidence limits are recorded.

Do not proceed to remediation, readiness gating, installation, activation, deployment, or broad implicit routing inside the run series.
