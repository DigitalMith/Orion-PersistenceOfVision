import os
import git
from datetime import datetime

# --- Configuration ---
# This script will automatically find the git repository by searching up 
# from the current script's location.
try:
    # Find the repository root by searching parent directories
    # This makes the script location-independent within the project
    REPO_PATH = git.Repo(os.getcwd(), search_parent_directories=True).working_dir
except git.exc.InvalidGitRepositoryError:
    # Fallback if not run from within the repo, default to C:\Orion
    REPO_PATH = r"C:\Orion"
    
# The default commit message. It will include the current date and time.
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
COMMIT_MESSAGE = f"Orion project sync at {now}"

# --- Main Script ---
print("--- Orion Git Sync Utility ---")

try:
    # 1. Open the repository
    print(f"Accessing repository at: {REPO_PATH}")
    repo = git.Repo(REPO_PATH)

    # Check if the repository is "dirty" (has uncommitted changes)
    if not repo.is_dirty(untracked_files=True):
        print("No changes to commit. Repository is clean.")
    else:
        # 2. Stage all changes (equivalent to "git add .")
        print("Staging all changes...")
        repo.git.add(A=True)

        # 3. Commit the staged changes
        print(f"Committing with message: '{COMMIT_MESSAGE}'")
        repo.index.commit(COMMIT_MESSAGE)
        print("Commit successful.")

        # 4. Push the commit to the remote repository
        origin = repo.remote(name='origin')
        print(f"Pushing to remote '{origin.name}'...")
        origin.push()
        print("Push successful!")

    print("\n--- Sync Complete ---")

except git.exc.InvalidGitRepositoryError:
    print(f"\nError: The path '{REPO_PATH}' is not a valid Git repository.")
except git.exc.GitCommandError as e:
    print(f"\nAn error occurred executing a Git command: {e}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")