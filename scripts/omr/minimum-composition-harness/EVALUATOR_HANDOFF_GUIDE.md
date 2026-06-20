# Independent Evaluator Handoff Guide v0.1

## Independence

Use a fresh evaluator context. Do not receive builder predictions, custodian preferences, or the System A/B key before the prescribed reveal stage.

## Stage 1 — Blinded behavioral scoring

Open only `Evaluator_First_Pass_Packet` and its evaluator-only P5 scoring authority.

For each cell:

1. score System A and System B in the provided presentation order;
2. apply the exact fixture criteria from full P5;
3. record outcome correctness, evidence overclaim, and visible procedural observables;
4. mark trace-dependent credit provisional;
5. lock and timestamp scores before Stage 2.

Do not infer identity from writing style or attempt to open another packet.

## Stage 2 — Blind trace audit

Open `Evaluator_Trace_Audit_Packet`. The A/B key remains withheld.

For each system, verify the required evidence—not merely the conclusion:

- goal/requiredness basis;
- independent capability derivation under the stated condition;
- exact O2 packet or legacy pre-seal transcript;
- coverage classification and evidence stage;
- selector rejection or invocation rejection where required;
- branch preservation;
- Case 8 impact facts and O4 readiness;
- terminal decision/stop;
- burden, intervention, and repair records.

Finalize pass/fail judgments and lock the trace audit before Stage 3.

## Stage 3 — Diagnostic attribution and identity reveal

Open `Evaluator_Diagnostic_Packet` only after Stages 1 and 2 are locked.

Use `system_key.json` to reveal architecture identity. Attribute misses using the P6 taxonomy. Separate:

- behavioral capability;
- trace/inspectability;
- platform packaging;
- model/runtime variance;
- burden and recovery cost.

Do not award a pass to a correct answer lacking required traces. Do not penalize a correct no-change decision for insufficient apparent effort.

## Terminal evaluator deliverable

Return:

- case-level A/B results;
- critical and noncritical failures;
- failure-source attribution;
- raw burden metrics;
- capability gains versus relabeling;
- Case 8 boundary survival;
- compact-task burden result;
- the experiment disposition authorized by the spike.

The prototype builder and run custodian do not participate in first-pass scoring.
