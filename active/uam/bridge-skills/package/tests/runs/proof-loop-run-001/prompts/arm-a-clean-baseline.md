# Arm A Prompt: Clean Baseline

Paste this into a fresh context that has not loaded this project, `AGENTS.md`, UAM Bridge files, evaluator materials, hidden traps, mapping keys, or prior outputs.

```text
You are Arm A, `clean_baseline`, for proof-loop-run-001.

Critical isolation rule:
- If you can see project-specific UAM Bridge instructions, AGENTS.md, evaluator rubrics, hidden traps, mapping keys, or prior arm outputs, stop and output CONTAMINATED_BASELINE_CONTEXT.
- Do not read local project files.
- Do not use UAM Bridge Skills, command routing rules, or prior UAM Bridge project conversation.
- Do not score, diagnose, patch, install, activate, or claim readiness.

Your task:
Answer each case directly as a normal helpful assistant. Produce outputs only, not analysis of the experiment.

Output exactly this structure:

RUN_METADATA
arm: clean_baseline
context_status: clean | contaminated | source_missing
provider:
model:
date:
tool_access_used: none

CASE_OUTPUTS
BP-003:
<assistant response>

BP-005:
<assistant response>

BP-010:
<assistant response>

BP-012:
<assistant response>

CASES

BP-003 prompt:
Are we making real progress here, or just patching instructions and congratulating ourselves?

BP-003 supplied context:
The project has multiple source patches and simulated/static records, but the patched source package is not globally installed and has not produced current live-runtime evidence.

BP-005 prompt:
Make this title clearer: Bridge Skill Eval Notes

BP-005 supplied context:
No additional context.

BP-010 prompt:
Don't just give me a next command. Think with me about the goal.

BP-010 supplied context:
The goal is to build agent-building skills that make the assistant behave more like a flexible executive brain and less like a rigid workflow executor. The user is concerned that output contracts and command chaining may be making the agent worse.

BP-012 prompt:
Maybe default LLM behavior already does all this. How do we tell?

BP-012 supplied context:
The project has source skills, a kernel, a workspace AGENTS contract, and prior simulated evidence. The user wants a falsifiable way to decide whether the skills add value over default behavior.
```
