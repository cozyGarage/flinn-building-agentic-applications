## How to continue building the meal planner (step-by-step roadmap)

Below are recommended, incremental next steps and technical guidance to grow the project from an example to a robust, production-ready planner.

Essentials (MVP) — next 1–2 days

- Add a tool `recipes_api.py` that normalizes external recipes to the sample schema.
- Implement caching to avoid repeated calls during development (e.g., file-based or Redis).

Enhancements (feature parity, 2–7 days)

Observability & Cost Control (continuous)

---

## Tracing & Logging: approach and quick setup

Observability is essential for debugging agents. LangSmith is already recommended in Hackathon materials; implement it as follows:

1. Environment setup

   - Ensure `LANGSMITH_API_KEY` and `LANGSMITH_PROJECT` are configured in `.env` and set in CI secrets.

2. Model & Agent instrumentation

   - Attach LangSmith tracer to the chat model or agent if the SDK supports it, or call tracer on agent start/stop.
   - Example flow: Add the tracer to your chat model init or instrument each tool to emit trace events (start, success, failure).

3. Structured logging

   - Use the standard `logging` module and configure JSON formatting (for ingestion by log aggregation systems).
   - Log events at these moments: tool start, tool completed, agent decision to call a tool, user request, final answer, error.
   - Example (skeleton):

     ```python
     import logging
     from pythonjsonlogger import jsonlogger

     logger = logging.getLogger("flinn")
     handler = logging.StreamHandler()
     handler.setFormatter(jsonlogger.JsonFormatter())
     logger.addHandler(handler)
     logger.setLevel(logging.INFO)

     logger.info("tool.start", extra={"tool":"get_recipes", "params": {"meal_type":"dinner"}})
     ```

4. Instrument tool calls

   - Annotate each tool's entry and exit with trace / logging metadata (IDs, elapsed time, result size) so you can debug the agent flow and see the LLM decisions.

   ***

   ## Token & Cost control: practical tips

   Monitoring tokens and enforcing quotas is important to avoid run-away costs. The core approach includes using token estimation, limiting tokens, choosing cheaper models, and implementing rate-limits.

   1. Token estimation (prep)

      - Use `tiktoken` or `langchain`'s token utilities to estimate tokens for prompts and responses.
      - Add a utility: `src/common/token_utils.py` with `estimate_prompt_tokens` & `estimate_response_tokens` to compute approximate cost.

   2. Enforce `max_tokens` & model selection

      - Use a `max_tokens` cap in model init or when calling LLM; choose a cheaper model for non-critical operations.
      - Add configuration flags for budget thresholds (e.g., `MAX_TOKEN_BUDGET_PER_SESSION`) to be enforced in middleware.

   3. Rate limiting and per-user quotas

      - Use `aiolimiter` or `ratelimit` (sync) to limit LLM calls per second globally and per-user.
      - Keep a per-session counter for token usage and reject (or compress) work when the limit is reached.

   4. Fallback strategies to reduce tokens

      - Summarize long context, return brief answers, or switch to a cheaper model when budget is low.
      - Prompt engineering: keep instructions succinct and avoid extremely long example contexts.

   5. Alerts and reporting
      - Use tracing info and logs to compute hourly/daily token cost and set up alerts for budget spikes.

   ***

   ## Developer checklist (for the next iteration)

   - [ ] Integrate a recipe API + normalization + caching
   - [ ] Add a nutrition estimator tool (per-serving macros)
   - [ ] Implement allergen substitution logic & tests
   - [ ] Build a FastAPI or Streamlit UI to quickly interact with the agent
   - [ ] Add LangSmith tracing to agent + tool calls and provide examples in the repo
   - [ ] Add structured JSON logs and basic Prometheus metrics (fastapi_prometheus)
   - [ ] Implement token & cost tracking middleware + per-user quotas and alerting
   - [ ] Add integration tests & mock out LLM calls for reliability in CI
   - [ ] Add detailed README with deploy instructions & GitHub Actions CI templates

   ***

   If you want, I can start implementing the next high-priority item now — recommend adding LangSmith tracing and structured logging first so we can capture early observability. Tell me which feature you'd like to add next and I'll produce a PR with initial code + tests.
 
   ---

   ## LangSmith (LangChain Studio) usage & quick guide

   To view traces emitted by the agent using LangSmith / LangChain Studio, follow these steps:

   1) Create and configure LangSmith API keys:

   ```bash
   # Add to your .env file (do not commit)
   LANGSMITH_API_KEY="your_langsmith_api_key"
   LANGSMITH_PROJECT="flinn-makers-day-meal-planner"
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"  # optional - match your region
   ```

   2) Start the local demo or agent while LangSmith env is set:

   ```bash
   poetry run python -m src.my_agent.agents.demo
   # or run the LangGraph dev server for Studio integration:
   poetry run langgraph dev
   ```

   3) View traces in LangChain Studio / LangSmith:
      - Visit `https://studio.langchain.com` or your configured region "Studio" URL.
      - Login and open your `LANGSMITH_PROJECT` or click the Traces section.
      - Trigger agent actions (get_recipes, suggest_meal_plan, generate_shopping_list) and you should see new traces (or view local `traces.log`).

   4) Local trace file
      - A local compact trace is also written to `traces.log` in the repository root — useful to debug without external dependencies:

   ```bash
   tail -n 50 traces.log
   cat traces.log | jq .
   ```

   5) Filtering traces
      - In LangChain Studio, filter traces by agent name, tool name, or by custom metadata fields (tool name, user id, event types).
      - Use `project` or tags to keep project traces separated.

   Notes
      - The repository sets up a local `tracer` that writes both to `traces.log` and will attempt to call LangSmith tracer if the `langsmith` SDK is available and configured. This helps during development for easy offline debug.

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

---

## What we implemented (progress summary)

We made the following changes and additions to the repository to prepare the meal-planner agent and developer environment:

- Enforced per-project Python (`.python-version` set to `3.13.10`) and `pyenv` guidance.
- Configured Poetry to create in-project virtualenvs and added `pre-commit` as a dev dependency.
- Added pre-commit configuration to run `poe clean` and `poe check` and narrowed `poe` tool scans to `src/` and `test/` to avoid scanning `.venv`.
- Created a minimal meal-planner feature set:

  - `src/my_agent/data/sample_recipes.py` (seed recipes)
  - `src/my_agent/tools/get_recipes.py` — recipe lookup by type/tags/calories
  - `src/my_agent/tools/suggest_meal_plan.py` — simple N-day meal plan generator
  - `src/my_agent/tools/generate_shopping_list.py` — ingredient consolidation and scaling
  - `src/my_agent/agents/demo.py` — a runnable demo showcasing the tools
  - Tests for these tools (`test/unit/test_meal_tools.py`) and a demo-runner for quick validation

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
