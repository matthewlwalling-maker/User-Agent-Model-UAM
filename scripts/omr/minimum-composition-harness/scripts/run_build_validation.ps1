$ErrorActionPreference = "Stop"
python -m compileall -q src tests
pytest -q
mch doctor --config configs/manual_pilot.example.yaml
mch plan --config configs/manual_pilot.example.yaml | Out-File -Encoding utf8 $env:TEMP\minimum_composition_plan.json
Write-Host "Build validation passed. Plan written to $env:TEMP\minimum_composition_plan.json"
