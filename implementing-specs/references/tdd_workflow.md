# Test-Driven Development (TDD) Workflow

This guide outlines the TDD workflow expected from a principal-level Python developer. TDD is not just about testing—it's a design discipline that leads to better code architecture, clearer requirements understanding, and higher confidence in changes.

## The Red-Green-Refactor Cycle

TDD follows a simple three-step cycle:

```
🔴 RED → 🟢 GREEN → 🔵 REFACTOR → 🔴 RED → ...
```

### 🔴 Red: Write a Failing Test

1. **Understand the requirement**: Know exactly what behavior you're implementing
2. **Write the test first**: Define the expected behavior before writing implementation
3. **Run the test**: Verify it fails for the right reason
4. **Keep it focused**: Test one thing at a time

**Why write the test first?**
- Ensures the test actually tests something (no false positives)
- Forces you to think about the interface before implementation
- Clarifies requirements and edge cases upfront
- Makes you write testable code from the start

### 🟢 Green: Make It Pass

1. **Write minimal code**: Just enough to make the test pass
2. **Don't over-engineer**: Resist the urge to add extra features
3. **Accept ugly code temporarily**: Perfection comes in refactoring
4. **Run the test**: Verify it passes

**Why minimal code?**
- Prevents scope creep and gold-plating
- Keeps you focused on the requirement at hand
- Faster iteration cycles
- Easier to refactor later

### 🔵 Refactor: Improve the Code

1. **Keep tests passing**: Run tests after each small change
2. **Improve design**: Extract functions, remove duplication, clarify names
3. **Maintain behavior**: Tests should still pass after refactoring
4. **Apply best practices**: Type hints, documentation, clean code principles

**Why refactor?**
- Pays down technical debt immediately
- Improves maintainability without fear of breaking things
- Tests give confidence that behavior is preserved
- Results in cleaner, more maintainable code

## TDD in Practice: Step-by-Step

### Example: Implementing a Query Parser

**Requirement**: Parse query string `"level:error since:7d"` into a structured Query object.

#### Step 1: Write the Test (RED)

```python
# tests/unit/test_query_parser.py
import pytest
from tern_tui.models.query import Query
from tern_tui.parsers.query_parser import parse_query

def test_parse_simple_level_filter():
    """Test parsing a simple level filter."""
    # Arrange
    query_string = "level:error"

    # Act
    result = parse_query(query_string)

    # Assert
    assert isinstance(result, Query)
    assert result.filters == {"level": "error"}
```

**Run the test**: It fails (module doesn't exist yet). ✅ Expected failure.

#### Step 2: Make It Pass (GREEN)

```python
# src/tern_tui/parsers/query_parser.py
from tern_tui.models.query import Query

def parse_query(query_string: str) -> Query:
    """Parse query string into Query object."""
    # Minimal implementation to pass the test
    parts = query_string.split(":")
    return Query(filters={parts[0]: parts[1]})
```

```python
# src/tern_tui/models/query.py
from dataclasses import dataclass
from typing import Dict

@dataclass
class Query:
    filters: Dict[str, str]
```

**Run the test**: It passes. ✅ Green!

#### Step 3: Refactor (BLUE)

At this point, the code is minimal and works. Add type hints, docstrings:

```python
from typing import Dict
from tern_tui.models.query import Query

def parse_query(query_string: str) -> Query:
    """
    Parse query string into Query object.

    Args:
        query_string: Query string in format "field:value"

    Returns:
        Parsed Query object

    Example:
        >>> query = parse_query("level:error")
        >>> query.filters
        {"level": "error"}
    """
    parts = query_string.split(":")
    field, value = parts[0], parts[1]
    return Query(filters={field: value})
```

**Run tests**: Still passing. ✅ Green!

#### Step 4: Next Test (RED again)

Now add complexity incrementally:

```python
def test_parse_multiple_filters():
    """Test parsing multiple space-separated filters."""
    query_string = "level:error component:auth"

    result = parse_query(query_string)

    assert result.filters == {
        "level": "error",
        "component": "auth"
    }
```

**Run the test**: Fails (doesn't handle multiple filters). ✅ Expected!

**Make it pass**, then **refactor**. Repeat.

## TDD Best Practices

### Test Organization

```python
# Good: Organized by feature/module
tests/
├── unit/
│   ├── test_query_parser.py
│   ├── test_query_model.py
│   └── test_query_controller.py
├── integration/
│   └── test_query_flow.py
└── fixtures/
    └── sample_queries.py
```

### Test Naming

Use descriptive test names that explain what they test:

```python
# Good: Clear, descriptive names
def test_parse_query_with_level_filter():
def test_parse_query_with_multiple_filters():
def test_parse_query_raises_error_on_invalid_syntax():

# Bad: Vague names
def test_parse_1():
def test_parse_2():
def test_error():
```

### AAA Pattern (Arrange-Act-Assert)

Every test should follow this structure:

```python
def test_something():
    # Arrange: Set up test data and conditions
    input_data = "level:error"
    expected_output = {"level": "error"}

    # Act: Execute the code under test
    result = parse_query(input_data)

    # Assert: Verify the result
    assert result.filters == expected_output
```

### Test One Thing

Each test should verify one specific behavior:

```python
# Good: Tests one behavior
def test_parse_level_filter():
    result = parse_query("level:error")
    assert result.filters["level"] == "error"

def test_parse_component_filter():
    result = parse_query("component:auth")
    assert result.filters["component"] == "auth"

# Bad: Tests multiple behaviors
def test_parse_everything():
    result1 = parse_query("level:error")
    result2 = parse_query("component:auth")
    result3 = parse_query("message:foo")
    assert result1.filters["level"] == "error"
    assert result2.filters["component"] == "auth"
    assert result3.filters["message"] == "foo"
```

### Use Parametrize for Similar Tests

```python
@pytest.mark.parametrize("input,expected_field,expected_value", [
    ("level:error", "level", "error"),
    ("level:warning", "level", "warning"),
    ("component:auth", "component", "auth"),
    ("component:database", "component", "database"),
])
def test_parse_single_filter(input, expected_field, expected_value):
    result = parse_query(input)
    assert result.filters[expected_field] == expected_value
```

### Mock External Dependencies

```python
from unittest.mock import Mock, patch

def test_query_execution_calls_database():
    # Arrange
    mock_db = Mock()
    mock_db.execute.return_value = [{"id": 1, "level": "error"}]

    # Act
    with patch('tern_tui.adapters.query_adapter.get_database', return_value=mock_db):
        result = execute_query(Query(filters={"level": "error"}))

    # Assert
    mock_db.execute.assert_called_once()
    assert len(result) == 1
```

## TDD Anti-Patterns to Avoid

### ❌ Writing Tests After Implementation

**Problem**: Tests may miss edge cases, may not fail when they should, may test implementation details rather than behavior.

**Solution**: Always write the test first.

### ❌ Testing Implementation Details

```python
# Bad: Tests internal implementation
def test_parser_uses_regex():
    parser = QueryParser()
    assert parser._regex_pattern == r'(\w+):(\w+)'

# Good: Tests behavior
def test_parser_extracts_field_and_value():
    result = parse_query("level:error")
    assert result.filters["level"] == "error"
```

### ❌ Overly Complex Tests

```python
# Bad: Test is more complex than the code it tests
def test_complex():
    data = generate_test_data()
    transformed = [transform(x) for x in data if x.valid]
    expected = [compute_expected(x) for x in transformed]
    result = process(data)
    assert result == expected

# Good: Simple, clear test
def test_process_filters_invalid_items():
    data = [Item(valid=True), Item(valid=False)]
    result = process(data)
    assert len(result) == 1
    assert result[0].valid is True
```

### ❌ Not Running Tests Frequently

**Problem**: Long gaps between test runs lead to uncertainty about which change broke what.

**Solution**: Run tests after every small change (use watch mode: `pytest-watch`).

### ❌ Skipping Refactoring

**Problem**: Tests pass, but code quality degrades over time (technical debt).

**Solution**: Always refactor after getting to green. Never skip the refactor step.

## TDD Integration with Phase-Based Implementation

When implementing phases from `plan.md`:

1. **Read the phase description**: Understand what needs to be built
2. **Break down into testable units**: Identify the smallest testable behaviors
3. **For each unit**:
   - 🔴 Write a failing test
   - 🟢 Implement just enough to pass
   - 🔵 Refactor and improve
4. **Verify phase completion**: All tests for the phase pass
5. **Run full test suite**: Ensure no regressions
6. **Mark phase complete**: Update tasks.md

## TDD Checklist

Before marking a phase complete, verify:

- [ ] All functionality has tests written first (TDD)
- [ ] Every test started red (failing) before going green
- [ ] Code has been refactored for clarity and maintainability
- [ ] Tests cover happy paths, edge cases, and error conditions
- [ ] Tests are independent and deterministic
- [ ] Test names clearly describe what they test
- [ ] No tests are skipped or marked xfail without good reason
- [ ] All tests pass consistently
- [ ] Coverage meets or exceeds threshold

## Resources for Deeper Learning

- **Test-Driven Development by Example** by Kent Beck
- **Growing Object-Oriented Software, Guided by Tests** by Freeman & Pryce
- **Python Testing with pytest** by Brian Okken

## Remember

> "The act of writing a unit test is more an act of design than of verification. It is also more an act of documentation than of verification. The act of writing a unit test closes a remarkable number of feedback loops, the least of which is the one pertaining to verification of function."
>
> — Robert C. Martin (Uncle Bob)

TDD is not about testing. It's about designing better software through rapid feedback loops.
