"""Shell actions."""

import subprocess
from actionlib.core.registry import registry


def _run_cmd(cmd: str) -> dict:
    """Run a shell command and return stdout, stderr, returncode."""
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }


def _run_pipe(cmd1: str, cmd2: str) -> str:
    """Pipe cmd1 output into cmd2."""
    p2 = subprocess.run(
        f"{cmd1} | {cmd2}",
        shell=True,
        capture_output=True,
        text=True
    )
    return p2.stdout


# Register shell actions
registry.register("run_cmd", _run_cmd)
registry.register("run_pipe", _run_pipe)
