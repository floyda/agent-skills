#!/bin/bash
# Quality gates script for Python projects
# Runs all standard quality checks that a principal developer would require
# Exit code 0 = all checks pass, non-zero = at least one check failed

set -e  # Exit on first error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track overall status
OVERALL_STATUS=0

# Configuration
MIN_COVERAGE=${MIN_COVERAGE:-80}
PROJECT_ROOT=${PROJECT_ROOT:-.}

echo "================================"
echo "Running Quality Gates"
echo "================================"
echo ""

# Function to run a check
run_check() {
    local name=$1
    local command=$2

    echo -e "${YELLOW}Running: ${name}${NC}"
    if eval "$command"; then
        echo -e "${GREEN}✓ ${name} passed${NC}"
        echo ""
        return 0
    else
        echo -e "${RED}✗ ${name} failed${NC}"
        echo ""
        OVERALL_STATUS=1
        return 1
    fi
}

# Change to project root
cd "$PROJECT_ROOT"

# 1. Linting (ruff)
run_check "Linting (ruff)" "ruff check ." || true

# 2. Formatting check (black)
run_check "Formatting (black)" "black --check ." || true

# 3. Import sorting (isort)
run_check "Import sorting (isort)" "isort --check-only ." || true

# 4. Type checking (mypy)
run_check "Type checking (mypy)" "mypy ." || true

# 5. Spell checking (codespell)
if command -v codespell &> /dev/null; then
    run_check "Spell checking (codespell)" "codespell" || true
fi

# 6. Tests with coverage
run_check "Tests with coverage" "pytest --cov=src --cov-report=term --cov-report=html --cov-fail-under=${MIN_COVERAGE}" || true

# Final summary
echo "================================"
if [ $OVERALL_STATUS -eq 0 ]; then
    echo -e "${GREEN}All quality gates passed ✓${NC}"
else
    echo -e "${RED}Some quality gates failed ✗${NC}"
fi
echo "================================"

exit $OVERALL_STATUS
