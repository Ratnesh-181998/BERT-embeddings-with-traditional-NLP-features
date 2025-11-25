# setup_github.ps1
# PowerShell script to initialize git and push to GitHub

Write-Host "Setting up Git repository for Jaguar_Project..." -ForegroundColor Cyan

# Initialize Git
if (-not (Test-Path ".git")) {
    Write-Host "Initializing new Git repository..."
    git init
} else {
    Write-Host "Git repository already initialized."
}

# Add all files
Write-Host "Adding files to staging..."
git add .

# Commit
Write-Host "Committing files..."
git commit -m "Initial commit: Jaguar Word Sense Disambiguation System"

# Check for remote
$remote = git remote get-url origin 2>$null
if (-not $remote) {
    Write-Host "No remote repository configured." -ForegroundColor Yellow
    $repoUrl = Read-Host "Please enter your GitHub repository URL (e.g., https://github.com/username/repo.git)"
    if ($repoUrl) {
        git remote add origin $repoUrl
        Write-Host "Remote 'origin' added."
        
        # Rename branch to main
        git branch -M main
        
        # Push
        Write-Host "Pushing to GitHub..."
        git push -u origin main
    } else {
        Write-Host "No URL provided. Skipping push."
    }
} else {
    Write-Host "Remote 'origin' already exists: $remote"
    Write-Host "Pushing to GitHub..."
    git push -u origin main
}

Write-Host "Done!" -ForegroundColor Green
