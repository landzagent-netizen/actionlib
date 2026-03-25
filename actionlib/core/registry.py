"""Core action registry."""

from typing import Callable, Any


class ActionNotFound(Exception):
    """Raised when an action is not found in the registry."""
    pass


class ActionError(Exception):
    """Raised when an action raises an exception."""
    pass


class ActionRegistry:
    """Registry for agent actions."""

    def __init__(self):
        self._actions: dict[str, Callable] = {}
        self._docs: dict[str, str] = {}

    @property
    def actions(self) -> dict[str, Callable]:
        """Return the actions dict for direct access."""
        return self._actions

    def register(self, name: str, fn: Callable, doc: str = "") -> None:
        """Register an action.

        Args:
            name: Action name
            fn: Callable implementing the action
            doc: Optional docstring
        """
        self._actions[name] = fn
        self._docs[name] = doc or (fn.__doc__ or "").strip()

    def execute(self, action_name: str, params: dict) -> Any:
        """Execute an action.

        Args:
            action_name: Name of the action
            params: Parameters to pass

        Returns:
            Result of the action

        Raises:
            ActionNotFound: If action not registered
            ActionError: If action raises
        """
        if action_name not in self._actions:
            raise ActionNotFound(f"Action '{action_name}' not found. Available: {list(self._actions.keys())}")

        fn = self._actions[action_name]
        try:
            return fn(**params)
        except Exception as e:
            raise ActionError(f"Action '{action_name}' failed: {e}") from e

    def list_actions(self) -> dict[str, str]:
        """List all actions and their docs."""
        return dict(self._docs)


# Singleton instance
registry = ActionRegistry()
