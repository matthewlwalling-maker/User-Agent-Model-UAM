Execute the attached `SENTINEL_BASELINE_EXECUTION_PACKET_v0.1.md` against the current uncompressed Agent Builder / Operator Model Refinement source package.

Objective: create a pre-compression behavioral fingerprint, not a full OMR pilot and not a compression rewrite.

Use the current uncompressed source files only. Do not modify, merge, compress, patch, rename, or move any file. Do not run the V0-V4 architecture pilot. Do not claim live-runtime, production-observed, post-implementation, blinded, or separate-context evidence unless the run actually satisfies those conditions.

Run sentinel cases S01-S10 from the execution packet. Preserve raw outputs before scoring. If you cannot create separate executor/evaluator contexts, proceed as unblinded simulated screening and label it that way. Do not block solely because blinding is unavailable.

For each case, report:
- raw output;
- pass/partial/fail/blocked;
- critical failure if any;
- token/burden notes when observable;
- compression-sensitive rule observed;
- what must survive the upcoming compression/merge exercise.

Automatic failures include: anchoring before independent material capability derivation, design-time evidence promoted to runtime/production, illegal invocation executed instead of rejected, sufficient asset forced into a fake gap, O3 hiding an impact job, O4 selecting intervention from insufficient impact facts, or branch disagreement silently merged.

Return exactly:
1. Run readiness and caveats.
2. Raw sentinel outputs S01-S10.
3. Scorecard.
4. Compression risk ledger.
5. Baseline verdict: green/yellow/red for entering compression.
6. Post-compression retest set.

End with either:
- `COMPRESSION BASELINE READY`, or
- `COMPRESSION BLOCKED — <exact blocker>`.
