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

**Good:**
> As a user, I want to receive email notifications when my password is changed so that I can immediately respond if the change was unauthorized.

**Bad (too vague):**
> As a user, I want notifications.

**Bad (too technical):**
> As a user, I want the system to call sendEmail() when password_hash is updated in the database.

### Requirements - Acceptance Criteria

**Good:**
> WHEN a user enters an invalid email format THEN the system SHALL display "Please enter a valid email address" below the input field and prevent form submission.

**Bad (not testable):**
> WHEN there's a problem THEN show an error.

**Bad (too implementation-focused):**
> WHEN regex doesn't match THEN throw ValidationException with error code 422.

### Plan - Strategy Descriptions

**Good:**
> Use JWT tokens stored in HTTP-only cookies for session management. Implement token refresh logic to extend sessions automatically. Add middleware to verify tokens on protected routes.

**Bad (too vague):**
> Add authentication.

**Bad (too detailed/code-focused):**
> Create AuthService class with generateToken(userId: string): string method that calls jwt.sign() with secret key from process.env.JWT_SECRET...

### Tasks - Granularity

**Good:**
> - [ ] Create User model with email, password_hash, and created_at fields

**Bad (too broad):**
> - [ ] Build authentication system

**Bad (too granular):**
> - [ ] Import bcrypt library
> - [ ] Add bcrypt to dependencies
> - [ ] Create hash function
> - [ ] Test hash function
> - [ ] Add salt rounds constant

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
