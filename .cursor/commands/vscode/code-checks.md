# VS Code Pre-Commit / Dev Checks

This file mirrors `.cursor/commands/pre-commit/code-checks.md` but is tailored for VS Code users and `tasks.json` integrations.

## Overview
Use these commands in a VS Code terminal or wire them into tasks in `.vscode/tasks.json` to run pre-commit checks and integrate with the editor.

## Steps (VS Code friendly)
1. Format & install types

```bash
poetry run poe clean
```

- Expect: Black format and mypy type stubs installed.
- If it fails: fix code style/type issues reported.

2. Run static checks in the editor

```bash
poetry run poe check
```

- Expect: Flake8, mypy, and vulture checks pass. Use the Problems panel to review issues.
- If it fails: click on Problems or more info to jump to files.

3. Run unit tests (from Test Explorer or tasks)

```bash
poetry run poe test:unit
```

- Expect: Unit tests pass locally.
- If it fails: open the failing test file and iterate; use the pytest extension for VS Code Test Explorer.

## VS Code Task Tips
- Add tasks to `.vscode/tasks.json` that map to the commands above for one-click execution.
- Configure `python.pythonPath` to point to the project's `.venv/bin/python`.
- Use `poetry config virtualenvs.in-project true --local` so `.venv` is easy for VS Code to find.
