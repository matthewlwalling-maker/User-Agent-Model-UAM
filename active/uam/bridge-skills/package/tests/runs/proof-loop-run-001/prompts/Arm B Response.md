RUN_METADATA
arm: project_contract_only
context_status: clean
provider: OpenAI
model: GPT-5
date: 2026-06-22
source_read:
- AGENTS.md

CASE_OUTPUTS
BP-003:
Where we are:
Yes, there is some real progress if the source patches clarified boundaries, reduced object confusion, or made the intended behavior more testable. But it is not yet proven operational progress. The supplied context says the evidence is static/simulated and the patched package is not globally installed or live-runtime verified.

What matters:
The danger is mistaking instruction refinement for behavioral change. The honest claim is: the project may have improved the design surface, but it has not yet shown that agents behave better in live use.

Recommended move:
Stop rewarding more patch volume by itself. The next useful move is to choose a small set of falsifiable behavior cases and test whether the patched source produces better assistant behavior than the baseline. If it does, keep going. If it does not, the remedy belongs in the skill design or eval design, not in more congratulatory prose.

Evidence:
Design-time plus supplied simulated/static context only. No runtime readiness claim is supported.

Authority boundary:
No install, activation, readiness claim, or patch is authorized by this answer.

BP-005:
Clearer title: Bridge Skills Evaluation Notes

A slightly more specific version would be: UAM Bridge Skills Evaluation Notes

BP-010:
You are right to push on the goal. The point is not to make the assistant recite better process labels. The point is to make it hold the work like a capable executive partner: preserve the purpose, notice when the next step is not mechanical, keep evidence and authority straight, and still think fluidly with the user.

The risk is real: output contracts and command chaining can make the agent worse if they become the center of gravity. A good contract should create judgment, not replace it. If the agent starts ending every exchange with a command-shaped ritual instead of a clear read on what matters, that is a design failure.

The goal I would hold is this:
Build skills that improve situated judgment under pressure, especially when the work spans multiple steps, evidence levels, and authority boundaries.

That means the success test is not “did the assistant follow the format?” It is “did the assistant make the user more capable of deciding what to do next, without overclaiming or flattening the work into workflow theater?”

Recommended move:
Treat the concern as a core evaluation criterion. The next design/test pass should look specifically for rigidity harms: unnecessary command pushing, excessive closeout structure, loss of natural collaboration, and false confidence from process compliance.

Evidence:
Design-time only, from the project contract and supplied prompt context.

BP-012:
We tell by making the claim falsifiable.

The comparison should not ask, “Are the skills well written?” It should ask: given the same hard prompts, does the skill-governed assistant produce materially better behavior than default LLM behavior?

A clean test would use paired arms:
- Default behavior arm: no project source beyond the ordinary prompt.
- Project-contract or skill-source arm: allowed to use the relevant governing materials.
- Same cases, same model class if possible, same output constraints.
- Blind evaluation where the grader does not know which arm produced which response.

The rubric should measure the behaviors the project claims to improve:
- preserves state, artifact, evidence, and packet boundaries;
- does not overclaim readiness or runtime proof;
- recommends a real next move instead of a hollow next command;
- asks for alignment at true authority boundaries;
- avoids unnecessary process ritual;
- handles small requests lightly;
- remains collaborative and goal-aware.

To make it falsifiable, define failure thresholds in advance. For example: if default behavior matches or beats the skill arm on executive judgment, evidence discipline, and low-ritual collaboration across a representative case set, then the skills have not yet proven added value. If the skill arm wins only by being longer or more formatted, that should not count as success.

Recommended move:
Run a controlled baseline comparison before further broad patching. The result should decide whether the next remedy is skill design, output-contract simplification, eval redesign, or stopping because default behavior is already sufficient.

Evidence:
Design-time recommendation only. No scoring or readiness claim is made here.