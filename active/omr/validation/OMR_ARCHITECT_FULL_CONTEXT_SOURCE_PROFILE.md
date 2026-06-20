# OMR Architect Full Context Source Profile

Generated: 2026-06-19
Purpose: source set for a ChatGPT instance serving as architect for the Operator Model, with AB comparison fully in scope.

## Verdict

Use the `omr_architect_full_context` staging profile.

Path:

`ChatGPT_Project_Source_Staging/omr_architect_full_context/`

## Core Sources

| Order | Source | Role |
|---:|---|---|
| 1 | `AGENTS.md` | Root operating rules, source boundaries, evidence discipline, handoff protocol. |
| 2 | `OMR_Operator_Prototype_Runtime_v0.2.md` | Primary architecture source for O1-O4, state sequencing, ownership, branch/evidence discipline, and prototype boundaries. |
| 3 | `P2_State_Schemas_v0.1.json` | Exact state object contracts; prevents architectural drift on schemas and ownership. |
| 4 | `P5_Executor_View_v0.1.yaml` | Public comparative fixtures; needed because AB comparison and operator evaluation are in scope. |
| 5 | `OMR_Evidence_Capture_Protocol_v0.1.md` | Capture/evidence requirements for valid OMR evaluations and run packages. |
| 6 | `AB_Runtime_Authority_Reference_v1.1.md` | AB authority/routing baseline; keeps AB1-AB9 distinct from O1-O4 and provides comparison boundary. |
| 7 | `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` | AB baseline behavior and E1-E12 comparison context; fully in scope for OMR-vs-AB architectural comparison. |
| 8 | `project-state.md` | Lightweight current-state map and adopted-source context. |
| 9 | `source-checksums_pre-and-post-compression.md` | Provenance/hash context to prevent stale-source confusion. |
| 10 | `compression-adoption-record_2026-06-18.md` | Adoption/status context for active compressed runtime sources. |

## Excluded From Operating Context

- Raw OMR run folders and raw output files.
- Evidence ZIPs unless a specific evaluation/rerun task needs them.
- Legacy `00`-`08`, split `01`, split `06`, and compressed candidate folders.
- Ideation archives, planning examples, O5 future-state packet, and Amazon Q export.
- Extracted package mirrors unless the task is package inspection.

## Use Rule

This profile is intentionally larger than the minimal architect set because AB comparison is explicitly in scope. It is still not a full repository dump: it includes active runtime, exact schemas/fixtures, and provenance only.

Task class: downstream-execution
Terminal state: OMR-first full-context architect source profile created
Do not do next: do not add raw evidence, archives, exports, examples, or legacy split sources to operating context by default
Only valid next step: none required
Recommended context window: current context window
Next role_class: downstream-execution
Next assignee_runtime: Codex
