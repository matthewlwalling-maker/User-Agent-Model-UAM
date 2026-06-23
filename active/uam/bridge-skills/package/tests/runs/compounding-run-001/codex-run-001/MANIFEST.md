# Codex Run 001 Manifest

Run: compounding-run-001 / codex-run-001
Evidence label: simulated transcript evidence after evaluator scoring
Cleanup label: static organization and hash verification

## Primary Audit Files

| Path | Role | Visibility |
|---|---|---|
| `collection/collection-record.md` | Collection method, run IDs, source session paths, dispatch status | Private audit |
| `collection/private-run-map.md` | Mapping from anonymized transcript labels to arms, replicates, and threads | Private until scoring is locked |
| `collection/private-hashes.sha256` | Historical private hash manifest created at collection time | Private audit |
| `evaluator-packet/ANONYMIZED_TRANSCRIPTS_FOR_EVALUATOR.md` | Blind evaluator input | Shareable with evaluator |
| `evaluator-packet/EVALUATOR_INSTRUCTIONS.md` | Blind evaluator instructions | Shareable with evaluator |
| `evaluator-packet/HASHES.sha256` | Evaluator packet hash manifest | Shareable with evaluator |
| `raw-private/` | Raw JSONL and transcript exports for runs 01-09 | Private audit |
| `scoring/scoring-record.md` | Locked evaluator scoring output | Audit record |
| `scoring/mapped-results.md` | Derived arm mapping and aggregate interpretation | Post-scoring analysis |
| `integrity/pre-cleanup-manifest.sha256` | Run-level hash manifest before cleanup relocation | Integrity audit |
| `integrity/relocation-map.md` | File moves and move-time hashes | Integrity audit |
| `integrity/post-cleanup-manifest.sha256` | Run-level hash manifest after cleanup relocation and index creation | Integrity audit |

## Integrity Commitments

- Raw private transcripts are preserved as collected.
- Anonymized evaluator packet files are preserved as dispatched.
- Locked scoring is preserved as received, then moved into `scoring/scoring-record.md`.
- Mapping and aggregate analysis are separate from the locked scoring record.
- No claim stronger than simulated transcript evidence is supported by this run.

