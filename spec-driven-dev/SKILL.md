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

## The Five Steps

### Step 1: Investigate & Gather Context
Ask the user what problem they're solving. Review codebase (README, docs, relevant code). Determine if this is a feature (new requirements) or defect (unmet requirements). Decide output folder: `specs/features/` or `specs/defects/`.

**See workflow-guide.md** for investigation checklist, reflection checkpoint, and Python-specific questions.

### Step 2: Analyze Current State
Document findings about what exists today, what's missing/broken, dependencies, and risks. Share analysis summary with user for validation.

**See workflow-guide.md** for gap analysis patterns and risk assessment guidance.

### Step 3: Define Requirements
Create `requirements.md` with Overview, numbered Requirements (each with User Story and Acceptance Criteria). Target 1-2 minute read time.

**See templates.md** for complete requirements template and examples. **See workflow-guide.md** for detailed best practices, user story patterns, and Python-specific requirement guidance.

### Step 4: Refine Implementation Plan
Create `plan.md` with Goal, Approach (phases with Priority/Requirements/Strategy/Risks), Dependencies, and Technical Considerations. Link each phase to specific requirement numbers. Target 1-2 minute read time.

**See templates.md** for complete plan template and examples. **See workflow-guide.md** for phase organization patterns (including Python library and CLI/TUI examples) and technical considerations.

### Step 5: Break Down Tasks
Create `tasks.md` with tasks organized by phase. Each task must have a unique ID (T001, T002, etc.), be formatted as a heading (`### T001: Task title`), include a status line (`**Status**: pending`), and be atomic, specific, and completable in one focused session. Link to plan phases and requirements.

**See templates.md** for complete tasks template and examples. **See workflow-guide.md** for task breakdown strategies, granularity guidance, and Python-specific testing patterns.

## Execution Guidance

When a coding agent picks up these specs:

1. **Read all three files** in order: requirements → plan → tasks
2. **Work in phases**: Complete Phase 1 before moving to Phase 2
3. **Mark progress**: Update task status from `pending` → `in_progress` → `completed` as work progresses
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
