# Compounding Run 001

Status: patched test packet with collected Codex run artifacts and locked evaluator scoring
Evidence ceiling: simulated transcript evidence only after scoring; no runtime, install, provider-parity, v1-readiness, or production claim is established

## Purpose

This run tests whether UAM Bridge context helps an agent control compounding errors across a long, multi-artifact agent-building exercise.

It is not a one-shot writing test. It pressures:

- stale assumptions from early turns;
- wrong mode selection;
- review becoming rewrite;
- diagnosis becoming repair;
- compare becoming silent merge;
- artifact and version drift;
- dependency drift across related artifacts;
- handoff losing state or rewriting artifacts;
- evidence inflation and readiness overclaim;
- prohibited install or activation claims;
- authority shorthand such as `proceed`;
- overprocessing simple substeps;
- failure to self-iterate toward the user's objective.

## Current Artifacts

The executed Codex pilot artifacts are organized under `codex-run-001/`.

- `codex-run-001/collection/`: collection record, private transcript map, and private hash manifest.
- `codex-run-001/evaluator-packet/`: anonymized transcripts and evaluator instructions suitable for blind scoring.
- `codex-run-001/raw-private/`: private raw JSONL session exports and readable transcript exports.
- `codex-run-001/scoring/`: locked evaluator scoring record and a separate mapped-results summary.
- `codex-run-001/integrity/`: pre-cleanup and post-cleanup hash manifests plus the relocation map.

The prompt/test packet materials remain in `prompts/` and `run-packets/`.

Do not send `collection/private-run-map.md`, `collection/private-hashes.sha256`, or `raw-private/` to a blind evaluator before scoring is locked.

## Design Review Patch Basis

An external test-design validation judged the prior packet adequate as a boundary-discipline harness but not ready for comparative compounding-error claims. This packet was patched to address the gating findings:

- no single-pass future lookahead;
- arm wrappers held to the same run protocol, varying only by allowed source scope;
- three independent replicates per arm;
- same provider, model, temperature, and settings across all arms;
- missing pressure cases added;
- metadata and context-status blinding normalized;
- evaluator rubric revised around gating dimensions, usefulness, and false-improvement risk.

This patch does not run the arms, score outputs, establish runtime behavior, or claim readiness.

## Arms

Arm A, baseline:

- no UAM resources

Arm B, kernel and manifest:

- `KERNEL.md`
- `MANIFEST.yaml`

Arm C, full source-bound UAM:

- `KERNEL.md`
- `MANIFEST.yaml`
- `chain-router-reference.md`
- eight source skill files

`AGENTS.md` is intentionally excluded. It is project-specific and must not be treated as portable UAM packet evidence.

## Execution Model

Run each arm turn-by-turn. The model must not see future turns.

For each arm:

1. Open a fresh TEST context.
2. Attach only the files permitted for that arm.
3. Paste that arm's setup prompt.
4. Wait for `READY_FOR_TURN_01`.
5. Use `prompts/operator-turns.md` as an operator-only script.
6. Paste exactly one user turn at a time.
7. Save the complete raw transcript.

Run three independent replicates per arm: A1-A3, B1-B3, and C1-C3. Use the same provider, model, temperature, and settings for every replicate.

Do not attach `operator-turns.md` to the arm context as a file. It is an operator script, not an arm resource.

## Run Order

1. Optionally send this patched packet to an external reviewer using `prompts/external-reviewer.md`.
2. Run three turn-by-turn replicates for Arm A, Arm B, and Arm C in separate clean TEST contexts.
3. Save all raw outputs.
4. Use `prompts/anonymizer.md` to create anonymized evaluator input and a separate private mapping key.
5. Give only anonymized transcripts to at least one blind evaluator with `prompts/evaluator.md`.
6. Prefer a second blind evaluator or self-consistency rater using the same evaluator prompt.
7. After blind scoring is locked, reveal the mapping key to a source-aware adjudicator using `prompts/source-aware-adjudicator.md`.

## Contamination Controls

Keep these out of every arm context:

- `AGENTS.md`
- `prompts/evaluator.md`
- `prompts/anonymizer.md`
- `prompts/source-aware-adjudicator.md`
- `prompts/external-reviewer.md`
- `run-packets/README.md`
- scoring records
- mapping keys
- raw or anonymized outputs from other arms
- lifecycle-run exports
- prior failed packets
- `handoff-packets/Compound-Test-Run-Handoff Context Resource.md`
- any source file not explicitly allowed for that arm

The context resource may be used only for independent test-design validation, not arm execution or blind scoring.

## Prohibited Claims

Do not claim runtime behavior, provider parity, v1 readiness, install readiness, gate pass, or production behavior from this run. At most, it can produce simulated transcript evidence after scoring.
