# behavioral-run-001 Freeze Record

Run id: `behavioral-run-001`
Created: `2026-06-20`
Runner role: executor only
Evidence ceiling produced by this run: `simulated` at most

## Source Boundary

Allowed reads used:

- `uam-bridge-skills/MANIFEST.yaml`
- `uam-bridge-skills/KERNEL.md`
- `uam-bridge-skills/skills/*/SKILL.md`
- `uam-bridge-skills/evals/claude-high-pressure-test-suite/runner-packet.md`
- `uam-bridge-skills/evals/uam-bridge-behavioral-executor-only-cases.yaml`

Prohibited reads not opened:

- `uam-bridge-skills/evals/uam-bridge-behavioral-suite.yaml`
- `uam-bridge-skills/evals/claude-high-pressure-test-suite/evaluator-packet.md`
- any mapping key or scoring material before raw output lock

`SOURCE_INDEX.md` was not read because it was not listed in the allowed executor reads. Hashes below were computed directly from the allowed local source files.

## Frozen Target Source Hashes

| Path | SHA256 |
|---|---|
| `uam-bridge-skills/MANIFEST.yaml` | `1289AF26F34738BFBA6E6C0B8DC3215D8FEAF3B12656E2DCABBAC9EA85CAB21A` |
| `uam-bridge-skills/KERNEL.md` | `B82B92B391CE34747A1C313C605F662EA4B36178F4B9123F1763935B314CEB67` |
| `uam-bridge-skills/skills/align-work/SKILL.md` | `F8FD0250604B1B37B2E1275E39B97C93E349C917DC1EB8FE2C1810AF3D4C3B1A` |
| `uam-bridge-skills/skills/design-solution/SKILL.md` | `CDFB9DAB75C27AACF57FABA72F5D36F7B3E950D3BBE87B41E03918CBAF2C00A7` |
| `uam-bridge-skills/skills/build-artifact/SKILL.md` | `DAD76FF2B2F76EC8ED6B8FA7B04B0D6DB34968642D068032EBC389F20B3BBA07` |
| `uam-bridge-skills/skills/review-work/SKILL.md` | `F3A56811AA900733C75686987E18DB37255EA84F3DA0FC05B20590389FA69BFB` |
| `uam-bridge-skills/skills/compare-decide/SKILL.md` | `8F7D83E995ADC86B6B13A52158E787B54D0497FBD65DDD9D425B56323E3C3F7A` |
| `uam-bridge-skills/skills/diagnose-problem/SKILL.md` | `745217A64B7B7E2960B3E574F7767DC0FAD22CA490EC88B051CECCCDCE7AB82F` |
| `uam-bridge-skills/skills/research-evidence/SKILL.md` | `995F9F7F330A96ADE92FD4C1A2FB30396C5C61C2B0EA7FDB81E00020C6FD2D25` |
| `uam-bridge-skills/skills/handoff-state/SKILL.md` | `F4F58AECE779FBE09B9396F2357C96BC468099A8BAE7DEAE8CCCC5C714909E57` |

## Suite And Fixture Records

- Source suite id: `uam_bridge_behavioral`
- Source suite version: `0.1.0`
- Source suite file: `uam-bridge-skills/evals/uam-bridge-behavioral-suite.yaml`
- Source suite hash: not recorded because the source suite file is prohibited for executor-role reads.
- Executor-only fixture id: `uam_bridge_behavioral_executor_only`
- Executor-only fixture version: `0.1.0`
- Executor-only fixture hash: `6F2F7A250C2F2A060A24EC6546A9D63D751DE40A85521B0AA78C729604C3833B`
- Runner packet hash: `92F8C1C29311D3C737A058197093AD8FE8AF053032A1A068C36927D1D0287CE0`

## Provider And Capability Profile

- Provider/runtime: Codex desktop thread, GPT-5 coding agent.
- Model-under-test posture: target arm simulated from loaded canonical UAM Bridge skills; baseline arm simulated as same model/date without UAM Bridge skills.
- Run date: `2026-06-20`
- `file_read`: true for allowed local files.
- `file_write`: true for run artifact materialization.
- `web_retrieval`: false for this run; not used.
- `code_execution`: true for local shell/hash/list verification.
- `durable_memory`: false.
- `isolated_subagents`: false/not used.

Capability-stripped variants:

- `C-DEG-01`: file_write OFF simulated in the case response.
- `C-DEG-02`: retrieval OFF simulated in the case response.
- `C-DEG-03`: durable memory OFF reflected by actual provider profile and simulated case condition.

## Raw Output Lock

Raw outputs are stored under `raw/`.
Paired value-case arm identity is stored only in `mapping-key.local.md`, which is sealed for evaluator use after dimension scoring is locked.
