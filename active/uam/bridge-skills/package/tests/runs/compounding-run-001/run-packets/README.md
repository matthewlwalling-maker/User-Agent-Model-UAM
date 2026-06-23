# Compounding Run 001 Run Packets

Status: patched packets for TEST project execution, not run
Evidence ceiling: design-time until outputs are generated and scored

Use each arm in a fresh TEST context with no inherent resources. Run three independent replicates per arm with the same provider, model, temperature, and settings.

## How To Run

1. Open a fresh TEST context.
2. Attach or copy only the flat files inside that arm's `attachments/` folder.
3. Paste the arm's `prompt.md`.
4. Wait for `READY_FOR_TURN_01`.
5. Use `operator-turns.md` as an operator-only script.
6. Paste exactly one user turn at a time.
7. Do not paste future turns or this README into the arm context.
8. Save the complete raw transcript for anonymization after all nine replicates are complete.

If the TEST project persists files between runs, clear the project root before each replicate so only that arm's allowed attachments are present.

Do not copy the `run-packets/` folder itself into the TEST project root.

## Arm Resources

Arm A, baseline:

- Prompt: `arm-a-baseline/prompt.md`
- Attachments: none

Arm B, kernel and manifest:

- Prompt: `arm-b-kernel-manifest/prompt.md`
- Attachments:
  - `KERNEL.md`
  - `MANIFEST.yaml`

Arm C, full source-bound UAM:

- Prompt: `arm-c-full-source/prompt.md`
- Attachments:
  - `KERNEL.md`
  - `MANIFEST.yaml`
  - `chain-router-reference.md`
  - `align-work.SKILL.md`
  - `design-solution.SKILL.md`
  - `build-artifact.SKILL.md`
  - `review-work.SKILL.md`
  - `compare-decide.SKILL.md`
  - `diagnose-problem.SKILL.md`
  - `research-evidence.SKILL.md`
  - `handoff-state.SKILL.md`

## Excluded From Arm Contexts

Do not attach or paste:

- this README;
- other arm packets;
- evaluator prompts;
- anonymizer prompts;
- source-aware adjudicator prompts;
- external reviewer prompts;
- `handoff-packets/Compound-Test-Run-Handoff Context Resource.md`;
- lifecycle-run exports;
- prior failed packets;
- anonymized outputs;
- scoring records;
- mapping keys;
- prior arm responses.

## After The Arms

Use `../prompts/anonymizer.md` in a coordinator context to create two separate files:

- `ANONYMIZED_TRANSCRIPTS_FOR_EVALUATOR.md`
- `MAPPING_KEY_PRIVATE_DO_NOT_SEND_TO_EVALUATOR.md`

Use `../prompts/evaluator.md` in at least one separate evaluator context with only the anonymized transcripts, not the mapping key. Prefer a second blind evaluator or self-consistency rater.

After blind scoring is locked, use `../prompts/source-aware-adjudicator.md` with the scoring record or records, mapping key, and raw transcript set.

Do not install, activate, patch source skills, run eval gates, or claim readiness from this packet.
