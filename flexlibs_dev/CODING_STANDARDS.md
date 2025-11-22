# Coding Standards

## Complete Data Access Initiative - Python Coding Standards

**Version**: 1.0
**Last Updated**: 2025-11-22

---

## 🎯 Philosophy

1. **Pythonic Code**: Embrace Python idioms
2. **Readability**: Code is read more than written
3. **Maintainability**: Easy to understand and modify
4. **Consistency**: Follow established patterns
5. **Safety**: Type hints, error handling, defensive programming

---

## 1. PYTHON VERSION

- **Minimum**: Python 3.7
- **Recommended**: Python 3.8+
- **Target**: Python 3.11+

---

## 2. CODE FORMATTING

### Black Formatter (Required)
```bash
black flexlibs_dev/
```

**Settings**:
- Line length: 88 characters
- Double quotes for strings
- Trailing commas in multi-line structures

---

## 3. NAMING CONVENTIONS

### Methods (PascalCase for FlexTools API)
```python
# Public API methods
def TextCreate(self, name: str) -> IText:
    pass

# Internal helpers
def _validate_name(self, name: str) -> bool:
    pass
```

### Variables (snake_case)
```python
text_name = "Genesis"
writing_system = self.default_ws
```

### Constants (UPPER_SNAKE_CASE)
```python
MAX_TEXT_LENGTH = 10000
DEFAULT_GENRE = "Narrative"
```

### HVO-or-Object Pattern
```python
def TextGetName(self, text_or_hvo: Union[IText, int]) -> str:
    pass
```

---

## 4. TYPE HINTS

### Always Use Type Hints
```python
from typing import Optional, Union, List, Generator, Dict

# Good
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    pass

# Bad
def TextCreate(self, name, genre=None):
    pass
```

### Common Patterns
```python
# Optional parameters
def foo(param: Optional[str] = None) -> None:
    pass

# Union types (HVO-or-object)
def bar(item: Union[IText, int]) -> IText:
    pass

# Generators
def get_all() -> Generator[IText, None, None]:
    yield text
```

---

## 5. DOCSTRINGS

### Google Style (Required)
```python
def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
    """
    Create a new text in the FLEx project.

    Args:
        name: The name of the text. Must be unique.
        genre: Optional genre classification.

    Returns:
        IText: The newly created text object.

    Raises:
        ValueError: If name is empty.
        KeyError: If text already exists.

    Example:
        >>> text = db.TextCreate("Genesis", genre="Narrative")
        >>> print(text.Name.BestAnalysisAlternative.Text)
        Genesis

    See Also:
        TextDelete, TextExists, TextGetAll
    """
    pass
```

### Required Sections
- **Summary line**: One-line description
- **Args**: Parameter descriptions
- **Returns**: Return value description
- **Raises**: Exceptions (when applicable)
- **Example**: Usage examples (for complex methods)
- **See Also**: Related methods (when applicable)

---

## 6. ERROR HANDLING

### Be Specific
```python
# Good
if not name:
    raise ValueError("Text name cannot be empty")
if self.TextExists(name):
    raise KeyError(f"Text '{name}' already exists")

# Bad
if not name:
    raise Exception("Invalid input")
```

### Exception Types
- **ValueError**: Invalid parameter values
- **TypeError**: Wrong parameter types
- **KeyError**: Object not found
- **RuntimeError**: FLEx operation failures

### Clear Error Messages
```python
# Good
raise ValueError(
    f"Text name '{name}' exceeds maximum length of {MAX_TEXT_LENGTH} characters"
)

# Bad
raise ValueError("Invalid name")
```

---

## 7. CODE STRUCTURE

### Import Organization
```python
# Standard library
import os
from pathlib import Path
from typing import Optional, Union

# Third-party
import pytest

# FLEx/COM
from SIL.FieldWorks.FDO import IText

# Local
from flexlibs_dev.utils import validate_name
```

### Function Length
- Keep methods <50 lines
- Extract helper methods for complex logic
- One method = one responsibility

---

## 8. PYTHONIC IDIOMS

### List Comprehensions
```python
# Good
text_names = [self.TextGetName(t) for t in texts]

# Bad
text_names = []
for t in texts:
    text_names.append(self.TextGetName(t))
```

### Generators for Large Collections
```python
# Good - Memory efficient
def TextGetAll(self) -> Generator[IText, None, None]:
    for hvo in self.cache.GetAllTextHvos():
        yield self.cache.GetObject(hvo)
```

### Context Managers
```python
# Good
with UndoableUnitOfWork(self.project, "Create Text"):
    text = self._create_text(name)
```

### String Formatting
```python
# Good - f-strings
message = f"Created text '{name}' with {count} paragraphs"

# Bad - concatenation
message = "Created text '" + name + "' with " + str(count) + " paragraphs"
```

---

## 9. COM INTEROP

### Null Checks
```python
def TextGetName(self, text_or_hvo: Union[IText, int]) -> str:
    text = self._get_text(text_or_hvo)
    if text is None:
        raise ObjectNotFoundError(f"Text not found: {text_or_hvo}")
    
    name_obj = text.Name
    if name_obj is None:
        return ""
    
    return name_obj.BestAnalysisAlternative.Text
```

### UndoableUnitOfWork
```python
def TextCreate(self, name: str) -> IText:
    with UndoableUnitOfWork(self.project, "Create Text"):
        text = self._create_text_object(name)
        self.project.TextsOC.Add(text)
        return text
```

---

## 10. TESTING CODE STANDARDS

### Test Naming
```python
def test_text_create_with_valid_name():
    pass

def test_text_create_raises_error_when_name_empty():
    pass
```

### AAA Pattern
```python
def test_text_create_with_genre():
    # Arrange
    name = "Genesis"
    genre = "Narrative"
    
    # Act
    text = db.TextCreate(name, genre=genre)
    
    # Assert
    assert text is not None
    assert db.TextGetName(text) == name
    
    # Cleanup
    db.TextDelete(text)
```

---

## 11. TOOLS

### Required
```bash
# Install
pip install black flake8 mypy pytest pytest-cov

# Format
black flexlibs_dev/

# Lint
flake8 flexlibs_dev/

# Type check
mypy flexlibs_dev/

# Test
pytest --cov=flexlibs_dev
```

---

## 12. CHECKLIST

Before submitting code:

- [ ] Code formatted with Black
- [ ] Passes Flake8
- [ ] Passes Mypy
- [ ] All methods have type hints
- [ ] All methods have docstrings
- [ ] Error handling is specific
- [ ] Tests written and passing
- [ ] Coverage >90%
- [ ] No TODOs without issue numbers
- [ ] Imports organized correctly

---

## REFERENCES

- **PEP 8**: https://peps.python.org/pep-0008/
- **Black**: https://black.readthedocs.io/
- **Google Style Guide**: https://google.github.io/styleguide/pyguide.html

---

**End of Coding Standards**
