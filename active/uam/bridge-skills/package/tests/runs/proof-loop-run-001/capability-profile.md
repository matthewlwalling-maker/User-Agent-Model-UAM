# Proof Loop Run 001 Capability Profile

Run id: `proof-loop-run-001`
Status: template, not run
Evidence ceiling: design-time until completed by a runner

Complete one profile per arm before output generation.

## Arm Profile Template

```text
arm_name:
attempt_id:
provider:
model:
date:
context_id_or_equivalent:
workspace_or_execution_location:
allowed_source:
forbidden_source_confirmed: yes/no
file_read_available: yes/no
file_write_available: yes/no
tool_execution_available: yes/no
web_retrieval_available: yes/no
fresh_context_confirmed: yes/no
evaluator_materials_not_seen: yes/no
mapping_key_not_seen: yes/no
prior_arm_outputs_not_seen: yes/no
manual_interventions:
limitations:
```

## Notes

- Arm A should be run in a blank or outside-project context when possible.
- Arm E must remain `blocked` unless isolated Codex dogfood installation is separately authorized and verified.
- Missing capability is not a failure by itself. Hiding the missing capability or claiming unavailable actions is a failure.
