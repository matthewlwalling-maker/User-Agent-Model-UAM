[CmdletBinding()]
param(
    [string]$MasterRepoUrl = "https://github.com/matthewlwalling-maker/User-Agent-Model-UAM.git",
    [string]$TargetRepoPath,
    [string]$ActiveRoot = "active/uam/bridge-skills",
    [string]$Branch = "main",
    [string]$CommitMessage = "Publish UAM Bridge Skills active set",
    [switch]$CloneIfMissing,
    [switch]$ReplaceActiveRoot,
    [switch]$AllowDirtyTarget,
    [switch]$Stage,
    [switch]$Commit,
    [switch]$Push,
    [switch]$SkipValidation,
    [string]$PushConfirmation
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PackageRoot = (Resolve-Path -LiteralPath (Join-Path $ScriptDir "..\..")).Path
$WorkspaceRoot = (Resolve-Path -LiteralPath (Join-Path $PackageRoot "..")).Path
$RequiredPushConfirmation = "PUSH UAM BRIDGE SKILLS TO MASTER"

function Join-PortablePath {
    param([string]$Base, [string]$Relative)
    $path = $Base
    foreach ($part in ($Relative -split "[/\\]+")) {
        if ($part.Length -gt 0) {
            $path = Join-Path $path $part
        }
    }
    return $path
}

function Assert-UnderRoot {
    param([string]$Path, [string]$Root)
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
    param([string]$Root, [string]$Path)
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

function Test-ExcludedPackagePath {
    param([string]$RelativePath)
    $portable = $RelativePath.Replace("\", "/").TrimStart([char[]]@(".", "/")).ToLowerInvariant()
    $patterns = @(
        "exports/generated/*",
        "exports/archive/*",
        "tests/archive/generated-cache/*",
        "*/__pycache__/*",
        "*.pyc",
        "*.local.md",
        "*.local.yaml",
        "*.local.yml",
        "*.local.json",
        "*/private.local/*",
        "*/scoring-keys.local/*",
        "*/raw-private/*",
        "*/raw/*",
        "*/raw-outputs.*",
        "*/private-run-map.*",
        "*/private-hashes.*",
        "*/mapping-key*.local.md",
        "*scoring-key*",
        "*scoring_keys*",
        "*/test responses/*"
    )
    foreach ($pattern in $patterns) {
        if ($portable -like $pattern) {
            return $true
        }
    }
    return $false
}

function Get-Sha256Lower {
    param([string]$Path)
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
}

function Invoke-SourceValidation {
    if ($SkipValidation) {
        Write-Warning "Skipping source validation because -SkipValidation was supplied."
        return
    }

    $pythonCandidates = @(
        (Join-Path $WorkspaceRoot ".venv\Scripts\python.exe"),
        "python"
    )
    $python = $pythonCandidates | Where-Object { $_ -eq "python" -or (Test-Path -LiteralPath $_) } | Select-Object -First 1
    if (-not $python) {
        throw "No Python runtime found for source validation."
    }

    $governanceValidator = Join-Path $PackageRoot "tools\active\validate_workspace_governance.py"
    $yamlValidator = Join-Path $PackageRoot "tools\active\validate_yaml.py"
    & $python $governanceValidator
    if ($LASTEXITCODE -ne 0) {
        throw "workspace governance validation failed"
    }
    & $python $yamlValidator
    if ($LASTEXITCODE -ne 0) {
        throw "YAML validation failed"
    }
}

function Copy-PublishedFile {
    param(
        [string]$SourcePath,
        [string]$DestinationRoot,
        [string]$RelativeDestination,
        [string]$SourceOrigin,
        [string]$ObjectType
    )

    $destPath = Join-PortablePath -Base $DestinationRoot -Relative $RelativeDestination
    Assert-UnderRoot -Path $destPath -Root $RepoRoot
    $destParent = Split-Path -Parent $destPath
    if (-not (Test-Path -LiteralPath $destParent)) {
        New-Item -ItemType Directory -Path $destParent -Force | Out-Null
    }
    Copy-Item -LiteralPath $SourcePath -Destination $destPath -Force
    $sourceHash = Get-Sha256Lower -Path $SourcePath
    $destHash = Get-Sha256Lower -Path $destPath
    if ($sourceHash -ne $destHash) {
        throw "Hash mismatch after copy: $RelativeDestination"
    }
    $repoRel = Get-RelativePathSafe -Root $RepoRoot -Path $destPath
    $publishedFiles.Add([pscustomobject]@{
        Path = $repoRel
        Sha256 = $destHash
        SourceOrigin = $SourceOrigin
        ObjectType = $ObjectType
    }) | Out-Null
}

function Add-GeneratedPublishedFile {
    param(
        [string]$Path,
        [string]$SourceOrigin,
        [string]$ObjectType
    )

    Assert-UnderRoot -Path $Path -Root $RepoRoot
    $repoRel = Get-RelativePathSafe -Root $RepoRoot -Path $Path
    $publishedFiles.Add([pscustomobject]@{
        Path = $repoRel
        Sha256 = (Get-Sha256Lower -Path $Path)
        SourceOrigin = $SourceOrigin
        ObjectType = $ObjectType
    }) | Out-Null
}

if (-not $TargetRepoPath) {
    throw "TargetRepoPath is required. Use a local clone path for $MasterRepoUrl."
}

if ($Push -and $PushConfirmation -ne $RequiredPushConfirmation) {
    throw "Push requires -PushConfirmation '$RequiredPushConfirmation'."
}

if ($Commit -and -not $Stage) {
    $Stage = $true
}

if ($Push -and -not $Commit) {
    throw "Push requires -Commit so the exact staged publication is committed before push."
}

Invoke-SourceValidation

if ((-not (Test-Path -LiteralPath $TargetRepoPath)) -and $CloneIfMissing) {
    $parent = Split-Path -Parent $TargetRepoPath
    if (-not $parent -or -not (Test-Path -LiteralPath $parent)) {
        throw "Clone parent does not exist: $parent"
    }
    & git clone $MasterRepoUrl $TargetRepoPath
    if ($LASTEXITCODE -ne 0) {
        throw "git clone failed for $MasterRepoUrl"
    }
}

$RepoRoot = Get-GitRoot -Path $TargetRepoPath
$remotes = & git -C $RepoRoot remote 2>$null
if ($LASTEXITCODE -eq 0 -and ($remotes -contains "origin")) {
    $origin = & git -C $RepoRoot remote get-url origin
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to read origin remote from target repository."
    }
    $normalizedOrigin = $origin.Trim().ToLowerInvariant()
    $normalizedTarget = $MasterRepoUrl.Trim().ToLowerInvariant()
    if ($normalizedOrigin -ne $normalizedTarget) {
        Write-Warning "Remote origin does not exactly match MasterRepoUrl. origin=$origin target=$MasterRepoUrl"
    }
} else {
    Write-Warning "Target repo has no origin remote. This is acceptable for prepare-only dry runs, but commit/push should use a clone of $MasterRepoUrl."
}

$status = & git -C $RepoRoot status --porcelain
if (($status | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }).Count -gt 0 -and -not $AllowDirtyTarget) {
    throw "Target repo has uncommitted changes. Re-run with -AllowDirtyTarget only after reviewing them."
}

$branchNow = & git -C $RepoRoot branch --show-current
if ($LASTEXITCODE -eq 0 -and $branchNow.Trim() -ne $Branch) {
    Write-Warning "Current branch is '$($branchNow.Trim())', expected '$Branch'. The script will not checkout automatically."
}

$ActiveRootPath = Join-PortablePath -Base $RepoRoot -Relative $ActiveRoot
$PackageDestRoot = Join-Path $ActiveRootPath "package"
$AuthorityDestRoot = Join-Path $ActiveRootPath "authority"
Assert-UnderRoot -Path $ActiveRootPath -Root $RepoRoot
Assert-UnderRoot -Path $PackageDestRoot -Root $RepoRoot
Assert-UnderRoot -Path $AuthorityDestRoot -Root $RepoRoot

$timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
if ((Test-Path -LiteralPath $ActiveRootPath) -and $ReplaceActiveRoot) {
    $archiveRoot = Join-PortablePath -Base $RepoRoot -Relative "archive/uam/bridge-skills"
    $archiveDest = Join-Path $archiveRoot "active-set-before-$timestamp"
    Assert-UnderRoot -Path $archiveDest -Root $RepoRoot
    New-Item -ItemType Directory -Path $archiveRoot -Force | Out-Null
    Copy-Item -LiteralPath $ActiveRootPath -Destination $archiveDest -Recurse
    if (-not (Test-Path -LiteralPath $archiveDest)) {
        throw "Archive copy failed: $archiveDest"
    }
    Remove-Item -LiteralPath $ActiveRootPath -Recurse -Force
    Write-Output "ARCHIVED_PREVIOUS_ACTIVE_ROOT: $archiveDest"
}

New-Item -ItemType Directory -Path $PackageDestRoot -Force | Out-Null
New-Item -ItemType Directory -Path $AuthorityDestRoot -Force | Out-Null

$publishedFiles = New-Object System.Collections.Generic.List[object]
$authorityFilesCopied = 0
$sourceFiles = Get-ChildItem -LiteralPath $PackageRoot -Recurse -File | Sort-Object FullName
foreach ($sourceFile in $sourceFiles) {
    $relative = Get-RelativePathSafe -Root $PackageRoot -Path $sourceFile.FullName
    if (Test-ExcludedPackagePath -RelativePath $relative) {
        continue
    }
    Copy-PublishedFile `
        -SourcePath $sourceFile.FullName `
        -DestinationRoot $PackageDestRoot `
        -RelativeDestination $relative `
        -SourceOrigin "uam-bridge-skills/$relative" `
        -ObjectType "package-source"
}

$workspaceAuthorityFiles = @(
    @{ Source = "AGENTS.md"; Destination = "AGENTS.md"; ObjectType = "agent-instructions" },
    @{ Source = "UAM_Artifact_Index.yaml"; Destination = "UAM_Artifact_Index.yaml"; ObjectType = "source-authority" },
    @{ Source = "UAM_Artifact_Naming_and_Archive_Convention.md"; Destination = "UAM_Artifact_Naming_and_Archive_Convention.md"; ObjectType = "source-authority" },
    @{ Source = "UAM_Model_Framework.md"; Destination = "UAM_Model_Framework.md"; ObjectType = "source-context" },
    @{ Source = "UAM_Model_Participation_and_Assurance_Plan.md"; Destination = "UAM_Model_Participation_and_Assurance_Plan.md"; ObjectType = "source-context" },
    @{ Source = "UAM_Source_Intake_and_Context_Map.md"; Destination = "UAM_Source_Intake_and_Context_Map.md"; ObjectType = "source-context" },
    @{ Source = "UAM_Bootstrap_Pair_Brief.md"; Destination = "UAM_Bootstrap_Pair_Brief.md"; ObjectType = "source-context" }
)
foreach ($entry in $workspaceAuthorityFiles) {
    $sourcePath = Join-Path $WorkspaceRoot $entry.Source
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        throw "Required workspace authority/source-context file missing: $($entry.Source)"
    }
    $destinationRoot = $AuthorityDestRoot
    $relativeDestination = $entry.Destination
    if ($entry.Source -eq "AGENTS.md") {
        $destinationRoot = $ActiveRootPath
    }
    Copy-PublishedFile `
        -SourcePath $sourcePath `
        -DestinationRoot $destinationRoot `
        -RelativeDestination $relativeDestination `
        -SourceOrigin $entry.Source `
        -ObjectType $entry.ObjectType
    $authorityFilesCopied += 1
}

$readmePath = Join-Path $ActiveRootPath "README.md"
$readme = @(
    "# UAM Bridge Skills",
    "",
    "Status: rollout-lab-candidate",
    "Evidence ceiling: design-time source publication only",
    "",
    "This folder is the master-repo active home for the UAM Bridge Skills workstream.",
    "",
    "## Contents",
    "",
    "- `AGENTS.md`: Bridge-specific operating contract for agents working in this subtree.",
    "- `authority/`: Workspace authority and source-context snapshots used by the Bridge package.",
    "- `package/`: Canonical Bridge Skills source package.",
    "- `PACKAGE_STAMP.yaml`: Active-set identity and package hash.",
    "- `SOURCE_MANIFEST.yaml`: File manifest for this active publication.",
    "- `PUBLICATION_RECORD.md`: Publication run record and claim limits.",
    "",
    "Publishing this folder does not install, activate, deploy, or prove runtime readiness."
)
Set-Content -LiteralPath $readmePath -Value $readme -Encoding UTF8
Add-GeneratedPublishedFile -Path $readmePath -SourceOrigin "publisher-generated:README.md" -ObjectType "publication-metadata"

$canonicalLines = $publishedFiles |
    Sort-Object Path |
    ForEach-Object { "$($_.Sha256)  $($_.Path)" }
$canonicalText = ($canonicalLines -join "`n") + "`n"
$bytes = [System.Text.UTF8Encoding]::new($false).GetBytes($canonicalText)
$treeHashBytes = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
$packageHash = (($treeHashBytes | ForEach-Object { $_.ToString("x2") }) -join "")

$sourceManifest = New-Object System.Collections.Generic.List[string]
$sourceManifest.Add("manifest_profile: UAM-BRIDGE-SKILLS-SOURCE-MANIFEST-1")
$sourceManifest.Add("generated_at: '$timestamp'")
$sourceManifest.Add("active_root: $ActiveRoot")
$sourceManifest.Add("package_root: $ActiveRoot/package")
$sourceManifest.Add("package_content_sha256: $packageHash")
$sourceManifest.Add("entries:")
foreach ($file in ($publishedFiles | Sort-Object Path)) {
    $sourceManifest.Add("- path: $($file.Path)")
    $sourceManifest.Add("  sha256: $($file.Sha256)")
    $sourceManifest.Add("  object_type: $($file.ObjectType)")
    $sourceManifest.Add("  source_origin: $($file.SourceOrigin)")
}
Set-Content -LiteralPath (Join-Path $ActiveRootPath "SOURCE_MANIFEST.yaml") -Value $sourceManifest -Encoding UTF8

$stamp = @(
    "stable_artifact_id: UAM-BRIDGE-SKILLS",
    "stable_name: UAM Bridge Skills",
    "artifact_revision: 1",
    "revision_date: '$((Get-Date).ToString("yyyy-MM-dd"))'",
    "package_manifest_path: $ActiveRoot/package/skills/active/uam-bridge-skills/MANIFEST.yaml",
    "workspace_agents_path: $ActiveRoot/AGENTS.md",
    "workspace_authority_root: $ActiveRoot/authority",
    "source_manifest_path: $ActiveRoot/SOURCE_MANIFEST.yaml",
    "content_sha256: $packageHash",
    "hash_profile: UAM-PACKAGE-TREE-SHA256-1",
    "evidence_ceiling: design-time",
    "release_status: rollout-lab-candidate",
    "install_status: not-installed",
    "activation_status: not-activated",
    "published_from:",
    "  local_workspace_root: $WorkspaceRoot",
    "  source_package_root: uam-bridge-skills",
    "  source_package_version: 0.1.0"
)
Set-Content -LiteralPath (Join-Path $ActiveRootPath "PACKAGE_STAMP.yaml") -Value $stamp -Encoding UTF8

$record = @(
    "# UAM Bridge Skills Publication Record",
    "",
    "Generated: $timestamp",
    "Master repo URL: $MasterRepoUrl",
    "Active root: $ActiveRoot",
    "Workspace AGENTS path: $ActiveRoot/AGENTS.md",
    "Workspace authority root: $ActiveRoot/authority",
    "Source package root: $PackageRoot",
    "Package content SHA-256: $packageHash",
    "Files copied: $($publishedFiles.Count)",
    "Workspace authority/source-context files copied: $authorityFilesCopied",
    "",
    "Evidence ceiling: design-time source publication only.",
    "Install status: not installed.",
    "Activation status: not activated.",
    "Readiness status: no readiness claim.",
    "",
    "Default exclusions applied: generated exports, generated caches, private/local files, raw outputs, raw-private folders, private run maps, private hashes, mapping keys, scoring keys, and test response folders.",
    "",
    "Commit requested: $($Commit.IsPresent)",
    "Push requested: $($Push.IsPresent)"
)
Set-Content -LiteralPath (Join-Path $ActiveRootPath "PUBLICATION_RECORD.md") -Value $record -Encoding UTF8

if ($Stage) {
    $stageRel = Get-RelativePathSafe -Root $RepoRoot -Path $ActiveRootPath
    & git -C $RepoRoot add -- $stageRel
    if ($LASTEXITCODE -ne 0) {
        throw "git add failed for $stageRel"
    }
    Write-Output "STAGED: $stageRel"
}

if ($Commit) {
    & git -C $RepoRoot commit -m $CommitMessage
    if ($LASTEXITCODE -ne 0) {
        throw "git commit failed"
    }
    Write-Output "COMMITTED: $CommitMessage"
}

if ($Push) {
    & git -C $RepoRoot push origin $Branch
    if ($LASTEXITCODE -ne 0) {
        throw "git push failed"
    }
    Write-Output "PUSHED: origin $Branch"
}

Write-Output "MASTER_REPO_URL: $MasterRepoUrl"
Write-Output "REPO_ROOT: $RepoRoot"
Write-Output "ACTIVE_ROOT: $ActiveRootPath"
Write-Output "PACKAGE_HASH: $packageHash"
Write-Output "FILES_COPIED: $($publishedFiles.Count)"
Write-Output "SOURCE_MANIFEST: $(Join-Path $ActiveRootPath "SOURCE_MANIFEST.yaml")"
Write-Output "PACKAGE_STAMP: $(Join-Path $ActiveRootPath "PACKAGE_STAMP.yaml")"
Write-Output "PUBLICATION_RECORD: $(Join-Path $ActiveRootPath "PUBLICATION_RECORD.md")"
