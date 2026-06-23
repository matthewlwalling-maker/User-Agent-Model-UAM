# Rollback

Version: `0.1.0`

## Current State

No global installation or activation is authorized in v0.1. The canonical package lives only as source under this project folder.

## Rollback From Source Edits

If a source change breaks the package:

1. Identify changed files and the last known good revision.
2. Revert only the affected source package files.
3. Preserve unrelated user changes.
4. Re-run manifest consistency and design-time checks.
5. Record the failure and fix layer before retrying.

## Rollback From Future Adapter Pilot

Before any future provider installation:

1. Back up the current provider profile or configuration.
2. Record exact installed paths, versions, and source hashes.
3. Install only the selected adapter.
4. Run routing, object-integrity, evidence-ceiling, degradation, and overactivation smoke checks.

To roll back:

1. Disable implicit routing first.
2. Remove or deactivate the installed adapter files.
3. Restore the backed-up provider profile.
4. Confirm the old profile behavior is active.
5. Record residual files or settings that still need cleanup.

## Known v0.1 Limitations

- Skill contracts are initial, not fully example-rich.
- Evals are fixtures, not executed results.
- Provider capability profiles are placeholders and must be rechecked before release.
- Cross-model parity is specified but untested.
- No global skills were installed or activated.

