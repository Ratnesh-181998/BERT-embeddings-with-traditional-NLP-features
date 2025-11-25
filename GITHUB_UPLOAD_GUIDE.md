# GitHub Upload Guide

This guide will help you upload the **Jaguar Word Sense Disambiguation Project** to GitHub.

## Prerequisites

1.  **Git Installed**: Ensure you have Git installed on your machine.
2.  **GitHub Account**: You need a GitHub account.
3.  **New Repository**: Create a new empty repository on GitHub (do not initialize with README, .gitignore, or License).

## Automated Upload (Recommended)

We have provided a PowerShell script to automate the process.

1.  Open a terminal in this directory.
2.  Run the script:
    ```powershell
    .\setup_github.ps1
    ```
3.  Follow the prompts. When asked, paste your new GitHub repository URL.

## Manual Upload

If you prefer to do it manually, follow these steps:

1.  **Initialize Git**:
    ```bash
    git init
    ```

2.  **Add Files**:
    ```bash
    git add .
    ```

3.  **Commit**:
    ```bash
    git commit -m "Initial commit"
    ```

4.  **Rename Branch**:
    ```bash
    git branch -M main
    ```

5.  **Add Remote**:
    Replace `YOUR_REPO_URL` with your actual GitHub repository URL.
    ```bash
    git remote add origin YOUR_REPO_URL
    ```

6.  **Push**:
    ```bash
    git push -u origin main
    ```

## Troubleshooting

-   **Authentication**: If prompted for a password, use your GitHub Personal Access Token (PAT) instead of your account password.
-   **Large Files**: The `.gitignore` file is configured to exclude large model artifacts (`model_artifacts/`) to avoid GitHub file size limits.
