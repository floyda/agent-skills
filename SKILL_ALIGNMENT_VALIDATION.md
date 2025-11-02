# Skill Alignment Validation Guide

This document describes how to validate that `spec-driven-dev` generates output compatible with `implementing-specs` expectations.

## Overview

The `spec-driven-dev` skill creates specification artifacts that the `implementing-specs` skill consumes. These two skills must remain aligned to work together seamlessly.

## Required Artifacts

Both skills must agree on:

1. **File names and locations**
2. **File structure (sections/headings)**
3. **Task format**

## Validation Checklist

### 1. Requirements.md Format

**spec-driven-dev generates:**
```markdown
# Requirements: [Feature Name]

## Overview
[2-3 sentence summary]

## Requirements

### 1. [Requirement Title]

**User Story**
> As a [user], I want [goal] so that [benefit]

**Acceptance Criteria**
> WHEN [condition] THEN the system SHALL [behavior]
```

**implementing-specs expects:**
- `## Overview` section exists
- `## Requirements` section exists
- Each requirement has acceptance criteria

**Validation command:**
```bash
grep -q "## Overview" requirements.md && \
grep -q "## Requirements" requirements.md && \
echo "✓ requirements.md structure valid"
```

### 2. Plan.md Format

**spec-driven-dev generates:**
```markdown
# Implementation Plan: [Feature Name]

## Goal
[1-2 sentences]

## Approach

### Phase 1: [Phase Name]
**Priority**: High
**Requirements**: #1, #2
**Strategy**: [approach]
**Risks**: [risks]

## Dependencies
[dependencies]

## Technical Considerations
[considerations]
```

**implementing-specs expects:**
- `## Goal` section exists
- `## Approach` section exists with phase subsections

**Validation command:**
```bash
grep -q "## Goal" plan.md && \
grep -q "## Approach" plan.md && \
echo "✓ plan.md structure valid"
```

### 3. Tasks.md Format

**spec-driven-dev generates:**
```markdown
# Tasks: [Feature Name]

## Phase 1: [Phase Name]
**Plan Reference**: See Phase 1 in plan.md
**Requirements**: #1, #2 from requirements.md

- [ ] T001: Create [component] with [functionality]
- [ ] T002: Implement [method] to handle [use case]
- [ ] T003: Add [validation] for [scenario]
```

**implementing-specs expects:**
- Phase sections starting with `## Phase`
- Tasks in checkbox format: `- [ ] T###: Description`
- Task IDs in format `T001`, `T002`, etc. (three digits)

**Validation commands:**
```bash
# Check for phase sections
grep -q "## Phase" tasks.md || echo "✗ No phase sections found"

# Check for properly formatted tasks
grep -q "^- \[ \] T[0-9][0-9][0-9]:" tasks.md && \
echo "✓ tasks.md format valid" || \
echo "✗ tasks.md missing properly formatted tasks"

# Count tasks
echo "Task count: $(grep -c "^- \[ \] T[0-9][0-9][0-9]:" tasks.md)"
```

## Automated Validation Script

A validation script exists at `implementing-specs/scripts/validate_spec_artifacts.py`:

```bash
python implementing-specs/scripts/validate_spec_artifacts.py specs/features/my-feature
```

This script checks:
- All three files exist
- Required sections are present
- Tasks are properly formatted

## Testing Alignment Between Skills

### Method 1: Manual Testing

1. Run `spec-driven-dev` to generate a complete spec
2. Run the validation script on the output
3. If validation passes, `implementing-specs` can consume it

### Method 2: Sample File Testing

Create sample files following the templates:

```bash
# Create sample spec
mkdir -p test-spec

# Copy templates and fill in
# Then validate
python implementing-specs/scripts/validate_spec_artifacts.py test-spec
```

### Method 3: Agent-Driven Validation

An agent can validate alignment by:

1. **Reading both skill definitions:**
   - `spec-driven-dev/SKILL.md`
   - `spec-driven-dev/references/templates.md`
   - `implementing-specs/SKILL.md`
   - `implementing-specs/scripts/validate_spec_artifacts.py`

2. **Extracting expectations:**
   - What sections does spec-driven-dev promise to generate?
   - What sections does implementing-specs expect?
   - Do task formats match?

3. **Comparing:**
   - Are section names identical?
   - Are task formats identical?
   - Are file names identical?

4. **Reporting mismatches:**
   - List any differences found
   - Suggest which file needs updating

## Common Mismatches to Check

### Section Name Mismatches

❌ **Bad - spec-driven-dev generates "Success Criteria" but implementing-specs expects "Requirements"**

✓ **Good - Both use "Requirements" section**

### Task Format Mismatches

❌ **Bad - spec-driven-dev uses headings `### T001:` but implementing-specs expects checkboxes**

✓ **Good - Both use checkbox format `- [ ] T001:`**

### Task ID Mismatches

❌ **Bad - spec-driven-dev uses `T1:` but implementing-specs expects `T001:`**

✓ **Good - Both use three-digit format `T001:`, `T002:`, etc.**

## Validation Script Location

The canonical validation script is:
```
implementing-specs/scripts/validate_spec_artifacts.py
```

This script should be the **source of truth** for what implementing-specs expects.

## Updating Template When Validation Changes

When updating validation requirements:

1. **Update validation script first:**
   - `implementing-specs/scripts/validate_spec_artifacts.py`

2. **Update spec-driven-dev templates:**
   - `spec-driven-dev/references/templates.md`
   - `spec-driven-dev/references/workflow-guide.md`
   - `spec-driven-dev/SKILL.md`

3. **Test the change:**
   - Generate a spec with spec-driven-dev
   - Run validation script
   - Ensure it passes

4. **Update documentation:**
   - Update this file (SKILL_ALIGNMENT_VALIDATION.md)
   - Document the change in both skills

## Quick Reference: Expected Formats

### requirements.md
```
Required sections:
- ## Overview
- ## Requirements
```

### plan.md
```
Required sections:
- ## Goal
- ## Approach
```

### tasks.md
```
Required patterns:
- ## Phase [N]: [Name]
- [ ] T001: Task description
```

Regex patterns:
- Phase section: `^## Phase`
- Task checkbox: `^- \[([ x])\] T\d{3}:`

## Troubleshooting

### Error: "Missing required section"
- Check that section names match exactly (case-sensitive)
- Ensure `##` heading level is correct (not `#` or `###`)

### Error: "tasks.md does not contain properly formatted tasks"
- Ensure task format is exactly: `- [ ] T001: Description`
- Check that task IDs have exactly 3 digits (T001, not T1)
- Verify space after checkbox: `[ ]` not `[]`

### Error: "Validation script not found"
- Ensure you're using the correct path to the script
- Check that implementing-specs skill is installed

## CI/CD Integration (Future)

To prevent mismatches in the future, consider:

1. **Pre-commit hook** that validates templates against validation script
2. **Test suite** that generates sample specs and validates them
3. **GitHub Actions** that run validation on template changes

Example test:
```python
def test_template_generates_valid_spec():
    # Use spec-driven-dev template to generate spec
    spec = generate_from_template()

    # Validate using implementing-specs validator
    result = validate_spec_artifacts(spec)

    assert result.is_valid
```
