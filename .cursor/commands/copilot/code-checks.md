# Copilot Pre-Commit / Dev Checks

This file mirrors `.cursor/commands/pre-commit/code-checks.md` but provides a format tailored for interactive assistant tools like GitHub Copilot, ChatGPT, or Cursor Copilot when run locally.

## Overview
Use these commands to run cleanup, static analysis, and unit tests during development. Copilot-style instructions below provide short advice and expected results.

## Steps (Copilot-friendly)
1. Run the cleanup (auto-fix / format) step

```bash
# Format code and pre-install types
poetry run poe clean
```

- Expect: Black formatting and mypy install types pass.
- If it fails: fix formatting issues or unsatisfied type problems, and re-run.

2. Run the static integrity checks

```bash
poetry run poe check
```

- Expect: flake8 and mypy validations to pass.
- If it fails: address flake8 or mypy errors as shown in the output.

3. Run unit tests

```bash
poetry run poe test:unit
```

- Expect: Unit tests pass or report failures with reasons.
- If it fails: fix failing tests and re-run.

4. Optional: Run integration tests

```bash
poetry run poe test:integration
```

- Expect: Integration tests pass; useful for PR validation.

## Copilot Tips
- If you want Copilot to auto-suggest fixes, use the suggestions with caution; cross-check tests and lints.
- Use the output from `poetry run poe check` to seed prompts for Copilot to generate patches.
