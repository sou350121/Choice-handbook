$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Resolve-Path "$scriptDir\..\.."

# Load .env if present
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

python -m market_radar.run --root $root --writeback-opportunity-map
