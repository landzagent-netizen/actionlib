# ActionLib

**Standard library for AI agents.** Stop burning tokens on deterministic actions. Import once, execute locally, save tokens.

## Why

Every AI agent framework re-generates prompts for basic actions like `read_file`, `run_cmd`, `http_get` on every single call. That's wasted tokens on code that's already correct.

ActionLib moves these actions out of the LLM's scope entirely. The agent decides **what** to call and **with what params**. The execution is pure Python — local, deterministic, zero-token.

## Install

```bash
pip install actionlib
```

## Quick Start

```python
from actionlib import actions, execute, list_actions

# List all available actions
print(list_actions())

# Execute an action
result = execute("read_file", {"path": "/tmp/foo.txt"})
print(result)

# Or call directly from the dict
content = actions["read_file"]("/tmp/foo.txt")
```

## The Core Idea

```
Agent: "execute read_file with path=/tmp/foo.txt"
ActionLib: looks up actions["read_file"], calls it locally
ActionLib: returns result  ← no LLM token burned
```

## Available Actions

### IO
- `read_file(path)` → str
- `write_file(path, content)` → bool
- `append_file(path, content)` → bool
- `list_dir(path)` → list[str]
- `file_exists(path)` → bool
- `make_dir(path)` → bool
- `remove_file(path)` → bool

### Shell
- `run_cmd(cmd)` → dict with stdout, stderr, returncode
- `run_pipe(cmd1, cmd2)` → str

### Net
- `http_get(url)` → str
- `http_post(url, data)` → str

### Git
- `git_status()` → dict
- `git_commit(message)` → str
- `git_branch()` → str
- `git_add(path)` → bool

### Text
- `grep(pattern, path)` → list[str]
- `regex_replace(pattern, replacement, path)` → bool
- `count_lines(path)` → int
- `word_count(path)` → int

## Register Your Own Actions

```python
from actionlib import register

def my_action(arg1, arg2):
    return arg1 + arg2

register("add", my_action, "Add two numbers")
```

## Token Comparison

**Without ActionLib:**
- Agent prompt includes full tool definitions: ~500 tokens
- Every tool call includes tool description: ~100 tokens
- Per-action cost: ~600 tokens

**With ActionLib:**
- Agent prompt: just the action name + params: ~20 tokens
- Execution: 0 tokens
- Per-action cost: ~20 tokens

**Savings: ~97% per action**

## License

MIT
