# Lifecycle Run 001 Prompt Set

Status: ready-to-paste prompts, not run
Evidence ceiling: design-time until outputs are generated and scored

This test checks whether UAM Bridge behavior adds value across a whole instruction-building lifecycle, not just one response.

The run is intentionally natural-language and self-routing. Do not tell the model which internal command, skill, or phase label to use in the user turns. The point is to see whether each arm can infer the appropriate work mode, preserve state, use available resources when helpful, and avoid process ceremony when the user has not prescribed a workflow.

Use these prompts in separate contexts:

1. `arm-a-ambient-baseline.md`
2. `arm-b-project-contract-only.md`
3. `arm-c-kernel-only.md`
4. `arm-d-source-bound-uam.md`
5. `anonymizer.md`
6. `evaluator.md`

For a TEST project with no inherent resources, use the prepared packets in:

```text
uam-bridge-skills/evals/lifecycle-run-001/run-packets/
```

Paste the arm's `prompt.md` into a fresh TEST context. Attach or copy only the flat files inside that arm's `attachments/` folder. Arm A intentionally has no attachments.

Each arm produces one full sequential transcript for the same eight-turn workstream:

1. think through a messy goal before artifact creation
2. propose a compact instruction architecture
3. draft inline artifact contents
4. inspect the artifact without rewriting unless needed
5. respond to a self-validation critique
6. patch only the highest-risk issue
7. shorten without losing behavior
8. package continuation for another agent

This is still a controlled simulated run, not live-runtime proof. It should reveal whether the source skills help preserve goal, artifact quality, boundaries, and continuity over a lifecycle without being explicitly marched through the UAM command sequence.

Do not install, activate, patch source skills, score inside runner contexts, or claim readiness.
