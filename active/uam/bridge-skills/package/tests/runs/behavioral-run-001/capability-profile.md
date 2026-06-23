# behavioral-run-001 Capability Profile

Provider/runtime: Codex desktop thread, GPT-5 coding agent.
Run date: 2026-06-20.

| Capability | Availability in this run | Notes |
|---|---:|---|
| `file_read` | true | Used only for allowed executor source files. |
| `file_write` | true | Used to materialize `behavioral-run-001` artifacts. |
| `web_retrieval` | false | Not used for this executor role. |
| `code_execution` | true | Used for local hashing, copying, and verification commands. |
| `durable_memory` | false | No durable project memory used or relied on. |
| `isolated_subagents` | false | No subagents used. |

Per-case capability limits:

- `C-DEG-01`: file write disabled inside the simulated prompt environment.
- `C-DEG-02`: live retrieval disabled inside the simulated prompt environment.
- `C-DEG-03`: durable memory disabled inside the simulated prompt environment.

Raw case outputs were generated as text-only simulated model responses. No per-case tool calls were executed.
