# Python Best Practices for Principal-Level Development

This reference guide outlines the coding standards and best practices expected from a principal Python software developer during implementation.

## Type Safety

### Comprehensive Type Hints

- **All function signatures** must include complete type hints for parameters and return values
- Use `typing` module types for complex structures: `List`, `Dict`, `Optional`, `Union`, `Callable`, etc.
- Prefer `typing` protocols and `TypedDict` for structural typing
- Use `Generic` and `TypeVar` for generic implementations

```python
from typing import List, Optional, Dict, TypeVar, Protocol

T = TypeVar('T')

def process_items(items: List[T], filter_fn: Callable[[T], bool]) -> List[T]:
    """Process items with type-safe filtering."""
    return [item for item in items if filter_fn(item)]
```

### Type Checking

- All code must pass `mypy --strict` with zero errors
- Configure mypy in `pyproject.toml` or `mypy.ini`
- Use `# type: ignore` sparingly and only with explanatory comments

## Testing Standards

### Test Coverage

- **Minimum coverage**: 80% overall, 90% for critical paths
- Every public function/method requires tests
- Test both happy paths and error cases

### Test Organization

```python
# tests/unit/test_module.py
def test_function_happy_path():
    """Test normal operation with valid inputs."""
    pass

def test_function_edge_cases():
    """Test boundary conditions and edge cases."""
    pass

def test_function_error_handling():
    """Test error conditions and exception handling."""
    pass
```

### Testing Patterns

- **Arrange-Act-Assert** (AAA) pattern for clarity
- Use **fixtures** for common test setup (pytest fixtures)
- Use **parametrize** for testing multiple inputs
- Mock external dependencies with `unittest.mock` or `pytest-mock`

```python
import pytest
from unittest.mock import Mock

@pytest.fixture
def sample_data():
    return {"key": "value"}

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert double(input) == expected
```

### Test-Driven Development (TDD)

1. **Write test first** - Define expected behavior
2. **Watch it fail** - Ensure test is valid
3. **Write minimal code** - Make test pass
4. **Refactor** - Improve code while keeping tests green
5. **Repeat** - Build incrementally

## Code Quality

### SOLID Principles

1. **Single Responsibility**: Each class/function does one thing well
2. **Open/Closed**: Open for extension, closed for modification
3. **Liskov Substitution**: Subtypes must be substitutable for base types
4. **Interface Segregation**: Many specific interfaces over one general
5. **Dependency Inversion**: Depend on abstractions, not concretions

### Clean Code Practices

- **Meaningful names**: Variables, functions, classes should reveal intent
- **Small functions**: Functions should do one thing (< 20 lines ideal)
- **DRY principle**: Don't Repeat Yourself
- **Comments explain "why"**, not "what" (code should be self-documenting)
- **Error handling**: Use exceptions appropriately, never silent failures

```python
# Good: Clear intent, single responsibility
def calculate_total_price(items: List[Item], discount: Decimal) -> Decimal:
    """Calculate total price after applying discount."""
    subtotal = sum(item.price * item.quantity for item in items)
    return subtotal * (1 - discount)

# Bad: Unclear, multiple responsibilities
def calc(x, y):
    t = 0
    for i in x:
        t += i[0] * i[1]
    return t * (1 - y)
```

### Pythonic Code

- Use **list/dict comprehensions** where readable
- Use **context managers** (`with` statements) for resource management
- Use **generators** for large data processing
- Prefer **dataclasses** or **attrs** for data structures
- Use **pathlib** for file path operations
- Follow **PEP 8** style guide

```python
from pathlib import Path
from dataclasses import dataclass
from typing import Iterator

@dataclass
class Config:
    """Application configuration."""
    host: str
    port: int
    debug: bool = False

def read_large_file(path: Path) -> Iterator[str]:
    """Read file line by line without loading into memory."""
    with path.open('r') as f:
        for line in f:
            yield line.strip()
```

## Error Handling

### Exception Patterns

- **Specific exceptions**: Create custom exception classes
- **Fail fast**: Validate inputs early
- **Don't catch everything**: Catch specific exceptions you can handle
- **Log before re-raising**: Preserve stack traces

```python
class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

def validate_input(data: Dict[str, Any]) -> None:
    """Validate input data, raising ValidationError if invalid."""
    if not data.get("required_field"):
        raise ValidationError("Missing required_field")
```

### Defensive Programming

- Validate inputs at API boundaries
- Use assertions for internal invariants
- Provide clear error messages
- Handle partial failures gracefully

## Documentation

### Docstrings

- All public modules, classes, functions need docstrings
- Use **Google style** or **NumPy style** consistently
- Include parameter types, return types, raised exceptions
- Provide examples for complex functions

```python
def query_dataset(
    path: Path,
    filters: Dict[str, Any],
    limit: int = 100
) -> List[Record]:
    """
    Query dataset with filters and return matching records.

    Args:
        path: Path to the dataset directory
        filters: Dictionary of field:value filters to apply
        limit: Maximum number of records to return (default: 100)

    Returns:
        List of records matching the filters

    Raises:
        DatasetNotFoundError: If dataset path does not exist
        ValidationError: If filters are invalid

    Example:
        >>> records = query_dataset(
        ...     Path("/data/logs"),
        ...     {"level": "error", "component": "auth"},
        ...     limit=50
        ... )
    """
    pass
```

## Dependency Management

- Pin dependencies with version constraints
- Use virtual environments (venv, hatch, poetry)
- Separate dev/test dependencies from runtime
- Keep dependencies minimal and up-to-date

## Performance Considerations

- **Profile before optimizing**: Use `cProfile`, `line_profiler`
- **Lazy evaluation**: Don't compute what you don't need
- **Appropriate data structures**: dict for lookups, set for membership, list for sequences
- **Avoid premature optimization**: Clarity first, optimize later with data

## Security

- **Never hardcode secrets**: Use environment variables or secret managers
- **Validate all inputs**: Especially from external sources
- **Use parameterized queries**: Prevent SQL injection
- **Sanitize output**: Prevent XSS and injection attacks
- **Keep dependencies updated**: Monitor for security vulnerabilities

## Code Review Readiness

Before marking any phase complete, ensure:

1. ✅ All tests pass
2. ✅ Type checking passes (mypy --strict)
3. ✅ Linting passes (ruff)
4. ✅ Formatting is correct (black, isort)
5. ✅ Test coverage meets minimum threshold
6. ✅ No security vulnerabilities introduced
7. ✅ Documentation is complete
8. ✅ Code is self-documenting with clear names
9. ✅ No debug code or commented-out code
10. ✅ Error handling is comprehensive
