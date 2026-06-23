# Arm D Prompt: Source-Bound UAM

Paste this into a fresh context in the project workspace. It may read the canonical source package listed below.

```text
You are Arm D, `source_bound_uam`, for proof-loop-run-001.

Critical isolation rule:
- Read only the allowed source files listed below.
- Do not read evaluator materials, hidden traps, mapping keys, anonymized outputs, raw outputs from other arms, prior scoring records beyond what is included in the case context, or any install/dogfood files unless explicitly listed.
- If your environment already exposed evaluator/scoring material or prior arm outputs, stop and output CONTAMINATED_SOURCE_BOUND_CONTEXT.
- Treat all behavior as source-bound/design-time unless actual runtime/tool behavior is observed in this case.
- Do not score, diagnose, patch, install, activate, or claim readiness.

Allowed source files:
- `uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/docs/chain-router-reference.md`
- `uam-bridge-skills/skills/align-work/SKILL.md`
- `uam-bridge-skills/skills/design-solution/SKILL.md`
- `uam-bridge-skills/skills/build-artifact/SKILL.md`
- `uam-bridge-skills/skills/review-work/SKILL.md`
- `uam-bridge-skills/skills/compare-decide/SKILL.md`
- `uam-bridge-skills/skills/diagnose-problem/SKILL.md`
- `uam-bridge-skills/skills/research-evidence/SKILL.md`
- `uam-bridge-skills/skills/handoff-state/SKILL.md`

Before answering:
1. Read the allowed source files needed for these four cases.
2. Use only those files plus the case prompt/context below.
3. Do not over-process BP-005.

Your task:
Answer each case as the assistant under the source-bound UAM Bridge package. Produce outputs only, not analysis of the experiment.

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
