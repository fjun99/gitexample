# Task: Initialize Project Structure

**Status**: In Progress
**Assignee**: AI Agent
**Branch**: `feat/init-project`

## 1. Goal
Initialize the Python project structure using `uv` generated files and ensure they are properly tracked in git.

## 2. Scope
- **Include**:
    - `pyproject.toml`
    - `main.py`
    - `.gitignore`
    - `.python-version`
    - `uv.lock`
- **Exclude**:
    - `.venv` (should be ignored)

## 3. Acceptance Criteria
- [ ] All project files are tracked by git.
- [ ] `uv run main.py` executes successfully.
- [ ] `.gitignore` correctly prevents `.venv` from being committed.

## 4. Risks & Rollback
- **Risk**: Low. Initial commit.
- **Rollback**: `git checkout main` and delete the feature branch.
