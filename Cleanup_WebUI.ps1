# =================================================================
# Orion Specialist - WebUI Cleanup Script
# Purpose: Moves non-essential development and documentation files
#          to a backup folder for a cleaner runtime environment.
# =================================================================

# --- Configuration ---
$SourceDirectory = "C:\Orion\text-generation-webui"
$BackupDirectory = "C:\Orion\WebUI_Dev_Files_Backup"

# --- Items to Move ---
# These are primarily for development, version control, and documentation.
$itemsToMove = @(
    ".github",
    ".git",
    ".dockerignore",
    ".gitignore",
    "docker",
    "docs",
    "llama.cpp", # The source code; compiled binaries are in the Python env.
    "tests",
    "pocs",
    "CHANGELOG.md",
    "Colab-TextGen-GPU.ipynb",
    "LICENSE",
    "README.md"
)

# --- Script Execution ---

# 1. Create the backup directory if it doesn't exist
if (-not (Test-Path -Path $BackupDirectory)) {
    Write-Host "[INFO] Creating backup directory at: $BackupDirectory"
    New-Item -ItemType Directory -Path $BackupDirectory | Out-Null
} else {
    Write-Host "[INFO] Backup directory already exists at: $BackupDirectory"
}

# 2. Loop through the items and move them
Write-Host "[INFO] Beginning cleanup process..."
foreach ($item in $itemsToMove) {
    $sourcePath = Join-Path $SourceDirectory $item
    $destinationPath = Join-Path $BackupDirectory $item

    if (Test-Path -Path $sourcePath) {
        Write-Host "Moving '$item' to backup..."
        Move-Item -Path $sourcePath -Destination $destinationPath -Force
    } else {
        Write-Host "[WARN] Item '$item' not found, skipping."
    }
}

Write-Host "[SUCCESS] Cleanup complete. Non-essential files have been moved."
Read-Host "Press Enter to exit."