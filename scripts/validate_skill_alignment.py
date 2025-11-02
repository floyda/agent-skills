#!/usr/bin/env python3
"""
Validate alignment between spec-driven-dev and implementing-specs skills.

This script checks that the output format specified in spec-driven-dev templates
matches the input format expected by implementing-specs validation.

Usage:
    python validate_skill_alignment.py [--skills-dir <path>]

Example:
    python validate_skill_alignment.py --skills-dir /Users/floyda/.claude/skills
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple


class AlignmentIssue:
    def __init__(self, severity: str, component: str, message: str):
        self.severity = severity  # "error" or "warning"
        self.component = component  # "requirements", "plan", "tasks", "general"
        self.message = message

    def __str__(self):
        icon = "❌" if self.severity == "error" else "⚠️"
        return f"{icon} [{self.component}] {self.message}"


def extract_validation_expectations(validator_script: Path) -> dict:
    """Extract what the validation script expects."""
    content = validator_script.read_text()

    expectations = {
        "requirements_sections": [],
        "plan_sections": [],
        "tasks_sections": [],
        "task_pattern": None
    }

    # Extract requirements sections
    req_match = re.search(
        r'REQUIREMENTS_SECTIONS\s*=\s*\[(.*?)\]',
        content,
        re.DOTALL
    )
    if req_match:
        sections = re.findall(r'"([^"]+)"', req_match.group(1))
        expectations["requirements_sections"] = sections

    # Extract plan sections
    plan_match = re.search(
        r'PLAN_SECTIONS\s*=\s*\[(.*?)\]',
        content,
        re.DOTALL
    )
    if plan_match:
        sections = re.findall(r'"([^"]+)"', plan_match.group(1))
        expectations["plan_sections"] = sections

    # Extract tasks sections
    tasks_match = re.search(
        r'TASKS_SECTIONS\s*=\s*\[(.*?)\]',
        content,
        re.DOTALL
    )
    if tasks_match:
        sections = re.findall(r'"([^"]+)"', tasks_match.group(1))
        expectations["tasks_sections"] = sections

    # Extract task pattern
    pattern_match = re.search(
        r'task_pattern\s*=\s*r"([^"]+)"',
        content
    )
    if pattern_match:
        expectations["task_pattern"] = pattern_match.group(1)

    return expectations


def extract_template_promises(template_file: Path) -> dict:
    """Extract what the template promises to generate."""
    content = template_file.read_text()

    promises = {
        "requirements_sections": [],
        "plan_sections": [],
        "tasks_sections": [],
        "task_format_examples": []
    }

    # Find requirements.md template section
    req_template = re.search(
        r'## requirements\.md Template.*?```markdown(.*?)```',
        content,
        re.DOTALL | re.IGNORECASE
    )
    if req_template:
        template_text = req_template.group(1)
        # Extract section headers (just the heading marker and name, not content in brackets)
        sections = re.findall(r'^(##\s+[A-Za-z\s]+)', template_text, re.MULTILINE)
        # Clean up sections - strip trailing spaces and ensure format
        sections = [s.strip() for s in sections]
        promises["requirements_sections"] = sections

    # Find plan.md template section
    plan_template = re.search(
        r'## plan\.md Template.*?```markdown(.*?)```',
        content,
        re.DOTALL | re.IGNORECASE
    )
    if plan_template:
        template_text = plan_template.group(1)
        # Extract section headers (just the heading marker and name, not content in brackets)
        sections = re.findall(r'^(##\s+[A-Za-z\s]+)', template_text, re.MULTILINE)
        sections = [s.strip() for s in sections]
        promises["plan_sections"] = sections

    # Find tasks.md template section
    tasks_template = re.search(
        r'## tasks\.md Template.*?```markdown(.*?)```',
        content,
        re.DOTALL | re.IGNORECASE
    )
    if tasks_template:
        template_text = tasks_template.group(1)
        # Extract phase sections
        sections = re.findall(r'^##\s+(Phase[^:]*)', template_text, re.MULTILINE)
        if sections:
            promises["tasks_sections"] = ["## Phase"]  # Generic pattern

        # Extract task format examples
        task_examples = re.findall(
            r'^- \[ \] (T\d+:.*?)$',
            template_text,
            re.MULTILINE
        )
        promises["task_format_examples"] = task_examples

    return promises


def validate_alignment(skills_dir: Path) -> List[AlignmentIssue]:
    """Validate alignment between the two skills."""
    issues = []

    # Locate files
    validator_script = skills_dir / "implementing-specs/scripts/validate_spec_artifacts.py"
    template_file = skills_dir / "spec-driven-dev/references/templates.md"

    if not validator_script.exists():
        issues.append(AlignmentIssue(
            "error",
            "general",
            f"Validation script not found: {validator_script}"
        ))
        return issues

    if not template_file.exists():
        issues.append(AlignmentIssue(
            "error",
            "general",
            f"Template file not found: {template_file}"
        ))
        return issues

    # Extract expectations and promises
    expectations = extract_validation_expectations(validator_script)
    promises = extract_template_promises(template_file)

    # Validate requirements.md
    if set(expectations["requirements_sections"]) != set(promises["requirements_sections"]):
        expected = expectations["requirements_sections"]
        promised = promises["requirements_sections"]

        missing = set(expected) - set(promised)
        extra = set(promised) - set(expected)

        if missing:
            issues.append(AlignmentIssue(
                "error",
                "requirements",
                f"Template missing required sections: {', '.join(missing)}"
            ))
        if extra:
            issues.append(AlignmentIssue(
                "warning",
                "requirements",
                f"Template has extra sections not validated: {', '.join(extra)}"
            ))

    # Validate plan.md
    if set(expectations["plan_sections"]) != set(promises["plan_sections"]):
        expected = expectations["plan_sections"]
        promised = promises["plan_sections"]

        missing = set(expected) - set(promised)
        extra = set(promised) - set(expected)

        if missing:
            issues.append(AlignmentIssue(
                "error",
                "plan",
                f"Template missing required sections: {', '.join(missing)}"
            ))
        if extra:
            issues.append(AlignmentIssue(
                "warning",
                "plan",
                f"Template has extra sections not validated: {', '.join(extra)}"
            ))

    # Validate tasks.md format
    if expectations["task_pattern"]:
        task_pattern = expectations["task_pattern"]

        # Check if any task examples match the expected pattern
        if promises["task_format_examples"]:
            example = promises["task_format_examples"][0]
            full_example = f"- [ ] {example}"

            if not re.match(task_pattern, full_example):
                issues.append(AlignmentIssue(
                    "error",
                    "tasks",
                    f"Task format '{full_example}' doesn't match expected pattern '{task_pattern}'"
                ))
        else:
            issues.append(AlignmentIssue(
                "warning",
                "tasks",
                "No task format examples found in template"
            ))

    # Validate tasks.md sections
    if expectations["tasks_sections"]:
        expected_pattern = expectations["tasks_sections"][0]
        if not promises["tasks_sections"] or expected_pattern not in promises["tasks_sections"][0]:
            issues.append(AlignmentIssue(
                "error",
                "tasks",
                f"Template doesn't have expected section pattern: {expected_pattern}"
            ))

    return issues


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate alignment between spec-driven-dev and implementing-specs"
    )
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=Path.home() / ".claude/skills",
        help="Path to skills directory (default: ~/.claude/skills)"
    )

    args = parser.parse_args()

    print("Validating skill alignment...")
    print(f"Skills directory: {args.skills_dir}")
    print("-" * 80)

    issues = validate_alignment(args.skills_dir)

    if not issues:
        print("✅ All checks passed! Skills are properly aligned.")
        return 0

    # Separate errors and warnings
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    if errors:
        print("\nErrors found:")
        for issue in errors:
            print(f"  {issue}")

    if warnings:
        print("\nWarnings:")
        for issue in warnings:
            print(f"  {issue}")

    print("\n" + "-" * 80)
    print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors:
        print("\n⚠️  Fix errors before using these skills together")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
