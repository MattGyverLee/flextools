# Quality Control Checklist

## Complete Data Access Initiative - Code Review Checklist

**Version**: 1.0
**Last Updated**: 2025-11-22
**Purpose**: Ensure consistent, high-quality implementation of all ~290 data access methods

---

## 📋 Quick Reference

Use this checklist for every cluster implementation. Check ✅ all items before approving.

---

## 1. METHOD SIGNATURE & INTERFACE

### 1.1 Method Naming
- [ ] Method name follows Pythonic conventions (PascalCase for class methods)
- [ ] Method name is clear and descriptive (e.g., `TextCreate`, `ParagraphDelete`)
- [ ] Method name follows established patterns from existing FlexTools methods
- [ ] Method name matches the specification in PROJECT_BOARD.md

### 1.2 Parameters
- [ ] Parameters use clear, descriptive names (avoid single letters except for standard cases)
- [ ] Optional parameters have sensible defaults
- [ ] `wsHandle` parameter defaults to `None` when applicable
- [ ] HVO-or-object pattern used correctly (`text_or_hvo`, `para_or_hvo`, etc.)
- [ ] Parameter order is logical (required first, optional last)

### 1.3 Return Types
- [ ] Return type is clearly documented
- [ ] Return type matches specification
- [ ] Generators used for collection returns (not lists) when appropriate
- [ ] `None` returned for void operations
- [ ] Consistent types across similar methods

### 1.4 Type Hints
- [ ] All parameters have type hints
- [ ] Return type is annotated
- [ ] Union types used correctly for HVO-or-object parameters
- [ ] Optional types used for nullable parameters
- [ ] Generic types (List, Generator, Dict) properly imported from typing

**Example:**
```python
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    """Create a new text with optional genre."""
    ...
```

---

## 2. IMPLEMENTATION QUALITY

### 2.1 Code Structure
- [ ] Method implementation is clear and readable
- [ ] No unnecessary complexity or nested logic
- [ ] Single Responsibility Principle followed
- [ ] DRY (Don't Repeat Yourself) principle applied
- [ ] Similar methods share common helper functions

### 2.2 Error Handling
- [ ] All expected errors are caught and handled appropriately
- [ ] Custom exceptions used where appropriate (avoid bare `except:`)
- [ ] Error messages are clear and actionable
- [ ] `ValueError` raised for invalid parameters
- [ ] `TypeError` raised for incorrect types
- [ ] `KeyError` or custom exceptions for missing objects
- [ ] FLEx COM exceptions properly handled and wrapped

**Good Error Example:**
```python
if not name:
    raise ValueError("Text name cannot be empty")
if not self.TextExists(name):
    raise KeyError(f"Text '{name}' not found in project")
```

**Bad Error Example:**
```python
try:
    text = self.cache.GetObjectByName(name)
except:  # Too broad, unclear
    return None
```

### 2.3 COM Interop
- [ ] COM objects accessed safely with proper null checks
- [ ] HVO (Handle Value Object) conversions correct
- [ ] Cache operations use correct methods
- [ ] UndoableUnitOfWork used for write operations
- [ ] PropChanged called after modifications
- [ ] COM object lifetime managed properly (no memory leaks)

### 2.4 Performance
- [ ] No unnecessary database queries
- [ ] Generators used for large result sets
- [ ] Caching utilized where appropriate
- [ ] Bulk operations preferred over loops when possible
- [ ] No obvious performance bottlenecks

---

## 3. DOCUMENTATION

### 3.1 Docstrings
- [ ] Method has comprehensive docstring
- [ ] Docstring follows Google or NumPy style
- [ ] Purpose clearly stated in first line
- [ ] All parameters documented with types
- [ ] Return value documented
- [ ] Exceptions documented (Raises section)
- [ ] Usage example provided for complex methods
- [ ] Related methods referenced (See Also section)

**Good Docstring Example:**
```python
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    """
    Create a new text in the project.

    Args:
        name: The name of the text. Must be unique.
        genre: Optional genre classification for the text.

    Returns:
        IText: The newly created text object.

    Raises:
        ValueError: If name is empty or None.
        KeyError: If a text with the same name already exists.

    Example:
        >>> text = db.TextCreate("Genesis", genre="Narrative")
        >>> print(text.Name.BestAnalysisAlternative.Text)
        Genesis

    See Also:
        TextDelete, TextExists, TextGetAll
    """
```

### 3.2 Code Comments
- [ ] Complex logic has explanatory comments
- [ ] "Why" comments present, not just "what"
- [ ] TODOs documented if any deferred work
- [ ] No commented-out code (remove or explain)
- [ ] FLEx API quirks documented

---

## 4. TESTING

### 4.1 Test Coverage
- [ ] All specified tests from PROJECT_BOARD.md implemented
- [ ] Each method has at least one test
- [ ] Happy path tested
- [ ] Edge cases tested
- [ ] Error conditions tested
- [ ] Coverage >90% for the cluster
- [ ] No critical paths untested

### 4.2 Test Quality
- [ ] Tests are independent (no cross-test dependencies)
- [ ] Tests use clear, descriptive names (test_text_create_with_genre)
- [ ] AAA pattern followed (Arrange, Act, Assert)
- [ ] Fixtures used for common setup
- [ ] Test data is realistic
- [ ] Tests clean up after themselves
- [ ] No hardcoded paths or project-specific assumptions

**Good Test Example:**
```python
def test_text_create_with_genre(db):
    """Test creating a text with a genre specified."""
    # Arrange
    name = "Genesis"
    genre = "Narrative"

    # Act
    text = db.TextCreate(name, genre=genre)

    # Assert
    assert text is not None
    assert db.TextGetName(text) == name
    assert db.TextGetGenre(text) == genre

    # Cleanup
    db.TextDelete(text)
```

### 4.3 Integration Tests
- [ ] Integration test verifies cluster methods work together
- [ ] Realistic workflow tested
- [ ] Data persists correctly
- [ ] No test failures
- [ ] Tests run in reasonable time (<5 seconds per test preferred)

---

## 5. CONSISTENCY & STANDARDS

### 5.1 Naming Consistency
- [ ] Follows established FlexTools naming patterns
- [ ] Consistent with similar methods in other clusters
- [ ] Uses standard terminology (Text, Paragraph, Segment, etc.)
- [ ] No abbreviations unless standard (POS, MSA, HVO)

### 5.2 Pattern Consistency
- [ ] CRUD operations follow consistent pattern:
  - `Create` returns the created object
  - `Delete` returns None
  - `GetAll` returns Generator
  - `Get/Set` pairs for properties
  - `Exists` returns bool
  - `Find` returns object or None
- [ ] HVO-or-object pattern applied consistently
- [ ] Writing system handling consistent

### 5.3 Code Style
- [ ] Passes `black` formatter
- [ ] Passes `flake8` linter
- [ ] Passes `mypy` type checker
- [ ] No unused imports
- [ ] Imports properly organized (stdlib, third-party, local)
- [ ] Line length <100 characters (black default: 88)

---

## 6. SECURITY & SAFETY

### 6.1 Input Validation
- [ ] All user inputs validated
- [ ] Type checking for critical parameters
- [ ] Range/bounds checking where applicable
- [ ] No SQL injection vulnerabilities (if any raw SQL)
- [ ] File paths sanitized if applicable

### 6.2 Data Integrity
- [ ] Transactions used for multi-step operations
- [ ] Rollback on errors
- [ ] No partial state modifications
- [ ] Database constraints respected
- [ ] Referential integrity maintained

### 6.3 Resource Management
- [ ] No resource leaks (file handles, COM objects)
- [ ] Proper cleanup in error paths
- [ ] Context managers used where appropriate

---

## 7. COMPATIBILITY & DEPENDENCIES

### 7.1 FLEx Version Compatibility
- [ ] Compatible with FLEx 9.x
- [ ] Known limitations documented
- [ ] Version-specific features flagged
- [ ] Graceful degradation if possible

### 7.2 Dependencies
- [ ] No new dependencies added without justification
- [ ] Dependencies documented in requirements.txt
- [ ] Version pins appropriate
- [ ] No circular dependencies

---

## 8. INTEGRATION & REGRESSION

### 8.1 Backward Compatibility
- [ ] No breaking changes to existing FlexTools API
- [ ] Existing tests still pass
- [ ] Migration path documented if changes required
- [ ] Deprecation warnings if methods replaced

### 8.2 Integration Points
- [ ] Works with existing FlexTools modules
- [ ] No conflicts with existing methods
- [ ] Properly integrates with FLExProject lifecycle
- [ ] Database operations compatible with FLEx

---

## 9. DOCUMENTATION & EXAMPLES

### 9.1 API Documentation
- [ ] Added to API reference documentation
- [ ] Method signature correct in docs
- [ ] Examples provided
- [ ] Common use cases documented

### 9.2 User Guide
- [ ] Usage examples added to user guide if significant feature
- [ ] Tutorial updated if applicable
- [ ] Migration guide updated if changes affect existing code

---

## 10. RELEASE READINESS

### 10.1 Code Review
- [ ] Code reviewed by at least one other developer
- [ ] All review comments addressed
- [ ] No outstanding TODOs or FIXMEs
- [ ] Approved by QC specialist (Agent 5)

### 10.2 CI/CD
- [ ] All CI checks pass
- [ ] No test failures
- [ ] Coverage requirements met
- [ ] Linters pass
- [ ] Build succeeds

### 10.3 Documentation Complete
- [ ] CHANGELOG.md updated
- [ ] Version number incremented if applicable
- [ ] Release notes drafted
- [ ] Breaking changes documented

---

## ✅ APPROVAL CHECKLIST

Before approving a cluster implementation, verify:

- [ ] All items in sections 1-10 checked
- [ ] All tests pass
- [ ] Coverage >90%
- [ ] Documentation complete
- [ ] Code review complete
- [ ] No blockers or critical issues
- [ ] Integration test successful
- [ ] Ready for merge

---

## 🚫 COMMON ISSUES TO WATCH FOR

### Anti-Patterns
- ❌ Bare `except:` clauses
- ❌ Mutable default arguments (e.g., `def foo(items=[]):`)
- ❌ Not using context managers for resources
- ❌ String concatenation in loops (use join)
- ❌ Not validating user input

### FlexTools-Specific Issues
- ❌ Forgetting UndoableUnitOfWork for writes
- ❌ Not handling null COM objects
- ❌ HVO/object confusion
- ❌ Writing system issues (always specify when needed)
- ❌ Cache inconsistencies

### Testing Issues
- ❌ Tests depend on each other
- ❌ Tests modify global state
- ❌ No cleanup in tests
- ❌ Hardcoded project paths
- ❌ Tests take too long (>30 seconds)

---

## 📊 METRICS TO TRACK

For each cluster, record:

- **Code Coverage**: ___% (target: >90%)
- **Test Count**: ___ tests
- **Method Count**: ___ methods
- **Documentation**: Complete / Partial / Missing
- **Review Status**: Approved / Needs Work / Blocked
- **Performance**: Acceptable / Needs Optimization
- **Issues Found**: ___ (link to issue tracker)

---

## 🔍 REVIEW PRIORITY LEVELS

### P0 - Critical (Must Fix)
- Security vulnerabilities
- Data corruption risks
- Breaking changes without migration
- Test failures
- Type safety violations

### P1 - High (Should Fix)
- Missing error handling
- Incomplete documentation
- Poor performance
- Inconsistent patterns
- Code style violations

### P2 - Medium (Consider Fixing)
- Minor style issues
- Optimization opportunities
- Enhanced error messages
- Additional test cases

### P3 - Low (Nice to Have)
- Additional examples
- Refactoring opportunities
- Code comments
- Minor naming improvements

---

## 📝 REVIEWER NOTES

Use this section to add cluster-specific notes:

```
Cluster: ____
Reviewer: ____
Date: ____

Notes:
-
-
-

Issues Found:
- [P0]
- [P1]
- [P2]

Recommendation: APPROVE / NEEDS_WORK / BLOCKED
```

---

**End of Checklist**

For questions or suggestions for improving this checklist, contact the QC team lead (Agent 5).
