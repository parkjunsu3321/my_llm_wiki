param(
    [string]$VaultRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path,
    [string]$ConfigPath = (Join-Path $PSScriptRoot "config.json"),
    [string]$CommitMessage = "",
    [switch]$SkipPush
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ConfigPath)) {
    throw "Config not found: $ConfigPath"
}

$config = Get-Content $ConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json
$remoteUrl = $config.remoteUrl
$repoPath = $config.localRepoPath
$destFolder = $config.destFolder
$branch = $config.branch
$wikiSource = Join-Path $VaultRoot $config.wikiSource

if (-not (Test-Path $wikiSource)) {
    throw "Wiki source not found: $wikiSource"
}

if (-not (Test-Path $repoPath)) {
    New-Item -ItemType Directory -Path $repoPath -Force | Out-Null
    git clone $remoteUrl $repoPath
}

$destPath = Join-Path $repoPath $destFolder
New-Item -ItemType Directory -Path $destPath -Force | Out-Null

robocopy $wikiSource $destPath /MIR /NFL /NDL /NJH /NJS /R:1 /W:1 | Out-Null
if ($LASTEXITCODE -ge 8) {
    throw "robocopy failed with exit code $LASTEXITCODE"
}

Push-Location $repoPath
try {
    git add $destFolder

    $status = git status --porcelain
    if (-not $status) {
        Write-Output "No wiki changes to push."
        return
    }

    if ([string]::IsNullOrWhiteSpace($CommitMessage)) {
        $date = Get-Date -Format "yyyy-MM-dd"
        $CommitMessage = "Sync wiki to $destFolder after ingest ($date)."
    }

    git commit -m $CommitMessage

    if (-not $SkipPush) {
        $currentBranch = git rev-parse --abbrev-ref HEAD
        if ($currentBranch -ne $branch) {
            git branch -M $branch
        }
        git push -u origin $branch
        Write-Output "Pushed wiki to $remoteUrl ($branch/$destFolder)."
    }
}
finally {
    Pop-Location
}
