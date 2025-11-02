# Workflow Execution Guide

This reference provides detailed guidance on executing the spec-driven development workflow effectively.

## When to Use This Workflow

### Ideal Scenarios
- **New features** in expanding projects that need structured planning
- **Bug fixes** that require understanding of requirements and impact
- **Refactoring** where changes need to be tracked and verified
- **Technical debt** items that need scoping and breakdown
- **Complex changes** spanning multiple files or systems

### Not Ideal For
- **Trivial fixes** (typos, obvious bugs with clear solutions)
- **Exploratory work** where requirements are still being discovered
- **Emergency hotfixes** requiring immediate action
- **Prototyping** where speed matters more than documentation

## Investigation Phase Deep Dive

### Questions to Ask Users

**For Features:**
- What problem does this solve for users?
- Who will use this feature?
- What's the expected behavior in different scenarios?
- Are there similar features elsewhere in the codebase?
- What's the success criteria?

**For Defects:**
- What's the current behavior vs expected behavior?
- When does this occur? Can you reproduce it?
- What's the impact on users?
- Are there workarounds currently in use?
- When did this start happening?

### Codebase Investigation Checklist

1. **Documentation First**
   - Read `README.md` for architecture overview
   - Check `docs/` folder for design docs
   - Look for ADRs (Architecture Decision Records)
   - Find existing specs in `specs/` folder

2. **Code Exploration**
   - Identify relevant modules/components
   - Understand data flow and dependencies
   - Note existing patterns and conventions
   - Find similar implementations to reference

3. **Environment Understanding**
   - What's the tech stack?
   - What are the testing patterns?
   - What's the deployment process?
   - What are the coding standards?

## Analysis Phase Patterns

### Gap Analysis Structure

```markdown
## Current State
- [What exists today]
- [Current implementation approach]
- [Known limitations]

## Desired State
- [What should exist]
- [Required capabilities]
- [Success criteria]

## Gap
- [What's missing]
- [What needs to change]
- [What needs to be added]
```

### Risk Assessment

Identify risks early and categorize:

**Technical Risks:**
- Unknowns in the technical approach
- Dependencies on external systems
- Performance or scalability concerns
- Integration complexity

**Process Risks:**
- Unclear requirements
- Blocked dependencies
- Resource constraints
- Timeline pressures

**Business Risks:**
- User impact during rollout
- Rollback complexity
- Data migration challenges
- Compatibility breaking changes

## Writing Effective Requirements

### User Story Formula

```
As a [persona]
I want [feature/capability]
So that [business value/benefit]
```

**Persona Types:**
- End user (customer, admin, guest)
- Developer (maintainer, contributor)
- System (automated process, integration)
- Stakeholder (product owner, business user)

### Acceptance Criteria Patterns

**Format:**
```
WHEN [trigger/condition]
THEN the system SHALL [expected outcome]
```

**Coverage Checklist:**
- ✓ Happy path (primary use case)
- ✓ Edge cases (boundary conditions)
- ✓ Error cases (invalid input, failures)
- ✓ Permissions (authorization checks)
- ✓ Data validation (format, range, required fields)
- ✓ State changes (what gets updated)
- ✓ Side effects (notifications, logs, events)

### Common Requirements Anti-Patterns

**Too Technical:**
❌ "System shall call API endpoint /users with POST method"
✓ "User profile data shall be stored securely"

**Too Vague:**
❌ "System shall be fast"
✓ "Page load time shall be under 2 seconds for 95% of requests"

**Implementation-Focused:**
❌ "System shall use Redis for caching"
✓ "System shall cache frequently accessed data to improve response times"

## Planning Best Practices

### Phase Organization

**Sequential Phases:** When work must happen in order
```
Phase 1: Foundation (database, models)
Phase 2: Core Logic (business rules)
Phase 3: API Layer (endpoints)
Phase 4: UI Integration (frontend)
```

**Parallel Phases:** When work can happen simultaneously
```
Phase 1A: Backend API
Phase 1B: Frontend Components
Phase 2: Integration & Testing
```

**Risk-Based Phases:** When addressing unknowns early
```
Phase 1: Proof of Concept (validate approach)
Phase 2: Core Implementation
Phase 3: Polish & Optimization
```

### Linking Requirements to Plan

Always use explicit references:
- "This addresses requirements #1 and #2"
- "Requirement #3 is implemented in Phase 2"
- "All requirements covered by Phase 1 and Phase 2"

### Dependency Documentation

**External Dependencies:**
```
- Library: lodash v4.x (utility functions)
- Service: SendGrid API (email delivery)
- Tool: Docker (containerization)
```

**Internal Dependencies:**
```
- Module: User service must be implemented first
- Database: Users table must exist
- Feature: Authentication must be functional
```

## Task Breakdown Strategies

### Atomic Task Criteria

A good task is:
- **Completable** in one focused session (1-4 hours)
- **Testable** with clear success criteria
- **Independent** or with explicit dependencies noted
- **Specific** enough to start without additional planning

### Task Ordering Principles

1. **Dependencies First:** Tasks that others depend on
2. **Foundation to Features:** Core infrastructure before features
3. **Risk Mitigation:** Uncertain tasks early in the phase
4. **Incremental Value:** Deliver working increments
5. **Testing Integrated:** Tests alongside implementation

### Task Description Format

**Good Structure:**
```
- [ ] Create User authentication service with login and token generation
```

**Better Structure (for complex tasks):**
```
- [ ] Create User authentication service
  - Implement login method with email/password validation
  - Generate JWT tokens with 24-hour expiration
  - Add token refresh capability
  - Include rate limiting (5 attempts per minute)
```

## Reflection Checkpoints Strategy

### Purpose of Checkpoints

Reflection checkpoints:
- **Validate assumptions** before investing more effort
- **Catch misunderstandings** early in the process
- **Ensure alignment** between you and the user
- **Prevent rework** from going down wrong paths
- **Build confidence** through incremental validation

### When to Pause

**Required Checkpoints:**
1. After investigation (before starting requirements)
2. After requirements (before planning)
3. After planning (before task breakdown)
4. After tasks (before starting implementation)

**Optional Checkpoints:**
- When making assumptions about requirements
- When technical approach has multiple options
- When risks are identified that need discussion
- When dependencies are unclear

### Effective Checkpoint Questions

**Open-ended:**
- "Does this match your understanding?"
- "Am I missing anything important?"
- "What concerns do you have about this approach?"

**Specific:**
- "Should requirement #3 include email notifications?"
- "Is Phase 1 the right priority, or should Phase 2 come first?"
- "Does the granularity of these tasks feel right?"

**Directional:**
- "Should I continue with this approach?"
- "Would you like me to add more detail here?"
- "Is this enough context for a coding agent?"

## Quality Assurance

### Requirements Quality Checklist

- [ ] Every requirement has a user story
- [ ] Every requirement has 2+ acceptance criteria
- [ ] Acceptance criteria are testable and specific
- [ ] Edge cases and error scenarios covered
- [ ] Requirements are numbered for reference
- [ ] Document is readable in 1-2 minutes

### Plan Quality Checklist

- [ ] Plan links to all requirements
- [ ] Each phase has a clear priority
- [ ] Risks are identified and documented
- [ ] Dependencies are explicit
- [ ] Phases are logically ordered
- [ ] Document is readable in 1-2 minutes

### Tasks Quality Checklist

- [ ] Tasks link to plan phases and requirements
- [ ] Each task is atomic and completable
- [ ] Tasks are in logical execution order
- [ ] Checkboxes present for tracking
- [ ] Task granularity is appropriate
- [ ] Document is readable in 1-2 minutes

## Common Pitfalls

### Over-Specifying

**Problem:** Requirements become implementation instructions
**Solution:** Focus on WHAT and WHY, not HOW

### Under-Specifying

**Problem:** Requirements too vague to implement
**Solution:** Add concrete acceptance criteria with examples

### Skipping Investigation

**Problem:** Writing specs without understanding context
**Solution:** Always investigate codebase and ask user questions first

### Ignoring Reflection Checkpoints

**Problem:** Building elaborate specs user doesn't want
**Solution:** Validate incrementally at every phase

### Wrong Folder Choice

**Problem:** Putting defect in features/ or vice versa
**Solution:** Features add requirements, defects fix unmet requirements

### Poor Task Granularity

**Problem:** Tasks too broad or too granular
**Solution:** Aim for 1-4 hour completion time per task

## Iteration and Refinement

### When to Update Specs

**During Implementation:**
- Mark tasks complete with `[x]`
- Add discovered tasks to appropriate phase
- Update requirements if understanding changes
- Document deviations in tasks.md

**After Implementation:**
- Review what worked vs what didn't
- Update templates for future specs
- Document lessons learned
- Refine estimation approaches

### Spec Evolution

Specs are living documents:
- **Add tasks** when new work is discovered
- **Update requirements** if understanding improves
- **Revise plan** if approach changes
- **Archive completed phases** to reduce noise

### Feedback Integration

After using specs:
- What was unclear in the requirements?
- What tasks were missing?
- What could be more specific?
- What was unnecessary detail?

Use this feedback to improve future specs.
