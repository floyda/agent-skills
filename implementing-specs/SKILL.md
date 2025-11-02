---
name: implementing-specs
description: Implements Python features/fixes from spec-driven-dev artifacts (requirements.md, plan.md, tasks.md). Writes tests first, writes production code, runs type checking and quality gates, manages task status with review checkpoints. Use when implementing specs, or when user says implement/build/execute/code from these specification files.
---

# Spec Implementation

## Overview

This skill provides a structured implementation workflow for executing software specifications created by the spec-driven-dev skill. It follows the practices and standards expected from a principal-level Python software developer, including test-driven development (TDD), type safety, comprehensive testing, and rigorous quality gates.

The skill is designed to work with the three core artifacts produced by spec-driven-dev:
- **requirements.md**: Feature specification with requirements and success criteria
- **plan.md**: Implementation plan broken down into phases
- **tasks.md**: Dependency-ordered task list with identifiers (T001, T002, etc.)

## Skill Directory Location

**IMPORTANT**: This skill's scripts and references must be accessed using their absolute paths. When you invoke this skill:

1. Determine where this SKILL.md file is located (the agent knows the skill path when loading it)
2. The scripts are in `<skill-directory>/scripts/`
3. The references are in `<skill-directory>/references/`

Throughout this document, `<SKILL_DIR>` is used as a placeholder. Replace it with the actual path to this skill's directory before running any commands.

Common locations:
- Claude Code: `~/.claude/skills/implementing-specs/`
- Codex CLI: `~/.codex/skills/implementing-specs/`
- Custom: wherever the user has installed this skill

## When to Use This Skill

Use this skill when:
- The user requests implementation of a specification in `specs/features/` or `specs/defects/`
- The spec-driven-dev workflow has completed and produced all three required artifacts
- Implementation should follow principal-level engineering standards
- Code quality, type safety, and test coverage are critical requirements

Do not use this skill when:
- Spec artifacts are missing or incomplete (validate first with `scripts/validate_spec_artifacts.py`)
- Quick prototyping or exploratory coding is needed
- The user explicitly requests a different implementation approach

## Implementation Workflow

### Phase 1: Preparation and Validation

Before beginning implementation, validate that all prerequisites are in place.

#### 1.1 Locate Spec Directory

The user will specify the spec directory location. Common patterns:
- `specs/features/<feature-name>/`
- `specs/defects/<defect-name>/`

#### 1.2 Validate Spec Artifacts

Run the validation script to ensure all required files exist and are well-formed:

```bash
python <SKILL_DIR>/scripts/validate_spec_artifacts.py <spec-directory>
```

Expected output: ✅ confirmation that requirements.md, plan.md, and tasks.md are present and properly structured.

If validation fails, stop and report the issues to the user. Do not proceed with implementation until all artifacts are valid.

#### 1.3 Review the Spec Artifacts

Read all three artifacts thoroughly to understand:
- **requirements.md**: What is being built, requirements, success criteria
- **plan.md**: Implementation phases and their objectives
- **tasks.md**: Specific tasks to complete, dependencies, and order

Load `<SKILL_DIR>/references/python_best_practices.md` into context for guidance on coding standards.

#### 1.4 Confirm Understanding

Before proceeding, confirm with the user:
- Understanding of the feature/fix scope
- Which phases will be implemented (all phases or specific ones)
- Any special considerations or constraints

### Phase 2: Phase-by-Phase Implementation

Implementation proceeds one phase at a time, following the order defined in plan.md. For each phase:

#### 2.1 Announce Phase Start

Clearly communicate to the user:
- Which phase is starting (e.g., "Phase 1: Core Data Models")
- The phase objectives from plan.md
- Expected deliverables

#### 2.2 Identify Tasks for This Phase

Review tasks.md and identify all tasks belonging to the current phase. Tasks are typically grouped by phase in the tasks.md file.

#### 2.3 Implement Using TDD

For each task, follow test-driven development (see `<SKILL_DIR>/references/tdd_workflow.md` for detailed guidance):

1. **🔴 Red** - Write failing test
2. **🟢 Green** - Minimal code to pass
3. **🔵 Refactor** - Apply `<SKILL_DIR>/references/python_best_practices.md`: type hints, docstrings, clean code
4. **Update task status**:
   ```bash
   python <SKILL_DIR>/scripts/update_task_status.py <spec-directory>/tasks.md <task-id> completed
   ```

#### 2.4 Run Quality Gates After Each Task

After completing each task, run automated quality checks:

```bash
bash <SKILL_DIR>/scripts/check_quality_gates.sh
```

This script runs:
- Linting (ruff)
- Formatting (black, isort)
- Type checking (mypy --strict)
- Spell checking (codespell)
- Tests with coverage (pytest --cov)

**If any quality gate fails**, fix the issues immediately before proceeding to the next task. Never accumulate quality debt.

**Quality standards required:**
- Zero linting errors
- Zero type checking errors
- All tests passing
- Minimum 80% overall coverage, 90% for critical paths
- All formatting correct

#### 2.5 Phase Completion Review

When all tasks in a phase are complete, perform a comprehensive manual review using `<SKILL_DIR>/references/code_review_checklist.md`.

For each failing item:
1. Document the issue
2. Determine if it blocks phase completion
3. Fix blocking issues immediately
4. Create follow-up tasks for non-blocking items

#### 2.6 Manual Review Checkpoint - Stop for User Confirmation

**IMPORTANT**: After completing phase review, STOP and present findings to the user:
- Phase completion status and quality gates results
- Code review findings and issue resolution
- Test coverage statistics
- Tasks completed in this phase

**Request explicit user approval** before proceeding to the next phase. Do not proceed until the user approves.

### Phase 3: Integration and Final Verification

After all phases are complete and approved:

#### 3.1 Integration Testing

Run the full test suite including integration tests to verify all components work together:

```bash
pytest tests/
```

Ensure:
- All unit tests pass
- All integration tests pass
- No regressions introduced
- End-to-end workflows function correctly

#### 3.2 Final Quality Gates

Run quality gates one final time on the entire codebase:

```bash
bash <SKILL_DIR>/scripts/check_quality_gates.sh
```

All checks must pass with zero errors.

#### 3.3 Documentation Updates

Update all relevant documentation:
- README.md (if functionality changed)
- CHANGELOG.md (document changes)
- API documentation (if public API changed)
- Migration notes (if breaking changes introduced)

#### 3.4 Final Tasks.md Update

Ensure tasks.md reflects final status of all tasks:

```bash
python <SKILL_DIR>/scripts/update_task_status.py <spec-directory>/tasks.md
```

Review the output and verify all tasks are marked appropriately (completed, blocked, etc.).

#### 3.5 Implementation Summary

Provide a comprehensive summary:

**Deliverables:** What was implemented (reference requirements.md), phases completed, documentation updates

**Quality Metrics:** Test count, coverage percentages, type checking status, linting status

**Follow-up Actions:** Known limitations, future enhancements, technical debt (if any)

## Handling Blockers and Spec Issues

If during implementation a blocker is encountered or the spec is found to be underspecified:

1. **Stop implementation immediately**
2. **Document the issue**:
   - What was being implemented when the blocker was found
   - Nature of the blocker (missing requirement, ambiguous spec, technical limitation)
   - Impact on implementation progress
3. **Report to the user**:
   - Clearly explain the issue
   - Provide context about why it's a blocker
   - Suggest potential solutions if possible
   - Ask for clarification or decision
4. **Mark affected task as blocked**:
   ```bash
   python <SKILL_DIR>/scripts/update_task_status.py <spec-directory>/tasks.md <task-id> blocked
   ```
5. **Do not proceed** until the blocker is resolved

Never make assumptions or workarounds that deviate from the spec without explicit user approval.

## Key Principles

- **Type Safety**: Use `mypy --strict` (zero errors required). See `references/python_best_practices.md`
- **Test Coverage**: 80%+ overall, 90%+ critical paths. Every public function requires tests
- **Quality Gates**: Run after each task, not just phase end. Fix issues immediately
- **Clear Communication**: Surface blockers immediately, request clarification when needed

## Script Reference

This skill includes utility scripts located at `<SKILL_DIR>/scripts/`:

### check_quality_gates.sh

Runs all automated quality checks: linting (ruff), formatting (black, isort), type checking (mypy), spell checking (codespell), tests with coverage (pytest).

```bash
bash <SKILL_DIR>/scripts/check_quality_gates.sh

# Override default 80% coverage threshold
MIN_COVERAGE=90 bash <SKILL_DIR>/scripts/check_quality_gates.sh
```

### update_task_status.py

Updates task status in tasks.md file. Valid statuses: `pending`, `in_progress`, `completed`, `blocked`

```bash
# Update task
python <SKILL_DIR>/scripts/update_task_status.py specs/features/autocomplete/tasks.md T005 completed

# List all tasks
python <SKILL_DIR>/scripts/update_task_status.py specs/features/autocomplete/tasks.md
```

### validate_spec_artifacts.py

Validates spec directory contains all required files with proper structure (spec.md, plan.md, tasks.md with correct sections/format).

```bash
python <SKILL_DIR>/scripts/validate_spec_artifacts.py specs/features/autocomplete-improvements
```

## Reference Documents

Load these from `<SKILL_DIR>/references/` as needed:

- **python_best_practices.md**: Type safety, testing standards, SOLID principles, error handling, security. Load at implementation start and when questions arise about coding standards.

- **code_review_checklist.md**: Complete checklist covering automated checks, code quality, testing, error handling, security, documentation, performance, functionality. Load before phase completion review.

- **tdd_workflow.md**: Red-Green-Refactor cycle, test organization, AAA pattern, parametrized testing, mocking. Load when implementing tasks requiring new functionality.

## Summary

This skill ensures implementation follows the highest professional standards:
- ✅ TDD enforced throughout (write tests first)
- ✅ Type safety with mypy --strict (zero errors)
- ✅ Comprehensive testing (80%+ coverage)
- ✅ Quality gates after every task
- ✅ Manual review checkpoints between phases
- ✅ User approval required before proceeding
- ✅ Complete documentation
- ✅ No technical debt accumulation

By following this workflow, implementation will be production-ready, maintainable, well-tested, and thoroughly documented.
