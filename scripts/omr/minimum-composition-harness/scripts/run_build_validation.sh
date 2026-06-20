#!/usr/bin/env bash
set -euo pipefail
python -m compileall -q src tests
pytest -q
mch doctor --config configs/manual_pilot.example.yaml
mch plan --config configs/manual_pilot.example.yaml > /tmp/minimum_composition_plan.json
printf 'Build validation passed. Plan written to %s\n' /tmp/minimum_composition_plan.json
