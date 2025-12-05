# Quickstart: Local Development Environment

This guide walks through verifying the environment, installing the required version of Python (3.13), setting up a per-project interpreter with `pyenv`, configuring Poetry, installing dependencies, and verifying the runtime/dev environment for the `flinn-building-agentic-applications` project.

## 🔎 Overview

This repository requires Python >=3.13,<3.14 (see `pyproject.toml`). We'll use `pyenv` to install Python 3.13 (3.13.10 is used in examples). After installing Python, we'll setup a project-local virtual environment using Poetry, install dependencies, and verify the LangGraph Studio is up.

⚠️ Important — What changed and why

- We've locked the project Python version in `.python-version` (3.13.10) so contributors run the same interpreter.
- `poetry` has been configured to create virtual environments in-project (`.venv`) and the repo uses `poetry env use "$(pyenv which python)"` to set the correct interpreter.
- `pre-commit` is now added to dev dependencies and a `.pre-commit-config.yaml` exists that runs `poe clean` and `poe check` on commit-time.
- We narrowed the `poe check` & `poe clean` tasks to only inspect `src` and `test` folders to avoid scanning `.venv` or third-party packages (which can cause many false-positive lint/type hits).
- Additional developer ergonomics added: `.vscode/` settings & `tasks.json`, and `.cursor/commands/` (Copilot snippets) to make running checks from the editor easier.

## 1) Verify system tools

Open a new terminal and run:

```bash
python3 --version
which python3
brew --version
poetry --version
```

Expected:

- Python may be a newer or older system version (we'll install 3.13 locally)
- `brew` should be present on macOS
- `poetry` must be installed

If not installed, install Homebrew (https://brew.sh/) and Poetry (`pip install poetry`).

## 2) Install prerequisite libraries for building Python

On macOS, run:

```bash
brew update
brew install openssl readline sqlite3 xz zlib bzip2 libffi
```

This ensures compile-time dependencies are available for `pyenv`.

## 3) Install pyenv (recommended) and configure your shell

```bash
brew install pyenv
# Add to ~/.zshrc (if using zsh)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
# Reload shell
exec "$SHELL"
```

## 4) Install Python 3.13 with pyenv

```bash
# Set flags (necessary on macOS when using Homebrew OpenSSL etc.)
export LDFLAGS="-L$(brew --prefix openssl@3)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib -L$(brew --prefix libffi)/lib"
export CPPFLAGS="-I$(brew --prefix openssl@3)/include -I$(brew --prefix zlib)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix libffi)/include"
export PKG_CONFIG_PATH="$(brew --prefix openssl@3)/lib/pkgconfig:$(brew --prefix zlib)/lib/pkgconfig"

pyenv install 3.13.10
# Set the project to use 3.13.10
echo "3.13.10" > .python-version
pyenv local 3.13.10

# Validate
pyenv versions
pyenv version
```

## 5) Configure Poetry for in-project venv & use the pyenv interpreter

```bash
cd /path/to/flinn-building-agentic-applications
poetry config virtualenvs.in-project true --local
poetry env use "$(pyenv which python)"
```

Verify:

```bash
poetry run python -V
poetry run python -c 'import sys; print(sys.executable)'
```

It should show Python 3.13.x and the path to the project's `.venv/bin/python`.

## 6) Install runtime and development dependencies

```bash
poetry install
# install dev groups
poetry install --with dev
```

## 7) Create `.env` and fill API keys

Copy the example `.env` (if not present) or create one:

```bash
cat > .env <<'EOF'
OPENAI_API_KEY=""
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"
LANGSMITH_API_KEY=""
LANGSMITH_PROJECT="flinn-makers-day-meal-planner"
LOG_LEVEL="ERROR"
EOF
```

Fill real keys for `OPENAI_API_KEY` and `LANGSMITH_API_KEY`.

## 8) Start LangGraph Studio (dev server)

```bash
poetry run langgraph dev
```

Expected outputs printed include:

- API URL: http://127.0.0.1:2024
- Studio UI URL: https://eu.smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

Open the Studio UI to test the agent.

## 9) Run Pre-Commit Checks, Lint and Tests

Format & fix issues:

```bash
poetry run poe clean
poetry run poe check  # runs checks only over src/ and test/ to avoid scanning .venv
poetry run poe test:unit
poetry run poe test:integration
```

If checks fail, fix the issues and re-run.

# Optional: Install and enable pre-commit hooks. This installs the pre-commit hooks added in
# `.pre-commit-config.yaml`. Contributors can also install pre-commit globally.
poetry run pip install pre-commit
poetry run pre-commit install
## 10) VS Code Integration

- Recommended settings (or use `.vscode/settings.json` in the repo):
  - `python.defaultInterpreterPath` or `python.pythonPath` should point to the project `.venv/bin/python`.
  - Ensure `poetry config virtualenvs.in-project true --local` is set so `.venv` is present at project root.
  - Install Python extension, pytest extension, and set `python.testing.pytestEnabled`.

## 11) Optional: asdf or Homebrew Python

If you prefer `asdf` or Homebrew's `python@3.13`, install those and then update Poetry to use the interpreter you prefer:

```bash
# Example for Homebrew python@3.13
brew install python@3.13
poetry env use /opt/homebrew/opt/python@3.13/bin/python3
```

## Troubleshooting

- If `pyenv install` fails, ensure Xcode CLI tools are installed:

```bash
xcode-select --install
```

- If build fails due to OpenSSL or zlib, set the `LDFLAGS`/`CPPFLAGS`/`PKG_CONFIG_PATH` to Homebrew paths.

## Helpful Commands

- Clean formatting + install types: `poetry run poe clean`
- Static checks: `poetry run poe check`
- Run LangGraph dev server: `poetry run langgraph dev`
- Run unit tests: `poetry run poe test:unit`
- Run integration tests: `poetry run poe test:integration`

## How to revert or restore a clean state (undo local changes)

If anything needs to be rolled back (for example we accidentally changed our environment config or want to restore to a pristine repository state), here are safe steps you can use. These commands do not push or change the remote branch — they only affect local working tree and the local `.venv`.

- Unstage any changes and restore files to the one in HEAD:

```bash
# Restore a single file
git restore --source=HEAD --staged path/to/file && git restore --source=HEAD path/to/file

# Restore all modified files to HEAD (careful: this discards uncommitted modifications)
git restore --source=HEAD --staged . && git restore --source=HEAD .
```

- Remove untracked files (including `.venv`) and reset the working tree:

```bash
# BE CAREFUL: runs in the repo root — removes untracked files/folders
git clean -fd
```

- Remove the project local venv (if created) — optional:

```bash
rm -rf .venv
```

- Unset the local pyenv version (so the project no longer sets an enforced `.python-version`):

```bash
pyenv local --unset
# or restore/remove .python-version from git (committed) if you need to revert the file entirely
git restore --source=HEAD --staged .python-version && git restore --source=HEAD .python-version
```

- Remove the local pyenv-installed version (optional):

```bash
pyenv uninstall --force 3.13.10
```

- Restore dependency lock file & re-install (reset lock file to latest from remote HEAD):

```bash
# Restore lockfile to HEAD (discarding the local lock file)
git restore --source=HEAD poetry.lock
poetry install
```

If commits were made locally and you want to undo them (but keep changes):

```bash
# Move the branch pointer back by 1 commit, keep the changes in working tree
git reset --soft HEAD~1
```

If you want to discard the commit entirely and its changes:

```bash
# Be very careful: this removes the last commit and its changes from working tree
git reset --hard HEAD~1
```

## What's next

1. Add your API keys to `.env`.
2. Open LangGraph Studio and run agents.
3. Implement features and tests in `src/my_agent/`.
4. Use the code-check files in `.cursor/commands/` to automate checks or integrate with Copilot.

---

This Quickstart consolidates project setup and development verification. If you want, I can wire the VS Code `tasks.json` and `settings.json` into the repo and add any missing pre-commit hooks so these commands can be triggered quickly from the editor.
