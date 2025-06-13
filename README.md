# codex-lab-harli

This repository contains utilities to automate GitHub tasks using Python. The `scripts` directory includes a script to create a repository and upload a README file via the GitHub API.

## Usage

1. Install the dependencies:
   ```bash
   pip install requests
   ```
2. Export the following environment variables:
   - `GITHUB_USERNAME`: your GitHub username.
   - `REPO_NAME`: name of the repository to create.
   - `GITHUB_TOKEN`: a GitHub personal access token with repo permissions.
3. Run the script:
   ```bash
   python scripts/create_repo.py
   ```

The script creates the repository and adds a README with predefined content.
