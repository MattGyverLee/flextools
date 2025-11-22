#!/bin/bash
# Verification Agent (Agent 4) - Automated Verification Script
# Purpose: Verify agent work completion before allowing merge
# Usage: ./verify_agent_work.sh <module_path> <expected_test_count>

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

MODULE_PATH=${1:-"flexlibs_dev"}
EXPECTED_TESTS=${2:-0}
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "========================================="
echo "VERIFICATION AGENT - Starting Verification"
echo "Timestamp: $TIMESTAMP"
echo "Module: $MODULE_PATH"
echo "========================================="
echo ""

# Track overall status
VERIFICATION_PASSED=true

# 1. Check Python environment
echo "1. Checking Python environment..."
if ! python --version >/dev/null 2>&1; then
    echo -e "${RED}❌ FAIL: Python not found${NC}"
    VERIFICATION_PASSED=false
else
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}✅ PASS: $PYTHON_VERSION${NC}"
fi
echo ""

# 2. Check required packages
echo "2. Checking required packages..."
REQUIRED_PACKAGES=("pytest" "black" "flake8" "mypy")
for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! python -c "import $package" 2>/dev/null; then
        echo -e "${RED}❌ FAIL: Package '$package' not installed${NC}"
        VERIFICATION_PASSED=false
    else
        echo -e "${GREEN}✅ PASS: Package '$package' installed${NC}"
    fi
done
echo ""

# 3. Verify all claimed modules import successfully
echo "3. Verifying module imports..."
MODULES=("flexlibs_dev.core" "flexlibs_dev.text_ops" "flexlibs_dev.paragraph_segment_ops" "flexlibs_dev.wordform_ops")
for module in "${MODULES[@]}"; do
    if python -c "import $module" 2>/dev/null; then
        echo -e "${GREEN}✅ PASS: $module imports successfully${NC}"
    else
        echo -e "${RED}❌ FAIL: $module import failed${NC}"
        VERIFICATION_PASSED=false
        # Show the actual error
        python -c "import $module" 2>&1 || true
    fi
done
echo ""

# 4. Check directory structure
echo "4. Verifying directory structure..."
REQUIRED_DIRS=(
    "flexlibs_dev/core"
    "flexlibs_dev/text_ops"
    "flexlibs_dev/paragraph_segment_ops"
    "flexlibs_dev/wordform_ops"
    "flexlibs_dev/tests"
)
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo -e "${GREEN}✅ PASS: Directory '$dir' exists${NC}"
    else
        echo -e "${RED}❌ FAIL: Directory '$dir' missing${NC}"
        VERIFICATION_PASSED=false
    fi
done
echo ""

# 5. Check required files exist
echo "5. Verifying required files..."
REQUIRED_FILES=(
    "flexlibs_dev/__init__.py"
    "flexlibs_dev/core/__init__.py"
    "flexlibs_dev/core/types.py"
    "flexlibs_dev/core/resolvers.py"
    "flexlibs_dev/core/validators.py"
    "flexlibs_dev/core/exceptions.py"
    "flexlibs_dev/core/constants.py"
    "flexlibs_dev/tests/test_integration.py"
)
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✅ PASS: File '$file' exists${NC}"
    else
        echo -e "${RED}❌ FAIL: File '$file' missing${NC}"
        VERIFICATION_PASSED=false
    fi
done
echo ""

# 6. Run basic syntax checks (flake8 for critical errors only)
echo "6. Running syntax checks (flake8)..."
if flake8 flexlibs_dev/ --count --select=E9,F63,F7,F82 --show-source --statistics 2>/dev/null; then
    echo -e "${GREEN}✅ PASS: No critical syntax errors${NC}"
else
    echo -e "${RED}❌ FAIL: Syntax errors found${NC}"
    VERIFICATION_PASSED=false
fi
echo ""

# 7. Run tests (if pytest available)
echo "7. Running tests..."
if python -m pytest --version &> /dev/null; then
    # Run tests and capture output
    if python -m pytest flexlibs_dev/tests/ -v --tb=short > test_results.tmp 2>&1; then
        TEST_PASS=true
        echo -e "${GREEN}✅ PASS: All tests passed${NC}"
        # Show summary
        grep -E "passed|failed|error" test_results.tmp | tail -1 || true
    else
        TEST_PASS=false
        echo -e "${RED}❌ FAIL: Tests failed${NC}"
        VERIFICATION_PASSED=false
        # Show failure details
        cat test_results.tmp
    fi

    # Check test count if specified
    if [ "$EXPECTED_TESTS" -gt 0 ]; then
        ACTUAL_TESTS=$(grep -oP '\d+(?= passed)' test_results.tmp | head -1 || echo "0")
        if [ "$ACTUAL_TESTS" -ge "$EXPECTED_TESTS" ]; then
            echo -e "${GREEN}✅ PASS: Test count ($ACTUAL_TESTS) meets expectation (>= $EXPECTED_TESTS)${NC}"
        else
            echo -e "${RED}❌ FAIL: Test count ($ACTUAL_TESTS) below expectation ($EXPECTED_TESTS)${NC}"
            VERIFICATION_PASSED=false
        fi
    fi

    rm -f test_results.tmp
else
    echo -e "${YELLOW}⚠️  SKIP: pytest not available${NC}"
fi
echo ""

# 8. Check documentation exists
echo "8. Verifying documentation..."
DOC_FILES=(
    "flexlibs_dev/README.md"
    "flexlibs_dev/ARCHITECTURE.md"
    "flexlibs_dev/CODING_STANDARDS.md"
    "flexlibs_dev/TESTING_GUIDELINES.md"
)
for doc in "${DOC_FILES[@]}"; do
    if [ -f "$doc" ]; then
        echo -e "${GREEN}✅ PASS: Documentation '$doc' exists${NC}"
    else
        echo -e "${YELLOW}⚠️  WARNING: Documentation '$doc' missing${NC}"
    fi
done
echo ""

# 9. Check for TODO/FIXME markers (informational only)
echo "9. Checking for TODO/FIXME markers (informational)..."
TODO_COUNT=$(grep -r "TODO\|FIXME" flexlibs_dev/*.py flexlibs_dev/**/*.py 2>/dev/null | grep -v "NotImplementedError" | wc -l || echo "0")
if [ "$TODO_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}⚠️  INFO: Found $TODO_COUNT TODO/FIXME markers${NC}"
else
    echo -e "${GREEN}✅ INFO: No TODO/FIXME markers found${NC}"
fi
echo ""

# Final Report
echo "========================================="
echo "VERIFICATION REPORT"
echo "========================================="
if [ "$VERIFICATION_PASSED" = true ]; then
    echo -e "${GREEN}✅ ALL VERIFICATION CHECKS PASSED${NC}"
    echo ""
    echo "Agent work is verified and ready for the next stage."
    echo "Timestamp: $TIMESTAMP"
    exit 0
else
    echo -e "${RED}❌ VERIFICATION FAILED${NC}"
    echo ""
    echo "Please fix the issues above before proceeding."
    echo "Timestamp: $TIMESTAMP"
    exit 1
fi
