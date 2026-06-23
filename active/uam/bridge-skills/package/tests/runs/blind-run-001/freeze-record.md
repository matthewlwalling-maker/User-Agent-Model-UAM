# Blind Run 001 Freeze Record

Run id: `blind-run-001`
Freeze date: `2026-06-20`
Package: `uam-bridge-skills`
Package version: `0.1.0`
Evidence stage: `design-time freeze only`
Run status: `not_run`

## Purpose

Freeze the current UAM Bridge Skills source package for a future blind comparative run against a baseline assistant. This record does not execute prompts, score outputs, validate behavior, or upgrade evidence.

## Target Boundary

Frozen target includes the canonical package files under `uam-bridge-skills/` that define source, adapters, docs, lenses, skills, eval fixtures, and runner scripts.

Frozen target excludes:

- generated `__pycache__` content
- `.pyc` files
- future raw run outputs
- future anonymized scoring sheets
- this `evals/blind-run-001/` packet directory, which is run-control material created after the source freeze

Git revision: unavailable. The workspace is not currently a Git repository from this directory, so SHA256 file hashes are the target identity.

## Frozen Goal And Capability Basis

The blind run will assess whether the eight UAM Bridge Skills improve behavioral utility over a same-model baseline while preserving:

- correct primary command routing
- state, artifact, evidence, and packet boundaries
- evidence-ceiling discipline
- useful next-step collaboration
- low-burden handling of simple requests
- honest provider degradation
- cross-command continuity

The run must not assess v1 release readiness, broad implicit routing, production behavior, or cross-model parity unless separate required evidence exists.

## Required Role Separation

For a result to be called blind:

- the runner must not see hidden traps, required behavior, prohibited behavior, scoring keys, evaluator packet, or arm mapping after anonymization
- the evaluator must not know which anonymized output came from UAM Bridge or baseline
- target and baseline outputs must be produced from the same prompt and supplied context
- retries must receive new attempt ids
- source files must not be edited during the frozen run series

If these conditions are violated, label the result `non-blind simulated` or lower.

## Source Hashes

Format: `relative_path sha256`

```text
adapters/chatgpt/README.md f57ab664805c9339a70224583992f0cf8d7a65ff9c62b97dbd0ec421897db67c
adapters/claude-code/README.md 92546d48e03a0de8bf2deb8245357a15561c3a399482663b5edd169a84f2c94c
adapters/codex/README.md 3a196aa86d0281e47424bfa4246e94aa6b3e70176a09022481a2241821f7b9c5
adapters/gemini/README.md bebc655755405ba4da461b02dc73647da643dd72e18d03ba3148cbbc4b6ea120
adapters/generic/README.md c4ab3df7a23cd01b72eceb2689ade46bbdbda8a24cf8233e3c467e1d48dc0cdd
docs/blind-test-protocol.md 21623efe69b05577ff48a0791c5b034cc4ac190922ba68596930b61de73c9f4a
docs/rollback.md b5eab987b7a2e742631e668c7746558e20a5fa34d3caf5e2705de19c67715d5c
docs/rollout-plan.md 4d37eab3d70d25435687541f7faa6feb75d7769db5168566a71ac2d1dba14a90
docs/v1-release-gate.md 321cac65b2916899a751f5aa0b29590a8d0870bafb76b5c445c7646c4bbb9463
evals/align-work-cases.yaml 573ff49a0222f2758dee6e1fda6039f8317c1e5b4b936ded73c513bf7f538d7c
evals/align-work-eval-record.md 74a092dfd7652648504f7b3f0126d321978bc28d6b67ce021f052610cfb4ae91
evals/blind-value-proposition-cases.yaml f852d46b0ddf3d3a2df09e77f761b2ef5d46b769bbfa80a556dd2a56f5f74311
evals/build-artifact-cases.yaml 3895d9808e71de1fc5fcf3cef7fa4827cff31a3cd561d5c8fe34e9b3c9e454a5
evals/build-artifact-eval-record.md cc33c999ffd7f0a11da528c5a7b334ea91904198ac90cf0fb0a1453c7e27a6c9
evals/compare-decide-cases.yaml 3c9e62d676e8e8247a159c62c57bc0f9055e3fde7a4a8bfcd94f1e1f066e4c64
evals/compare-decide-eval-record.md 3527b1563419c89c950b1c00b7469515f42cfb0856dc6d6b88409427c1277285
evals/cross-model-parity.yaml cb4945365b3c9ef62031a927fa36a047b6adc2d6b65e9df1907fb9c2a80824c2
evals/degradation-cases.yaml f272f1cf77ef15e52dd88a697e20856633cb9595e3fac83ce3f0e1d236dd5095
evals/design-solution-cases.yaml 8b68e1af3e88aef582d3f35707ee92f05ca5a121822d5a9405842c9c0bf526a7
evals/diagnose-problem-cases.yaml 8da9cb6bb6536f74d71bc4bc5dafcea07b7c48c8f77a56920c3408eb479b7fcb
evals/evidence-ceiling-cases.yaml aa87969de4a9cb32c0a12fce0762e4a4af3c395de01a7571d1e093071d7477ab
evals/handoff-state-cases.yaml 04b97c4e432f857bbef9e888db1090d228af34b287c68695886076b85b411d65
evals/object-integrity-cases.yaml 91992ddf27d39ff565d28542e22c83f21af9aef1b02076ab2c69d07fc06daf6d
evals/overactivation-cases.yaml 03a13f51d6380c818291b58afabb37368d697f091cb11b6b7a82a1bbe890c0a1
evals/research-evidence-cases.yaml 91301d7dfe396d7aef2b281aa46d7c2a908319266da930e2c7356dc27a5e742b
evals/research-evidence-eval-record.md b773c5e2ceda53622bd2c842197f2ef20cc5afff98dfba05a4da00a446d6593b
evals/review-work-cases.yaml 593bedc92b53a4e34bc838187b8129886b151065dd3e5e62ed5aed100a0397b8
evals/review-work-eval-record.md 96776bed921ee34a3ff01b859b647006dcca33941ed07eca230c1aad1fc4d4cb
evals/routing-cases.yaml 2fc9e48eaadde29272bce36b2bdce0b40037f0e84aa6e9971721304f51959e25
evals/run_compare_decide_eval.py 31568d4fc6bfe62a58cd9639dfcdb5489ab35d658543841f91d5f344cecd2978
evals/run_static_eval.py 8d60a406cd73f842d4474d7582c3e0cc314ca778950132cf4e9d4ce16b80898c
evals/test-suite-eval-record.md 5c14600a8a15e1b91327370d38d6a13ceb6538ecdc747637a7a82950b31dd279
KERNEL.md b82b92b391ce34747a1c313c605f662ea4b36178f4b9123f1763935b314ceb67
lenses/blind-grading.md 568969542139b45ef8efaa0c92ef0b9f1794ab8140aa0942ce618a0415a3c2f9
lenses/break-it-testing.md 55880fe7e7efdfebaf3e24a14826ed14c6fcd3c5486f235639c807abd910a771
lenses/capability-first.md 62c7c2f6d96928271803df44d83e6b63eb4333d4639ee748fcf85bff1be41975
lenses/evidence-ceiling.md 212051b5b02396d0078e44f439bdc5d03ba8c4f4b33fb1a9541fd1a2eeaa48b7
lenses/gold-standard.md 65825c5b4c5fe84b436a36fd08af34826506e730f4033382de010f1978789aca
lenses/narrative-substance.md 6fb3e8336dd62422f5cd6faf370d6c82735a43c188abf326ce4d11fdd3025b91
lenses/premortem.md 63113b473ee10db9567917f4df3cecbd50382d0f12dfd15d7b02d243336f743f
lenses/safe-compression.md d1400b0910f9ead4f16ca645e99e0a91a0b0d06e4a1864692518ed8d3548bc41
lenses/state-projection.md 1841021b55e1a6be925f30f9ad6c3643c3bbaf331da2db7e159fc2b8b108a562
lenses/variant-reconciliation.md a509ec8170ef1a87a6aaf008d0ca34e0b1bfa8fada8e5ce267286fb50c68dc73
MANIFEST.yaml 378cffa6b934fb707ee0e438cd717765dc82dfd42a6706a98d60b88d583ddf00
skills/align-work/SKILL.md f8fd0250604b1b37b2e1275e39b97c93e349c917dc1eb8fe2c1810af3d4c3b1a
skills/build-artifact/SKILL.md dad76ff2b2f76ec8ed6b8fa7b04b0d6db34968642d068032ebc389f20b3bba07
skills/compare-decide/SKILL.md 8f7d83e995adc86b6b13a52158e787b54d0497fbd65ddd9d425b56323e3c3f7a
skills/design-solution/SKILL.md cdfb9dab75c27aacf57faba72f5d36f7b3e950d3bbe87b41e03918cbaf2c00a7
skills/diagnose-problem/SKILL.md 745217a64b7b7e2960b3e574f7767dc0fad22ca490ec88b051cecccdce7ab82f
skills/handoff-state/SKILL.md f4f58aece779fbe09b9396f2357c96bc468099a8bae7deae8cccc5c714909e57
skills/research-evidence/SKILL.md 995f9f7f330a96ade92fd4c1a2fb30396c5c61c2b0ea7fdb81e00020c6fd2d25
skills/review-work/SKILL.md f3a56811aa900733c75686987e18db37255ea84f3da0fc05b20590389fa69bfb
```

## Verification Owed Before Running

- Confirm runner and evaluator are separate contexts.
- Confirm runner receives only `runner-packet.md`.
- Confirm evaluator receives anonymized outputs plus `evaluator-packet.md`, not arm mapping.
- Confirm source hashes still match this record immediately before the run.
- Record provider, model, date, tool access, and capability profile.

## Stop Condition

Stop before execution. The next authorized operation must explicitly permit blind prompt runs or suite evaluation.

