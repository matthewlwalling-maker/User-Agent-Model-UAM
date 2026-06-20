# UAM Artifact Working-Set Reconciliation Report

**Artifact ID:** `UAM-ARTIFACT-RECONCILIATION-REPORT`  
**Status:** completed design-time reconciliation record  
**Date:** 2026-06-20  
**Canonical set:** this package root

<!-- UAM:ARTIFACT-STAMP-BEGIN -->
**Artifact stamp**

```yaml
artifact_revision: 1
revision_date: 2026-06-20
content_sha256: a6f3c6d914ef041be6ef3326db3c1074e65445a5ef2e479ecd5b6d322e534d11
hash_profile: UAM-CANONICAL-TEXT-SHA256-1
```
<!-- UAM:ARTIFACT-STAMP-END -->

## Verdict

The mixed working set has been reconciled into one canonical active set. `AGENTS.md` is the sole active source-material placement for the Architect instructions. The standalone instruction files are immutable displaced history, not alternate active instructions.

The framework remains a candidate and the participation plan remains semantically unreconciled for bootstrap ordering. This transaction resolves artifact identity and duplicate-active-file risk; it does not adopt the framework or dispatch the bootstrap pair.

## Selected active artifacts

| Stable ID | Canonical path | Revision | Status |
|---|---|---:|---|
| `UAM-ARTIFACT-NAMING` | `UAM_Artifact_Naming_and_Archive_Convention.md` | r2 | adopted rule |
| `UAM-ARCHITECT-INSTRUCTIONS` | `AGENTS.md` | r2 | active project instructions |
| `UAM-FRAMEWORK` | `UAM_Model_Framework.md` | r2 | candidate |
| `UAM-MODEL-PARTICIPATION` | `UAM_Model_Participation_and_Assurance_Plan.md` | r2 | candidate; compatibility unresolved |
| `UAM-SOURCE-CONTEXT-MAP` | `UAM_Source_Intake_and_Context_Map.md` | r2 | candidate intake aid |
| `UAM-BRIEF-BOOTSTRAP` | `UAM_Bootstrap_Pair_Brief.md` | r2 | candidate; not dispatch-ready |

## Duplicate comparison and disposition

| Family | Comparison | Finding | Disposition |
|---|---|---|---|
| Architect instructions | root active-set copy vs identity-migration copy vs `AGENTS.md` | Same role contract with competing identity schemes; `AGENTS.md` carries the user-confirmed source placement and the latest content-hash convention. | `AGENTS.md` retained and revised; all standalone copies archived. |
| Framework | active-set vs identity-migration snapshot; line similarity 0.9723 | Core architecture agrees. The identity-migration snapshot adds the explicit §6.11 contract and stricter actionable-reference requirements. | Semantic superset retained, converted to the ratified stamp convention, and patched so D3/D7 provide requirements while the Spine Contract Architect authors/freezes the packet contract. |
| Artifact index | two incompatible r1 schemas | Neither could safely resolve the mixed root because their recorded stamps pointed to different packages. | Rebuilt from the reconciled active files; prior indexes archived. |
| Naming convention | active-slot convention vs payload/snapshot migration convention | Same stable-name intent but conflicting hash fields and archive forms. | Consolidated to one authoritative `content_sha256` profile and the ratified archive naming rule. |
| Bootstrap brief | legacy v0.1 vs patched r1 | Patched r1 corrected readiness, ownership, source, role/context, and evidence gates but used the superseded payload/snapshot stamp form. | Patched semantics retained, converted to r2, repinned to the reconciled candidate framework and `AGENTS.md`, and indexed. |

## Known prior references without materialized bytes

The uploaded-source index exposed several later r1 stamps whose exact bytes were not simultaneously present in the reconciliation filesystem because same-path uploads had overwritten one another. They are recorded in the new index as known, non-materialized predecessors rather than fabricated archives:

- `UAM-FRAMEWORK` r1 — `8a77e4da02681fff3f94efdb58fe15ab816c2e9f8ad7962612bd347401b9b9a4`
- `UAM-ARTIFACT-INDEX` r1 — `429daa20ceeab2a6a1e27d5edfccfe6426f7f2860134a57c88ed693432b9803e`
- `UAM-ARTIFACT-NAMING` r1 — `2c0286178c4a317dc516cff966b4d6658b12a6abfee2c66b434d40b399dd352b`
- `UAM-MODEL-PARTICIPATION` r1 — `67a3b795d645d59cc0fe34f00753bbce3f1a74268b5b58a51006b0ccc91b533e`
- `UAM-SOURCE-CONTEXT-MAP` r1 — `8d6597becb3c2a321cf20027a1f55bce88a356135f49672a8bbc94cb6105d79d`

The Architect-instruction r1 bytes were present as `AGENTS.md` and are archived exactly.

## Remaining blocks

- Framework adoption is still pending.
- The four Phase-1 Spine contracts do not yet exist as frozen artifacts.
- The participation plan's sequencing conflict remains unresolved.
- The bootstrap brief is indexed but remains not dispatch-ready.
