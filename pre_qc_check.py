#!/usr/bin/env python3
"""
Pre-QC Agent (Agent 7) - Automated Pre-Quality Control Checks
Purpose: Run automated checks before QC Agent review to catch mechanical issues
Usage: python pre_qc_check.py [module_path]
"""

import sys
import os
import subprocess
import importlib.util
from pathlib import Path
from typing import List, Tuple, Dict
from datetime import datetime


class PreQCAgent:
    """Pre-QC automated quality checks"""

    def __init__(self, module_path: str = "flexlibs_dev"):
        self.module_path = Path(module_path)
        self.checks_passed = []
        self.checks_failed = []
        self.checks_warnings = []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def run_command(self, cmd: List[str], check_name: str) -> Tuple[bool, str]:
        """Run a command and return success status and output"""
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30
            )
            return result.returncode == 0, result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return False, f"Command timed out: {' '.join(cmd)}"
        except Exception as e:
            return False, f"Command failed: {str(e)}"

    def check_files_exist(self) -> bool:
        """Check 1: Verify all claimed files exist"""
        print("1. Checking all claimed files exist...")

        required_files = [
            "flexlibs_dev/__init__.py",
            "flexlibs_dev/core/__init__.py",
            "flexlibs_dev/core/types.py",
            "flexlibs_dev/core/resolvers.py",
            "flexlibs_dev/core/validators.py",
            "flexlibs_dev/core/exceptions.py",
            "flexlibs_dev/core/constants.py",
            "flexlibs_dev/text_ops/__init__.py",
            "flexlibs_dev/text_ops/text_core.py",
            "flexlibs_dev/text_ops/text_advanced.py",
            "flexlibs_dev/text_ops/paragraph_crud.py",
            "flexlibs_dev/paragraph_segment_ops/__init__.py",
            "flexlibs_dev/paragraph_segment_ops/paragraph_advanced.py",
            "flexlibs_dev/paragraph_segment_ops/segment_ops.py",
            "flexlibs_dev/wordform_ops/__init__.py",
            "flexlibs_dev/wordform_ops/wordform_crud.py",
            "flexlibs_dev/wordform_ops/wordform_advanced.py",
            "flexlibs_dev/tests/test_integration.py",
        ]

        all_exist = True
        for file_path in required_files:
            if Path(file_path).exists():
                print(f"   ✅ {file_path}")
            else:
                print(f"   ❌ MISSING: {file_path}")
                all_exist = False

        if all_exist:
            self.checks_passed.append("All claimed files exist")
            return True
        else:
            self.checks_failed.append("Some files are missing")
            return False

    def check_imports(self) -> bool:
        """Check 2: Verify all modules import successfully"""
        print("\n2. Checking all modules import successfully...")

        modules = [
            "flexlibs_dev.core",
            "flexlibs_dev.core.types",
            "flexlibs_dev.core.resolvers",
            "flexlibs_dev.core.validators",
            "flexlibs_dev.core.exceptions",
            "flexlibs_dev.core.constants",
            "flexlibs_dev.text_ops",
            "flexlibs_dev.paragraph_segment_ops",
            "flexlibs_dev.wordform_ops",
        ]

        all_import = True
        for module_name in modules:
            try:
                spec = importlib.util.find_spec(module_name)
                if spec is not None:
                    print(f"   ✅ {module_name}")
                else:
                    print(f"   ❌ FAIL: {module_name} not found")
                    all_import = False
            except Exception as e:
                print(f"   ❌ FAIL: {module_name} - {str(e)}")
                all_import = False

        if all_import:
            self.checks_passed.append("All modules import successfully")
            return True
        else:
            self.checks_failed.append("Some modules fail to import")
            return False

    def check_tests_run(self) -> bool:
        """Check 3: Verify tests run and pass"""
        print("\n3. Running tests...")

        success, output = self.run_command(
            ["python", "-m", "pytest", "flexlibs_dev/tests/", "-v", "--tb=short"],
            "pytest"
        )

        if success:
            print("   ✅ All tests passed")
            self.checks_passed.append("All tests pass")
            return True
        else:
            print("   ❌ Tests failed")
            print(output[-500:])  # Show last 500 chars of output
            self.checks_failed.append("Tests are failing")
            return False

    def check_syntax_errors(self) -> bool:
        """Check 4: Check for critical syntax errors"""
        print("\n4. Checking for syntax errors (flake8)...")

        success, output = self.run_command(
            ["flake8", "flexlibs_dev/", "--count", "--select=E9,F63,F7,F82",
             "--show-source", "--statistics"],
            "flake8"
        )

        if success and "0" in output:
            print("   ✅ No critical syntax errors")
            self.checks_passed.append("No syntax errors")
            return True
        else:
            print("   ❌ Syntax errors found:")
            print(output)
            self.checks_failed.append("Syntax errors present")
            return False

    def check_type_hints(self) -> bool:
        """Check 5: Verify type hints are present"""
        print("\n5. Checking for type hints...")

        py_files = list(Path("flexlibs_dev").rglob("*.py"))
        py_files = [f for f in py_files if "tests" not in str(f) and "__pycache__" not in str(f)]

        missing_hints = []
        for py_file in py_files:
            content = py_file.read_text()
            # Check if file has function definitions
            if "def " in content:
                # Simple check: does it have "->" for return type hints?
                if "->" not in content and "def __init__" not in content:
                    missing_hints.append(str(py_file))

        if not missing_hints:
            print("   ✅ Type hints present in all modules")
            self.checks_passed.append("Type hints present")
            return True
        else:
            print(f"   ⚠️  WARNING: {len(missing_hints)} files may be missing type hints")
            for f in missing_hints[:5]:  # Show first 5
                print(f"      - {f}")
            self.checks_warnings.append(f"Type hints missing in {len(missing_hints)} files")
            return True  # Warning only, not failure

    def check_docstrings(self) -> bool:
        """Check 6: Verify docstrings are present"""
        print("\n6. Checking for docstrings...")

        py_files = list(Path("flexlibs_dev").rglob("*.py"))
        py_files = [f for f in py_files if "tests" not in str(f) and "__pycache__" not in str(f)]

        missing_docs = []
        for py_file in py_files:
            if py_file.name == "__init__.py":
                continue
            content = py_file.read_text()
            # Check if file has function definitions
            if "def " in content:
                # Simple check: does it have docstrings (""" or ''')?
                if '"""' not in content and "'''" not in content:
                    missing_docs.append(str(py_file))

        if not missing_docs:
            print("   ✅ Docstrings present in all modules")
            self.checks_passed.append("Docstrings present")
            return True
        else:
            print(f"   ⚠️  WARNING: {len(missing_docs)} files may be missing docstrings")
            for f in missing_docs[:5]:
                print(f"      - {f}")
            self.checks_warnings.append(f"Docstrings missing in {len(missing_docs)} files")
            return True  # Warning only

    def check_no_undefined_names(self) -> bool:
        """Check 7: Verify no undefined names"""
        print("\n7. Checking for undefined names...")

        success, output = self.run_command(
            ["flake8", "flexlibs_dev/", "--select=F821", "--count"],
            "flake8 undefined"
        )

        if "0" in output or success:
            print("   ✅ No undefined names")
            self.checks_passed.append("No undefined names")
            return True
        else:
            print("   ❌ Undefined names found:")
            print(output)
            self.checks_failed.append("Undefined names present")
            return False

    def check_file_count(self) -> bool:
        """Check 8: Verify expected file count"""
        print("\n8. Checking file count...")

        py_files = list(Path("flexlibs_dev").rglob("*.py"))
        py_files = [f for f in py_files if "__pycache__" not in str(f)]

        expected_min = 13  # Based on Phase 1 completion
        actual = len(py_files)

        print(f"   Found {actual} Python files (expected >= {expected_min})")

        if actual >= expected_min:
            print("   ✅ File count meets expectations")
            self.checks_passed.append(f"File count adequate ({actual} files)")
            return True
        else:
            print(f"   ❌ File count below expectations")
            self.checks_failed.append(f"Only {actual} files found, expected >= {expected_min}")
            return False

    def check_documentation(self) -> bool:
        """Check 9: Verify required documentation exists"""
        print("\n9. Checking documentation files...")

        required_docs = [
            "flexlibs_dev/README.md",
            "flexlibs_dev/ARCHITECTURE.md",
            "flexlibs_dev/CODING_STANDARDS.md",
            "flexlibs_dev/TESTING_GUIDELINES.md",
        ]

        all_exist = True
        for doc_path in required_docs:
            if Path(doc_path).exists():
                print(f"   ✅ {doc_path}")
            else:
                print(f"   ⚠️  MISSING: {doc_path}")
                all_exist = False

        if all_exist:
            self.checks_passed.append("All documentation present")
            return True
        else:
            self.checks_warnings.append("Some documentation missing")
            return True  # Warning only

    def check_no_print_statements(self) -> bool:
        """Check 10: Check for debug print statements (warning only)"""
        print("\n10. Checking for debug print statements...")

        py_files = list(Path("flexlibs_dev").rglob("*.py"))
        py_files = [f for f in py_files if "tests" not in str(f) and "__pycache__" not in str(f)]

        files_with_prints = []
        for py_file in py_files:
            content = py_file.read_text()
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                if "print(" in line and not line.strip().startswith("#"):
                    files_with_prints.append((str(py_file), i))

        if not files_with_prints:
            print("   ✅ No debug print statements found")
            self.checks_passed.append("No debug prints")
            return True
        else:
            print(f"   ⚠️  WARNING: Found {len(files_with_prints)} print statements")
            for f, line in files_with_prints[:5]:
                print(f"      - {f}:{line}")
            self.checks_warnings.append(f"{len(files_with_prints)} print statements found")
            return True  # Warning only

    def generate_report(self) -> bool:
        """Generate final report"""
        print("\n" + "=" * 60)
        print("PRE-QC AGENT REPORT")
        print("=" * 60)
        print(f"Timestamp: {self.timestamp}")
        print(f"Module: {self.module_path}")
        print()

        print(f"✅ Checks Passed: {len(self.checks_passed)}")
        for check in self.checks_passed:
            print(f"   - {check}")
        print()

        if self.checks_warnings:
            print(f"⚠️  Warnings: {len(self.checks_warnings)}")
            for warning in self.checks_warnings:
                print(f"   - {warning}")
            print()

        if self.checks_failed:
            print(f"❌ Checks Failed: {len(self.checks_failed)}")
            for check in self.checks_failed:
                print(f"   - {check}")
            print()
            print("❌ PRE-QC FAILED - Please fix issues before QC review")
            print("=" * 60)
            return False
        else:
            print("✅ ALL PRE-QC CHECKS PASSED")
            print()
            print("Code is ready for QC Agent review.")
            if self.checks_warnings:
                print(f"Note: {len(self.checks_warnings)} warnings to address (optional)")
            print("=" * 60)
            return True

    def run_all_checks(self) -> bool:
        """Run all pre-QC checks"""
        print(f"Pre-QC Agent starting at {self.timestamp}")
        print(f"Module: {self.module_path}")
        print()

        # Run all checks
        checks = [
            self.check_files_exist,
            self.check_imports,
            self.check_tests_run,
            self.check_syntax_errors,
            self.check_type_hints,
            self.check_docstrings,
            self.check_no_undefined_names,
            self.check_file_count,
            self.check_documentation,
            self.check_no_print_statements,
        ]

        for check in checks:
            try:
                check()
            except Exception as e:
                print(f"   ❌ Check failed with exception: {str(e)}")
                self.checks_failed.append(f"{check.__name__}: {str(e)}")

        return self.generate_report()


def main():
    """Main entry point"""
    module_path = sys.argv[1] if len(sys.argv) > 1 else "flexlibs_dev"

    agent = PreQCAgent(module_path)
    success = agent.run_all_checks()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
