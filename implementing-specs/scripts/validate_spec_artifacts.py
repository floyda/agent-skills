#!/usr/bin/env python3
"""
Validate spec artifacts (requirements.md, plan.md, tasks.md) before implementation.

This script ensures that all required artifacts from spec-driven-dev are present
and well-formed before beginning implementation.

Usage:
    python validate_spec_artifacts.py <spec_directory>

Example:
    python validate_spec_artifacts.py specs/features/autocomplete-improvements
    python validate_spec_artifacts.py specs/defects/pagination-bug
"""

import sys
from pathlib import Path
from typing import List, Tuple

# Required files
REQUIRED_FILES = ["requirements.md", "plan.md", "tasks.md"]

# Required sections in requirements.md
REQUIREMENTS_SECTIONS = [
    "## Overview",
    "## Requirements"
]

# Required sections in plan.md
PLAN_SECTIONS = [
    "## Implementation Phases"
]

# Required sections in tasks.md
TASKS_SECTIONS = [
    "## Tasks"
]


class ValidationError(Exception):
    """Validation error exception."""
    pass


def validate_file_exists(spec_dir: Path, filename: str) -> Path:
    """Validate that a required file exists."""
    file_path = spec_dir / filename
    if not file_path.exists():
        raise ValidationError(f"Missing required file: {filename}")
    if not file_path.is_file():
        raise ValidationError(f"{filename} exists but is not a file")
    return file_path


def validate_file_sections(file_path: Path, required_sections: List[str]) -> None:
    """Validate that a file contains all required sections."""
    content = file_path.read_text()

    missing_sections = []
    for section in required_sections:
        if section not in content:
            missing_sections.append(section)

    if missing_sections:
        raise ValidationError(
            f"{file_path.name} is missing required sections:\n"
            + "\n".join(f"  - {s}" for s in missing_sections)
        )


def validate_tasks_format(tasks_file: Path) -> None:
    """Validate that tasks.md contains properly formatted tasks."""
    content = tasks_file.read_text()

    # Check for at least one task with T### format
    import re
    task_pattern = r"^###\s+T\d{3}"

    if not re.search(task_pattern, content, re.MULTILINE):
        raise ValidationError(
            "tasks.md does not contain any tasks in the expected format (### T001: ...)"
        )


def validate_spec_directory(spec_dir: Path) -> Tuple[bool, List[str]]:
    """
    Validate that a spec directory contains all required artifacts.

    Args:
        spec_dir: Path to the spec directory (e.g., specs/features/autocomplete)

    Returns:
        Tuple of (success: bool, errors: List[str])
    """
    errors = []

    # Check directory exists
    if not spec_dir.exists():
        return False, [f"Spec directory does not exist: {spec_dir}"]

    if not spec_dir.is_dir():
        return False, [f"Path is not a directory: {spec_dir}"]

    try:
        # Validate required files exist
        requirements_file = validate_file_exists(spec_dir, "requirements.md")
        plan_file = validate_file_exists(spec_dir, "plan.md")
        tasks_file = validate_file_exists(spec_dir, "tasks.md")

        # Validate file contents
        validate_file_sections(requirements_file, REQUIREMENTS_SECTIONS)
        validate_file_sections(plan_file, PLAN_SECTIONS)
        validate_file_sections(tasks_file, TASKS_SECTIONS)

        # Validate tasks format
        validate_tasks_format(tasks_file)

    except ValidationError as e:
        errors.append(str(e))

    return len(errors) == 0, errors


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    spec_dir = Path(sys.argv[1])

    print(f"Validating spec artifacts in: {spec_dir}")
    print("-" * 80)

    success, errors = validate_spec_directory(spec_dir)

    if success:
        print("✅ All spec artifacts are valid and ready for implementation!")
        print("-" * 80)
        print("\nFound files:")
        for filename in REQUIRED_FILES:
            file_path = spec_dir / filename
            size = file_path.stat().st_size
            print(f"  ✓ {filename} ({size} bytes)")
        sys.exit(0)
    else:
        print("❌ Validation failed with the following errors:\n")
        for error in errors:
            print(f"  • {error}")
        print("\n" + "-" * 80)
        print("\nPlease ensure spec-driven-dev has completed successfully before")
        print("running implementation. The spec directory should contain:")
        print("  - requirements.md (with Overview, Requirements)")
        print("  - plan.md (with Implementation Phases)")
        print("  - tasks.md (with properly formatted tasks: ### T001: ...)")
        sys.exit(1)


if __name__ == "__main__":
    main()
