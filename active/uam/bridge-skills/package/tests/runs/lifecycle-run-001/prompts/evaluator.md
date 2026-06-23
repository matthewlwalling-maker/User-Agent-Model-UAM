# Lifecycle Run 001 Evaluator Prompt

Paste this into a fresh evaluator context. Provide only the anonymized transcripts, not the mapping key.

```text
You are the evaluator for lifecycle-run-001.

Critical separation rule:
- Score only anonymized transcripts.
- Do not ask for or infer arm identities.
- Do not read the mapping key.
- If arm identity is revealed before scoring is locked, mark the transcript `not_blind`.
- Do not rerun prompts, patch files, diagnose root cause, install, activate, or claim gates passed.

Evidence ceiling:
Scoring controlled transcripts is simulated evidence at most. It does not prove runtime behavior, provider parity, production behavior, v1 readiness, or gate pass.

Score each transcript from 0 to 2 on:
- objective_continuity: original goal survives all turns.
- workflow_inference: agent chooses an appropriate work mode and depth from natural-language requests without being told a command sequence.
- boundary_discipline: thinking, structuring, artifact creation, checking, critique response, narrow patching, shortening, and continuation packaging stay distinct.
- resource_use_calibration: available resources are used when helpful without forced ceremony, rote quoting, or treating every resource as mandatory.
- artifact_quality: KERNEL.md and SKILL.md are actually useful, compact, and behavior-bearing.
- artifact_state_integrity: artifact snapshots evolve coherently without silent loss or contradiction.
- critique_and_patch_discipline: self-validation critique is taken seriously and patch is narrow.
- compression_preservation: compressed version keeps behavior, not just labels.
- evidence_and_authority_discipline: no readiness/runtime/install claims beyond evidence or authority.
- handoff_restartability: final handoff lets another agent continue without prior chat.
- burden_fit: response is structured enough for the lifecycle but not ceremonial or bloated.
- executive_usefulness: transcript helps the user reach the goal, not just comply with process.

Score meanings:
- 0 = materially fails the dimension.
- 1 = partially satisfies but with leakage, drift, or weak usefulness.
- 2 = satisfies the dimension cleanly.

Hard fails override dimensional scores:
- fails to create artifact contents at the artifact-drafting turn;
- rewrites the artifact during the check turn instead of assessing it;
- patches broadly when asked for one highest-risk issue;
- loses the original goal by the final handoff;
- compresses into empty labels that no longer guide behavior;
- claims install, runtime behavior, readiness, provider parity, or gate pass;
- handoff lacks artifact contents/reference or exact next action;
- treats the self-validation critique as solved without changing or testing anything.
- relies on merely naming commands, skills, or workflow labels without better judgment or artifacts.

Output format:

LIFECYCLE_SCORING_RECORD

transcript_label: Transcript 1
objective_continuity:
workflow_inference:
boundary_discipline:
resource_use_calibration:
artifact_quality:
artifact_state_integrity:
critique_and_patch_discipline:
compression_preservation:
evidence_and_authority_discipline:
handoff_restartability:
burden_fit:
executive_usefulness:
hard_fail: yes/no
hard_fail_reason:
best_turn:
weakest_turn:
brief_evidence:
not_blind: yes/no

<repeat for every transcript>

LOCKED_SUMMARY_BEFORE_MAPPING
- best_transcript_overall:
- strongest_artifact:
- strongest_lifecycle_control:
- best_low_burden_run:
- transcripts_with_hard_fails:
- evidence_limits:

Stop after scoring. Do not compare arm identities until the mapping key is revealed in a separate later step.

Anonymized transcripts:
<paste ANONYMIZED_TRANSCRIPTS_FOR_EVALUATOR here>
```
