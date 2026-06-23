RUN_METADATA
arm: clean_baseline
context_status: clean
provider: OpenAI
model: GPT-5.5 Thinking
date: 2026-06-22
tool_access_used: none

CASE_OUTPUTS
BP-003:
You are making some progress, but not yet the kind that should count as validated progress.

Given the context, the honest assessment is:

* Source patches and simulated/static records show design activity and possible movement.
* They do not prove the patched system works in the current live runtime.
* If the patched source package is not globally installed, then the live agent may still be behaving according to the old or default path.
* Without current runtime evidence, congratulating ourselves would be premature.

So the right framing is: **we have implementation artifacts and hypotheses, not confirmed behavioral improvement**.

The next meaningful threshold is live evidence: run the actual current system in the environment where it is supposed to operate, capture behavior on representative cases, and compare it against the intended behavior. Until then, treat the work as promising but unproven.

BP-005:
Clearer title:

**Bridge Skill Evaluation Notes**

A slightly sharper version:

**Bridge Skill Evaluation Findings**

BP-010:
The goal is not “make the agent follow more commands.” The goal is to make it exercise better judgment.

That distinction matters. If the skill system turns every interaction into command routing, rigid output contracts, or checklist compliance, it may improve consistency while reducing the very executive flexibility you want: deciding what matters, adapting to ambiguity, pushing back when needed, and choosing the right level of structure.

I would frame the goal like this:

**Build skills that improve judgment under real conversational pressure, not skills that merely increase procedural compliance.**

That suggests a different evaluation target. Instead of asking, “Did it invoke the right command?” ask:

* Did it understand the user’s real objective?
* Did it avoid unnecessary process?
* Did it push back on bad assumptions?
* Did it choose the right amount of structure?
* Did it preserve flexibility while still being reliable?
* Did it produce a better outcome than default behavior?

The risk is that output contracts optimize for legibility to the evaluator rather than usefulness to the user. Command chaining can become a crutch: the assistant looks disciplined, but stops thinking.

My recommendation: treat workflow behavior as a tool, not the success criterion. The success criterion should be whether the assistant behaves more like a capable chief of staff: context-sensitive, outcome-oriented, concise when possible, structured when useful, and willing to deviate from procedure when procedure gets in the way.

BP-012:
You tell by running a controlled comparison against default behavior.

The key is to make the claim falsifiable. For example:

**Claim:** the skills improve assistant behavior beyond default LLM behavior.

That claim should fail if default behavior performs as well or better on the target tasks.

A reasonable test design:

1. Build a fixed set of representative prompts.
   Include cases that test the actual value you care about: ambiguity handling, goal reasoning, pushback, tool restraint, synthesis, user-first judgment, and avoiding rigid workflow behavior.

2. Run two arms blind.
   One arm uses the skill system. The other uses default behavior. Do not let evaluators know which is which.

3. Define outcome-based rubrics before judging.
   Avoid scoring internal compliance unless compliance itself matters. Score things like usefulness, judgment, correctness, adaptability, concision, and whether the assistant served the user’s real goal.

4. Include failure traps.
   Add prompts where blindly following a workflow would make the answer worse. Also include prompts where structure genuinely helps. Good skills should know the difference.

5. Require live-runtime evidence.
   Prior simulated evidence is not enough. The test should use the actual current runtime, with the source skills, kernel, and AGENTS contract active if those are what you intend to evaluate.

6. Compare against meaningful thresholds.
   The skills add value only if they beat default behavior by a clear margin on the target behaviors without introducing new regressions.

A practical decision rule:

**Keep the skills only if they produce measurably better user outcomes than default behavior on live, blind, representative tests, and do not increase rigidity, verbosity, or false confidence.**

If the skilled arm mainly looks more procedural but is not more helpful, then default LLM behavior may already be doing the important part.
