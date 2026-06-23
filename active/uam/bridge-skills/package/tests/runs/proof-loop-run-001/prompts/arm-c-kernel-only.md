# Arm C Prompt: Kernel Only

Paste this into a fresh context in the project workspace. It may read only the kernel and manifest.

```text
You are Arm C, `kernel_only`, for proof-loop-run-001.

Critical isolation rule:
- Read only:
  - `uam-bridge-skills/KERNEL.md`
  - `uam-bridge-skills/MANIFEST.yaml`
- Do not read `AGENTS.md`, source `SKILL.md` files, `docs/chain-router-reference.md`, evaluator materials, hidden traps, mapping keys, or prior arm outputs.
- If your environment already exposed source skills, chain-router-reference, evaluator/scoring material, or prior arm outputs, stop and output CONTAMINATED_KERNEL_CONTEXT.
- Do not score, diagnose, patch, install, activate, or claim readiness.

Before answering:
1. Read `uam-bridge-skills/KERNEL.md`.
2. Read `uam-bridge-skills/MANIFEST.yaml`.
3. Use only those files plus the case prompt/context below.

Your task:
Answer each case as the assistant under kernel-only UAM Bridge guidance. Produce outputs only, not analysis of the experiment.

Output exactly this structure:

RUN_METADATA
arm: kernel_only
context_status: clean | contaminated | source_missing
provider:
model:
date:
source_read:
- uam-bridge-skills/KERNEL.md
- uam-bridge-skills/MANIFEST.yaml

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
