# GUIDE: Flinn Makers Day — Hackathon Preparation & Day-of Checklist

This concise guide summarizes the host message and provides a practical checklist and commands you can use to verify your environment and be successful on the day.

---

## Quick Summary from Host

- Date & Time: Saturday, December 6. Arrive 09:45, session 10:00–17:00 (you can stay later).
- Location: Flinn office, Porzellangasse 23, top 2, 1090, Wien.
- Bring: Laptop & charger (monitors, snacks, drinks, and whiteboards will be provided).
- Format: 4 blocks (lecture + hands-on). The day will cover building agentic applications; each block adds to your agent and at the end you’ll have a deployable agent with observability.
- Tech stack for the day: Python 3.13, LangGraph, LangChain, LangSmith for tracing.
- Key asks: Create a LangSmith account (get the API key), clone the repository, set up the environment (Poetry + Python 3.13), and run `poetry run langgraph dev` to verify the LangGraph Studio UI works.

---

## What to prepare before arriving (priority checklist)

1. Account & keys

   - [x] Create a LangSmith account and copy your API key.
   - [ ] If you have one already, save the OpenAI API key (we will be given an OpenAI key on the day).

2. Dev environment (macOS checklist)
   - [x] Homebrew installed and up-to-date (https://brew.sh/)
   - [x] Xcode CLI Tools installed
     - Command: `xcode-select --install` (if not installed)
   - [x] Install pyenv & build dependencies:

```bash
brew update
brew install openssl readline sqlite3 xz zlib bzip2 libffi pyenv
```

- [x] Configure `~/.zshrc` for pyenv (restart shell or run `exec "$SHELL"`):

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"
```

- [x] Install Python 3.13 with pyenv (we used 3.13.10 in the repo examples):

```bash
export LDFLAGS="-L$(brew --prefix openssl@3)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib -L$(brew --prefix libffi)/lib"
export CPPFLAGS="-I$(brew --prefix openssl@3)/include -I$(brew --prefix zlib)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix libffi)/include"
export PKG_CONFIG_PATH="$(brew --prefix openssl@3)/lib/pkgconfig:$(brew --prefix zlib)/lib/pkgconfig"
pyenv install 3.13.10
pyenv local 3.13.10  # sets project-level .python-version
```

- [x] Install Poetry:

```bash
pip install poetry
# confirm
poetry --version
```

3. Clone the repo and run Quickstart before the event
   - [x] Clone the repository and follow QUICKSTART.md, or run the commands below:

```bash
git clone <repository-url>
cd flinn-building-agentic-applications
# Configure Poetry to use venv in the project root
poetry config virtualenvs.in-project true --local
# Use pyenv python interpreter
poetry env use "$(pyenv which python)"
poetry install  # installs runtime dependencies
poetry install --with dev  # installs dev dependencies
```

4. `LANGSMITH` & `.env`

   - [x] Create `.env` file with placeholders present in the repo. Replace `OPENAI_API_KEY` & `LANGSMITH_API_KEY` with your keys.

5. Verify LangGraph Studio works (example)

```bash
poetry run langgraph dev  # starts local dev server
# check studio link provided in the CLI output, usually https://eu.smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

If you don't have the OpenAI API key yet, you can still verify most features - the agent may crash on a tool or LLM call without a key; this is expected.

---

## Pre-reading & Resources (useful but not mandatory)

- LangGraph docs + intro to multi-agent architecture
- LangChain Quickstart
- LangSmith docs — tracing & observability
- Antropic: Writing effective tools for agents (longer deeper read)

We included these links in the README and Quickstart. A quick skim is helpful prior to the event.

---

## Day-of workflow to maximize success

1. Arrive early (09:45) with the laptop fully charged; connect to office Wi-Fi if needed.
2. Open a terminal, run these quick checks to make sure everything is prepared:

```bash
# verify pyenv config & python
python3 --version
pyenv version
poetry --version
poetry run python -V
poetry run python -c 'import sys; print(sys.executable)'
```

3. If everything looks good, start LangGraph dev server:

```bash
cd /path/to/flinn-building-agentic-applications
poetry run langgraph dev
# Studio UI should be printed in CLI.
```

4. If the agent or the server errors due to missing keys, ask the host for the OpenAI key and update `.env`.
5. Follow the 4-block lecture+hands-on structure; replicate and test code after each block.
6. Save your progress and run pre-commit checks before submitting or sharing your work.

---

## Troubleshooting Quick Hits

- pyenv install fails: install Xcode CLI Tools and ensure `LDFLAGS`, `CPPFLAGS`, and `PKG_CONFIG_PATH` are set to the Homebrew paths.
- Poetry is not installed (or wrong version): `pip install poetry` or follow Poetry installation docs.
- LangGraph dev server doesn’t start: run `poetry run langgraph dev` and check for errors; look for missing packages, or check `.env` if LLM call errors.
- If flake8 or mypy scans `.venv` or site-packages causing false positives: ensure `.venv` is excluded in `pyproject.toml` and in the editor settings.

---

## Day-of checklist (compact)

- [ ] Laptop & charger, backup battery, external cable if needed
- [ ] Pyenv + Python 3.13 installed & configured
- [ ] Poetry installed and configured for in-project virtualenv
- [ ] Git repo cloned, dependencies installed
- [ ] LangSmith account + API key set in `.env`
- [ ] Server started: `poetry run langgraph dev` (works, Studio loaded)
- [ ] Basic `poetry run poe check` & `poetry run poe test:unit` pass or are ready to iterate

---

If you'd like, I can:

- Add a pre-commit hook that checks `poe check` prior to a commit.
- Add a GitHub Actions workflow for running the checks in CI (on push/PR).
- Provide a short cutlist for saving your work and a basic Git workflow during the event.

Good luck, & have a great hackathon at Flinn! 🚀
