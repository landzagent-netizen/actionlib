"""Git actions."""

import subprocess
from actionlib.core.registry import registry


def _git_status() -> dict:
    """Get git status."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )
    return {
        "changed": [line for line in result.stdout.strip().split("\n") if line],
        "returncode": result.returncode
    }


def _git_commit(message: str) -> str:
    """Create a git commit with the given message."""
    result = subprocess.run(
        ["git", "commit", "-m", message],
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr


def _git_branch() -> str:
    """Get current git branch."""
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def _git_add(path: str = ".") -> bool:
    """Git add a file or directory."""
    result = subprocess.run(
        ["git", "add", path],
        capture_output=True,
        text=True
    )
    return result.returncode == 0


# Register git actions
registry.register("git_status", _git_status)
registry.register("git_commit", _git_commit)
registry.register("git_branch", _git_branch)
registry.register("git_add", _git_add)
