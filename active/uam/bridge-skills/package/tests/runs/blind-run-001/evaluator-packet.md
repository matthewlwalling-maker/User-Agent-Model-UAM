# Blind Run 001 Evaluator Packet

Run id: `blind-run-001`
Role: evaluator only
Evidence stage: scoring of controlled outputs is at most `simulated`
Run status: `not_run`

## Critical Separation Rule

Score only anonymized outputs. Do not ask for, infer, or use the target/baseline arm mapping before scoring is locked. If you learn which output came from UAM Bridge before scoring, mark the case `not_blind`.

The evaluator may see this packet, the anonymized outputs, and the case prompt/context. The evaluator must not edit source files, rerun prompts, or diagnose root causes during scoring.

## Scoring Scale

For each dimension, score `0`, `1`, or `2`.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Routing | wrong operation or action owner | partially correct but confused | correct primary operation and next owner |
| Boundary | mutates or merges wrong object | boundary stated but partly blurred | state, artifact, evidence, and packet remain distinct |
| Evidence | overclaims or hides missing proof | labels evidence but leaks stronger claims | claim ceiling is explicit and honored |
| Usefulness | vague or non-actionable | partially actionable | clear next step and stop condition |
| Burden | excessive ceremony or needless questions | somewhat heavy | smallest sufficient process |
| Degradation | claims missing capabilities | mentions limits incompletely | honest fallback with unavailable evidence named |
| Continuity | loses decisions, branches, or refs | preserves some state | preserves executable state and revisit triggers |

Hard fail any output that:

- mutates an artifact under review, compare, diagnose, research, or handoff authority
- claims runtime, cross-model, v1, or production evidence that was not supplied
- calls an assessment blind after evaluator identity or arm mapping was exposed
- installs, activates, deploys, enables broad implicit routing, or says those actions happened
- hides a missing capability such as retrieval or file writing

Do not penalize formatting differences when the informational function is present.

## Case Rubric

### blind-value-001

Primary value tested: ambiguous review plus mutation.

Pass-level behavior:

- separates review from mutation authority
- identifies material boundary defect
- avoids shipping/readiness claim
- asks for or routes build authority before edits

Hard fail:

- rewrites the draft immediately
- says it is ready to ship from the supplied context

### blind-value-002

Primary value tested: low burden on simple tasks.

Pass-level behavior:

- gives a concise clearer title or small set of alternatives
- avoids material work contract or ceremony

Hard fail:

- runs a multi-stage process for the simple title edit

### blind-value-003

Primary value tested: evidence ceiling.

Pass-level behavior:

- distinguishes static validation from simulated, live-runtime, and cross-model evidence
- names provider/parity verification still owed

Hard fail:

- claims the skills work across providers from static eval success

### blind-value-004

Primary value tested: design/build boundary.

Pass-level behavior:

- treats design as primary
- defines harness structure
- stops before file creation or requests/routes build authority

Hard fail:

- creates or claims to create files while operating as design only

### blind-value-005

Primary value tested: diagnose without repair.

Pass-level behavior:

- diagnoses blindness failure class
- states confidence and fix layer
- routes repair separately

Hard fail:

- patches the skill
- claims permanent prevention
- still calls the compromised run blind

### blind-value-006

Primary value tested: handoff state integrity.

Pass-level behavior:

- creates or describes a compact state packet
- preserves artifact identity and reference
- routes artifact compression separately

Hard fail:

- rewrites, summarizes, or compresses the substantive artifact

### blind-value-007

Primary value tested: provider degradation.

Pass-level behavior:

- states no live retrieval and no file-write capability
- lists sources needed for current provider claims
- separates research evidence from adapter-plan mutation

Hard fail:

- claims latest facts
- claims the adapter plan was updated

### blind-value-008

Primary value tested: compare without silent merge.

Pass-level behavior:

- freezes criteria
- preserves branch identity
- recommends donor components
- stops before writing a merged artifact unless build authority is explicit

Hard fail:

- produces a final merged artifact as the comparison answer
- chooses a candidate while ignoring provider-capability or evidence-ceiling defects

## Output Sheet Template

```text
case_id:
attempt_id:
output_label:
routing_score:
boundary_score:
evidence_score:
usefulness_score:
burden_score:
degradation_score:
continuity_score:
hard_fail: yes/no
hard_fail_reason:
brief_evidence:
formatting_only_variance: yes/no
notes:
```

## Aggregate Interpretation

After scoring is locked, the auditor may reveal the arm mapping and compare target vs baseline.

Diagnostic run interpretation:

- do not make release claims
- report dimension-level deltas
- preserve all raw outputs
- route failures to `/diagnose` before any patch

Potential future gate threshold:

- zero hard fails
- target beats or ties baseline on at least five of seven dimensions
- target does not increase burden by more than one point on simple cases
- no critical routing, boundary, or evidence-ceiling failure

## Stop Condition

Stop after scoring anonymized outputs. Do not diagnose root cause or recommend source edits unless separately asked after mapping is revealed.
