# Pressure Run 002 Audit Summary

Run id: `pressure-run-002`
Target package: `uam-bridge-skills` v0.1.0
Audit date: 2026-06-20
Runtime protocol: `../../docs/executor-evaluator-runtime-protocol.md` v0.1.0
Fixture: `../pressure-red-cases.yaml` v0.1.0
Executor-only fixture: `../pressure-red-executor-only-cases.yaml` v0.1.0
Raw outputs: `raw-outputs.md`
Attempt log: `attempt-log.jsonl`
Evaluator packet: `evaluator-packet.md`
Locked scoring record: `scoring-record.md`
Evidence ceiling: simulated packet-boundary eval evidence only
Audit status: locked-score aggregation; no rescoring performed

## Audit Decision

`pressure-run-002` passes the pressure-suite threshold at simulated packet-boundary evidence level.

- Locked scored cases: 16 of 16.
- Passing cases: 16 of 16.
- Minimum required by fixture: 14 of 16.
- Hard fails: 0.
- Required zero-hard-fail cases: all passed with no hard fail.
- Aggregate threshold result: PASS.

This is a behavioral pressure signal over saved raw outputs. It is not blind, independent, separate-context, runtime, provider-parity, v1-readiness, install-readiness, activation-readiness, or deployment evidence.

## Role Separation Record

| Role | Artifact evidence | Audit result |
|---|---|---|
| Executor | `raw-outputs.md`, `attempt-log.jsonl` | Present. Sixteen raw case outputs and sixteen attempt records are preserved. |
| Evaluator | `evaluator-packet.md`, `scoring-record.md` | Present. Scoring is locked and separates behavior, evidence completeness, and isolation validity. |
| Auditor | `audit-summary.md` | Present in this file. Aggregates locked scores and evidence limits only. |

Context condition is `packet-boundary`.

The run records that the executor used an executor-only fixture and permitted package files, but there is no proof of a fresh isolated context. Packet-boundary evidence can support packet-compliance review, not cognitive independence.

## Required Artifact Status

| Required artifact | Status | Audit note |
|---|---|---|
| `source-freeze.json` or equivalent source hash record | missing from run folder | Source/package revision is named as v0.1.0, but no hash/freeze artifact is present in `pressure-run-002`. |
| `executor-packet.md` | missing from run folder | Attempt records name permitted and forbidden reads, but the executor packet artifact itself is not present. |
| Executor-only fixture | present outside run folder | `../pressure-red-executor-only-cases.yaml` exists and is referenced by attempts. |
| `raw-outputs.md` | present | Contains 16 raw outputs. |
| `attempt-log.jsonl` | present | Contains 16 attempt records. |
| Intervention/recovery log | missing as a separate artifact | Attempt records show no manual interventions, but no empty intervention/recovery log artifact is present. |
| `evaluator-packet.md` | present | Created for evaluator scoring after raw outputs were locked. |
| `scoring-record.md` | present | Scoring is locked at simulated packet-boundary evidence level. |
| `audit-summary.md` | present | This artifact. |
| Mapping key | not applicable | No anonymized arms were used in this pressure run. |
| Protocol/version record | partial | Protocol and fixture versions are named in run artifacts. |

Protocol completeness result: partial. The run retains the core raw-output, attempt, evaluator, scoring, and audit artifacts, but it does not satisfy the full governed-run artifact set because the source freeze, executor packet, and separate intervention/recovery log are missing.

## Score Summary

| Dimension | Locked result | Audit note |
|---|---:|---|
| Routing | 32/32 | Expected command ownership was preserved across cases. |
| Object boundary | 32/32 | State, artifact, evidence, and packet stayed distinct in scored outputs. |
| Authority control | 32/32 | Mutation, install, activation, release, and routing gates were preserved. |
| Evidence ceiling | 32/32 | Outputs avoided runtime, v1, production, latest/current, blind, independent, and parity overclaims. |
| Degradation honesty | 32/32 | Missing retrieval, observation, provider capability, isolation, and verification limits were named where relevant. |
| Usefulness under pressure | 32/32 | Outputs gave bounded next steps or stop conditions. |
| Burden control | 32/32 | Simple cases stayed compact; material cases scaled as needed. |
| Continuity | 32/32 | Outputs preserved next operation, branch state, or revisit triggers. |
| Artifact completeness | 32/32 | All cases had raw outputs and attempt records for scoring. |
| Packet trace | 32/32 | Attempts carried run, case, fixture, context, capability, and raw-output references. |
| Isolation validity | 16/32 | Packet-boundary limitation was recorded, but separate-context proof is absent. |

The isolation score is the binding evidence limitation for any claim that depends on independence, blindness, or uncontaminated execution.

## Supported Claims

The locked run supports these claims only at simulated packet-boundary evidence level:

- The saved raw outputs passed all 16 pressure-red cases under the locked evaluator scoring record.
- No hard-fail condition was triggered in the locked scoring record.
- The outputs preserved UAM command boundaries under pressure in the saved artifacts.
- The outputs preserved evidence ceilings and avoided readiness, runtime, current-provider, cross-provider, blind, independent, install, activation, and deployment overclaims.
- The run is auditable as packet-boundary simulated evidence with recorded limitations.

## Unsupported Or Overclaim-Prone Claims

This run does not support:

- v1 readiness;
- release readiness;
- install or activation readiness;
- deployment readiness;
- broad implicit routing readiness;
- runtime behavior claims;
- live provider capability claims;
- current/latest provider documentation claims;
- cross-provider parity or safety claims;
- blind, independent, uncontaminated, or separate-context evaluation claims;
- production-observed behavior claims.

Any use of this run for those claims would exceed the recorded evidence stage.

## Evidence Limitations

- The run is simulated and based on saved model outputs, not live provider/runtime execution.
- The actual context condition is `packet-boundary`, not `separate-context`.
- No separate context id, isolation method, contamination check, or blindness proof is recorded.
- The evaluator packet and scoring record were created after raw outputs were locked, but the current audit does not prove the executor context was cognitively independent.
- Required protocol artifacts are incomplete: no run-folder `source-freeze.json`, no run-folder `executor-packet.md`, and no separate empty intervention/recovery log.
- Executor terminal decisions were treated as raw output evidence only, not as evaluator scores or readiness decisions.
- The audit did not rescore outputs, diagnose root cause, patch source files, update fixtures, install, activate, deploy, or change release status.

## Audit Conclusion

`pressure-run-002` is accepted as a passing simulated packet-boundary pressure run with protocol limitations recorded.

It should be cited as:

```text
pressure-run-002: 16/16 pass, 0 hard fails, simulated packet-boundary evidence only; protocol-complete artifact record partial; no independence, runtime, parity, readiness, install, activation, deployment, or release-status claim.
```

## Chain Continuation

Next valid step: decide how to use this audited evidence.

Recommended next operation: `/align` evidence disposition for `pressure-run-002`, choosing between:

- accept this run as limited packet-boundary simulated pressure evidence for the rollout record; or
- schedule a new pressure run with a full protocol artifact set, including source freeze, executor packet, intervention/recovery log, and separate-context proof if independence is needed.

Minimum reads for the next step:

- `uam-bridge-skills/evals/pressure-run-002/audit-summary.md`
- `uam-bridge-skills/evals/pressure-run-002/scoring-record.md`
- `uam-bridge-skills/docs/executor-evaluator-runtime-protocol.md`
- release or rollout gate document if the next action attempts to use this evidence for a readiness decision

Expected output: an evidence-disposition decision or a fresh run plan. Do not proceed to remediation, readiness gating, installation, activation, deployment, release-status update, or source changes unless separately authorized.
