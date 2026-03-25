"""ActionLib - Standard library for AI agents."""

from actionlib.core.registry import registry

#: Main actions dict — import this in your agent
actions = registry.actions


def execute(action_name: str, params: dict) -> any:
    """Execute an action by name with params.

    Args:
        action_name: Name of the action to execute
        params: Dict of parameters to pass to the action

    Returns:
        The result of the action

    Raises:
        ActionNotFound: If action_name is not registered
        ActionError: If the action raises an exception
    """
    return registry.execute(action_name, params)


def register(name: str, fn: callable, doc: str = "") -> None:
    """Register a new action.

    Args:
        name: Action name (used by agent to call it)
        fn: Callable that implements the action
        doc: Optional docstring for the action
    """
    registry.register(name, fn, doc)


def list_actions() -> dict:
    """List all registered actions and their docs.

    Returns:
        Dict mapping action names to their docstrings
    """
    return registry.list_actions()


# Register core actions (import for side-effect only)
from actionlib.actions import io as _io  # noqa: E402, F401
from actionlib.actions import shell as _shell  # noqa: E402, F401
from actionlib.actions import net as _net  # noqa: E402, F401
from actionlib.actions import git as _git  # noqa: E402, F401
from actionlib.actions import text as _text  # noqa: E402, F401
