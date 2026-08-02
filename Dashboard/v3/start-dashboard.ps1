param(
  [int]$Port = 8766
)

$dashboardDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -LiteralPath $dashboardDirectory
python server.py --host 127.0.0.1 --port $Port
