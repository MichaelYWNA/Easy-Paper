param(
    [string]$Destination = "$env:USERPROFILE\.codex\skills\easy-paper"
)

$ErrorActionPreference = "Stop"
$Source = Split-Path -Parent $MyInvocation.MyCommand.Path

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

Copy-Item -LiteralPath (Join-Path $Source "SKILL.md") -Destination (Join-Path $Destination "SKILL.md") -Force

foreach ($Dir in @("agents", "assets", "references", "scripts", "docs", "examples")) {
    $SourceDir = Join-Path $Source $Dir
    if (Test-Path -LiteralPath $SourceDir) {
        $DestinationDir = Join-Path $Destination $Dir
        New-Item -ItemType Directory -Force -Path $DestinationDir | Out-Null
        Copy-Item -Path (Join-Path $SourceDir "*") -Destination $DestinationDir -Recurse -Force
    }
}

Write-Host "Easy-Paper installed to $Destination"
Write-Host "Restart Codex or open a new task, then invoke: `$easy-paper"
