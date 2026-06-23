# Codex Run 001

Run: compounding-run-001 / codex-run-001
Status: collected, anonymized, dispatched, and scored
Evidence ceiling: simulated transcript evidence only

## Purpose

This folder contains the Codex-executed artifacts for the compounding pilot comparing:

- Arm A: baseline, no UAM resources.
- Arm B: `KERNEL.md` plus `MANIFEST.yaml`.
- Arm C: `KERNEL.md`, `MANIFEST.yaml`, chain router reference, and the eight source skill files.

The run tests lifecycle behavior over a multi-turn agent-building exercise. It does not prove runtime behavior, provider parity, installation success, v1 readiness, release readiness, or production behavior.

## Folder Map

- `collection/`: run collection record, private label mapping, and private hashes.
- `evaluator-packet/`: anonymized evaluator packet and packet-local hashes.
- `raw-private/`: raw JSONL and transcript exports for the nine Codex test threads.
- `scoring/`: locked evaluator scoring record plus mapped, derived analysis.
- `integrity/`: cleanup relocation map and before/after run-level hash manifests.

## Data Handling

The blind evaluator packet is `evaluator-packet/ANONYMIZED_TRANSCRIPTS_FOR_EVALUATOR.md` plus `evaluator-packet/EVALUATOR_INSTRUCTIONS.md`.

Keep these private unless the scoring phase is already locked:

- `collection/private-run-map.md`
- `collection/private-hashes.sha256`
- `raw-private/`

The locked evaluator output is `scoring/scoring-record.md`. Any arm mapping, aggregate score, or interpretation belongs in a separate derived file, currently `scoring/mapped-results.md`.

## Integrity Notes

The cleanup pass moved metadata and scoring files into subfolders, then recorded the move hashes in `integrity/relocation-map.md`. Raw transcripts, anonymized evaluator packet files, prompt packets, and locked scoring content were not edited by the relocation step.

