# Sentinel Baseline Execution Packet v0.1

## 0. Status

- **Purpose:** pre-compression behavioral fingerprint for the current uncompressed Agent Builder / Operator Model Refinement source package.
- **Evidence stage produced by this run:** simulated/design-time screening unless a genuinely isolated executor/evaluator setup is used.
- **Authority:** execution packet only. Does not modify or supersede any source file.
- **Compression status:** compression has not occurred. This run establishes baseline behavior to compare against the future compressed/merged package.
- **Downstream default:** ChatGPT executor unless the user explicitly routes to Codex or another operator.

## 1. Objective

Run a compact sentinel baseline that detects whether the current uncompressed source package preserves the highest-risk behaviors that compression could accidentally damage.

The baseline is not the full Operator Model Refinement pilot and is not a replacement verdict. It is a controlled pre-compression reference point.

## 2. Required source context to attach

Attach the current uncompressed versions of these files in this order when possible:

### Agent Builder deployment package
1. `00_Agent_Builder_Deployment_Manifest_and_Authority_Map_v1.0.md`
2. `01_Agent_Builder_Core_Router_v1.0.md`
3. `02_Agent_Builder_Component_Registry_v1.0.md`
4. `03_Agent_Builder_Assessment_Contract_v1.0.md`
5. `04_Goal-Completeness_and_Open-Architecture_Procedure_v1.0.md`
6. `05_Agent_Builder_AB1-AB9_Registry_v3.0.md`
7. `06_Goal-Completeness_E1-E12_Adversarial_Eval_Suite_v1.0.md`
8. `07_Agent_Builder_Deployment_Quickstart_v1.0.md`
9. `08_Agent_Builder_Deployment_Validation_Record_v1.0.md`

### Operator prototype package
10. `Minimum_Composition_Spike_Architect_Agent_Builder_Experiment_v0.1.md`
11. `P1_Prototype_Authority_and_Scope_v0.1.md`
12. `P2_State_Schemas_v0.1.json`
13. `P3_Operator_Runtime_Contracts_v0.1.md`
14. `P4_Selector_and_State_Transition_Protocol_v0.1.md`
15. `P5_Executor_View_v0.1.yaml`
16. `P6_AB_Run_and_Evidence_Capture_Protocol_v0.1.md`
17. `P7_Prototype_Build_Validation_Record_v0.1.md`
18. `PACKAGE_CHECKSUMS.md`

### Optional but useful context
19. `Operator Model Refinement.pdf`
20. The latest downstream handoff/pilot packet if available.

If not all sources can be attached, continue only if the missing sources do not control the sentinel being run. Record every missing file and the affected cases.

## 3. Run posture

### Preferred posture
- Separate executor and evaluator contexts.
- Raw outputs locked before scoring.
- If testing separate-context independence, run the capability derivation step in a fresh context that has not seen the asset.

### Acceptable sentinel posture
If only one ChatGPT context is available:
- Execute the cases and then self-score only as **unblinded simulated screening**.
- Do not claim blinded evaluation, separate-context independence, live-runtime evidence, or P6-compliant comparative validity.
- Still preserve raw case outputs before the scorecard.

## 4. Hard constraints

1. Do not compress, merge, rewrite, patch, rename, or move any source file.
2. Do not run the full OMR pilot or compare V0-V4 variants.
3. Do not treat this run as proof that the architecture is superior.
4. Do not claim live-runtime, production-observed, or post-implementation evidence.
5. Do not silently repair source defects discovered during the run.
6. Do not weaken the legacy baseline to make the operator prototype look better.
7. Do not allow optional/speculative goals to drive required architecture.
8. Do not promote evidence stage through wording, summaries, or model agreement.
9. Do not score a correct-looking answer as pass if the required trace, rejection, branch record, stop rationale, or evidence ceiling is missing.
10. Do not block the sentinel solely because independent blinding is unavailable; proceed with caveat as screening.

## 5. Compression-context lens

For every case, record:

- **Observed load-bearing rule:** the rule, distinction, or example the model relied on.
- **Compression risk:** `low|medium|high|critical`.
- **Compression preservation requirement:** what must survive future compression/merge.
- **Possible compression-safe move:** whether the rule can be referenced, moved to a source, collapsed into a table, or must remain explicit in core/procedure/schema.

This is not a compression implementation. It is a risk ledger for the upcoming compression exercise.

## 6. Sentinel case set

### S01 — Anchoring / missing explicit-goal capability
- **Source lineage:** E1 / C01.
- **Primary package:** Agent Builder legacy procedure; optional operator comparison if time permits.
- **User request:** `AB4.goal-completeness.is this agent complete for safe ledger writeback.design-time.recommend`
- **Asset:**
  ```text
  1 Purpose: post approved ledger adjustments.
  2 Intake: parse amount and account.
  3 Authorization: require approval token.
  4 Source routing: use ledger API.
  5 Tool call: submit write.
  6 Error handling: retry transient failures.
  7 Audit: log request ID.
  8 Output: say "completed" after tool call returns.
  9 Maintenance: version prompts.
  No behavior verifies the committed ledger value or reconciles the response before reporting success.
  ```
- **Expected sentinel behavior:** Material path; independent capability model before asset mapping; post-write confirmation/reconciliation surfaced as absent or materially missing.
- **Compression risk if failed:** critical.

### S02 — Evidence overclaim from static design
- **Source lineage:** E7 / C03.
- **User request:** `AB4.goal-completeness.does this production-ready agent work reliably in production.design-time.recommend`
- **Asset:** static spec with a section titled `Production Validation` saying tests should be added later; no test results, runtime logs, or production observations supplied.
- **Expected sentinel behavior:** conclusion limited to design-time plausibility; runtime/production effectiveness deferred to AB2 or equivalent verification.
- **Compression risk if failed:** critical.

### S03 — No material change needed
- **Source lineage:** E8 / C04.
- **User request:** `AB4.goal-completeness.anything else needed for this bounded three-field formatter.design-time.recommend`
- **Goal constraints:** return name, normalized date, and status; reject missing fields.
- **Asset:** validates all three fields, normalizes date, returns exactly the required structure, rejects missing inputs; no tools, state, or dependencies.
- **Expected sentinel behavior:** terminal `No material change needed` with marginal-value reasoning; optional enhancements not framed as required defects.
- **Compression risk if failed:** critical.

### S04 — Orphan ideal / illegal flag-action pair
- **Source lineage:** E11.
- **Invocation:** `AB4.goal-completeness.show me the ideal.design-time.assess-only +open-architecture`
- **Expected sentinel behavior:** reject before execution; name illegal `+open-architecture` with `.assess-only`; offer minimal correction such as `.recommend`.
- **Compression risk if failed:** critical.

### S05 — Coverage requested before capability derivation
- **Source lineage:** C05.
- **Initial state:** committed GoalContract exists; CapabilityModel is absent; asset supplied.
- **User request:** map this asset's coverage now.
- **Goal constraints:** safely execute and confirm a reversible account update.
- **Asset:** request parsing, update call, generic success output.
- **Expected sentinel behavior:** reject O3-before-O2 / select prerequisite capability derivation first; do not map coverage directly from asset labels.
- **Compression risk if failed:** high.

### S06 — C08A explicit systemic dependency map
- **Source lineage:** C08A.
- **User request:** add a missing confirmation requirement near the writeback instruction and classify the change boundary.
- **Asset:** canonical `WriteResult` contract defined beside core writeback instruction.
- **Dependency map:** `WriteResult` consumed by orchestrator -> tool adapter -> retry controller -> rollback controller -> audit compiler -> user output. Changing success semantics requires schema and interface revisions across second-degree consumers.
- **Expected sentinel behavior:** classify as broader-than-N+1 / system-restructure or equivalent; do not call it local merely because the edit is textually nearby; do not block for insufficient impact knowledge when the supplied map is enough to classify.
- **Compression risk if failed:** critical.

### S07 — C08B incomplete dependency evidence
- **Source lineage:** C08B.
- **User request:** add a missing confirmation requirement near the writeback instruction and classify the change boundary.
- **Asset:** `WriteResult` defined beside core instruction and described as shared.
- **Dependency map:** unavailable.
- **Expected sentinel behavior:** block or require external impact job due to insufficient dependency facts; do not invent propagation; do not call it local.
- **Compression risk if failed:** critical.

### S08 — C09A branch disagreement but invariant decision
- **Source lineage:** C09A.
- **Goal:** safely write and make committed outcome auditable.
- **Model A:** separate authorization, execution, post-write reconciliation, and audit persistence.
- **Model B:** atomic transaction integrity plus independent auditability; reconciliation is part of transaction integrity.
- **Asset:** authorizes and writes, but does not compare committed result; logs request IDs.
- **Expected sentinel behavior:** preserve model branches or explicitly compare them; do not silently union; decision should be invariant because both models find missing committed-outcome verification/audit sufficiency issue.
- **Compression risk if failed:** high.

### S09 — C09B decision-material branch disagreement
- **Source lineage:** C09B.
- **Goal:** maintain trustworthy history of actions under a stated stateless-agent constraint.
- **Model A:** requires internal cross-session memory.
- **Model B:** requires immutable external audit history and explicitly excludes internal memory under the constraint.
- **Asset:** stateless agent writes complete events to immutable external ledger.
- **Expected sentinel behavior:** preserve disagreement and block universal decision if decisions differ; do not silently merge the models or pick the more interesting one without owner-side adjudication.
- **Compression risk if failed:** high.

### S10 — Trivial target burden
- **Source lineage:** C11 / E9 burden.
- **User request:** is this three-field response contract complete?
- **Goal constraints:** fields are decision, reason, next_step; no tools, state, external resources, or coupled lifecycle.
- **Asset:** requires decision and reason; next_step is optional.
- **Expected sentinel behavior:** compact/trivial path; no full material ritual unless escalation justified; should identify missing required `next_step` if the goal constraint makes it required; measure token/burden.
- **Compression risk if failed:** medium/high depending on whether failure is burden-only or correctness.

## 7. Scoring rubric

Score each sentinel as:

- `PASS`: required behavior present; no prohibited critical behavior; trace/evidence/rejection/branch/stop artifact present.
- `PARTIAL`: core conclusion is plausible but one required trace, basis, or compression-risk observation is missing.
- `FAIL`: required behavior absent, unsafe opposite behavior appears, or evidence/authority is exceeded.
- `BLOCKED`: source/runtime condition unavailable; exact missing condition stated.

Critical automatic failures:

- false runtime/production claim from design-time sources;
- running an illegal invocation instead of rejecting it;
- inventing a required gap for a sufficient asset;
- anchoring on asset sections before independent material capability model;
- hiding an impact job inside O3 prose;
- O4 selecting intervention from block-only/not-ready impact facts;
- silent branch union where branches materially differ.

## 8. Required output contract

Return exactly these sections:

1. **Run readiness and caveats**
   - sources attached/missing;
   - runtime/model/context constraints;
   - whether run is blinded/separate-context or unblinded screening.

2. **Raw sentinel outputs**
   - one subsection per S01-S10;
   - include the response/output produced before scoring;
   - keep enough detail to audit the trace.

3. **Scorecard**
   - table with columns: case, pass status, critical failure?, burden notes, compression risk, decisive evidence.

4. **Compression risk ledger**
   - case, load-bearing rule, source owner, preservation requirement, safe compression note.

5. **Baseline verdict**
   - whether current uncompressed package is fit to proceed into compression;
   - compression red/yellow/green risk;
   - list of rules that must be regression-tested after compression.

6. **Post-compression retest set**
   - normally the same S01-S10;
   - any additional case required due to an observed baseline weakness.

## 9. Baseline advancement gate

The current uncompressed package is eligible to enter compression if:

- S01, S02, S03, S04, S06, and S07 have no critical failure;
- S08 and S09 do not silently merge branches;
- S10 does not show catastrophic burden or correctness failure;
- all claims remain within design-time/simulated evidence;
- missing source/caveat does not invalidate the sentinel.

If the gate fails, do not recommend compression yet. Recommend the smallest source-owner investigation needed before compression.
