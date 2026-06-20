# UAM repo layout initializer
# Run from the repository root:
#   cd "C:\path\to\User-Agent-Model-UAM"
#   powershell -ExecutionPolicy Bypass -File .\init-uam-repo-layout.ps1

$ErrorActionPreference = "Stop"

$dirs = @(
  "intake",
  "intake/uam-current-active-source-set",
  "intake/phase-0-packets",
  "intake/ab",
  "intake/omr",
  "intake/deployment-readiness",
  "intake/conversation-donors",
  "intake/misc-unsorted",

  "active",
  "active/uam",
  "active/ab",
  "active/omr",

  "registers",
  "archive",
  "archive/uam",
  "archive/ab",
  "archive/omr",

  "evidence",
  "packets",
  "tests",
  "handoffs",
  "scripts"
)

foreach ($dir in $dirs) {
  New-Item -ItemType Directory -Force -Path $dir | Out-Null

  # Keep empty folders visible in Git
  $gitkeep = Join-Path $dir ".gitkeep"
  if (!(Test-Path $gitkeep)) {
    New-Item -ItemType File -Path $gitkeep | Out-Null
  }
}

$readme = @"
# User Agent Model — UAM Repository

This repository is the canonical workspace for UAM source control, artifact intake, active artifacts, archive lineage, registers, packets, evidence, tests, and handoffs.

## Directory roles

- `/intake` — raw supplied files, packets, donor material, and unsorted source drops. Files here are not active authority merely because they exist.
- `/active` — canonical active artifact locations after reconciliation and indexing.
- `/registers` — project state, artifact index, source authority register, decision log, conflict register, adoption/rollback register, component registry, assignment register, and evaluation register.
- `/archive` — immutable prior snapshots and displaced material.
- `/evidence` — evaluation records, verification outputs, run logs, and evidence packets.
- `/packets` — source-complete handoff and dispatch packets.
- `/tests` — test decks, fixtures, harnesses, and validation material.
- `/handoffs` — prepared prompts, transition notes, and operator handoff records.
- `/scripts` — repo maintenance and validation scripts.

## Authority rule

The repo may contain many files. Only indexed active artifacts are active authority. Intake files, packet exports, displaced copies, and archive material do not become governing merely by being present.
"@

Set-Content -Path "README.md" -Value $readme -Encoding UTF8

$gitignore = @"
# OS/editor noise
.DS_Store
Thumbs.db
*.tmp
*.bak
~$*

# Python / local tooling
__pycache__/
.venv/
.env

# Large local-only scratch
scratch/
local-only/
"@

if (!(Test-Path ".gitignore")) {
  Set-Content -Path ".gitignore" -Value $gitignore -Encoding UTF8
}

Write-Host "UAM repo layout created."
Write-Host ""
Write-Host "Next suggested commands:"
Write-Host "  git status"
Write-Host "  git add ."
Write-Host "  git commit -m `"Initialize UAM repo layout`""
Write-Host "  git push"