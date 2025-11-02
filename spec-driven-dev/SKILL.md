---
name: spec-driven-dev
description: Structured workflow for spec-driven software development with AI. Optimized for Python projects (libraries, CLI/TUI apps, data tools) as well as web backends. Use when creating or fixing features in expanding projects that need clear requirements, implementation plans, and task breakdowns. Guides through investigation, analysis, spec definition, planning, and task decomposition with reflection checkpoints throughout.
---

# Spec-Driven Development Workflow

Transform vague requirements into executable, trackable development tasks through a systematic investigation, analysis, and planning process.

## About This Skill

This workflow is particularly effective for:
- **Python Libraries** - Designing public APIs, managing backward compatibility, packaging
- **CLI/TUI Applications** - Planning user interactions, keyboard shortcuts, command structures
- **Data Processing Tools** - Designing pipelines, error handling, data integrity
- **Web Backends** - Traditional REST APIs, authentication, integrations
- **Complex Features** - Any significant change requiring clear scoping and coordination

The skill includes Python-specific guidance on dependency management, testing patterns, packaging, and type safety throughout the workflow.

## Workflow Overview

1. **Investigate** - Gather context from user, codebase, and documentation
2. **Analyze** - Understand current state and identify what needs to change
3. **Define Spec** - Create clear requirements with user stories and acceptance criteria
4. **Refine Plan** - Develop detailed implementation strategy
5. **Break Down Tasks** - Create actionable, trackable task list

All outputs are markdown files stored in `specs/features/` or `specs/defects/` folders.

## Step 1: Investigate & Gather Context

**Goal**: Build comprehensive understanding before writing anything.

### Investigation Checklist

- **Ask the user**: What problem are they solving? What should the outcome be?
- **Review codebase**: 
  - Check `docs/` folder for existing documentation
  - Read project `README.md` for architecture and conventions
  - Examine relevant code files to understand current implementation
- **Identify the type**: Is this a feature (new requirements) or defect (unmet/undefined requirements)?

### Output Location Decision

Determine the appropriate folder:
- **`specs/features/`** - New functionality with new requirements and user stories
- **`specs/defects/`** - Bug fixes, gaps, or unmet existing requirements

**Reflection Checkpoint**: Before proceeding, ask yourself: "Do I understand what currently exists and what needs to change?" If not, gather more information.

## Step 2: Analyze Current State

**Goal**: Document findings and clarify the gap between current and desired state.

### Analysis Questions

- What exists today that's relevant to this work?
- What's missing or broken?
- What are the dependencies and risks?
- What assumptions am I making that need validation?

**Reflection Checkpoint**: Share your analysis summary with the user and ask: "Does this match your understanding? Am I missing anything important?"

## Step 3: Define Requirements (requirements.md)

**Goal**: Create a concise, readable requirements document (1-2 minute read).

### File Location

- `specs/features/<feature-name>/requirements.md`
- `specs/defects/<defect-name>/requirements.md`

### Structure

```markdown
# Requirements: [Feature/Defect Name]

## Overview
[2-3 sentence summary of what this addresses]

## Requirements

### 1. [Requirement Title]

**User Story**
> As a [user type], I want [goal] so that [benefit/reason]

**Acceptance Criteria**
> WHEN [condition] THEN the system SHALL [expected behavior]
> WHEN [another condition] THEN the system SHALL [expected behavior]

### 2. [Next Requirement]
...
```

### Best Practices

- **Keep it concise**: 1-2 minutes to read the entire file
- **Be specific**: Acceptance criteria should be testable
- **Cover edge cases**: Include error handling, validation, persistence
- **Number sequentially**: Makes references easier in later phases
- **Group logically**: Related requirements together

**Reflection Checkpoint**: Ask the user: "Do these requirements capture what you need? Should I add, remove, or clarify anything before moving to planning?"

## Step 4: Refine Implementation Plan (plan.md)

**Goal**: Bridge requirements to implementation with a strategic approach (1-2 minute read).

### File Location

- `specs/features/<feature-name>/plan.md`
- `specs/defects/<defect-name>/plan.md`

### Structure

```markdown
# Implementation Plan: [Feature/Defect Name]

## Goal
[1-2 sentence objective]

## Approach

### Phase 1: [Phase Name]
**Priority**: High | Medium | Low
**Requirements**: Links to requirements.md (#1, #2)
**Strategy**: [How we'll approach this]
**Risks**: [What could go wrong]

### Phase 2: [Phase Name]
...

## Dependencies
- [External dependencies, libraries, or prerequisites]

## Technical Considerations
- [Architecture decisions, patterns, trade-offs]
```

### Best Practices

- **Link everything**: Reference requirement numbers explicitly
- **Prioritize clearly**: High/Medium/Low for each phase
- **Identify risks**: Call out uncertainties early
- **Stay high-level**: Focus on "what" not "how" (save details for tasks)
- **Keep it scannable**: Use headers and bullets effectively

**Reflection Checkpoint**: Review with user: "Does this implementation strategy make sense? Are the phases in the right order? Any concerns about the approach?"

## Step 5: Break Down Tasks (tasks.md)

**Goal**: Create actionable, trackable checklist a coding agent can execute (1-2 minute read).

### File Location

- `specs/features/<feature-name>/tasks.md`
- `specs/defects/<defect-name>/tasks.md`

### Structure

```markdown
# Tasks: [Feature/Defect Name]

## Phase 1: [Phase Name]
**Plan Reference**: [Link to plan.md section]
**Requirements**: [Links to requirements.md]

- [ ] Task 1: [Clear, actionable description]
- [ ] Task 2: [Another specific task]
- [ ] Task 3: [Verifiable completion criteria]

## Phase 2: [Phase Name]
...
```

### Best Practices

- **Make tasks atomic**: Each task should be completable in one focused session
- **Be specific**: "Implement user authentication" → "Create User model with password hashing"
- **Maintain order**: Tasks should follow logical execution sequence
- **Link upstream**: Reference plan sections and requirement numbers
- **Use checkboxes**: `- [ ]` for pending, `- [x]` for completed
- **Right granularity**: Meaningful units, not busywork. Not too broad, not too granular.

**Reflection Checkpoint**: Ask the user: "Do these tasks make sense? Are they in the right order? Is anything missing or unnecessarily detailed?"

## Execution Guidance

When a coding agent picks up these specs:

1. **Read all three files** in order: requirements → plan → tasks
2. **Work in phases**: Complete Phase 1 before moving to Phase 2
3. **Mark progress**: Update tasks.md with `[x]` as work completes
4. **Stay bounded**: Focus on the current phase's tasks only
5. **Verify alignment**: Check that implementation meets acceptance criteria

## Folder Structure Example

```
specs/
├── features/
│   ├── user-authentication/
│   │   ├── requirements.md
│   │   ├── plan.md
│   │   └── tasks.md
│   └── payment-integration/
│       ├── requirements.md
│       ├── plan.md
│       └── tasks.md
└── defects/
    ├── login-validation-bug/
    │   ├── requirements.md
    │   ├── plan.md
    │   └── tasks.md
    └── data-persistence-issue/
        ├── requirements.md
        ├── plan.md
        └── tasks.md
```

## Quality Checklist

Before finalizing any spec, verify:

- [ ] Each file is readable in 1-2 minutes
- [ ] Requirements have user stories and acceptance criteria
- [ ] Plan links to specific requirement numbers
- [ ] Tasks link to plan phases and requirements
- [ ] Tasks are ordered logically
- [ ] Reflection checkpoints were used with the user
- [ ] Files are in correct folder (features/ or defects/)

## Tips for Success

- **Start simple**: Better to iterate than over-spec initially
- **Assume nothing**: Use codebase and user input to build understanding
- **Validate often**: Reflection checkpoints catch issues early
- **Stay concise**: Every sentence should earn its place
- **Think execution**: A future agent needs to pick this up and run with it
