# Workspace Governance QC Record

Date: 2026-06-23
Evidence ceiling: static validation
Scope: active hierarchy, future file-placement governance, manifest/registry paths, and GitHub publication automation guards

## Commands Run

```powershell
.\.venv\Scripts\python.exe uam-bridge-skills\tools\active\validate_workspace_governance.py
.\.venv\Scripts\python.exe uam-bridge-skills\tools\active\validate_yaml.py
```

PowerShell parser validation was also run for:

```text
uam-bridge-skills/tools/active/export_relevant_files.ps1
uam-bridge-skills/tools/active/publish_bridge_skills_to_master_repo.ps1
```

## Result

```text
WORKSPACE_GOVERNANCE_QC_PASSED: 0 error(s), 1 warning(s)
- WARNING: evals/ exists as an empty delete-gated compatibility placeholder

YAML validation passed: 36 file(s) parsed, 19 test suite(s) checked, 246 case id(s) checked.
POWERSHELL_PARSE_PASSED: uam-bridge-skills\tools\active\export_relevant_files.ps1
POWERSHELL_PARSE_PASSED: uam-bridge-skills\tools\active\publish_bridge_skills_to_master_repo.ps1
```

## Interpretation

Future file-placement controls point to the active hierarchy:

- active package anchors and commands under `skills/active/uam-bridge-skills/`;
- docs under `docs/cleanup`, `docs/governance`, `docs/install`, `docs/protocols`, and `docs/publication`;
- tests under `tests/suites`, `tests/runs`, `tests/records`, `tests/tools`, and `tests/templates`;
- generated exports under `exports/generated`;
- active tools under `tools/active`;
- active lenses under `lenses/active`;
- package packets under `packets/`.

The remaining `evals/` directory is empty and intentionally non-active. It remains only because deletion was not authorized in the no-delete cleanup pass.
