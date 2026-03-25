"""Text processing actions."""

import re
from actionlib.core.registry import registry


def _grep(pattern: str, path: str) -> list[str]:
    """Grep for pattern in file. Returns matching lines."""
    with open(path, "r") as f:
        return [line.rstrip() for line in f if re.search(pattern, line)]


def _regex_replace(pattern: str, replacement: str, path: str) -> bool:
    """Replace pattern with replacement in file (in-place)."""
    with open(path, "r") as f:
        content = f.read()
    new_content = re.sub(pattern, replacement, content)
    with open(path, "w") as f:
        f.write(new_content)
    return True


def _count_lines(path: str) -> int:
    """Count lines in a file."""
    with open(path, "r") as f:
        return sum(1 for _ in f)


def _word_count(path: str) -> int:
    """Count words in a file."""
    with open(path, "r") as f:
        return sum(len(line.split()) for line in f)


# Register text actions
registry.register("grep", _grep)
registry.register("regex_replace", _regex_replace)
registry.register("count_lines", _count_lines)
registry.register("word_count", _word_count)
