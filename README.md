# Claude Skills Collection

A curated collection of skills for Claude AI assistants. Skills are modular packages that extend Claude's capabilities with specialized knowledge, workflows, and tools.

## What Are Skills?

Skills are folders containing instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. They act as "onboarding guides" that transform Claude from a general-purpose assistant into a domain specialist with procedural knowledge.

Each skill consists of:
- **SKILL.md**: Core instructions with YAML metadata
- **scripts/**: Executable code for deterministic tasks
- **references/**: Documentation loaded as needed
- **assets/**: Templates and files used in outputs

## Available Skills

### Development Workflow

- **spec-driven-dev**: Structured workflow for spec-driven software development with AI. Guides through investigation, analysis, spec definition, planning, and task decomposition. Optimized for Python projects (libraries, CLI/TUI apps, data tools) and web backends.

- **implementing-specs**: Implements Python features from spec-driven-dev artifacts using test-driven development, type safety with mypy --strict, comprehensive testing, and quality gates after every task.

- **commit-prep**: Prepares local repository changes for committing by running pre-commit hooks, project linters, full tests, and drafting concise commit messages.

### Meta Skills

- **skill-creator**: Guide for creating effective skills. Provides structured workflow for designing, implementing, and packaging new skills.

### Document Processing

- **document-skills**: Production-grade reference implementations for working with complex file formats:
  - **DOCX**: Word document creation with tracked changes
  - **PDF**: Text extraction, merging, form handling
  - **PPTX**: Presentation creation with automated slides
  - **XLSX**: Spreadsheet creation with formulas

## Installation

### For Claude Code

Claude Code has native skill support. You can install skills in two ways:

#### Method 1: Local Installation (Recommended for Custom Skills)

1. Copy skill folders to Claude's skills directory:
   ```bash
   # macOS/Linux
   cp -r <skill-name> ~/.claude/skills/

   # Windows
   copy <skill-name> %USERPROFILE%\.claude\skills\
   ```

2. Skills are automatically discovered and available immediately.

#### Method 2: Plugin Installation (For Skill Collections)

```bash
# Install from a skill collection
/plugin install <collection-name>@<namespace>
```

### For Codex CLI

Codex CLI requires a small setup to enable skill discovery:

#### 1. Install Skills Globally

Place skills in your Codex skills directory:

```bash
# Create skills directory
mkdir -p ~/.codex/skills

# Copy skills to global directory
cp -r spec-driven-dev ~/.codex/skills/
cp -r implementing-specs ~/.codex/skills/
cp -r commit-prep ~/.codex/skills/
cp -r skill-creator ~/.codex/skills/
```

#### 2. Create Skills Enumerator Script

Create a `list-skills` script in your PATH (e.g., `~/.local/bin/list-skills` or `/usr/local/bin/list-skills`):

```python
#!/usr/bin/env python3
"""Skills enumerator for Codex CLI."""

import json
import sys
from pathlib import Path
from typing import Any

import yaml


def find_skills(skills_dir: Path) -> list[dict[str, Any]]:
    """Find all SKILL.md files and parse their frontmatter."""
    skills = []

    for skill_file in skills_dir.glob("**/SKILL.md"):
        try:
            content = skill_file.read_text()

            # Extract YAML frontmatter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    skills.append({
                        "name": frontmatter.get("name", ""),
                        "description": frontmatter.get("description", ""),
                        "path": str(skill_file.parent),
                    })
        except Exception as e:
            print(f"Warning: Failed to parse {skill_file}: {e}", file=sys.stderr)

    return skills


def main() -> None:
    """List available skills as JSON."""
    skills_dir = Path.home() / ".codex" / "skills"

    if not skills_dir.exists():
        print(f"Error: Skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    skills = find_skills(skills_dir)
    print(json.dumps(skills, indent=2))


if __name__ == "__main__":
    main()
```

Make it executable:

```bash
chmod +x ~/.local/bin/list-skills
```

#### 3. Configure AGENTS.md

Add this instruction to your project's `AGENTS.md` (or global `~/.codex/AGENTS.md`):

```markdown
## Skills Discovery

List your skills directly after reading this via `list-skills` and load them into memory.
Remember them throughout the conversation. If a skill matches the current task, read its
full SKILL.md documentation and use it accordingly.
```

#### 4. Verify Installation

Test the enumerator:

```bash
list-skills
```

You should see JSON output listing all available skills with their names, descriptions, and paths.

## Usage

### In Claude Code

Skills are invoked automatically when Claude detects a matching task. You can also invoke them explicitly:

```bash
# Claude will automatically use spec-driven-dev when you say:
"Help me create a spec for adding user authentication"

# Or invoke the skill explicitly:
/skill spec-driven-dev

# Implement a spec
"Implement the spec in specs/features/authentication/"
# Claude will use implementing-specs automatically

# Prepare a commit
"Prepare my changes for commit"
# Claude will use commit-prep automatically
```

### In Codex CLI

Skills work the same way once configured:

```bash
# Start Codex, it will auto-load skills via list-skills
codex

# Skills are invoked automatically based on context
"Create a spec for the new dashboard feature"

# Or reference them explicitly in your prompt
"Use the spec-driven-dev skill to plan this feature"
```

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md              # Core instructions (required)
│   ├── YAML frontmatter  # name, description, metadata
│   └── Instructions      # Markdown content
├── scripts/              # Executable utilities (optional)
├── references/           # Documentation to load as needed (optional)
└── assets/               # Templates and output files (optional)
```

### SKILL.md Format

```markdown
---
name: skill-identifier
description: Clear description of what the skill does and when to use it
---

# Skill Name

[Instructions that Claude will follow when using this skill]
```

## Creating Your Own Skills

Use the **skill-creator** skill to design and build custom skills:

```bash
# In Claude Code
"Help me create a skill for [your use case]"

# The skill-creator will guide you through:
# 1. Understanding concrete examples
# 2. Planning reusable contents
# 3. Initializing the skill structure
# 4. Editing SKILL.md and resources
# 5. Packaging for distribution
```

## Development Workflow Example

Here's how the development skills work together:

```bash
# 1. Create a specification
"Create a spec for adding rate limiting to the API"
# Uses: spec-driven-dev
# Output: specs/features/rate-limiting/{requirements.md, plan.md, tasks.md}

# 2. Implement the specification
"Implement the rate limiting spec"
# Uses: implementing-specs
# - Follows TDD (red-green-refactor)
# - Runs quality gates after each task
# - Maintains 80%+ test coverage
# - Type checks with mypy --strict

# 3. Prepare for commit
"Prepare my changes for commit"
# Uses: commit-prep
# - Runs pre-commit hooks
# - Executes linters
# - Runs full test suite
# - Drafts commit message
```

## Key Differences: Claude Code vs Codex CLI

| Feature | Claude Code | Codex CLI |
|---------|-------------|-----------|
| Skill Discovery | Native, automatic | Requires `list-skills` script |
| Installation | Copy to `~/.claude/skills/` | Copy to `~/.codex/skills/` |
| Configuration | None needed | Add instruction to `AGENTS.md` |
| Invocation | Automatic or `/skill` | Automatic after setup |
| Plugin System | Built-in (`/plugin install`) | Manual installation |

## Best Practices

### For Using Skills

- Let Claude choose skills automatically based on context
- Skills are most effective for repetitive, specialized tasks
- Review skill outputs and provide feedback for iteration

### For Creating Skills

- Start with concrete usage examples
- Keep SKILL.md concise (<5k words)
- Move detailed documentation to `references/`
- Store reusable code in `scripts/`
- Use `assets/` for templates and output files
- Follow progressive disclosure: metadata → SKILL.md → resources

## Contributing

To add skills to this collection:

1. Use the **skill-creator** skill to design your skill
2. Test thoroughly with real tasks
3. Package using the validation script
4. Submit with clear documentation

## License

Skills may have individual licenses. Check each skill's SKILL.md or LICENSE file for details.

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Official Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Codex CLI Skills Guide](https://www.robert-glaser.de/claude-skills-in-codex-cli/)

## Troubleshooting

### Claude Code

**Skills not appearing:**
- Verify skills are in `~/.claude/skills/`
- Check SKILL.md has valid YAML frontmatter
- Restart Claude Code

### Codex CLI

**Skills not loading:**
- Verify `list-skills` is in PATH and executable
- Check `~/.codex/skills/` contains skill folders
- Confirm `AGENTS.md` has discovery instruction
- Run `list-skills` manually to test

**Skill not triggering:**
- Improve the `description` field in YAML frontmatter
- Be more explicit in your prompts
- Reference the skill by name directly

## Support

For issues with:
- **Claude Code**: [GitHub Issues](https://github.com/anthropics/claude-code/issues)
- **Skills Framework**: [Anthropic Skills Repository](https://github.com/anthropics/skills)
- **This Collection**: Open an issue in this repository
