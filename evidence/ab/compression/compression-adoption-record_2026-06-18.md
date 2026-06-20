# Compression Adoption Record 2026-06-18

Operation: execute upstream `ADOPT` recommendation for compressed runtime package
Evidence ceiling: simulated/design-time plus parser/hash validation
Full OMR pilot: not run
Live-runtime validation: not claimed

## Result

`ADOPT` executed as a reversible compressed-runtime promotion.

The candidate package from `Context Resources/Runtime/Compressed_Candidate_v0.1/` was promoted to active runtime paths. Current pre-compression sources were copied to a clearly labeled archive before promotion. Original source files were not deleted.

## Promoted Active Files

| Active path | Source |
|---|---|
| `AGENTS.md` | `Context Resources/Runtime/Compressed_Candidate_v0.1/AGENTS.md` |
| `Context Resources/Runtime/AB_Runtime_Authority_Reference_v1.1.md` | candidate copy |
| `Context Resources/Runtime/AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` | candidate copy |
| `Context Resources/Runtime/OMR_Operator_Prototype_Runtime_v0.2.md` | candidate copy |
| `Context Resources/Runtime/P2_State_Schemas_v0.1.json` | exact candidate/original P2 copy |
| `Context Resources/Runtime/P5_Executor_View_v0.1.yaml` | exact candidate/original P5 copy |

## Archive

Pre-compression source archive:

`Context Resources/Archive/PreCompression_Source_v0.1_2026-06-18/`

Archive manifest:

`Context Resources/Archive/PreCompression_Source_v0.1_2026-06-18/ARCHIVE_SHA256.txt`

The archive contains copies of root `AGENTS.md`, Agent Builder source files `00`-`08` where present in active source paths, the eval suite, OMR P1-P7/prototype sources, and package checksums. The originals also remain in their prior locations for traceability.

## Validation

| Check | Result |
|---|---|
| Pre-compression archive created before active promotion | PASS |
| Active root matches adopted candidate root | PASS |
| Active `AB_Runtime_Authority_Reference_v1.1.md` matches candidate | PASS |
| Active `AB_GoalCompleteness_Procedure_and_Evals_v1.1.md` matches candidate | PASS |
| Active `OMR_Operator_Prototype_Runtime_v0.2.md` matches candidate | PASS |
| Active P2 matches candidate and original | PASS; `05d19c0e372070caa87ef30e3d57466d2bfbb5631b372c894f9dedab8c6f14e3` |
| Active P5 matches candidate and original | PASS; `ad689ece75ffb6d4da72a41e23e7cf1e354292b9b5f69460aabf99c36c3a8c66` |
| Active P2 JSON parse | PASS via PowerShell `ConvertFrom-Json` |
| P5 YAML parse | PASS by upstream review using PyYAML before adoption; not rerun locally |
| Post-promotion sentinel S01-S10 plus mixed AB/O smoke | PASS at simulated/design-time; see `post-adoption-sentinel-results_v0.1.md` |

## Claims Not Made

- No Green release claim.
- No live-runtime validation.
- No post-implementation validation.
- No production-observed validation.
- No independent evaluator claim by this adopting agent.
- No full OMR pilot.
- No comparative superiority claim.

## Remaining Conditions

- Treat the adopted compressed package as active runtime compression, not higher-stage evidence.
- Keep P2 and P5 byte-identical unless a separate validated schema/fixture change is authorized.
- If active paths are moved again, rerun S01-S10 plus mixed AB/O smoke.
- Use archived pre-compression sources for rollback/provenance if needed.

## Post-Remediation Update 2026-06-19

The 2026-06-18 validation table remains the historical adoption-time record. On 2026-06-19, the user explicitly adopted the then-current `AGENTS.md` revision as canonical root instructions:

| File | Adopted SHA-256 | Prior adoption-time SHA-256 |
|---|---|---|
| `AGENTS.md` | `e6ea55672bf5ab6f9eb578d2e3ce0c7bcd2ab3b0a6def6d9dedb3e25ff772d2f` | `50a5510c8285cc01778225458a065f9c5d00f3d63d6d53836dc265319d56caf6` |

The active runtime markdown headers were also normalized from compressed-candidate wording to active adopted runtime wording. These changes do not promote evidence beyond the design-time / simulated ceiling recorded above.
