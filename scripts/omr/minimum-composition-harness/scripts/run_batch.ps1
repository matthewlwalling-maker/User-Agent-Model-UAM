param(
    [string]$Config = "configs/run_series.yaml",
    [Parameter(Mandatory=$true)][string]$Cases
)
$ErrorActionPreference = "Stop"

mch doctor --config $Config --require-provider-auth
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

mch plan --config $Config
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

mch run --config $Config --cases $Cases
$runCode = $LASTEXITCODE

mch usage-summary --config $Config

if ($runCode -eq 4) {
    Write-Host "Codex usage window exhausted. The run paused safely. Re-run this same batch after reset or credits." -ForegroundColor Yellow
    exit 4
}
if ($runCode -eq 3) {
    Write-Host "Batch completed, but the full configured series is still incomplete. Continue with the next batch." -ForegroundColor Cyan
    exit 0
}
exit $runCode
