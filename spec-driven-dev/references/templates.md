# Document Templates

Use these templates when creating requirements.md, plan.md, and tasks.md files.

## requirements.md Template

```markdown
# Requirements: [Feature/Defect Name]

## Overview
[2-3 sentence summary explaining what this addresses and why it matters]

## Requirements

### 1. [First Requirement Title]

**User Story**
> As a [user type/role], I want [specific goal] so that [clear benefit or reason]

**Acceptance Criteria**
> WHEN [specific condition or user action] THEN the system SHALL [expected behavior with measurable outcome]
> WHEN [edge case or error condition] THEN the system SHALL [error handling or validation behavior]
> WHEN [another relevant scenario] THEN the system SHALL [expected response]

### 2. [Second Requirement Title]

**User Story**
> As a [user type/role], I want [specific goal] so that [clear benefit or reason]

**Acceptance Criteria**
> WHEN [specific condition] THEN the system SHALL [expected behavior]
> WHEN [edge case] THEN the system SHALL [error handling]

[Continue numbering for additional requirements...]
```

## plan.md Template

```markdown
# Implementation Plan: [Feature/Defect Name]

## Goal
[1-2 sentences describing the primary objective and expected outcome]

## Approach

### Phase 1: [Foundation/Setup/Core Feature Name]
**Priority**: High
**Requirements**: #1, #2 from requirements.md
**Strategy**: [Describe the technical approach, key decisions, and implementation method]
**Risks**: [Identify potential blockers, uncertainties, or technical challenges]

### Phase 2: [Enhancement/Integration/Next Feature Name]
**Priority**: Medium
**Requirements**: #3, #4 from requirements.md
**Strategy**: [Describe approach building on Phase 1]
**Risks**: [Note dependencies on Phase 1 and potential issues]

### Phase 3: [Polish/Testing/Advanced Features]
**Priority**: Low
**Requirements**: #5 from requirements.md
**Strategy**: [Describe final implementation steps]
**Risks**: [Minimal at this stage, focus on quality assurance]

## Dependencies
- [External libraries or packages needed]
- [APIs or services required]
- [Other project components this depends on]

## Technical Considerations
- **Architecture**: [Key architectural decisions and patterns]
- **Data Model**: [Database or data structure changes needed]
- **Performance**: [Any performance considerations or optimizations]
- **Security**: [Authentication, authorization, data protection needs]
- **Testing**: [Testing strategy and coverage approach]
```

## tasks.md Template

```markdown
# Tasks: [Feature/Defect Name]

## Phase 1: [Phase Name from plan.md]
**Plan Reference**: See Phase 1 in plan.md
**Requirements**: #1, #2 from requirements.md

- [ ] Create [specific component/module/file] with [key functionality]
- [ ] Implement [specific method/function] to handle [use case]
- [ ] Add [validation/error handling] for [edge case scenario]
- [ ] Write [unit/integration] tests for [component] covering [scenarios]
- [ ] Update [documentation/README] to reflect [changes]

## Phase 2: [Phase Name from plan.md]
**Plan Reference**: See Phase 2 in plan.md
**Requirements**: #3, #4 from requirements.md

- [ ] Integrate [component A] with [component B] via [interface/API]
- [ ] Configure [service/library] with [specific settings]
- [ ] Implement [feature] following [pattern/approach]
- [ ] Add [logging/monitoring] for [operations]
- [ ] Test [integration scenario] with [test data]

## Phase 3: [Phase Name from plan.md]
**Plan Reference**: See Phase 3 in plan.md
**Requirements**: #5 from requirements.md

- [ ] Optimize [component] for [performance metric]
- [ ] Refactor [code section] to improve [quality aspect]
- [ ] Add [UI polish/error messages/user feedback]
- [ ] Conduct [end-to-end/performance] testing
- [ ] Document [usage examples/API reference]
```

## Good vs Bad Examples

### Requirements - User Stories

**Good (CLI app):**
> As a developer, I want to filter log entries by severity level so that I can focus on errors and warnings during debugging.

**Good (Python library):**
> As a library user, I want to deserialize JSON data with automatic type validation so that I catch schema errors early.

**Good (Data tool):**
> As an analyst, I want to transform CSV data with a declarative pipeline so that I can reuse transformations across projects.

**Bad (too vague):**
> As a user, I want better filtering.

**Bad (too technical):**
> As a CLI, I want the system to call the filter_by_level() function with severity='ERROR'.

### Requirements - Acceptance Criteria

**Good (CLI/TUI):**
> WHEN a user presses `/` in the query window THEN the system SHALL open an interactive search prompt and highlight matching entries as they type.

**Good (Library):**
> WHEN invalid data is passed to the deserializer THEN the system SHALL raise ValidationError with a message describing which fields failed and why.

**Good (Data tool):**
> WHEN a transformation step fails THEN the system SHALL log the error with source row number and halt with clear exit code.

**Bad (not testable):**
> WHEN there's a problem THEN show an error.

**Bad (too implementation-focused):**
> WHEN user input fails regex THEN raise ValueError with code 422.

### Plan - Strategy Descriptions

**Good (Python library):**
> Build a type-safe validation layer using Pydantic, then implement deserialization methods that leverage these validators. Add comprehensive error messages with field paths. Include optional type coercion for common patterns.

**Good (CLI app):**
> Implement a query parser that builds AST structures, then create filter engines for different data sources. Start with in-memory filtering, add streaming support later.

**Bad (too vague):**
> Add validation.

**Bad (too detailed/code-focused):**
> Create ValidationService class with validate(data: dict) -> dict method that calls pydantic.BaseModel.model_validate()...

### Tasks - Granularity

**Good (Python library):**
> - [ ] Create TypedDict schemas for API response validation with required/optional fields

**Good (CLI app):**
> - [ ] Implement search highlighting in the log viewer with keyword matching

**Bad (too broad):**
> - [ ] Build validation system

**Bad (too granular):**
> - [ ] Import pydantic
> - [ ] Add pydantic to requirements.txt
> - [ ] Create BaseModel class
> - [ ] Test BaseModel
> - [ ] Add to __init__.py

## Tips for Each Document Type

### requirements.md
- Focus on WHAT the system should do, not HOW
- User stories explain the "why" behind each requirement
- Acceptance criteria must be specific, testable, and measurable
- Cover happy path, edge cases, and error conditions
- Group related requirements together

### plan.md
- Bridge between requirements and implementation
- Link each phase explicitly to requirement numbers
- Identify risks and dependencies early
- Stay at strategic level - save tactical details for tasks
- Use priorities to guide execution order

### tasks.md
- Each task should be completable in one focused work session
- Tasks should be ordered logically for execution
- Link back to both plan phases and requirements
- Use checkboxes for tracking progress
- Balance between actionable and not too granular
