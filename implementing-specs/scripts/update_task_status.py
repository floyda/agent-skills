#!/usr/bin/env python3
"""
Update task status in tasks.md file.

This script helps maintain task tracking during implementation by updating
task statuses in the tasks.md file produced by spec-driven-dev.

Usage:
    python update_task_status.py <tasks_file> <task_id> <status>

Example:
    python update_task_status.py specs/features/autocomplete/tasks.md T001 completed
    python update_task_status.py specs/defects/pagination/tasks.md T005 in_progress
"""

import sys
import re
from pathlib import Path
from typing import Literal

Status = Literal["pending", "in_progress", "completed", "blocked"]

VALID_STATUSES = ["pending", "in_progress", "completed", "blocked"]

def update_task_status(tasks_file: Path, task_id: str, new_status: Status) -> bool:
    """
    Update the status of a specific task in tasks.md.

    Args:
        tasks_file: Path to the tasks.md file
        task_id: Task identifier (e.g., "T001", "T005")
        new_status: New status (pending, in_progress, completed, blocked)

    Returns:
        True if update was successful, False otherwise
    """
    if not tasks_file.exists():
        print(f"Error: Tasks file not found: {tasks_file}", file=sys.stderr)
        return False

    if new_status not in VALID_STATUSES:
        print(f"Error: Invalid status '{new_status}'. Must be one of: {', '.join(VALID_STATUSES)}", file=sys.stderr)
        return False

    content = tasks_file.read_text()

    # Find the task heading and update the status line that follows
    # Pattern matches: ### T001: Task description
    # Followed by: **Status**: <current_status>
    task_pattern = rf"^(###\s+{task_id}:\s+.+?)$\s+^\*\*Status\*\*:\s*\w+"

    def replace_status(match):
        task_line = match.group(1)
        return f"{task_line}\n**Status**: {new_status}"

    updated_content, count = re.subn(task_pattern, replace_status, content, flags=re.MULTILINE)

    if count == 0:
        print(f"Warning: Task {task_id} not found in {tasks_file}", file=sys.stderr)
        return False

    if count > 1:
        print(f"Warning: Multiple matches found for {task_id}. Updated {count} occurrences.", file=sys.stderr)

    tasks_file.write_text(updated_content)
    print(f"✓ Updated {task_id} to '{new_status}'")
    return True


def list_tasks(tasks_file: Path) -> None:
    """List all tasks in the tasks.md file with their current status."""
    if not tasks_file.exists():
        print(f"Error: Tasks file not found: {tasks_file}", file=sys.stderr)
        return

    content = tasks_file.read_text()

    # Match task headers followed by status lines
    pattern = r"^###\s+(T\d{3}):\s+(.+?)$\s+^\*\*Status\*\*:\s*(\w+)"

    print(f"\nTasks in {tasks_file}:")
    print("-" * 80)

    for match in re.finditer(pattern, content, re.MULTILINE):
        task_id = match.group(1)
        description = match.group(2).strip()
        status = match.group(3).strip()

        print(f"{task_id}: {description[:60]}... [{status}]")

    print("-" * 80)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    tasks_file = Path(sys.argv[1])

    # List mode
    if len(sys.argv) == 2:
        list_tasks(tasks_file)
        sys.exit(0)

    # Update mode
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        print(__doc__)
        sys.exit(1)

    task_id = sys.argv[2].upper()
    new_status = sys.argv[3].lower()

    if not re.match(r"^T\d{3}$", task_id):
        print(f"Error: Invalid task ID format '{task_id}'. Expected format: T001, T042, etc.", file=sys.stderr)
        sys.exit(1)

    success = update_task_status(tasks_file, task_id, new_status)  # type: ignore
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
