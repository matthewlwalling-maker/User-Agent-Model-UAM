# Lifecycle Run 001 Run Packets

Status: prepared packets for TEST project execution, not run
Evidence ceiling: design-time until arm outputs are generated and scored

Use each arm in a fresh TEST project context with no inherent resources.

## How To Run

1. Open a fresh TEST context.
2. Paste the arm's `prompt.md`.
3. Attach or copy only the flat files inside that arm's `attachments/` folder.
4. If the TEST project persists files between runs, clear the project root before each arm so only that arm's allowed attachments are present.
5. Do not copy the `run-packets/` folder itself into the TEST project root.
6. Do not attach this README, other arm packets, evaluator prompts, anonymized outputs, scoring records, or prior arm responses.
7. Save the raw output for anonymization after all four arms are complete.

## Arm Resources

Arm A, ambient baseline:
- Prompt: `arm-a-ambient-baseline/prompt.md`
- Attachments: none

Arm B, project contract only:
- Prompt: `arm-b-project-contract-only/prompt.md`
- Attachments:
  - `AGENTS.md`

Arm C, kernel only:
- Prompt: `arm-c-kernel-only/prompt.md`
- Attachments:
  - `KERNEL.md`
  - `MANIFEST.yaml`

Arm D, source-bound UAM:
- Prompt: `arm-d-source-bound-uam/prompt.md`
- Attachments:
  - `MANIFEST.yaml`
  - `KERNEL.md`
  - `chain-router-reference.md`
  - `align-work.SKILL.md`
  - `design-solution.SKILL.md`
  - `build-artifact.SKILL.md`
  - `review-work.SKILL.md`
  - `compare-decide.SKILL.md`
  - `diagnose-problem.SKILL.md`
  - `research-evidence.SKILL.md`
  - `handoff-state.SKILL.md`

## After The Arms

Use `../prompts/anonymizer.md` in a coordinator context to anonymize raw outputs.

Use `../prompts/evaluator.md` in a separate evaluator context with only the anonymized outputs, not the mapping key.

Do not install, activate, patch source skills, run eval gates, or claim readiness from this packet.
