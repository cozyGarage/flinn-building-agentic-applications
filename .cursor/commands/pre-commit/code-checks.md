# Run Pre-Commit Checks

## Overview
Run the various pre-commit code checks to make sure the code meets the static code analysis check to be put up for PR.

## Steps
1. **Run Code Cleanup Command**
   - Execute code cleanup command with `poetry run poe clean`
   - Capture output and identify failures
   - If failures are present, fix code that causes errors
   - Repeat until all failures are fixed
2. **Run Code Integrity Checks Command**
   - Execute code cleanup command with `poetry run poe check`
   - Capture output and identify failures
   - If failures are present, fix code that causes errors
   - Repeat until all failures are fixed
3. **Run Unit Tests Command**
   - Execute code cleanup command with `poetry run poe test:unit`
   - Capture output and identify failures
   - If failures are present, fix code that causes errors
   - Repeat until all failures are fixed