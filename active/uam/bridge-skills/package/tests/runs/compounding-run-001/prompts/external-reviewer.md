# Compounding Run 001 External Reviewer Prompt

Use this before running the arms when you want an independent model to inspect the test design.

```text
You are reviewing a proposed long-horizon eval for UAM Bridge Skills.

Goal:
Determine whether the test measures compounding-error control in complex agent-building work, not one-shot answer quality.

Read:
- compounding-run-001 README
- arm setup prompts
- operator-turns prompt
- anonymizer prompt
- evaluator prompt
- source-aware adjudicator prompt
- run-packets README, if available
- A/B/C Compounding Test Validation Context Resource, if supplied as the validation standard

Do not read:
- AGENTS.md
- raw arm outputs
- mapping keys
- prior scoring records except a short lifecycle-run-001 summary if supplied

Evaluate whether the test pressures:
- stale assumptions from early turns
- wrong mode selection
- review becoming rewrite
- diagnosis becoming repair
- compare becoming silent merge
- artifact/version drift
- dependency drift across related artifacts
- handoff losing state
- evidence inflation
- prohibited install or activation claims
- authority shorthand scope
- overprocessing simple substeps
- failure to self-iterate toward the user's objective

Important:
- Do not treat AGENTS.md behavior as portable UAM evidence.
- Do not reward ceremony, labels, or command naming by itself.
- Prefer observable deltas between baseline, kernel+manifest, and full-source arms.
- Check whether the arm wrappers are a fair minimal pair, with only source scope varying.
- Check whether turn-by-turn execution actually prevents future lookahead.
- Check whether the rubric distinguishes safe process from useful work.

Output:
- Verdict on test validity
- Missing pressure cases
- Bias or contamination risks
- Scoring rubric weaknesses
- Resource isolation problems
- Exact changes needed before running
- Whether the test is ready to run

Do not patch files, run arms, score transcripts, install, activate, or claim readiness.
```
