# Code Review Checklist

This checklist should be used at the end of each implementation phase before marking it complete. A principal-level developer ensures all items are verified before moving forward.

## Pre-Review: Automated Checks

Run all automated quality gates first (use `scripts/check_quality_gates.sh`):

- [ ] **Linting passes** (ruff check)
- [ ] **Formatting is correct** (black --check, isort --check)
- [ ] **Type checking passes** (mypy --strict with zero errors)
- [ ] **All tests pass** (pytest)
- [ ] **Coverage meets threshold** (≥80% overall, ≥90% for critical paths)
- [ ] **Spell checking passes** (codespell)

If any automated check fails, fix issues before proceeding with manual review.

## Code Quality

### Design & Architecture

- [ ] **Single Responsibility**: Each class/function has one clear purpose
- [ ] **DRY**: No unnecessary code duplication
- [ ] **Appropriate abstractions**: Code is neither over-engineered nor too concrete
- [ ] **Dependencies**: External dependencies are injected, not hardcoded
- [ ] **Separation of concerns**: Business logic separate from I/O, UI, infrastructure
- [ ] **SOLID principles**: Code follows SOLID where applicable

### Readability & Maintainability

- [ ] **Self-documenting**: Variable, function, class names clearly express intent
- [ ] **Consistent style**: Follows project conventions and PEP 8
- [ ] **Appropriate complexity**: No overly complex functions (cyclomatic complexity < 10)
- [ ] **No magic numbers**: Constants are named and explained
- [ ] **Clear control flow**: Easy to follow logic without excessive nesting
- [ ] **No commented-out code**: Dead code removed, not commented

### Type Safety

- [ ] **Complete type hints**: All function signatures have parameter and return type hints
- [ ] **Accurate types**: Type hints correctly represent actual types
- [ ] **No `Any` abuse**: `Any` used only when truly necessary
- [ ] **Generic types**: Use of `TypeVar`, `Generic` where appropriate
- [ ] **Mypy strict compliance**: Code passes `mypy --strict` with zero errors

## Testing

### Test Coverage

- [ ] **Coverage threshold met**: Meets or exceeds minimum coverage requirements
- [ ] **Critical paths covered**: All important code paths have tests
- [ ] **Public API tested**: Every public function/method has tests
- [ ] **No untested code**: All new code is tested (no coverage gaps)

### Test Quality

- [ ] **Tests are independent**: Tests don't depend on each other
- [ ] **Tests are deterministic**: Tests produce same results every run
- [ ] **Clear test names**: Test names describe what they test
- [ ] **AAA pattern**: Tests follow Arrange-Act-Assert structure
- [ ] **Happy & sad paths**: Both successful and error cases tested
- [ ] **Edge cases**: Boundary conditions and edge cases covered
- [ ] **Mocks used appropriately**: External dependencies are mocked

### Integration Testing

- [ ] **Integration tests present**: Tests verify components work together
- [ ] **Realistic scenarios**: Tests use realistic data and workflows
- [ ] **End-to-end coverage**: Critical user workflows tested end-to-end

## Error Handling

- [ ] **Specific exceptions**: Custom exceptions for domain errors
- [ ] **Input validation**: All inputs validated at API boundaries
- [ ] **Error messages**: Clear, actionable error messages
- [ ] **No silent failures**: All errors logged or raised
- [ ] **Resource cleanup**: Resources properly cleaned up (context managers, try/finally)
- [ ] **Partial failure handling**: Graceful handling of partial failures

## Security

- [ ] **No hardcoded secrets**: No API keys, passwords, tokens in code
- [ ] **Input sanitization**: External inputs validated and sanitized
- [ ] **SQL injection prevention**: Parameterized queries used
- [ ] **XSS prevention**: Output properly escaped/sanitized
- [ ] **Dependency vulnerabilities**: No known vulnerabilities in dependencies
- [ ] **Least privilege**: Code runs with minimal necessary permissions

## Documentation

- [ ] **Public API documented**: All public modules/classes/functions have docstrings
- [ ] **Docstring completeness**: Args, returns, raises, examples included
- [ ] **Complex logic explained**: Non-obvious code has explanatory comments
- [ ] **README updated**: If applicable, README reflects new functionality
- [ ] **CHANGELOG updated**: Changes documented in changelog
- [ ] **Migration notes**: Breaking changes documented with migration guide

## Performance

- [ ] **No obvious bottlenecks**: Code doesn't have glaring performance issues
- [ ] **Appropriate algorithms**: Using efficient algorithms for the task
- [ ] **Lazy evaluation**: Avoiding unnecessary computation
- [ ] **Resource management**: No memory leaks, files/connections closed properly
- [ ] **Database efficiency**: Queries are optimized (no N+1 queries)

## Functionality

- [ ] **Requirements met**: Implementation matches spec requirements
- [ ] **Success criteria satisfied**: All success criteria from spec are met
- [ ] **No scope creep**: Implementation doesn't add unplanned features
- [ ] **Backwards compatibility**: Existing functionality not broken (if applicable)
- [ ] **Edge cases handled**: Implementation handles edge cases gracefully

## Code Organization

- [ ] **Logical file structure**: Code organized in appropriate modules/packages
- [ ] **Import organization**: Imports sorted and organized (stdlib, third-party, local)
- [ ] **No circular dependencies**: Import structure is clean
- [ ] **Appropriate file size**: Files are not excessively long (< 500 lines ideal)

## Git Hygiene

- [ ] **Clean commits**: Commits are logical, focused units of work
- [ ] **Descriptive messages**: Commit messages explain why, not just what
- [ ] **No debug artifacts**: No debug prints, breakpoints, or temporary code
- [ ] **Files staged correctly**: Only relevant files included

## Phase-Specific Checks

### After Each Phase

- [ ] **Phase objectives met**: All goals for this phase achieved
- [ ] **Tests pass**: All tests for this phase pass
- [ ] **Phase documented**: Implementation notes added to phase section in plan.md
- [ ] **Tasks updated**: Relevant tasks marked complete in tasks.md

### Before Final Completion

- [ ] **All phases complete**: Every phase in plan.md is implemented
- [ ] **Integration verified**: All components work together correctly
- [ ] **Documentation complete**: All docs updated (README, API docs, etc.)
- [ ] **tasks.md finalized**: All tasks marked with final status
- [ ] **Clean workspace**: No uncommitted changes or temporary files

## Manual Review Actions

For each item that fails review:

1. **Document the issue**: Note what needs to be fixed
2. **Prioritize**: Determine if it's blocking or can be addressed later
3. **Fix immediately**: Address blocking issues before proceeding
4. **Create follow-up**: For non-blocking items, create follow-up tasks

## Sign-Off

Only mark a phase complete when:

- ✅ All automated checks pass
- ✅ All applicable manual checklist items are verified
- ✅ No blocking issues remain
- ✅ Code is production-ready (for that phase)

**Remember**: It's better to spend extra time on quality now than to accumulate technical debt that compounds over time.
