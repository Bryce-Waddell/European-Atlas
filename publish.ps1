# Commit and push a new version of the atlas.
# Usage:  .\publish.ps1 "1.4.0" "Equal-voice method; quiz research data"
param([Parameter(Mandatory=$true)][string]$Version,[Parameter(Mandatory=$true)][string]$Message)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

git add -A
git commit -m "v$Version - $Message"
git tag -a "v$Version" -m $Message
git push origin main --follow-tags
Write-Host "Published v$Version" -ForegroundColor Green
