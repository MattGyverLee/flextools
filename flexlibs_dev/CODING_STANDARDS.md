# Coding Standards

## Complete Data Access Initiative - Python Coding Standards

**Version**: 1.0
**Last Updated**: 2025-11-22
**Scope**: FlexTools flexlibs_dev module and all data access methods

---

## 🎯 Philosophy

Our coding standards prioritize:

1. **Pythonic Code**: Embrace Python idioms and conventions
2. **Readability**: Code is read more often than written
3. **Maintainability**: Make it easy for others to understand and modify
4. **Consistency**: Follow established patterns across the codebase
5. **Safety**: Type hints, error handling, and defensive programming

---

## 1. PYTHON VERSION & COMPATIBILITY

### 1.1 Target Version
- **Minimum**: Python 3.7
- **Recommended**: Python 3.8+
- **Target**: Python 3.11+ for new development

### 1.2 Compatibility Requirements
```python
# Use features compatible with Python 3.7+
# Avoid Python 3.10+ exclusive features unless documented

# Good (3.7+ compatible)
from typing import Optional, List, Dict

# Avoid (3.10+ only)
# def foo(items: list[str]) -> str | None:  # Use Union instead
```

### 1.3 Future Compatibility
- Write code that will work with Python 3.12+
- Use `from __future__ import annotations` when beneficial
- Avoid deprecated features

---

## 2. CODE FORMATTING

### 2.1 Formatter: Black
We use **Black** as our code formatter with default settings.

```bash
# Install
pip install black

# Format files
black flexlibs_dev/

# Check without modifying
black --check flexlibs_dev/
```

**Configuration** (pyproject.toml):
```toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
```

### 2.2 Key Black Conventions
- Line length: 88 characters
- Double quotes for strings
- Trailing commas in multi-line structures
- 2 blank lines between top-level definitions

**Example:**
```python
# Black formatted code
def TextCreate(
    self,
    name: str,
    genre: Optional[str] = None,
) -> IText:
    """Create a new text."""
    return self._create_text(
        name=name,
        genre=genre,
        writing_system=self.default_ws,
    )
```

---

## 3. NAMING CONVENTIONS

### 3.1 Methods (PascalCase for FlexTools API)
```python
# Public API methods - PascalCase (FlexTools convention)
def TextCreate(self, name: str) -> IText:
    pass

def ParagraphDelete(self, para_or_hvo: Union[IStTxtPara, int]) -> None:
    pass

# Internal/helper methods - snake_case
def _validate_name(self, name: str) -> bool:
    pass

def _get_default_ws(self) -> int:
    pass
```

**Rationale**: FlexTools has established PascalCase for public API methods. We maintain this for consistency with existing code.

### 3.2 Variables & Parameters (snake_case)
```python
# Good
text_name = "Genesis"
writing_system = self.project.DefaultVernacularWritingSystem
segment_count = 0

# Bad
TextName = "Genesis"  # Avoid
textName = "Genesis"  # Avoid
```

### 3.3 Constants (UPPER_SNAKE_CASE)
```python
# Module-level constants
MAX_TEXT_LENGTH = 10000
DEFAULT_GENRE = "Narrative"
SUPPORTED_VERSIONS = ["9.0", "9.1"]
```

### 3.4 Classes (PascalCase)
```python
class TextOperations:
    """Text CRUD operations."""
    pass

class FlexToolsCache:
    """FLEx object cache wrapper."""
    pass
```

### 3.5 Special Naming Patterns

#### HVO-or-Object Pattern
Use `_or_hvo` suffix for parameters that accept either an object or its HVO:
```python
def TextGetName(self, text_or_hvo: Union[IText, int]) -> str:
    """Get text name from text object or HVO."""
    pass
```

#### Writing System Parameters
Use `wsHandle` or `ws` for writing system parameters:
```python
def TextGetName(
    self,
    text_or_hvo: Union[IText, int],
    wsHandle: Optional[int] = None,
) -> str:
    pass
```

---

## 4. TYPE HINTS

### 4.1 Always Use Type Hints
```python
# Good - Full type hints
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    pass

# Bad - No type hints
def TextCreate(self, name, genre=None):
    pass
```

### 4.2 Import Types Correctly
```python
from typing import (
    Optional,
    Union,
    List,
    Dict,
    Generator,
    Tuple,
    Any,
)

# For Python 3.9+, can also use:
# from collections.abc import Generator

# COM interface types
from SIL.FieldWorks.FDO import IText, IStTxtPara, ISegment
```

### 4.3 Common Type Patterns
```python
# Optional parameters
def foo(param: Optional[str] = None) -> None:
    pass

# Union types (object or HVO)
def bar(item: Union[IText, int]) -> IText:
    pass

# Collections
def get_all() -> Generator[IText, None, None]:
    pass

def get_items() -> List[IStTxtPara]:
    pass

def get_mapping() -> Dict[str, int]:
    pass

# Return None explicitly
def delete(item: IText) -> None:
    pass
```

### 4.4 Type Aliases
For complex types, use type aliases:
```python
from typing import Union, TypeAlias

# Define reusable type aliases
TextOrHvo: TypeAlias = Union[IText, int]
ParaOrHvo: TypeAlias = Union[IStTxtPara, int]

# Use in method signatures
def TextGetName(self, text_or_hvo: TextOrHvo) -> str:
    pass
```

---

## 5. DOCSTRINGS

### 5.1 Style: Google Format
We use Google-style docstrings for consistency.

```python
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    """
    Create a new text in the FLEx project.

    This method creates a new text with the specified name and optional
    genre. The text is added to the project's text collection and can
    immediately be used for adding paragraphs and content.

    Args:
        name: The name of the text. Must be unique within the project.
        genre: Optional genre classification. If None, no genre is set.

    Returns:
        IText: The newly created text object.

    Raises:
        ValueError: If name is empty or None.
        KeyError: If a text with the same name already exists.
        RuntimeError: If FLEx database operation fails.

    Example:
        >>> db = FLExProject()
        >>> text = db.TextCreate("Genesis", genre="Narrative")
        >>> print(text.Name.BestAnalysisAlternative.Text)
        Genesis

    See Also:
        TextDelete: Delete a text
        TextExists: Check if text exists
        TextGetAll: Get all texts in project

    Note:
        This operation is automatically wrapped in an UndoableUnitOfWork.
        If the operation fails, changes will be rolled back.
    """
    pass
```

### 5.2 Docstring Sections

#### Required Sections
- **Summary line**: One-line description (imperative mood)
- **Args**: Parameter descriptions
- **Returns**: Return value description

#### Optional Sections (when applicable)
- **Raises**: Exceptions that can be raised
- **Example**: Usage examples
- **See Also**: Related methods
- **Note**: Important implementation details
- **Warning**: Critical warnings for users

### 5.3 Docstring Best Practices
```python
# Good - Clear, complete
def TextExists(self, name: str) -> bool:
    """
    Check if a text with the given name exists in the project.

    Args:
        name: The text name to search for.

    Returns:
        True if the text exists, False otherwise.

    Example:
        >>> if db.TextExists("Genesis"):
        ...     print("Text found!")
    """
    pass

# Bad - Too brief, missing details
def TextExists(self, name: str) -> bool:
    """Check if text exists."""
    pass

# Bad - Implementation details instead of behavior
def TextExists(self, name: str) -> bool:
    """Queries the cache for text by name and returns boolean."""
    pass
```

---

## 6. ERROR HANDLING

### 6.1 Be Specific with Exceptions
```python
# Good - Specific exceptions
def TextCreate(self, name: str) -> IText:
    if not name:
        raise ValueError("Text name cannot be empty")
    if self.TextExists(name):
        raise KeyError(f"Text '{name}' already exists")

# Bad - Generic exception
def TextCreate(self, name: str) -> IText:
    if not name:
        raise Exception("Invalid input")  # Too generic
```

### 6.2 Exception Hierarchy
Use appropriate exception types:

- **ValueError**: Invalid parameter values
- **TypeError**: Wrong parameter types
- **KeyError**: Object not found
- **AttributeError**: Invalid attribute access
- **RuntimeError**: FLEx operation failures
- **NotImplementedError**: Not yet implemented

### 6.3 Custom Exceptions
Define custom exceptions when appropriate:
```python
class FlexToolsError(Exception):
    """Base exception for FlexTools operations."""
    pass

class ObjectNotFoundError(FlexToolsError):
    """Raised when an object cannot be found."""
    pass

class InvalidOperationError(FlexToolsError):
    """Raised when an operation is invalid in current context."""
    pass
```

### 6.4 Error Messages
Write clear, actionable error messages:
```python
# Good - Clear and actionable
raise ValueError(
    f"Text name '{name}' exceeds maximum length of {MAX_TEXT_LENGTH} characters"
)

# Bad - Vague
raise ValueError("Invalid name")

# Good - Provides context
raise KeyError(
    f"Paragraph with HVO {hvo} not found. "
    f"It may have been deleted or belongs to a different project."
)

# Bad - No context
raise KeyError("Not found")
```

### 6.5 Exception Handling
```python
# Good - Specific exception handling
try:
    text = self.cache.GetObjectByName(name)
except AttributeError:
    raise ObjectNotFoundError(f"Text '{name}' not found")
except COMException as e:
    raise RuntimeError(f"FLEx operation failed: {e}")

# Bad - Bare except
try:
    text = self.cache.GetObjectByName(name)
except:  # Never use bare except
    return None
```

---

## 7. CODE STRUCTURE

### 7.1 Imports Organization
```python
"""Module docstring."""

# Standard library imports
import os
import sys
from pathlib import Path
from typing import Optional, Union, List, Generator

# Third-party imports
import pytest

# FLEx/COM imports
from SIL.FieldWorks.FDO import IText, IStTxtPara
from SIL.FieldWorks.Common.COMInterfaces import ITsString

# Local imports
from flexlibs_dev.utils import validate_name
from flexlibs_dev.base import FlexToolsBase
```

Order: stdlib → third-party → COM/FLEx → local

### 7.2 Function/Method Length
- Keep methods focused and concise
- Aim for <50 lines per method
- Extract helper methods for complex logic
- One method = one responsibility

```python
# Good - Focused method
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    """Create a new text."""
    self._validate_text_name(name)
    text = self._create_text_object(name)
    if genre:
        self._set_text_genre(text, genre)
    return text

# Better - Complex logic extracted
def _validate_text_name(self, name: str) -> None:
    """Validate text name meets requirements."""
    if not name:
        raise ValueError("Text name cannot be empty")
    if len(name) > MAX_TEXT_LENGTH:
        raise ValueError(f"Text name exceeds {MAX_TEXT_LENGTH} characters")
    if self.TextExists(name):
        raise KeyError(f"Text '{name}' already exists")
```

### 7.3 Class Organization
```python
class TextOperations:
    """Text CRUD operations."""

    # 1. Class-level constants
    MAX_NAME_LENGTH = 255

    # 2. __init__ and special methods
    def __init__(self, project):
        self.project = project

    def __repr__(self):
        return f"TextOperations({self.project})"

    # 3. Public API methods (alphabetically)
    def TextCreate(self, name: str) -> IText:
        pass

    def TextDelete(self, text_or_hvo: Union[IText, int]) -> None:
        pass

    def TextExists(self, name: str) -> bool:
        pass

    # 4. Private helper methods (alphabetically)
    def _create_text_object(self, name: str) -> IText:
        pass

    def _validate_text_name(self, name: str) -> None:
        pass
```

---

## 8. PYTHONIC IDIOMS

### 8.1 Use List Comprehensions
```python
# Good
text_names = [self.TextGetName(t) for t in texts]
even_hvos = [hvo for hvo in hvos if hvo % 2 == 0]

# Bad
text_names = []
for t in texts:
    text_names.append(self.TextGetName(t))
```

### 8.2 Use Generators for Large Collections
```python
# Good - Memory efficient
def TextGetAll(self) -> Generator[IText, None, None]:
    """Get all texts in project."""
    for hvo in self.cache.GetAllTextHvos():
        yield self.cache.GetObject(hvo)

# Bad - Loads everything into memory
def TextGetAll(self) -> List[IText]:
    """Get all texts in project."""
    return [self.cache.GetObject(hvo) for hvo in self.cache.GetAllTextHvos()]
```

### 8.3 Use Context Managers
```python
# Good
with UndoableUnitOfWork(self.project, "Create Text"):
    text = self._create_text(name)

# Bad
uow = UndoableUnitOfWork(self.project, "Create Text")
uow.Begin()
try:
    text = self._create_text(name)
    uow.Commit()
except:
    uow.Rollback()
```

### 8.4 Truthiness and None Checks
```python
# Good
if not name:
    raise ValueError("Name cannot be empty")

if text is None:
    return None

# Bad
if name == "":
    raise ValueError("Name cannot be empty")

if text == None:  # Don't use == for None
    return None
```

### 8.5 String Formatting
```python
# Good - f-strings (Python 3.6+)
message = f"Created text '{name}' with {count} paragraphs"

# Acceptable - format() for complex cases
message = "User {user} created {count} {item}".format(
    user=username,
    count=count,
    item="text" if count == 1 else "texts",
)

# Bad - %-formatting
message = "Created text '%s' with %d paragraphs" % (name, count)

# Bad - Concatenation
message = "Created text '" + name + "' with " + str(count) + " paragraphs"
```

### 8.6 Dictionary Operations
```python
# Good - Use get() with default
value = config.get("timeout", 30)

# Good - Use setdefault()
cache.setdefault(key, []).append(item)

# Good - Dictionary comprehension
name_to_hvo = {self.TextGetName(t): t.Hvo for t in texts}
```

---

## 9. PERFORMANCE BEST PRACTICES

### 9.1 Avoid Repeated Lookups
```python
# Good - Cache lookup result
text = self._get_text(text_or_hvo)
name = text.Name.BestAnalysisAlternative.Text
genre = text.Genre.Name.BestAnalysisAlternative.Text

# Bad - Repeated lookups
name = self._get_text(text_or_hvo).Name.BestAnalysisAlternative.Text
genre = self._get_text(text_or_hvo).Genre.Name.BestAnalysisAlternative.Text
```

### 9.2 Bulk Operations
```python
# Good - Bulk operation
def TextDeleteAll(self, text_hvos: List[int]) -> None:
    """Delete multiple texts in one transaction."""
    with UndoableUnitOfWork(self.project, "Delete Texts"):
        for hvo in text_hvos:
            self._delete_text(hvo)

# Bad - Individual transactions
def TextDeleteAll(self, text_hvos: List[int]) -> None:
    """Delete multiple texts."""
    for hvo in text_hvos:
        self.TextDelete(hvo)  # Each creates a transaction
```

### 9.3 Lazy Evaluation
```python
# Good - Generator (lazy)
def TextGetAll(self) -> Generator[IText, None, None]:
    for hvo in self.cache.GetAllTextHvos():
        yield self.cache.GetObject(hvo)

# Bad - Eager evaluation
def TextGetAll(self) -> List[IText]:
    return [self.cache.GetObject(hvo) for hvo in self.cache.GetAllTextHvos()]
```

---

## 10. COMMENTS

### 10.1 When to Comment
```python
# Good - Explain WHY, not WHAT
# FLEx requires PropChanged call after modifying TsStrings
# See: https://github.com/sillsdev/FieldWorks/issues/1234
text.Name.set_String(wsHandle, ts_string)
self.cache.PropChanged(text.Hvo, "Name")

# Good - Explain complex logic
# Binary search requires sorted list; HVOs may not be sorted in cache
sorted_hvos = sorted(hvos)
index = bisect_left(sorted_hvos, target_hvo)

# Bad - Obvious comment
# Increment counter
counter += 1

# Bad - Commented-out code (remove it)
# def OldTextCreate(self, name):
#     return self.cache.CreateText(name)
```

### 10.2 TODO Comments
```python
# Good - Actionable TODO with context
# TODO(john): Add support for RTL writing systems (#123)
# TODO: Optimize with caching after benchmarking (needs 10k+ texts)

# Bad - Vague TODO
# TODO: Fix this
# TODO: Make better
```

---

## 11. TESTING CODE STANDARDS

### 11.1 Test Naming
```python
# Good - Descriptive test names
def test_text_create_with_valid_name():
    pass

def test_text_create_raises_error_when_name_empty():
    pass

def test_text_delete_removes_from_project():
    pass

# Bad - Vague names
def test_text1():
    pass

def test_error():
    pass
```

### 11.2 AAA Pattern (Arrange-Act-Assert)
```python
def test_text_create_with_genre():
    """Test creating a text with a genre specified."""
    # Arrange
    db = FLExProject()
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

### 11.3 Test Fixtures
```python
import pytest

@pytest.fixture
def project():
    """Provide test FLEx project."""
    proj = FLExProject()
    yield proj
    proj.Close()

@pytest.fixture
def sample_text(project):
    """Provide a sample text for testing."""
    text = project.TextCreate("Test Text")
    yield text
    project.TextDelete(text)

def test_paragraph_create(sample_text):
    """Test paragraph creation with fixture."""
    para = sample_text.ParagraphCreate("Test content")
    assert para is not None
```

---

## 12. COM INTEROP STANDARDS

### 12.1 Null Checks
```python
# Good - Check for None
def TextGetName(self, text_or_hvo: Union[IText, int]) -> str:
    text = self._get_text(text_or_hvo)
    if text is None:
        raise ObjectNotFoundError(f"Text not found: {text_or_hvo}")

    name_obj = text.Name
    if name_obj is None:
        return ""

    return name_obj.BestAnalysisAlternative.Text
```

### 12.2 UndoableUnitOfWork Pattern
```python
# Good - Wrap writes in UoW
def TextCreate(self, name: str) -> IText:
    """Create a new text."""
    with UndoableUnitOfWork(self.project, "Create Text"):
        text = self._create_text_object(name)
        self.project.TextsOC.Add(text)
        self.cache.PropChanged(self.project.Hvo, "Texts")
        return text
```

### 12.3 HVO Conversions
```python
# Good - Clear HVO conversion
def _get_text(self, text_or_hvo: Union[IText, int]) -> IText:
    """Convert text or HVO to text object."""
    if isinstance(text_or_hvo, int):
        return self.cache.GetObject(text_or_hvo)
    return text_or_hvo

# Use in methods
def TextDelete(self, text_or_hvo: Union[IText, int]) -> None:
    text = self._get_text(text_or_hvo)
    # ... deletion logic
```

---

## 13. GOOD vs BAD EXAMPLES

### Example 1: Method Implementation

**Bad:**
```python
def CreateText(self, n, g=None):
    if n == None or n == "":
        return None
    try:
        t = self.cache.CreateText()
        t.Name = n
        if g != None:
            t.Genre = g
        return t
    except:
        return None
```

**Good:**
```python
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    """
    Create a new text in the project.

    Args:
        name: The name of the text. Must be unique and non-empty.
        genre: Optional genre classification for the text.

    Returns:
        The newly created text object.

    Raises:
        ValueError: If name is empty or None.
        KeyError: If a text with the same name already exists.
    """
    if not name:
        raise ValueError("Text name cannot be empty")

    if self.TextExists(name):
        raise KeyError(f"Text '{name}' already exists")

    with UndoableUnitOfWork(self.project, "Create Text"):
        text = self.cache.CreateText(name)

        if genre:
            self._set_text_genre(text, genre)

        return text
```

### Example 2: Error Handling

**Bad:**
```python
def TextGetName(self, text):
    try:
        return text.Name.BestAnalysisAlternative.Text
    except:
        return ""
```

**Good:**
```python
def TextGetName(
    self,
    text_or_hvo: Union[IText, int],
    wsHandle: Optional[int] = None,
) -> str:
    """
    Get the name of a text.

    Args:
        text_or_hvo: Text object or its HVO.
        wsHandle: Optional writing system handle. Uses default if None.

    Returns:
        The text name in the specified writing system.

    Raises:
        ObjectNotFoundError: If text does not exist.
    """
    text = self._get_text(text_or_hvo)

    if text is None:
        raise ObjectNotFoundError(f"Text not found: {text_or_hvo}")

    if wsHandle is None:
        wsHandle = self.project.DefaultAnalysisWritingSystem

    name_obj = text.Name
    if name_obj is None:
        return ""

    try:
        return name_obj.get_String(wsHandle).Text
    except AttributeError:
        return ""
```

---

## 14. TOOLS & AUTOMATION

### 14.1 Required Tools
```bash
# Install development tools
pip install black flake8 mypy pytest pytest-cov

# Format code
black flexlibs_dev/

# Lint code
flake8 flexlibs_dev/

# Type check
mypy flexlibs_dev/

# Run tests with coverage
pytest --cov=flexlibs_dev --cov-report=html
```

### 14.2 Pre-commit Hooks
Use `.pre-commit-config.yaml` to automate checks (see separate file).

### 14.3 IDE Configuration

**VSCode settings.json:**
```json
{
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "editor.formatOnSave": true,
    "python.testing.pytestEnabled": true
}
```

---

## 15. CHECKLIST FOR NEW CODE

Before submitting code, verify:

- [ ] Code formatted with Black
- [ ] Passes Flake8 linting
- [ ] Passes Mypy type checking
- [ ] All methods have type hints
- [ ] All methods have docstrings
- [ ] Error handling is specific and clear
- [ ] Tests written and passing
- [ ] Test coverage >90%
- [ ] No TODOs without issue numbers
- [ ] No commented-out code
- [ ] Imports organized correctly
- [ ] Naming follows conventions
- [ ] No hardcoded values (use constants)

---

## REFERENCES

- **PEP 8**: https://peps.python.org/pep-0008/
- **PEP 257**: https://peps.python.org/pep-0257/ (Docstrings)
- **PEP 484**: https://peps.python.org/pep-0484/ (Type Hints)
- **Black**: https://black.readthedocs.io/
- **Google Python Style Guide**: https://google.github.io/styleguide/pyguide.html

---

**End of Coding Standards**

For questions or suggestions, contact the QC team lead (Agent 5).
