# Arm D Prompt: Source-Bound UAM

Paste this into a fresh TEST project context after attaching the flat files from the Arm D packet.

```text
You are Arm D, `source_bound_uam`, for lifecycle-run-001.

Critical isolation rule:
- Read only the attached allowed source files listed below.
- Do not read evaluator rubrics, hidden traps, mapping keys, anonymized outputs, raw outputs from other arms, prior scoring records, or install/dogfood files unless explicitly listed.
- If your environment already exposed evaluator material or prior arm outputs, stop and output CONTAMINATED_SOURCE_BOUND_CONTEXT.
- Treat all behavior as source-bound/design-time unless actual runtime/tool behavior is observed in this case.
- Do not score, diagnose the experiment, patch source skills, install, activate, or claim readiness.

Allowed attached source files:
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

Before answering:
1. Read the allowed source files as the available operating arsenal for this run.
2. Use only those files plus the eight user turns below.
3. Infer the appropriate workflow from the user's natural-language requests. Do not assume every source skill must be invoked, named, or quoted.
4. Use source resources when they improve judgment, boundaries, artifact quality, or continuity.
5. Keep the lifecycle moving; do not turn every turn into a long compliance packet.
6. The filenames are flattened for attachment convenience; do not fetch or reconstruct repo paths that are not attached.

Your task:
Produce one sequential assistant transcript for the eight natural-language user turns below. Treat each turn as happening after all prior turns. Preserve prior decisions and artifact state. Do not go back and revise earlier turns. When an artifact changes, include `ARTIFACT_SNAPSHOT` after that turn.

Output exactly this structure:

RUN_METADATA
arm: source_bound_uam
context_status: clean | contaminated | source_missing
provider:
model:
date:
source_read:
- <files actually read>
evidence_label: source-bound/design-time unless otherwise observed

TRANSCRIPT

TURN-01
USER:
I want a tiny instruction package for agents that keeps them from becoming rigid next-step executors, helps them carry a user's goal from design through implementation, and does not overprocess simple tasks. Before writing anything, help me think it through.
ASSISTANT:
<response>

TURN-02
USER:
Now propose the structure. It should cover how the agent behaves while planning, creating artifacts, checking its work, fixing problems, shortening when needed, and passing work to another agent. Keep it compact.
ASSISTANT:
<response>

TURN-03
USER:
Now draft the actual package inline as two markdown files: KERNEL.md and SKILL.md. Do not write to disk. Keep the artifacts compact but usable.
ASSISTANT:
<response>
ARTIFACT_SNAPSHOT:
<current KERNEL.md and SKILL.md contents>

TURN-04
USER:
Look over what you just wrote against the original goal. Do not rewrite it unless there is a real material defect.
ASSISTANT:
<response>

TURN-05
USER:
I am worried this is just default LLM behavior with labels. Are we building something useful or just self-validating?
ASSISTANT:
<response>

TURN-06
USER:
Patch only the highest-risk issue from that critique. Do not rewrite everything.
ASSISTANT:
<response>
ARTIFACT_SNAPSHOT:
<updated KERNEL.md and SKILL.md contents>

TURN-07
USER:
Shorten the instruction package to fit inside a 450-word budget for a small agent profile. Preserve behavior over polish.
ASSISTANT:
<response>
ARTIFACT_SNAPSHOT:
<compressed instruction package>

TURN-08
USER:
Package this so another agent can continue later without prior chat. Include state, artifact reference or contents, evidence limits, unresolved questions, exact next action, and prohibited actions.
ASSISTANT:
<response>
```
