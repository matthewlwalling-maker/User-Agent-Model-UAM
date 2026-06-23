# Arm A Prompt: Ambient Baseline

Paste this into a fresh TEST project context with no attached files. This is not a perfect clean baseline if account/project instructions are unavoidable; label any known contamination in `context_status`.

```text
You are Arm A, `ambient_baseline`, for lifecycle-run-001.

Critical isolation rule:
- The TEST project should have no files attached for this arm.
- Do not read project-specific instruction files, evaluator rubrics, hidden traps, mapping keys, or prior arm outputs.
- Do not use any attached source package, routing docs, or custom skill docs.
- If unavoidable account/project/global instructions may influence you, set `context_status: ambient_contaminated` and continue.
- Do not score, diagnose the experiment, patch source skills, install, activate, or claim readiness.

Your task:
Produce one sequential assistant transcript for the eight natural-language user turns below. Treat each turn as happening after all prior turns. Preserve prior decisions and artifact state. Do not go back and revise earlier turns. When an artifact changes, include `ARTIFACT_SNAPSHOT` after that turn.

Output exactly this structure:

RUN_METADATA
arm: ambient_baseline
context_status: clean | ambient_contaminated | contaminated
provider:
model:
date:
source_read: none

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
