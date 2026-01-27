$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Resolve-Path "$scriptDir\..\.."

# Load .env if present (same as run_market_radar.ps1)
$envFile = Join-Path $scriptDir ".env"
if (Test-Path $envFile) {
  Get-Content $envFile | ForEach-Object {
    if ($_ -match '^[\s]*([^#=]+)=(.*)$') {
      $name = $Matches[1].Trim()
      $value = $Matches[2].Trim()
      if ($name -and $value) {
        [System.Environment]::SetEnvironmentVariable($name, $value)
      }
    }
  }
}

$env:PYTHONPATH = Join-Path $scriptDir "src"

python -m market_radar.run --root $root --writeback-opportunity-map --config tools/market_radar/config/watchlist.yaml
python -m market_radar.run --root $root --writeback-opportunity-map --config tools/market_radar/config/topics/aiinfra_bottleneck_shift.yaml
python -m market_radar.run --root $root --writeback-opportunity-map --config tools/market_radar/config/topics/model_price_war_profit_pool_shift.yaml

