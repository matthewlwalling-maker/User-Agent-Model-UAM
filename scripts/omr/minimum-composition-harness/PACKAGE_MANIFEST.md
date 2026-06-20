# Package Manifest - Codex Harness v0.3-current

## Purpose

Run the Minimum Composition smoke harness through the user's existing Codex CLI using the current adopted compressed runtime source set.

## Material Changes

- `authorities_current/`: current adopted AB/OMR runtime source freeze and hash lock.
- `sources.py`: verifies the current frozen source lock instead of hard-coded v0.2 split-source hashes.
- `prompts.py`: loads compressed AB/OMR runtime references when present.
- `configs/*.yaml`: defaults now point at `authorities_current`.
- `archive/outdated_2026-06-19/`: preserves stale v0.2 configs, split authorities, planned smoke output, and handoffs.

## Preserved

- P2 schema and P5 executor view semantics.
- Operator boundaries.
- Selector rules.
- P2 canonical state validation.
- Legacy control.
- Fixtures and holdouts policy.
- Blinding and evaluator protocol.

## Deferred

- Live Codex smoke execution against `api-smoke-current-20260619-C01-C08`.
- Holdout selection.
- Comparative scoring.
