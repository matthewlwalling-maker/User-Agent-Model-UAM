param(
    [string]$Config = "configs/run_series.yaml"
)
$ErrorActionPreference = "Stop"
mch doctor --config $Config --require-provider-auth
mch plan --config $Config
mch run --config $Config
mch validate-run --config $Config
