# UAM Artifact Index
# UAM:DOCUMENT-STAMP-BEGIN
artifact_stamp:
  artifact_revision: 1
  updated_at: '2026-06-20T00:30:20Z'
  payload_sha256: e3de1f97ceaee91c080957eb74b3114ef055a94d08c55408823d037f6053ff0b
  hash_scope: full UTF-8 document with this stamp block removed; UTF-8 without BOM; LF line endings
# UAM:DOCUMENT-STAMP-END

index:
  stable_artifact_id: UAM-ARTIFACT-INDEX
  canonical_name: UAM Artifact Index
  canonical_filename: UAM_Artifact_Index.yaml
  status: active project register
  naming_authority: UAM_Artifact_Naming_and_Archive_Convention.md
  complete_file_hash_location: SHA256SUMS
  single_writer_rule: serialized update under the Artifact Custodian/index transaction lock
  generated_at: '2026-06-20T00:30:20Z'
active_artifacts:
- stable_artifact_id: UAM-ARTIFACT-NAMING
  canonical_name: UAM Artifact Identity, Naming, and Archive Convention
  canonical_filename: UAM_Artifact_Naming_and_Archive_Convention.md
  active_stamp:
    artifact_revision: 1
    updated_at: '2026-06-20T00:30:20Z'
    payload_sha256: 3b03c563167fa59a1abe94da0df36da4dc1e053017349827790afe2ee5e268b6
  active_snapshot_sha256: dc97f2c0a28683dfed1f9480ef6d5100d3f77bb69c2d5fd6ab575213790b833c
  status: adopted project rule
  authority_scope: project-wide artifact identity, stamping, freshness, and archive discipline
  single_writer_owner: Artifact Custodian or deterministic artifact service
  archive_snapshots: []
  parent_artifacts: []
  compatibility_conditions: []
- stable_artifact_id: UAM-FRAMEWORK
  canonical_name: UAM Model Framework
  canonical_filename: UAM_Model_Framework.md
  active_stamp:
    artifact_revision: 1
    updated_at: '2026-06-20T00:30:20Z'
    payload_sha256: 5dc3bd2318333f662af22375ab861e7d5b28ef81d51bd4ce4a6cb9ed8ace83ab
  active_snapshot_sha256: 3fa0bf77668bcccd1aceddfe0cf90d0f8fcdcb80047fb3a9ad8781c43c73a0e9
  status: candidate
  authority_scope: candidate common architecture; not adopted runtime authority
  single_writer_owner: Artifact Custodian or deterministic artifact service
  archive_snapshots:
  - archive_ref: archive/UAM_Model_Framework/UAM_Model_Framework__legacy-v0.21__2026-06-19__0e0065ed485d.md
    archive_snapshot_sha256: 0e0065ed485d2f15271cfb0eab9a95c55a8e651d1c9801076bf6bae0df0fc9d0
    legacy_label: legacy-v0.21
    source_date: '2026-06-19'
    archived_stamp: null
    reason: supplied pre-convention snapshot preserved unchanged during naming migration
  parent_artifacts: []
  compatibility_conditions: []
- stable_artifact_id: UAM-MODEL-PARTICIPATION
  canonical_name: UAM Model Participation and Assurance Plan
  canonical_filename: UAM_Model_Participation_and_Assurance_Plan.md
  active_stamp:
    artifact_revision: 1
    updated_at: '2026-06-20T00:30:20Z'
    payload_sha256: 71cc384a10121e19f63a48de3fb4a2e830e81894464f423f014dbae5486f6c32
  active_snapshot_sha256: 926d0c0e16eed3718f57f07b7509d2afa03c06b54b4032681ff18639f088c44b
  status: candidate
  authority_scope: candidate participation donor; semantic reconciliation pending
  single_writer_owner: Artifact Custodian or deterministic artifact service
  archive_snapshots:
  - archive_ref: archive/UAM_Model_Participation_and_Assurance_Plan/UAM_Model_Participation_and_Assurance_Plan__legacy-v0.2__2026-06-19__eb42440c488d.md
    archive_snapshot_sha256: eb42440c488d2a107da8c43e466bc13047fc6ae0ddd24868498c4ce0459b103e
    legacy_label: legacy-v0.2
    source_date: '2026-06-19'
    archived_stamp: null
    reason: supplied pre-convention snapshot preserved unchanged during naming migration
  parent_artifacts:
  - stable_artifact_id: UAM-FRAMEWORK
    relationship: candidate parent; exact adopted pin required before action
  compatibility_conditions: []
- stable_artifact_id: UAM-ARCHITECT-INSTRUCTIONS
  canonical_name: UAM Architect Project Instructions
  canonical_filename: UAM_Architect_Project_Instructions.md
  active_stamp:
    artifact_revision: 1
    updated_at: '2026-06-20T00:30:20Z'
    payload_sha256: 98e93526d73bd49380d02f48847adc1f2c39560a2a5ab79a25623e26c1039db2
  active_snapshot_sha256: 5944c8798042f3f2a8d820d79f410cefdf3bcdefd1b9164cc8536712af7fa293
  status: candidate
  authority_scope: design-time Architect role and project instructions
  single_writer_owner: Artifact Custodian or deterministic artifact service
  archive_snapshots:
  - archive_ref: archive/UAM_Architect_Project_Instructions/UAM_Architect_Project_Instructions__legacy-v0.1__2026-06-20__458c800a9810.md
    archive_snapshot_sha256: 458c800a98104263e274d3cbf429c2cfbc68fd028ce3ab9c3545b259c1f7c481
    legacy_label: legacy-v0.1
    source_date: '2026-06-20'
    archived_stamp: null
    reason: supplied pre-convention snapshot preserved unchanged during naming migration
  parent_artifacts:
  - stable_artifact_id: UAM-FRAMEWORK
    relationship: candidate parent
  compatibility_conditions: []
- stable_artifact_id: UAM-SOURCE-CONTEXT-MAP
  canonical_name: UAM Source Intake and Context Map
  canonical_filename: UAM_Source_Intake_and_Context_Map.md
  active_stamp:
    artifact_revision: 1
    updated_at: '2026-06-20T00:30:20Z'
    payload_sha256: 4cbf15f69d58540e099f42d047b12d4aae234db713878a01f0c730167806f90f
  active_snapshot_sha256: 3f75f5bd8c6394769c418e2b6b1a9c62903db57b19613140fa9fe7b446277ef8
  status: candidate
  authority_scope: source-intake and context-loading aid
  single_writer_owner: Artifact Custodian or deterministic artifact service
  archive_snapshots:
  - archive_ref: archive/UAM_Source_Intake_and_Context_Map/UAM_Source_Intake_and_Context_Map__legacy-v0.1__2026-06-20__a126f509e875.md
    archive_snapshot_sha256: a126f509e875716c87d43631989ff1015e37a1f7dbda14bf337c28741d583032
    legacy_label: legacy-v0.1
    source_date: '2026-06-20'
    archived_stamp: null
    reason: supplied pre-convention snapshot preserved unchanged during naming migration
  parent_artifacts:
  - stable_artifact_id: UAM-ARCHITECT-INSTRUCTIONS
    relationship: candidate parent
  compatibility_conditions: []
- stable_artifact_id: UAM-ARTIFACT-WORKSPACE
  canonical_name: UAM Artifact Workspace
  canonical_filename: UAM_Artifact_Workspace.md
  active_stamp:
    artifact_revision: 1
    updated_at: '2026-06-20T00:30:20Z'
    payload_sha256: 276b2cec379cb1548c3d9d52ab8ccccb62cf4e850010845cf3fbe7ea661c4953
  active_snapshot_sha256: d62135201ee686c85d4db31deafe8c816ad5b1244c2e0f4c9f4f72d5afc8f6f8
  status: active navigation aid
  authority_scope: human navigation only
  single_writer_owner: Artifact Custodian or deterministic artifact service
  archive_snapshots: []
  parent_artifacts:
  - stable_artifact_id: UAM-ARTIFACT-NAMING
    relationship: governing naming rule
  compatibility_conditions: []
index_self_identity:
  active_stamp_ref: document header in this file
  active_snapshot_sha256_ref: SHA256SUMS
  recursion_reason: the index cannot embed its own complete-file hash without changing that hash
known_legacy_lineage_gaps:
- stable_artifact_id: UAM-FRAMEWORK
  legacy_labels:
  - v0.1
  - v0.2
  snapshot_available: false
  treatment: recorded lineage only; obtain exact files before claiming reconstructable snapshots
- stable_artifact_id: UAM-MODEL-PARTICIPATION
  legacy_labels:
  - UAM-MULTIMODEL-OWNERSHIP-0.1
  snapshot_available: false
  treatment: recorded predecessor claim only; exact file not supplied
notes:
- Bare stable names are explanatory references.
- Acting references pin the updater-recorded stamp, complete-file snapshot hash, and attached or immutable exact content.
- Naming migration does not adopt candidate architecture or resolve semantic compatibility conflicts.
