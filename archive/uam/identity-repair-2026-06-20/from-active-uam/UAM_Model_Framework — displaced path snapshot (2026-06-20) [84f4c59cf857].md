# UAM:ARTIFACT-STAMP-BEGIN
artifact_stamp:
  artifact_revision: 2
  revision_date: '2026-06-20'
  content_sha256: c764d25a9abc5f2a9188dbc04590a9301933cf99023857f6d3b736bd9f35fe5c
  hash_profile: UAM-CANONICAL-TEXT-SHA256-1
# UAM:ARTIFACT-STAMP-END

stable_artifact_id: UAM-ARTIFACT-INDEX
stable_name: UAM Artifact Index
canonical_filename: UAM_Artifact_Index.yaml
status: active project record
authority_scope: canonical active-path resolution, current stamps, archive lineage, write ownership, and known predecessor
  gaps
canonical_active_set_root: .
resolution_policy:
  active_membership: only entries in active_artifacts are active; files outside this package root are intake or history
  artifact_header: source of truth for its own current stamp
  shared_index: discovery and consistency mirror
  mismatch_response: flag-and-block material action
write_control:
  default_owner: UAM Architect under user/Gatekeeper authority
  mode: single-writer serialized archive-replace-restamp-reindex transaction
  concurrent_writer_response: create candidate branch for reconciliation; never overwrite canonical active file
hash_authority:
  identity_field: content_sha256
  profile: UAM-CANONICAL-TEXT-SHA256-1
  computed_by: designated updater during committed replacement transaction
  consumer_rule: reference recorded value; only a conforming validator may recompute
active_artifacts:
- stable_artifact_id: UAM-ARTIFACT-NAMING
  stable_name: UAM Artifact Identity, Naming, and Archive Convention
  canonical_filename: UAM_Artifact_Naming_and_Archive_Convention.md
  status: adopted
  current_stamp:
    artifact_revision: 2
    revision_date: '2026-06-20'
    content_sha256: 01a6ea18021702339c406f65cc71b6d86eadc1df8f01194b0b12bdfb6a091403
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: attached:UAM_Artifact_Naming_and_Archive_Convention.md
  integrity_file_sha256: 3114c77f64426996c0a693c2db250e09bede3989c98383cfd6c67876836d1fdd
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Artifact Identity, Naming, and Archive Convention/UAM Artifact Identity, Naming, and Archive
      Convention — displaced active-set snapshot (2026-06-20) [a6133476143d].md
    file_sha256: a6133476143dbfa4f74ac33fb85f8fc70f74a7933b11826963d042bbfbe957e9
    source_kind: displaced active-set snapshot
    observed_filename: UAM_Artifact_Naming_and_Archive_Convention.md
  - archive_ref: archive/UAM Artifact Identity, Naming, and Archive Convention/UAM Artifact Identity, Naming, and Archive
      Convention — displaced identity-migration snapshot (2026-06-20) [dc97f2c0a286].md
    file_sha256: dc97f2c0a28683dfed1f9480ef6d5100d3f77bb69c2d5fd6ab575213790b833c
    source_kind: displaced identity-migration snapshot
    observed_filename: UAM_Artifact_Naming_and_Archive_Convention.md
- stable_artifact_id: UAM-ARCHITECT-INSTRUCTIONS
  stable_name: UAM Architect Project Instructions
  canonical_filename: AGENTS.md
  status: active project instructions; design-time authority only
  current_stamp:
    artifact_revision: 2
    revision_date: '2026-06-20'
    content_sha256: 76bebac70d542e29f82454c427b414235894e0b5892ccdaf71308fb19130b585
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: attached:AGENTS.md
  integrity_file_sha256: fc995e3fb6e0168c8f26da9e9e11c9818d8bd8414ad09194664503aab17b2bc4
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Architect Project Instructions/UAM Architect Project Instructions — pre-convention v0.1 (2026-06-20)
      [458c800a9810].md
    file_sha256: 458c800a98104263e274d3cbf429c2cfbc68fd028ce3ab9c3545b259c1f7c481
    source_kind: pre-convention source
    observed_filename: UAM_Architect_Project_Instructions_v0.1.md
    legacy_label: v0.1
  - archive_ref: archive/UAM Architect Project Instructions/UAM Architect Project Instructions — displaced active-set snapshot
      (2026-06-20) [871a5d1d97ef].md
    file_sha256: 871a5d1d97ef09c8b651b98fa0965e2d55b17d7d0bd19b6e4151587fe67b1f2e
    source_kind: displaced active-set snapshot
    observed_filename: UAM_Architect_Project_Instructions.md
  - archive_ref: archive/UAM Architect Project Instructions/UAM Architect Project Instructions — displaced identity-migration
      snapshot (2026-06-20) [5944c8798042].md
    file_sha256: 5944c8798042f3f2a8d820d79f410cefdf3bcdefd1b9164cc8536712af7fa293
    source_kind: displaced identity-migration snapshot
    observed_filename: UAM_Architect_Project_Instructions.md
  - archive_ref: archive/UAM Architect Project Instructions/UAM Architect Project Instructions — r1 (2026-06-20) [cad6931cd919].md
    file_sha256: be7171ae8c9a7b0fc30a042863594f02fe598dc46a6b37bae0c9aaf9d6bbefe0
    source_kind: prior active source-material snapshot
    observed_filename: AGENTS.md
- stable_artifact_id: UAM-FRAMEWORK
  stable_name: UAM Model Framework
  canonical_filename: UAM_Model_Framework.md
  status: candidate; not adopted
  current_stamp:
    artifact_revision: 2
    revision_date: '2026-06-20'
    content_sha256: c5d3f5ce9d2259f8c04db769b63ccda2d4b55acd8f5b50e72d9b8528daf3017d
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: attached:UAM_Model_Framework.md
  integrity_file_sha256: a8ffb6c07cacea4ca8d863533359cc6b52dedb3e702adfad4b05a7880558f89d
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Model Framework/UAM Model Framework — pre-convention v0.21 (2026-06-19) [0e0065ed485d].md
    file_sha256: 0e0065ed485d2f15271cfb0eab9a95c55a8e651d1c9801076bf6bae0df0fc9d0
    source_kind: pre-convention source
    observed_filename: UAM_Model_Framework__legacy-v0.21__superseded-20260620T001210Z__sha256-0e0065ed485d.md
    legacy_label: v0.21
  - archive_ref: archive/UAM Model Framework/UAM Model Framework — displaced active-set snapshot (2026-06-20) [e2eb44f4ba7e].md
    file_sha256: e2eb44f4ba7eaa12e8db84550224550a07317e849ce0b2e4b71192adf8a59a5f
    source_kind: displaced active-set snapshot
    observed_filename: UAM_Model_Framework.md
  - archive_ref: archive/UAM Model Framework/UAM Model Framework — displaced identity-migration snapshot (2026-06-20) [3fa0bf77668b].md
    file_sha256: 3fa0bf77668bcccd1aceddfe0cf90d0f8fcdcb80047fb3a9ad8781c43c73a0e9
    source_kind: displaced identity-migration snapshot
    observed_filename: UAM_Model_Framework.md
  parent_artifacts:
  - UAM-ARTIFACT-NAMING
- stable_artifact_id: UAM-MODEL-PARTICIPATION
  stable_name: UAM Model Participation and Assurance Plan
  canonical_filename: UAM_Model_Participation_and_Assurance_Plan.md
  status: candidate; framework compatibility and sequencing unresolved
  current_stamp:
    artifact_revision: 2
    revision_date: '2026-06-20'
    content_sha256: 6d579196285b1be3beb1258fe2e8d3dd820aac39d8d9ccaadf305b6b11a8bb7d
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: attached:UAM_Model_Participation_and_Assurance_Plan.md
  integrity_file_sha256: 87dea04af79323efe93372881f93f9617addb9b914594ad3f90b27a4b5ad56d0
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Model Participation and Assurance Plan/UAM Model Participation and Assurance Plan — pre-convention
      v0.2 (2026-06-19) [eb42440c488d].md
    file_sha256: eb42440c488d2a107da8c43e466bc13047fc6ae0ddd24868498c4ce0459b103e
    source_kind: pre-convention source
    observed_filename: UAM_Model_Participation_and_Assurance_Plan__legacy-v0.2__superseded-20260620T001210Z__sha256-eb42440c488d.md
    legacy_label: v0.2
  - archive_ref: archive/UAM Model Participation and Assurance Plan/UAM Model Participation and Assurance Plan — displaced
      active-set snapshot (2026-06-20) [d7a4327e7a3b].md
    file_sha256: d7a4327e7a3b1c3b6f71cf89fbe71160657625e062cbd958b51cc36b7cb2155d
    source_kind: displaced active-set snapshot
    observed_filename: UAM_Model_Participation_and_Assurance_Plan.md
  - archive_ref: archive/UAM Model Participation and Assurance Plan/UAM Model Participation and Assurance Plan — displaced
      identity-migration snapshot (2026-06-20) [926d0c0e16ee].md
    file_sha256: 926d0c0e16eed3718f57f07b7509d2afa03c06b54b4032681ff18639f088c44b
    source_kind: displaced identity-migration snapshot
    observed_filename: UAM_Model_Participation_and_Assurance_Plan.md
  parent_artifacts:
  - UAM-FRAMEWORK
  - UAM-ARTIFACT-NAMING
- stable_artifact_id: UAM-SOURCE-CONTEXT-MAP
  stable_name: UAM Source Intake and Context Map
  canonical_filename: UAM_Source_Intake_and_Context_Map.md
  status: candidate intake aid
  current_stamp:
    artifact_revision: 2
    revision_date: '2026-06-20'
    content_sha256: 6a296c658cc5f27a0262a7e6e86ebb906d9f218281dbd7bb96394a09f0127c39
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: attached:UAM_Source_Intake_and_Context_Map.md
  integrity_file_sha256: a1b79bf685f5d581dfd022a3ac07351b67551af268674643be2fa060c0982a86
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Source Intake and Context Map/UAM Source Intake and Context Map — pre-convention v0.1 (2026-06-20)
      [a126f509e875].md
    file_sha256: a126f509e875716c87d43631989ff1015e37a1f7dbda14bf337c28741d583032
    source_kind: pre-convention source
    observed_filename: UAM_Source_Intake_and_Context_Map_v0.1.md
    legacy_label: v0.1
  - archive_ref: archive/UAM Source Intake and Context Map/UAM Source Intake and Context Map — displaced active-set snapshot
      (2026-06-20) [d534a2a08ea5].md
    file_sha256: d534a2a08ea57987dc91a71a06770cac43953f21330ebffd5e38c508d64a6020
    source_kind: displaced active-set snapshot
    observed_filename: UAM_Source_Intake_and_Context_Map.md
  - archive_ref: archive/UAM Source Intake and Context Map/UAM Source Intake and Context Map — displaced identity-migration
      snapshot (2026-06-20) [3f75f5bd8c63].md
    file_sha256: 3f75f5bd8c6394769c418e2b6b1a9c62903db57b19613140fa9fe7b446277ef8
    source_kind: displaced identity-migration snapshot
    observed_filename: UAM_Source_Intake_and_Context_Map.md
  parent_artifacts:
  - UAM-ARCHITECT-INSTRUCTIONS
  - UAM-ARTIFACT-NAMING
- stable_artifact_id: UAM-BRIEF-BOOTSTRAP
  stable_name: UAM Sub-Architect Brief — Bootstrap Pair
  canonical_filename: UAM_Bootstrap_Pair_Brief.md
  status: candidate; not dispatch-ready
  current_stamp:
    artifact_revision: 2
    revision_date: '2026-06-20'
    content_sha256: 351a029d46a508bb5dcead5f0cb8f2c9f333b934200098634878dc3fa6595f93
    hash_profile: UAM-CANONICAL-TEXT-SHA256-1
  content_ref: attached:UAM_Bootstrap_Pair_Brief.md
  integrity_file_sha256: 2fbffd2b351c074d04bf9751a41ce53d4ec959645813fe9bb29aca40d9074465
  current_stamp_authority: active document header
  active_write_owner: UAM Architect under user/Gatekeeper authority
  archive_pointers:
  - archive_ref: archive/UAM Bootstrap Pair Brief/UAM Bootstrap Pair Brief — pre-convention v0.1 (2026-06-19) [9e8cc60e0360].md
    file_sha256: 9e8cc60e0360bc0eca0f8338920d889d6249e35d182f1ad33c45e9a5ee4d658b
    source_kind: pre-convention source
    observed_filename: UAM_Bootstrap_Pair_Brief__legacy-v0.1__2026-06-19__9e8cc60e0360.md
    legacy_label: v0.1
  - archive_ref: archive/UAM Bootstrap Pair Brief/UAM Bootstrap Pair Brief — r1 legacy-stamp (2026-06-20) [5830caaf4ec6].md
    file_sha256: 5830caaf4ec61a3e616bfc5a1c6233e2d2e85a3efc132091aa404b7c6b974979
    source_kind: prior patched snapshot
    observed_filename: UAM_Bootstrap_Pair_Brief.md
  parent_artifacts:
  - UAM-FRAMEWORK
  - UAM-ARCHITECT-INSTRUCTIONS
  - UAM-ARTIFACT-NAMING
supporting_records:
- stable_artifact_id: UAM-ARTIFACT-RECONCILIATION-REPORT
  canonical_filename: UAM_Artifact_Working_Set_Reconciliation_Report.md
  artifact_revision: 1
  revision_date: '2026-06-20'
  content_sha256: a6f3c6d914ef041be6ef3326db3c1074e65445a5ef2e479ecd5b6d322e534d11
  content_ref: attached:UAM_Artifact_Working_Set_Reconciliation_Report.md
  integrity_file_sha256: ca1c97677a9192984b90cde1a4febe85892f5f750978383a29ac89174d1531a7
  status: completed design-time reconciliation record
- path: supporting/UAM_Bootstrap_Pair_Readiness_Assessment.md
  file_sha256: a85e58ca411ecba2b902a57cc82af210209631d762edd1649b85f4eb2f58bb5a
  status: design-time supporting assessment; preserved unchanged
known_unmaterialized_predecessors:
- stable_artifact_id: UAM-FRAMEWORK
  artifact_revision: 1
  revision_date: '2026-06-20'
  content_sha256: 8a77e4da02681fff3f94efdb58fe15ab816c2e9f8ad7962612bd347401b9b9a4
  materialization_status: known stamp; exact bytes unavailable in reconciliation filesystem
- stable_artifact_id: UAM-ARTIFACT-INDEX
  artifact_revision: 1
  revision_date: '2026-06-20'
  content_sha256: 429daa20ceeab2a6a1e27d5edfccfe6426f7f2860134a57c88ed693432b9803e
  materialization_status: known stamp; exact bytes unavailable in reconciliation filesystem
- stable_artifact_id: UAM-ARTIFACT-NAMING
  artifact_revision: 1
  revision_date: '2026-06-20'
  content_sha256: 2c0286178c4a317dc516cff966b4d6658b12a6abfee2c66b434d40b399dd352b
  materialization_status: known stamp; exact bytes unavailable in reconciliation filesystem
- stable_artifact_id: UAM-MODEL-PARTICIPATION
  artifact_revision: 1
  revision_date: '2026-06-20'
  content_sha256: 67a3b795d645d59cc0fe34f00753bbce3f1a74268b5b58a51006b0ccc91b533e
  materialization_status: known stamp; exact bytes unavailable in reconciliation filesystem
- stable_artifact_id: UAM-SOURCE-CONTEXT-MAP
  artifact_revision: 1
  revision_date: '2026-06-20'
  content_sha256: 8d6597becb3c2a321cf20027a1f55bce88a356135f49672a8bbc94cb6105d79d
  materialization_status: known stamp; exact bytes unavailable in reconciliation filesystem
reconciliation_record:
  decision_date: '2026-06-20'
  decision: one canonical package-scoped active set; AGENTS.md is sole active Architect instruction placement
  framework_adoption_effect: none; framework remains candidate
  bootstrap_dispatch_effect: none; brief remains blocked pending adoption and Phase-1/Phase-2 prerequisites
