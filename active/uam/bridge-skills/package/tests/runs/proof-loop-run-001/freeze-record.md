# Proof Loop Run 001 Freeze Record

Run id: `proof-loop-run-001`
Status: packet-draft, not frozen, not run
Created: 2026-06-22
Evidence ceiling: design-time

## Current Status

This record defines the intended freeze set for a future proof-loop run. It is not yet a formal run freeze because no runner has confirmed topology, no attempt id has started, and hashes have not been rechecked immediately before execution.

Do not run, score, install, activate, or claim evidence from this record.

## Packet Files

- `uam-bridge-skills/docs/behavioral-proof-loop.md`
- `uam-bridge-skills/evals/proof-loop-run-001/runner-packet.md`
- `uam-bridge-skills/evals/proof-loop-run-001/evaluator-packet.md`
- `uam-bridge-skills/evals/proof-loop-run-001/freeze-record.md`
- `uam-bridge-skills/evals/proof-loop-run-001/capability-profile.md`
- `uam-bridge-skills/evals/proof-loop-run-001/intervention-log.md`

## Source Files For Arms

Arm A, `clean_baseline`:

- none from this project

Arm B, `project_contract_only`:

- `AGENTS.md`

Arm C, `kernel_only`:

- `uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/MANIFEST.yaml`

Arm D, `source_bound_uam`:

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

Arm E, `isolated_codex_dogfood`:

- blocked until Stage 2 isolated dogfood install is separately authorized and verified

## Hash Status

Hashes must be recorded immediately before a formal attempt begins. The freeze record's own hash may be excluded or recorded by an auditor after finalization.

Required algorithm: `SHA256`.

## Formal Freeze Checklist

- [ ] Confirm packet files are final for the attempt.
- [ ] Record SHA256 hashes for all packet files, excluding this freeze record if self-hash is impractical.
- [ ] Record SHA256 hashes for every source file exposed to arms B through D.
- [ ] Record provider, model, date, runtime, workspace path, and tool access per arm.
- [ ] Confirm runner contexts have not read evaluator materials.
- [ ] Confirm evaluator context will not see mapping key before scoring locks.
- [ ] Confirm no source patching will occur during the run series.
- [ ] Assign attempt id.

## Prohibited Actions

- Do not run cases from this draft record.
- Do not score outputs before anonymization and mapping separation.
- Do not install or activate any skills.
- Do not patch source files during the run series.
- Do not claim gate pass, v1 readiness, runtime behavior, provider parity, or production behavior.
