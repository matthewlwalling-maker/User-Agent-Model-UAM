# UAM:ARTIFACT-STAMP-BEGIN
artifact_stamp:
  artifact_revision: 1
  revision_date: '2026-06-20'
  content_sha256: cb56bc578ae3c967022f030edee5f00af98a1d717c3f158e2f1825d6c5d87d83
  hash_profile: UAM-CANONICAL-TEXT-SHA256-1
# UAM:ARTIFACT-STAMP-END

stable_artifact_id: UAM-ARTIFACT-INDEX
stable_name: UAM Artifact Index
canonical_filename: UAM_Artifact_Index.yaml
status: active project record
authority_scope: current artifact resolution, pinned stamps, archive pointers, and serialized write ownership
self_stamp_authority: this document header
resolution_policy:
  artifact_header: source of truth for its own current stamp
  shared_index: discovery map and consistency mirror
  mismatch_response: flag-and-block material action
write_control:
  default_owner: UAM Architect under user/Gatekeeper authority
  mode: single-writer serialized replacement transaction
  concurrent_writer_response: create candidate branch for reconciliation; never overwrite canonical active file
hash_authority:
  identity_field: content_sha256
  profile: UAM-CANONICAL-TEXT-SHA256-1
  computed_by: designated updater during committed replacement transaction
  consumer_rule: reference recorded value; do not recompute ad hoc
active_artifacts:
- stable_artifact_id: UAM-ARTIFACT-NAMING
  stable_name: UAM Artifact Identity, Naming, and Archive Convention
  canonical_filename: UAM_Artifact_Naming_and_Archive_Convention.md
  status: adopted
  current_stamp:
    artifact_revision: 1
    revision_date: '2026-06-20'
    content_sha256: b8317dc4308ba22cf45f2d51ab1891b5a3855f4808505b6c9ec59eaf784b9593
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers: []
- stable_artifact_id: UAM-FRAMEWORK
  stable_name: UAM Model Framework
  canonical_filename: UAM_Model_Framework.md
  status: candidate
  current_stamp:
    artifact_revision: 1
    revision_date: '2026-06-20'
    content_sha256: a33115b50743a065e692f28b243180ac496f4735ffe2ef0fd4242d7bc903f5d7
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Model Framework/UAM Model Framework — pre-convention v0.21 (2026-06-19) [0e0065ed485d].md
    legacy_label: pre-convention v0.21
    source_date: '2026-06-19'
    content_sha256: 0e0065ed485d2f15271cfb0eab9a95c55a8e651d1c9801076bf6bae0df0fc9d0
- stable_artifact_id: UAM-MODEL-PARTICIPATION
  stable_name: UAM Model Participation and Assurance Plan
  canonical_filename: UAM_Model_Participation_and_Assurance_Plan.md
  status: candidate
  current_stamp:
    artifact_revision: 1
    revision_date: '2026-06-20'
    content_sha256: 9ab2be2213ebf33bcc20ce4bb296bed0ee27a53cbb26e924d096f0af76716e47
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Model Participation and Assurance Plan/UAM Model Participation and Assurance Plan — pre-convention
      v0.2 (2026-06-19) [0e0065ed485d].md
    legacy_label: pre-convention v0.2
    source_date: '2026-06-19'
    content_sha256: 0e0065ed485d2f15271cfb0eab9a95c55a8e651d1c9801076bf6bae0df0fc9d0
- stable_artifact_id: UAM-ARCHITECT-INSTRUCTIONS
  stable_name: UAM Architect Project Instructions
  canonical_filename: UAM_Architect_Project_Instructions.md
  status: candidate
  current_stamp:
    artifact_revision: 1
    revision_date: '2026-06-20'
    content_sha256: 13c32c61558b86837b07a2dbe3cd15f0b5288f951924356ff3cd2e6b066908fb
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Architect Project Instructions/UAM Architect Project Instructions — pre-convention v0.1 (2026-06-20)
      [458c800a9810].md
    legacy_label: pre-convention v0.1
    source_date: '2026-06-20'
    content_sha256: 458c800a98104263e274d3cbf429c2cfbc68fd028ce3ab9c3545b259c1f7c481
- stable_artifact_id: UAM-SOURCE-CONTEXT-MAP
  stable_name: UAM Source Intake and Context Map
  canonical_filename: UAM_Source_Intake_and_Context_Map.md
  status: candidate
  current_stamp:
    artifact_revision: 1
    revision_date: '2026-06-20'
    content_sha256: 4f0f09e35cd2ab917d9957fe47b624b7b0d76975f9463dc65683cc7c06c90427
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Source Intake and Context Map/UAM Source Intake and Context Map — pre-convention v0.1 (2026-06-20)
      [a126f509e875].md
    legacy_label: pre-convention v0.1
    source_date: '2026-06-20'
    content_sha256: a126f509e875716c87d43631989ff1015e37a1f7dbda14bf337c28741d583032
migration_record:
  decision_date: '2026-06-20'
  decision: stable versionless active names plus immutable stamped archives
  official_active_series_starts_at: r1
  quarantined_pre_ratification_drafts: quarantine/pre-ratification-naming-migration-20260620T003218Z
  missing_exact_pre_convention_snapshots:
  - UAM Model Framework v0.1
  - UAM Model Framework v0.2
  - UAM Model Participation and Assurance Plan v0.1
  missing_snapshot_rule: record the gap; do not fabricate content
