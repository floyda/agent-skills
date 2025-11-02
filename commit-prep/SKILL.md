---
name: commit-prep
description: This skill should be used when Claude needs to prepare local repository changes for committing by running pre-commit hooks, project linters, full tests, and drafting a concise commit message.
---

## Purpose

Ensure local changes are commit-ready by validating formatting, linting, tests, and documenting the work in a clear commit message.

## Prerequisites

- Confirm `pre-commit` is installed (`pre-commit --version`) and the repo contains a `.pre-commit-config.yaml`.
- Ensure project-specific tooling (linters, package managers, test runners) is installed via the repository’s setup instructions.

## Workflow

- Review the working tree
  - Run `git status --short` to inspect modified, staged, and untracked files.
  - Clean up noise (remove debug files, revert accidental edits, add essential new files).
- Run pre-commit hooks
  - Install hooks if needed: `pre-commit install`.
  - Execute over the full tree: `pre-commit run --all-files`.
  - Re-run until hooks succeed; commit any automatic fixes before continuing.
- Execute linting
  - Discover lint commands from project metadata (`package.json` scripts, `pyproject.toml`, `Makefile`, etc.).
  - Run each lint target relevant to the touched code (`npm run lint`, `pnpm lint`, `make lint`, `ruff check .`, etc.).
  - Address reported issues or document intentional deviations.
- Run the test suite
  - Identify the primary test command (`pytest`, `npm test`, `go test ./...`, etc.).
  - Execute targeted tests first if the suite is large, then run the canonical full suite before committing.
  - Investigate flaky failures; re-run to confirm the baseline is passing.
- Finalize the diff
  - Review changes with `git diff` (unstaged) and `git diff --cached` (staged).
  - Ensure only intentional edits remain; stage updates via `git add`.

## Commit Message

- Summarize the change in the subject line (≤72 characters, imperative mood).
- Capture key behaviors, fixes, or outcomes in a short body when necessary.
- Reference issues or tickets succinctly when relevant.
- Verify the message reflects the staged diff by cross-checking `git status`.

## Final Gate

- Confirm all checks are green: pre-commit, linting, and tests.
- Ensure the working tree is clean (`git status` shows nothing to commit).
- Proceed with `git commit` once the staged diff and message are finalized.
