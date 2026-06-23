# Folder Organization Map

Version: `0.1.0`
Status: current workspace map
Evidence level: static inspection updated on 2026-06-23

## Scope And Limits

This map covers the current workspace rooted at:

```text
C:\Users\Matthew\OneDrive\Documents\UAM MODEL FRAMEWORK\0A. UAM Bridge Skills
```

Git branch metadata is unavailable from this folder. `git rev-parse --show-toplevel` and `git branch --all --no-color` both returned "not a git repository", so "branches" in this resource means project work branches: canonical package, root governance context, donor resources, eval/run material, and generated/transient files.

This map now reflects cleanup batches executed on 2026-06-22 and source-control alignment on 2026-06-23. It is descriptive governance, not delete authority.

## Top-Level Hierarchy

```text
0A. UAM Bridge Skills/
  AGENTS.md
  Prior Agent Context for Task.txt
  UAM_Bridge_Skills_Deployment_Recommendation.md
  UAM_Bridge_Skills_New_Project_Handoff.md
  UAM_Model_Framework.md
  FOR CONTEXT/
  uam-bridge-skills/
    adapters/
      chatgpt/
      claude-code/
      codex/
      gemini/
      generic/
    docs/
      cleanup/
      governance/
      install/
      protocols/
      publication/
    packets/
      operator/
      evaluator/
      install/
      external-review/
    tests/
      runs/
      suites/
      records/
      tools/
      templates/
      archive/
    lenses/
      active/
      candidates/
      archive/
    skills/
      active/
        uam-bridge-skills/
          KERNEL.md
          CHAIN_ROUTER.md
          MANIFEST.yaml
          commands/
      candidates/
      archive/
    tools/
      active/
      candidates/
      archive/
    exports/
      generated/
      archive/
```

## Project Branch Map

| Branch | Primary path | Role | Authority | Cleanup class |
|---|---|---|---|---|
| Operating contract | `AGENTS.md` | Workspace agent instructions and project operating rules. | High for agents in this workspace. | Preserve. Patch only with explicit authorization. |
| Root source context | `UAM_Model_Framework.md`, handoff, recommendation, prior-context files | Project source, state, recommendation, and historical continuity. | High as context and design basis. | Preserve. Do not move without a migration plan. |
| Donor vault | `FOR CONTEXT/` | Old Codex, Claude, and skill-kit resources used as donors. | Donor-only; does not override canonical package. | Preserve as read-only donor material unless user authorizes archival cleanup. |
| Canonical package | `uam-bridge-skills/` | Source package for UAM Bridge Skills rollout. | Canonical package authority through the active skill package at `skills/active/uam-bridge-skills/`. | Preserve structure. Changes must respect manifest authority. |
| Active skill package | `uam-bridge-skills/skills/active/uam-bridge-skills/` | `MANIFEST.yaml`, `KERNEL.md`, `CHAIN_ROUTER.md`, and all active command skill markdowns. | Canonical source for active skill behavior and routing. | Preserve as one package. Patch anchors and commands together when paths or package semantics change. |
| Chain Router | `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md` | Active package routing reference for bounded continuation, stop gates, evidence-stage upgrades, and handoff routing. | Canonical routing support loaded by the kernel and all eight skills. | Preserve with the active skill package and keep loadable in local/provider installs. |
| Skills | `uam-bridge-skills/skills/active/uam-bridge-skills/commands/*/SKILL.md` | Eight portable command skills. | Canonical source for active skill behavior through the active package manifest. | Preserve. Patch only target skill or authorized dependency. Candidate and archive skills are not loadable by default. |
| Lenses | `uam-bridge-skills/lenses/active/*.md` | Reusable reasoning lenses behind skills. | Supporting canonical resources through `MANIFEST.yaml`. | Preserve. Patch when a skill/lens dependency requires it. |
| Adapters | `uam-bridge-skills/adapters/*/README.md` | Provider-specific packaging guidance. | Derived from canonical package; cannot redefine ownership. | Preserve. Update only from manifest/kernel/skill source. |
| Docs | `uam-bridge-skills/docs/<category>/` | Rollout, rollback, install protocol, release gate, blind protocol, executor/evaluator runtime protocol, publication plans, and organization resources. | Governance and process documentation. | Place new docs in the matching category; preserve and update when process or package map changes. |
| Source authority changelog | `uam-bridge-skills/docs/governance/source-authority-change-log.md` | Canonical narrative record explaining why source-authority resources changed. | Governance record supplementing stamps, archives, registries, manifests, and source control commits. | Append/update in the same transaction as source-authority changes. |
| Exports | `uam-bridge-skills/exports/generated/` | Git/API-facing export bundles and source snapshots for external review, provider tests, or architecture audit. | Derived artifacts only; do not treat as canonical source. | Preserve generated records; regenerate through export automation when source changes. |
| Package tools | `uam-bridge-skills/tools/active/` | Manifest-listed source package tooling. | Tooling support derived from package source authority. | Patch with code/tool authority and keep manifest paths current. |
| Reusable test fixtures | `uam-bridge-skills/tests/suites/` | Static and future simulated test cases. | Test fixture source. | Preserve. Patch only with test-design authorization. |
| Test records | `uam-bridge-skills/tests/records/` | Static validation records and evidence records. | Evidence artifacts at stated evidence stage. | Preserve. Do not overwrite historical records without explicit retest/update intent. |
| Test runner scripts | `uam-bridge-skills/tests/tools/runners/` | Deterministic helper scripts for static checks or specialized tests. | Tooling support, not behavioral proof by itself. | Preserve. Patch with code/test authority. |
| Blind run control | `uam-bridge-skills/tests/runs/blind-run-001/` | Frozen run packets and run-control material for future blind assessment. | Evidence/run-control material; run status currently `not_run`. | Preserve. Do not fold into reusable fixtures. |
| Generated/transient files | `**/__pycache__/`, `*.pyc` | Python bytecode generated by prior script execution. | No source authority. | Cleanup candidate after approval and path verification. |

## Canonical Package Structure

| Path | Contains | Notes |
|---|---|---|
| `uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md` | Collaboration Kernel. | Always-on operating discipline, not a ninth command. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml` | Source authority, commands, provider profiles, test suite registry. | Single source of truth for package identity and source ownership. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md` | Chain Router reference used by the kernel and all eight skills. | Skill-routing infrastructure. Preserve with the active skill package and keep loadable in local/provider installs. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/align-work/SKILL.md` | `/align`. | Work contracts, routing, ambiguity and scope gates. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/design-solution/SKILL.md` | `/design`. | Architecture, plans, specifications, target designs. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/build-artifact/SKILL.md` | `/build`. | Authorized artifact creation, patching, augmentation, materialization. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/review-work/SKILL.md` | `/review`. | Read-only assessment, readiness, adversarial and regression review. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/compare-decide/SKILL.md` | `/compare`. | Version, option, baseline, and reconciliation comparison. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/diagnose-problem/SKILL.md` | `/diagnose`. | Failure mechanism, fix layer, impact, and recovery planning. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/research-evidence/SKILL.md` | `/research`. | Source-bounded evidence, verification, synthesis, source maps. |
| `uam-bridge-skills/skills/active/uam-bridge-skills/commands/handoff-state/SKILL.md` | `/handoff`. | State projection, continuation packets, transfer material. |
| `uam-bridge-skills/lenses/active/*.md` | Ten hidden reasoning lenses. | Capability-first, evidence ceiling, blind grading, safe compression, etc. |
| `uam-bridge-skills/adapters/*/README.md` | Provider adapter notes. | Codex, Claude Code, ChatGPT, Gemini, generic. |
| `uam-bridge-skills/tests/` | Suites, records, runner tools, templates, run packets, and generated-cache archive material. | Keep reusable fixtures, evidence records, tools, and run-control folders separated. |
| `uam-bridge-skills/docs/` | Categorized governance docs and process resources. | Use `docs/cleanup/`, `docs/governance/`, `docs/install/`, `docs/protocols/`, and `docs/publication/` according to workstream. |
| `uam-bridge-skills/docs/governance/source-authority-change-log.md` | Source-authority change record. | Update when agent instructions, active package authority, registries, install/publication controls, file-placement maps, or QC authority changes. |
| `uam-bridge-skills/exports/generated/` | Generated export bundles and snapshots. | Use `tools/active/export_relevant_files.ps1`; exports are shareable derivatives, not canonical source. |
| `uam-bridge-skills/tools/active/export_relevant_files.ps1` | Narrow export helper. | Copies curated files into local exports or a target Git repo with SHA-256 verification. |
| `uam-bridge-skills/tools/active/publish_bridge_skills_to_master_repo.ps1` | Master repo publisher. | Prepares or explicitly stages/commits/pushes the active Bridge Skills package to the master UAM GitHub repo with package stamps and source manifests. |
| `uam-bridge-skills/tools/active/validate_workspace_governance.py` | Workspace governance QC. | Checks active hierarchy, future file-placement governance, registry paths, and publication automation guards. |

## Test Folder Map

| Subtype | Path pattern | Purpose | Cleanup rule |
|---|---|---|---|
| Per-skill fixtures | `tests/suites/command-skills/*-cases.yaml` | Design-time cases for command behavior. | Preserve as reusable source. |
| Cross-suite fixtures | `tests/suites/routing/`, `tests/suites/object-integrity/`, `tests/suites/evidence-ceiling/`, `tests/suites/degradation/`, `tests/suites/overactivation/`, `tests/suites/cross-model-parity/`, `tests/suites/behavioral/`, `tests/suites/pressure/` | Shared test families, pressure suites, behavioral suites, executor-only fixture views, and blind value proposition design. | Preserve as reusable source. |
| Test records | `tests/records/` | Evidence at stated stage. | Preserve history; append or version rather than overwrite unless explicitly intended. |
| Runner scripts | `tests/tools/runners/run_static_eval.py`, `tests/tools/runners/run_compare_decide_eval.py` | Static/specialized validation helpers. | Preserve as tooling source. |
| Run-control packets | `tests/runs/blind-run-001/*.md`, `tests/runs/claude-high-pressure-test-suite/*.md` | Freeze, suite design, runner, and evaluator packets for future blind or pressure runs. | Preserve as run-control material; do not treat as executed evidence. |
| Generated cache | `tests/archive/generated-cache/evals-pycache-2026-06-22/*.pyc` | Generated Python bytecode. | Cleanup candidate after approval. |

## Donor Vault Map

| Path | Role | Cleanup rule |
|---|---|---|
| `FOR CONTEXT/*.zip` | Original donor archives. | Preserve unless user explicitly authorizes deduplication or archive migration. |
| `FOR CONTEXT/Claude Skills/` | Claude skill donor material and backlog. | Preserve donor identity. Do not copy one-for-one into canonical package. |
| `FOR CONTEXT/skill-kits/agent-builder-assessment-skills-v1.0.1/` | Unpacked AB donor skill kit. | Preserve as donor and reference corpus. |
| `FOR CONTEXT/**/__pycache__/*.pyc` | Generated bytecode inside donor unpack. | Cleanup candidate only if donor fidelity is not being preserved byte-for-byte. |

## Cleanup Classification

| Class | Meaning | Examples | Default action |
|---|---|---|---|
| `preserve-authority` | Governs project or package behavior. | `AGENTS.md`, `skills/active/uam-bridge-skills/MANIFEST.yaml`, `skills/active/uam-bridge-skills/KERNEL.md`, `skills/active/uam-bridge-skills/CHAIN_ROUTER.md`, `skills/active/uam-bridge-skills/commands/*/SKILL.md`, `docs/governance/source-authority-change-log.md`. | Do not move/delete. Patch only with authority. |
| `preserve-source` | Source material or reusable project artifact. | `docs/<category>/*.md`, `lenses/active/*.md`, `adapters/*/README.md`, `tools/active/*`, `tests/suites/**/*.yaml`. | Keep in place unless map update authorizes move. |
| `preserve-evidence` | Records, freeze packets, test records, run packets. | `tests/records/**/*.md`, `tests/runs/blind-run-001/*.md`. | Do not overwrite or delete. Version/append. |
| `preserve-donor` | Donor resources used for mining patterns. | `FOR CONTEXT/`. | Keep read-only by default. |
| `cleanup-candidate` | Generated or redundant files with no source authority. | `__pycache__/`, `*.pyc`. | List for approval before deletion. |
| `needs-triage` | Ambiguous placement or duplicate status. | Future ad hoc outputs, uncategorized run folders. | Diagnose first; do not move/delete in same step unless authorized. |

## Known Current Cleanup Candidates

Static inspection found generated Python cache files:

```text
uam-bridge-skills/tests/archive/generated-cache/evals-pycache-2026-06-22/run_static_eval.cpython-314.pyc
FOR CONTEXT/skill-kits/agent-builder-assessment-skills-v1.0.1/tests/__pycache__/test_pm_router_kit.cpython-312.pyc
FOR CONTEXT/skill-kits/agent-builder-assessment-skills-v1.0.1/skills/_shared/scripts/__pycache__/validate_pm_invocation.cpython-312.pyc
```

These are candidates only. Do not delete them without explicit cleanup authorization, especially because two live under donor material where byte-for-byte preservation may matter.

## Recommended Future Organization

No immediate restructuring is required. If the workspace grows, add new files under the governed homes below:

- New governance/release docs: `uam-bridge-skills/docs/governance/<topic>.md`
- New source-authority change entries: append/update `uam-bridge-skills/docs/governance/source-authority-change-log.md`
- New cleanup maps, ledgers, and records: `uam-bridge-skills/docs/cleanup/<topic>.md`
- New protocol docs: `uam-bridge-skills/docs/protocols/<topic>.md`
- New publication/export plans: `uam-bridge-skills/docs/publication/<topic>.md`
- New install/dogfood docs: `uam-bridge-skills/docs/install/<topic>.md`
- New reusable test fixtures: `uam-bridge-skills/tests/suites/<category>/<suite>-cases.yaml`
- New test run packets: `uam-bridge-skills/tests/runs/<run-id>/`
- New package packets: `uam-bridge-skills/packets/<operator|evaluator|install|external-review>/<packet-id>/`
- New provider adapter material: `uam-bridge-skills/adapters/<provider>/`
- New generated exports: `uam-bridge-skills/exports/generated/<export-id>/`
- New active tools: `uam-bridge-skills/tools/active/<tool-name>`
- New candidate tools: `uam-bridge-skills/tools/candidates/<tool-name>`
- New active lenses: `uam-bridge-skills/lenses/active/<lens-name>.md`
- New active command skills: `uam-bridge-skills/skills/active/uam-bridge-skills/commands/<skill>/SKILL.md` after manifest authorization
- New candidate skills: `uam-bridge-skills/skills/candidates/<forward|experimental|parked>/<skill>/SKILL.md`
- New donor resources: `FOR CONTEXT/<source-name>/`

Avoid adding new top-level folders unless the object is neither canonical package material nor donor/context material.
