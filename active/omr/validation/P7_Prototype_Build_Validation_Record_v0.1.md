# P7 — Prototype Build Validation Record

**Version:** 0.1  
**Evidence stage:** design-time construction validation only  
**Comparative verdict:** Not issued

## 1. Cross-artifact consistency audit

| Check | Result | Evidence |
|---|---|---|
| Exactly five architectural state objects | PASS | P1/P2 define only GoalContract, CapabilityModel, EvidenceLedger, CoverageMap, ChangeDecision |
| Metadata envelope is not a sixth object | PASS | P2 `$defs.MetadataEnvelope` is embedded and cannot be selected as a top-level object |
| Exactly four operators | PASS | P3 contains O1–O4 only; P4 selector can select only O1–O4 |
| Legacy baseline unchanged | PASS | P1/P6 freeze the Assessment Contract and Procedure; operator path alone excludes AB routing |
| O3 does not select interventions | PASS | P2 CoverageMap has no decision field; P3/P4 reject it with MCP-E430 |
| O4 does not redo coverage/impact analysis | PASS | P3 makes O3 facts immutable; P4/P2 reject upstream rewrites with MCP-E530 |
| O3-before-O2 rejected | PASS | P4 eligibility and C05 require MCP-E400 rejection |
| O4 without impact knowledge rejected or block-limited | PASS | P4 distinguishes `not-ready` from `block-only`; P3 maps block-only only to a block |
| Shared EvidenceLedger remains one logical object | PASS | Stable ledger ID/revision/digest, full or referenced-subset projection, append delta; no copied independent ledgers |
| Evidence promotion requires new evidence | PASS | P2 ledger conditions, P3 ceilings, C03/C10, P6 raw capture |
| Compact projection preserves safeguards | PASS at specification level | P2 projection rules and P3 compact requirements preserve requiredness, trace, refs, ceiling, branch, readiness, decision/stop |
| Material model disagreement preserved | PASS | P2/P4 prohibit silent union; C09A/C09B score invariant versus decision-material disagreement |
| State invalidation complete | PASS | P2 and P4 matrices cover goal, model, asset, evidence, coverage, and branch changes |
| Equivalent independence for legacy | PASS | P6 defines packet-boundary and separate-context protocols for both systems |
| Case 8 has decisive variants | PASS | C08A supplies systemic facts; C08B forces block rather than hidden graph analysis |
| All inherited E1–E12 behaviors covered | PASS | P5 coverage matrix maps every E1–E12 behavior to one or more fixed cases |
| Holdouts are not design-tuned | PASS by protocol | P5 requires post-freeze evaluator/custodian selection and prohibits near-duplicates |
| Correct answer without trace cannot pass | PASS | P5 shared scoring and P6 retention/scoring rule |
| No runtime/production validation claim | PASS | All artifacts label the package design-time; P6 defines future runs |

## 2. Mandatory implementation questions resolved

1. **Metadata without a sixth object:** P2 embeds a non-instantiable schema definition in each of the five objects.
2. **One logical EvidenceLedger in handoffs:** packets carry a full snapshot or proof-carrying referenced subset with stable ID, exact revision/digest, all cited entries, omitted count, and append delta.
3. **Compact integrity:** compact projection cannot omit requiredness class/basis, traces, exact refs, provenance, ceiling, branch/conflict/freshness, impact readiness, decision, or stop basis.
4. **Decision-ready CoverageMap fields:** gap type, origin layer candidates, touched/first-/second-degree refs, semantic centrality, propagation facts, reach, completeness, preservation feasibility, material unknowns, impact-job flag, and O4 readiness.
5. **Impact-job boundary:** new evidence collection, undocumented graph traversal, runtime inspection, causal simulation, or design work is separate; O3 marks block-only and O4 blocks.
6. **Disagreeing models:** separate branches, separate coverage, no silent union; only invariant downstream decisions proceed.
7. **Invalidation:** exact matrix is in P2/P4.
8. **Illegal sequencing:** P4 hard-rejects O3-before-O2 and limits O4 to intervention-ready/block-only maps.
9. **Equivalent legacy independence:** P6 runs both systems under packet-boundary and separate-context conditions and reports them separately.
10. **Deferred packaging:** model adapters, persistence, transport, authentication, UI, fixture-view export, orchestration, and deployment are outside capability architecture.

## 3. Construction validation performed

- P2 is valid JSON and uses JSON Schema Draft 2020-12 constructs.
- All five P2 valid examples structurally validate against their object schemas.
- All five invalid examples are rejected structurally or by the named semantic validation rule.
- P5 parses as YAML and contains 12 mandatory top-level cases, two C08 variants, two C09 variants, and two holdout placeholders.
- P5's E1–E12 matrix covers every inherited evaluation ID.
- Cross-file references P1→P7, P2→P3/P4, P3→P4/P5, and P5→P6 are resolvable by exact filename/version in the package inventory.
- No extra operator or state object is required for construction correctness.

## 4. Known experiment risks, not build defects

- Case 8 may reveal that block-only behavior is too frequent or that O3's bounded impact observation is still a hidden separate job.
- Compact state may impose unjustified burden despite preserving fields.
- Packet-boundary isolation may not reduce anchoring relative to the legacy seal.
- Typed state can produce compliance theater without better reasoning.
- The prototype intentionally lacks implementation, target-architecture generation, and lifecycle continuation.

These are comparative hypotheses the run must test. They do not make the package unrunnable.

## 5. Preconditions for the run executor

1. Freeze artifact/source digests.
2. Generate the P5 executor-only view without evaluator fields.
3. Select runtime/model configurations and record them.
4. Do not fill holdout placeholders until after the package is frozen.
5. Preserve first-pass failures and all repair evidence.

## 6. Final build disposition

`READY FOR COMPARATIVE EXECUTION`

The package is internally consistent and runnable as a platform-neutral comparative specification. The four-operator boundary has not been proven correct; it has only been made executable and falsifiable. No comparative architecture verdict is issued.
