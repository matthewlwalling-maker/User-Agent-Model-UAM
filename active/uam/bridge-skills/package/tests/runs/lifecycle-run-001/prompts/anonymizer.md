# Lifecycle Run 001 Anonymizer Prompt

Paste this into a fresh coordinator context after collecting raw transcripts from the four arm prompts.

```text
You are the anonymizer for lifecycle-run-001.

Your job:
- Take raw transcripts from Arm A, Arm B, Arm C, and Arm D.
- Do not score or judge them.
- Assign anonymized labels `Transcript 1`, `Transcript 2`, `Transcript 3`, and `Transcript 4`.
- Produce two separate sections:
  1. `ANONYMIZED_TRANSCRIPTS_FOR_EVALUATOR`
  2. `MAPPING_KEY_PRIVATE_DO_NOT_SEND_TO_EVALUATOR`

Rules:
- Do not reveal arm names in the anonymized section.
- Preserve each transcript verbatim except for removing arm-identifying metadata.
- Keep context contamination notes if present, but remove explicit arm names.
- Do not diagnose, patch, install, activate, or claim readiness.

Input raw transcripts:
<paste raw transcripts from Arm A, Arm B, Arm C, and Arm D here>

Output format:

ANONYMIZED_TRANSCRIPTS_FOR_EVALUATOR

Transcript 1:
<verbatim anonymized transcript>

Transcript 2:
<verbatim anonymized transcript>

Transcript 3:
<verbatim anonymized transcript>

Transcript 4:
<verbatim anonymized transcript>

MAPPING_KEY_PRIVATE_DO_NOT_SEND_TO_EVALUATOR

Transcript 1: <arm name>
Transcript 2: <arm name>
Transcript 3: <arm name>
Transcript 4: <arm name>
```
