[CmdletBinding()]
param(
    [string]$TargetRepoPath,
    [string]$ExportName = "chatgpt-architecture-audit-2026-06-22",
    [string]$TargetSubdir = "uam-bridge-skills/exports/generated",
    [switch]$Stage
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PackageRoot = (Resolve-Path -LiteralPath (Join-Path $ScriptDir "..\..")).Path
$WorkspaceRoot = (Resolve-Path -LiteralPath (Join-Path $PackageRoot "..")).Path

function Join-PortablePath {
    param(
        [string]$Base,
        [string]$Relative
    )
    $path = $Base
    foreach ($part in ($Relative -split "[/\\]+")) {
        if ($part.Length -gt 0) {
            $path = Join-Path $path $part
        }
    }
    return $path
}

function Assert-UnderRoot {
    param(
        [string]$Path,
        [string]$Root
    )
    $fullPath = [System.IO.Path]::GetFullPath($Path)
    $fullRoot = [System.IO.Path]::GetFullPath($Root)
    if (-not $fullRoot.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $fullRoot = $fullRoot + [System.IO.Path]::DirectorySeparatorChar
    }
    $rootSelf = $fullRoot.TrimEnd([System.IO.Path]::DirectorySeparatorChar)
    if (-not ($fullPath.Equals($rootSelf, [System.StringComparison]::OrdinalIgnoreCase) -or $fullPath.StartsWith($fullRoot, [System.StringComparison]::OrdinalIgnoreCase))) {
        throw "Path escapes allowed root: $fullPath"
    }
}

function Get-RelativePathSafe {
    param(
        [string]$Root,
        [string]$Path
    )
    $fullPath = [System.IO.Path]::GetFullPath($Path)
    $fullRoot = [System.IO.Path]::GetFullPath($Root)
    if (-not $fullRoot.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $fullRoot = $fullRoot + [System.IO.Path]::DirectorySeparatorChar
    }
    if (-not $fullPath.StartsWith($fullRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Path escapes root: $fullPath"
    }
    return $fullPath.Substring($fullRoot.Length).Replace("\", "/")
}

function Get-GitRoot {
    param([string]$Path)
    $resolved = (Resolve-Path -LiteralPath $Path).Path
    $root = & git -C $resolved rev-parse --show-toplevel 2>$null
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($root)) {
        throw "TargetRepoPath is not inside a usable Git repository: $resolved"
    }
    return $root.Trim()
}

$DefaultExportDenyPatterns = @(
    "*.local.md",
    "*.local.yaml",
    "*.local.yml",
    "*.local.json",
    "*/private.local/*",
    "private.local/*",
    "*/scoring-keys.local/*",
    "scoring-keys.local/*",
    "*/raw-private/*",
    "raw-private/*",
    "*/raw/*",
    "raw/*",
    "*/raw-outputs.*",
    "raw-outputs.*",
    "*/private-run-map.*",
    "private-run-map.*",
    "*/private-hashes.*",
    "private-hashes.*",
    "*/mapping-key*.local.md",
    "mapping-key*.local.md",
    "*scoring-key*",
    "*scoring_keys*",
    "*/test responses/*",
    "test responses/*"
)

function ConvertTo-PortablePathLower {
    param([string]$Path)
    return $Path.Replace("\", "/").TrimStart(".", "/").ToLowerInvariant()
}

function Assert-ExportRelativePathAllowed {
    param(
        [string]$RelativePath,
        [string]$PathRole
    )
    $portable = ConvertTo-PortablePathLower -Path $RelativePath
    foreach ($pattern in $DefaultExportDenyPatterns) {
        if ($portable -like $pattern) {
            throw "Export $PathRole matches private/raw exclusion pattern '$pattern': $RelativePath"
        }
    }
}

$ExportFiles = @(
    @{
        Source = "handoff-packets/open/chatgpt-architecture-audit-packet-2026-06-22.md"
        Target = "CHATGPT_ARCHITECTURE_AUDIT_PACKET.md"
        Purpose = "copy-ready ChatGPT architecture audit packet"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/KERNEL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/KERNEL.md"
        Purpose = "collaboration kernel"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/MANIFEST.yaml"
        Target = "source-snapshot/skills/active/uam-bridge-skills/MANIFEST.yaml"
        Purpose = "source authority and package manifest"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/CHAIN_ROUTER.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/CHAIN_ROUTER.md"
        Purpose = "bounded continuation and route governance"
    },
    @{
        Source = "uam-bridge-skills/adapters/chatgpt/README.md"
        Target = "source-snapshot/adapters/chatgpt/README.md"
        Purpose = "ChatGPT adapter placeholder and limits"
    },
    @{
        Source = "uam-bridge-skills/tests/runs/compounding-run-001/README.md"
        Target = "source-snapshot/tests/runs/compounding-run-001/README.md"
        Purpose = "compounding run protocol and claim ceiling"
    },
    @{
        Source = "uam-bridge-skills/tests/runs/compounding-run-001/codex-run-001/scoring/mapped-results.md"
        Target = "source-snapshot/tests/runs/compounding-run-001/codex-run-001/scoring/mapped-results.md"
        Purpose = "mapped A/B/C simulated transcript summary"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/align-work/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/align-work/SKILL.md"
        Purpose = "align command source"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/design-solution/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/design-solution/SKILL.md"
        Purpose = "design command source"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/build-artifact/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/build-artifact/SKILL.md"
        Purpose = "build command source"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/review-work/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/review-work/SKILL.md"
        Purpose = "review command source"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/compare-decide/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/compare-decide/SKILL.md"
        Purpose = "compare command source"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/diagnose-problem/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/diagnose-problem/SKILL.md"
        Purpose = "diagnose command source"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/research-evidence/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/research-evidence/SKILL.md"
        Purpose = "research command source"
    },
    @{
        Source = "uam-bridge-skills/skills/active/uam-bridge-skills/commands/handoff-state/SKILL.md"
        Target = "source-snapshot/skills/active/uam-bridge-skills/commands/handoff-state/SKILL.md"
        Purpose = "handoff command source"
    }
)

if ($TargetRepoPath) {
    $RepoRoot = Get-GitRoot -Path $TargetRepoPath
    $ExportBase = Join-PortablePath -Base $RepoRoot -Relative $TargetSubdir
    $DestinationRoot = Join-PortablePath -Base $ExportBase -Relative $ExportName
    $AllowedRoot = $RepoRoot
} else {
    $RepoRoot = $null
    $ExportBase = Join-Path $PackageRoot "exports\generated"
    $DestinationRoot = Join-PortablePath -Base $ExportBase -Relative $ExportName
    $AllowedRoot = $PackageRoot
}

Assert-UnderRoot -Path $DestinationRoot -Root $AllowedRoot
if (-not (Test-Path -LiteralPath $DestinationRoot)) {
    New-Item -ItemType Directory -Path $DestinationRoot | Out-Null
}

$ManifestRows = New-Object System.Collections.Generic.List[string]
$ManifestRows.Add("# Export Manifest")
$ManifestRows.Add("")
$ManifestRows.Add("Export: $ExportName")
$ManifestRows.Add("Created: 2026-06-22")
$ManifestRows.Add("Evidence ceiling: design-time plus simulated transcript evidence where explicitly marked.")
$ManifestRows.Add("Install/activation status: not installed, not activated, not release-ready.")
$ManifestRows.Add("Default exclusions: .local files, private.local, scoring-keys.local, raw/raw-private material, private run maps, private hashes, mapping keys, and scoring key files.")
$ManifestRows.Add("")
$ManifestRows.Add("| Source | Exported path | SHA-256 | Purpose |")
$ManifestRows.Add("|---|---|---|---|")

$HashRows = New-Object System.Collections.Generic.List[string]
$CurrentTargets = New-Object System.Collections.Generic.HashSet[string]

foreach ($item in $ExportFiles) {
    Assert-ExportRelativePathAllowed -RelativePath $item.Source -PathRole "source"
    Assert-ExportRelativePathAllowed -RelativePath $item.Target -PathRole "target"

    $sourcePath = Join-PortablePath -Base $WorkspaceRoot -Relative $item.Source
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        throw "Required export source is missing: $($item.Source)"
    }

    $targetPath = Join-PortablePath -Base $DestinationRoot -Relative $item.Target
    Assert-UnderRoot -Path $targetPath -Root $AllowedRoot
    $targetParent = Split-Path -Parent $targetPath
    if (-not (Test-Path -LiteralPath $targetParent)) {
        New-Item -ItemType Directory -Path $targetParent | Out-Null
    }

    Copy-Item -LiteralPath $sourcePath -Destination $targetPath -Force
    $sourceHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash.ToLowerInvariant()
    $targetHash = (Get-FileHash -LiteralPath $targetPath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($sourceHash -ne $targetHash) {
        throw "Hash mismatch after copy: $($item.Source)"
    }

    $targetRel = Get-RelativePathSafe -Root $DestinationRoot -Path $targetPath
    [void]$CurrentTargets.Add($targetRel)
    $HashRows.Add("$targetHash  $targetRel")
    $ManifestRows.Add("| $($item.Source) | $targetRel | $targetHash | $($item.Purpose) |")
}

$ManifestPath = Join-PortablePath -Base $DestinationRoot -Relative "EXPORT_MANIFEST.md"
Set-Content -LiteralPath $ManifestPath -Value $ManifestRows -Encoding UTF8
$manifestHash = (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash.ToLowerInvariant()
$HashRows.Add("$manifestHash  EXPORT_MANIFEST.md")
[void]$CurrentTargets.Add("EXPORT_MANIFEST.md")

$HashesPath = Join-PortablePath -Base $DestinationRoot -Relative "HASHES.sha256"
Set-Content -LiteralPath $HashesPath -Value ($HashRows | Sort-Object) -Encoding UTF8
[void]$CurrentTargets.Add("HASHES.sha256")

$Stale = @()
Get-ChildItem -LiteralPath $DestinationRoot -Recurse -File | ForEach-Object {
    $rel = Get-RelativePathSafe -Root $DestinationRoot -Path $_.FullName
    if (-not $CurrentTargets.Contains($rel)) {
        $Stale += $rel
    }
}

if ($Stale.Count -gt 0) {
    Write-Warning "Export folder contains files not written by this run. They were preserved, not deleted: $($Stale -join ', ')"
}

if ($Stage) {
    if (-not $RepoRoot) {
        throw "-Stage requires -TargetRepoPath so the script knows which Git index to update."
    }
    $stageRel = Get-RelativePathSafe -Root $RepoRoot -Path $DestinationRoot
    & git -C $RepoRoot add -- $stageRel
    if ($LASTEXITCODE -ne 0) {
        throw "git add failed for $stageRel"
    }
    Write-Output "STAGED: $stageRel"
}

Write-Output "EXPORT_ROOT: $DestinationRoot"
Write-Output "MANIFEST: $ManifestPath"
Write-Output "HASHES: $HashesPath"
Write-Output "FILES_EXPORTED: $($ExportFiles.Count)"
