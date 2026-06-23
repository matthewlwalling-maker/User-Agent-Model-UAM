# Workspace Taxonomy V2

Status: implemented workspace taxonomy for completed cleanup batches; remaining stop gates listed below
Date: 2026-06-22
Evidence ceiling: design-time/static review
Scope: UAM Bridge Skills workspace organization, package source lifecycle, test/eval structure, packets, exports, and archives

## Purpose

Define the next workspace architecture in terms that match how the project is actually being worked:

- active governance remains easy to find;
- active command skills are separated from forward candidates and archived lineage;
- eval work is reframed as tests with clear suites, runs, roles, scoring, and results;
- packets, exports, and evidence remain distinct;
- archives preserve truthful lineage without creating duplicate active authority;
- future cleanup can move quickly without breaking manifest paths, private evidence boundaries, or artifact-index rules.

This document began as the target design. Cleanup execution records now identify the moves completed on 2026-06-22. It still does not authorize deletion, install, publish, stage, commit, push, activation, or readiness claims.

## Governing Constraints

1. `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml` is the active skill package source of truth.
2. `UAM_Artifact_Index.yaml` remains the root governed-artifact index for UAM framework artifacts.
3. `AGENTS.md`, `KERNEL.md`, `CHAIN_ROUTER.md`, active command skill files, and manifest-registered eval suites are preserve-authority or preserve-source material.
4. Candidate skills must never become loadable command skills by directory scanning alone.
5. Test raw material, evaluator scoring keys, mapping keys, and private run maps must be excluded from public exports by default.
6. Archive history must be truthful: use observed dates, source labels, hashes, and `backfilled-lineage`; do not fabricate or backdate history.
7. A move that changes manifest paths, adapter expectations, export inputs, or artifact-index references requires a migration ledger and verification.
8. Source-authority changes must update `docs/governance/source-authority-change-log.md` in the same transaction as the authority edit.

## Target Root Shape

```text
0A. UAM Bridge Skills/
  AGENTS.md
  UAM_Artifact_Index.yaml
  UAM_Artifact_Naming_and_Archive_Convention.md
  UAM_Model_Framework.md
  UAM_Model_Participation_and_Assurance_Plan.md
  UAM_Source_Intake_and_Context_Map.md
  UAM_Bootstrap_Pair_Brief.md
  archive/
    root-governance/
      backfilled-lineage/
      displaced-snapshots/
  FOR CONTEXT/
    archive/
  handoff-packets/
    open/
    archive/
  uam-bridge-skills/
```

Local runtime folders such as `.codex/` and `.venv/` may remain at root. Empty invalid runtime shells such as empty `.agents/` and empty invalid `.git/` remain cleanup candidates only after immediate pre-action verification.

## Target Package Shape

```text
uam-bridge-skills/
  requirements-dev.txt
  adapters/
    codex/
    claude-code/
    chatgpt/
    gemini/
    generic/
  skills/
    active/
      uam-bridge-skills/
        KERNEL.md
        CHAIN_ROUTER.md
        MANIFEST.yaml
        commands/
          align-work/
          build-artifact/
          compare-decide/
          design-solution/
          diagnose-problem/
          handoff-state/
          research-evidence/
          review-work/
    candidates/
      forward/
      experimental/
      parked/
    archive/
      backfilled-lineage/
      retired/
    SKILL_REGISTRY.yaml
  tests/
    suites/
      command-skills/
      routing/
      object-integrity/
      evidence-ceiling/
      degradation/
      overactivation/
      cross-model-parity/
      pressure/
      behavioral/
      lifecycle/
      compounding/
    runs/
      <run-id>/
        RUN_MANIFEST.yaml
        source-freeze/
        runner/
        evaluator/
        scorer/
        results/
        public-evidence/
        private.local/
        scoring-keys.local/
        integrity/
        packets/
    tools/
    records/
      static-validation/
      regression/
    archive/
    TEST_REGISTRY.yaml
  docs/
    governance/
    cleanup/
    publication/
    install/
    protocols/
    archive/
  packets/
    operator/
    evaluator/
    install/
    external-review/
    archive/
  exports/
    generated/
    archive/
  tools/
    active/
    candidates/
    archive/
  lenses/
    active/
    candidates/
    archive/
```

## Authority Model

`skills/active/uam-bridge-skills/MANIFEST.yaml` controls active package load paths. It is the only source that makes a command skill active.

`SKILL_REGISTRY.yaml` describes skill lifecycle status. It does not activate skills by itself.

`TEST_REGISTRY.yaml` describes test suites, run types, evidence stages, and exportability. It does not upgrade evidence by itself.

`UAM_Artifact_Index.yaml` controls root governed UAM artifacts. It does not make package-local candidates active unless the manifest or a governed artifact transaction says so.

Exports and packets are derived transport material. They can carry source snapshots and evidence, but they are not canonical source unless promoted through the appropriate active-source transaction.

## Skill Lifecycle Rules

Active command skills:

- must be named in `MANIFEST.yaml`;
- must live at the manifest path;
- must remain housed with `KERNEL.md`, `CHAIN_ROUTER.md`, and `MANIFEST.yaml` inside the active skill package;
- must have one command identity and one `SKILL.md`;
- must preserve the eight-command surface.

Candidate skills:

- may live under `skills/candidates/`;
- must include lifecycle metadata;
- must default to `loadable: false`;
- must not share an active command ID unless explicitly marked as a replacement candidate;
- must not be exported as active command source unless a test packet intentionally includes them as candidates.

Archived skills:

- must preserve original bytes when possible;
- must include observed source, observed date, prior path, hash, and reason archived;
- must use truthful lineage labels such as `backfilled-lineage`, `retired`, or `displaced-snapshot`.

Proposed registry skeleton:

```yaml
skills:
  - skill_id: uam.review-work
    command: /review
    status: active
    path: skills/active/uam-bridge-skills/commands/review-work/SKILL.md
    loadable: true
    manifest_controlled: true
  - skill_id: uam.some-forward-candidate
    command: null
    status: forward-candidate
    path: skills/candidates/forward/some-forward-candidate/SKILL.md
    loadable: false
    manifest_controlled: false
```

## Test Architecture Rules

The rename from `evals/` to `tests/` was executed on 2026-06-22 through a compatibility migration.

Reusable suite files belong under `tests/suites/`.

Run instances belong under `tests/runs/<run-id>/`.

Every run must include `RUN_MANIFEST.yaml` with:

```yaml
run_id: string
run_type: static-validation | blind | pressure | behavioral | lifecycle | compounding | comparison
source_basis: list
evidence_stage: design-time | simulated | live-runtime | post-implementation | production-observed
exportability: public | internal | private-local
private_material:
  allowed: true | false
  paths: []
roles:
  runner: required | optional | not-used
  evaluator: required | optional | not-used
  scorer: required | optional | not-used
status: planned | frozen | run | scored | reviewed | archived
```

Role folders are optional by run type. A static validation run does not need to pretend it has a runner/evaluator/scorer workflow if it does not.

Private and scoring material must use `.local` directory names or another explicit non-exportable marker.

`public-evidence/` is the only run subfolder that export tooling may include by default.

## Docs, Packets, Exports, And Tools

Docs are organized by workstream:

- `docs/governance/` for source authority, release gates, rollout rules, and registry semantics;
- `docs/cleanup/` for workspace cleanup plans and execution records;
- `docs/publication/` for master repo and export publication planning;
- `docs/install/` for isolated profile install and activation packets;
- `docs/protocols/` for blind tests, executor/evaluator runtime, proof loops, and comparable procedures.

Packets should move toward package-local `packets/` for future generated operator/evaluator/install/external-review packets. Existing top-level `handoff-packets/` can remain as the workspace-level open/historical handoff area until references are migrated.

Exports should remain clearly generated. Export folders must include source references, hashes, and exclusions. Generated exports must not be treated as active package source.

Tools are split into `tools/active/`, `tools/candidates/`, and `tools/archive/`. Active manifest-listed tools live under `tools/active/`, and any future tool move requires a paired manifest/reference patch when applicable.

`docs/governance/source-authority-change-log.md` is the canonical narrative record for changes to agent instructions, active package authority, registries, install/publication controls, file-placement maps, and QC authority. It supplements hashes, archives, migration ledgers, and commits.

## Migration Gates

For any future package path move, satisfy these gates before execution:

1. `AGENTS.md` active-index mismatch is reconciled or explicitly excluded from the migration scope.
2. A migration ledger exists with `current_path`, `target_path`, `class`, `manifest_impact`, `reference_impact`, `privacy_impact`, `hash_before`, `hash_after`, and `rollback`.
3. `MANIFEST.yaml` has a paired patch for any affected root, tool path, command path, export profile, lens path, or test suite path.
4. Export tooling has explicit private-material exclusions for `private.local`, `scoring-keys.local`, raw transcripts, private maps, and evaluator keys.
5. Active skills have a manifest whitelist so candidates cannot be loaded by scanner behavior.
6. Existing handoff, export, and eval-run references have been searched and classified.
7. A post-migration validation script or checklist can verify that active command paths, suite paths, and tool paths resolve.

## Fast Execution Sequence

The fast execution sequence now stands as follows:

1. Stage 2 root cleanup is partially executed: displaced `README.md` is archived and `requirements-dev.txt` has moved into `uam-bridge-skills/` with the paired validator guidance patch. Empty invalid runtime shells remain cleanup candidates only after immediate verification.
2. Create non-invasive v2 scaffolding docs and registries before source moves.
3. `SKILL_REGISTRY.yaml` now reflects the active `skills/active/uam-bridge-skills/commands/` root and keeps candidates non-loadable by default.
4. Export rules were patched before moving or exposing run material.
5. Treat `tests/` as the active test root; the former `evals/` contents moved on 2026-06-22.
6. Treat `skills/active/uam-bridge-skills/`, `tools/active/`, `lenses/active/`, and `exports/generated/` as the active homes after the final cleanup batch.
7. Run static validation after each future migration batch.

## Source Controls Now Active

These governance surfaces now command the active map:

1. `AGENTS.md` points source-bound command work to `skills/active/uam-bridge-skills/commands/<command-skill>/SKILL.md` and the active package anchors.
2. `MANIFEST.yaml` uses `skills/active/uam-bridge-skills/commands`, `tools/active`, `lenses/active`, `tests`, and `exports/generated`.
3. `SKILL_REGISTRY.yaml` describes active skills under `skills/active/uam-bridge-skills/commands` and keeps candidates and archives non-loadable by default.
4. `TEST_REGISTRY.yaml` uses active `tests/` paths and preserves private/scoring export exclusions.
5. `folder-organization-map.md` and this taxonomy define future file placement by workstream.
6. `docs/governance/source-authority-change-log.md` records why source-authority resources changed and what validation bounded the claim.

## Stop Conditions

Stop before execution if:

- a proposed move affects a manifest path without a paired manifest patch;
- candidate skills could be mistaken for active command skills;
- private test material could enter public exports;
- an artifact-index mismatch blocks material action;
- a target path already exists unexpectedly;
- a source path is missing or hash verification fails;
- the change would imply install, activation, publication, or readiness.

## Recommended Next Move

Treat file cleanup as complete at the current no-delete boundary. Future movement should be targeted: delete-gated placeholders, donor vault cleanup, or generated-cache deletion only after explicit user authority and immediate pre-action verification.
