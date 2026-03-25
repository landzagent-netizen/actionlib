"""IO actions - file read/write."""

from actionlib.core.registry import registry


def _read_file(path: str) -> str:
    """Read a file and return its contents."""
    with open(path, "r") as f:
        return f.read()


def _write_file(path: str, content: str) -> bool:
    """Write content to a file. Creates or overwrites."""
    with open(path, "w") as f:
        f.write(content)
    return True


def _append_file(path: str, content: str) -> bool:
    """Append content to a file."""
    with open(path, "a") as f:
        f.write(content)
    return True


def _list_dir(path: str = ".") -> list[str]:
    """List directory contents."""
    import os
    return sorted(os.listdir(path))


def _file_exists(path: str) -> bool:
    """Check if a file or directory exists."""
    import os
    return os.path.exists(path)


def _make_dir(path: str) -> bool:
    """Create a directory (recursively)."""
    import os
    os.makedirs(path, exist_ok=True)
    return True


def _remove_file(path: str) -> bool:
    """Remove a file."""
    import os
    os.remove(path)
    return True


# Register all IO actions
registry.register("read_file", _read_file)
registry.register("write_file", _write_file)
registry.register("append_file", _append_file)
registry.register("list_dir", _list_dir)
registry.register("file_exists", _file_exists)
registry.register("make_dir", _make_dir)
registry.register("remove_file", _remove_file)
