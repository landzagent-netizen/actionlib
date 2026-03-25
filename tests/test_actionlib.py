"""Tests for ActionLib."""

import tempfile
import os
from actionlib import execute, list_actions, register


def test_read_write_file():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("hello world")
        path = f.name

    result = execute("read_file", {"path": path})
    assert result == "hello world"
    os.unlink(path)


def test_write_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        path = f.name

    result = execute("write_file", {"path": path, "content": "test"})
    assert result is True
    with open(path) as f:
        assert f.read() == "test"
    os.unlink(path)


def test_list_dir():
    result = execute("list_dir", {"path": "/tmp"})
    assert isinstance(result, list)


def test_file_exists():
    assert execute("file_exists", {"path": "/tmp"}) is True
    assert execute("file_exists", {"path": "/nonexistent_file_xyz"}) is False


def test_run_cmd():
    result = execute("run_cmd", {"cmd": "echo hello"})
    assert result["stdout"].strip() == "hello"
    assert result["returncode"] == 0


def test_grep():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("line1\nhello world\nline3\n")
        path = f.name

    result = execute("grep", {"pattern": "hello", "path": path})
    assert "hello world" in result
    os.unlink(path)


def test_register_custom_action():
    def custom_add(a, b):
        return a + b

    register("custom_add", custom_add, "Add two numbers")
    result = execute("custom_add", {"a": 1, "b": 2})
    assert result == 3


def test_action_not_found():
    try:
        execute("nonexistent_action", {})
        assert False, "Should have raised ActionNotFound"
    except Exception as e:
        assert "not found" in str(e)


def test_list_actions():
    all_actions = list_actions()
    assert "read_file" in all_actions
    assert "run_cmd" in all_actions
    assert "http_get" in all_actions
