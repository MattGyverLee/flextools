# Testing Guidelines

## Complete Data Access Initiative - Testing Standards & Requirements

**Version**: 1.0
**Last Updated**: 2025-11-22
**Framework**: pytest
**Coverage Target**: >90%

---

## 🎯 Testing Philosophy

Our testing approach emphasizes:

1. **Comprehensive Coverage**: Every method tested, every path validated
2. **Independence**: Tests don't depend on each other
3. **Clarity**: Tests serve as documentation
4. **Speed**: Fast enough to run frequently
5. **Reliability**: No flaky tests

---

## 1. TESTING FRAMEWORK

### 1.1 Tools
- **Test Framework**: pytest 7.0+
- **Coverage Tool**: pytest-cov
- **Fixtures**: pytest fixtures
- **Mocking**: unittest.mock or pytest-mock
- **Test Data**: pytest fixtures + factory pattern

### 1.2 Installation
```bash
pip install pytest pytest-cov pytest-mock
```

### 1.3 Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=flexlibs_dev --cov-report=html

# Run specific test file
pytest tests/test_text_ops.py

# Run specific test
pytest tests/test_text_ops.py::test_text_create

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x

# Run only failed tests from last run
pytest --lf
```

---

## 2. TEST ORGANIZATION

### 2.1 Directory Structure
```
flexlibs_dev/
├── text_ops/
│   ├── __init__.py
│   └── text_operations.py
├── paragraph_segment_ops/
│   ├── __init__.py
│   └── paragraph_operations.py
└── tests/
    ├── __init__.py
    ├── conftest.py                 # Shared fixtures
    ├── test_text_ops.py            # Text operation tests
    ├── test_paragraph_ops.py       # Paragraph tests
    ├── test_segment_ops.py         # Segment tests
    ├── test_integration.py         # Integration tests
    └── fixtures/
        ├── __init__.py
        ├── project_fixtures.py     # Project fixtures
        └── data_fixtures.py        # Test data fixtures
```

### 2.2 Test File Naming
- Test files: `test_<module_name>.py`
- Test functions: `test_<feature>_<condition>`
- Test classes: `Test<Feature>` (if grouping related tests)

```python
# File: test_text_ops.py
def test_text_create_with_valid_name():
    pass

def test_text_create_raises_error_when_name_empty():
    pass

def test_text_create_raises_error_when_duplicate_name():
    pass
```

---

## 3. TEST STRUCTURE

### 3.1 AAA Pattern (Arrange-Act-Assert)
Every test should follow the AAA pattern:

```python
def test_text_create_with_genre(db_project):
    """Test creating a text with a genre specified."""

    # Arrange - Set up test data
    text_name = "Genesis"
    genre_name = "Narrative"

    # Act - Execute the operation
    text = db_project.TextCreate(text_name, genre=genre_name)

    # Assert - Verify results
    assert text is not None
    assert db_project.TextGetName(text) == text_name
    assert db_project.TextGetGenre(text) == genre_name

    # Cleanup (if needed)
    db_project.TextDelete(text)
```

### 3.2 Test Naming Convention
Use descriptive names that explain what's being tested:

```python
# Good - Clear what's being tested
def test_text_create_with_valid_name():
    pass

def test_text_create_raises_valueerror_when_name_empty():
    pass

def test_text_delete_removes_text_from_project():
    pass

def test_text_get_all_returns_generator():
    pass

# Bad - Unclear purpose
def test_text1():
    pass

def test_creation():
    pass

def test_error():
    pass
```

### 3.3 One Assertion Focus Per Test
```python
# Good - Focused tests
def test_text_create_returns_itext_object(db_project):
    text = db_project.TextCreate("Test")
    assert isinstance(text, IText)
    db_project.TextDelete(text)

def test_text_create_sets_name_correctly(db_project):
    text = db_project.TextCreate("Genesis")
    assert db_project.TextGetName(text) == "Genesis"
    db_project.TextDelete(text)

# Acceptable - Related assertions
def test_text_create_with_all_parameters(db_project):
    text = db_project.TextCreate("Genesis", genre="Narrative")
    assert text is not None
    assert db_project.TextGetName(text) == "Genesis"
    assert db_project.TextGetGenre(text) == "Narrative"
    db_project.TextDelete(text)
```

---

## 4. FIXTURES

### 4.1 Fixture Scope
Choose appropriate scope for fixtures:

- **function**: Default, new instance per test
- **class**: Shared across test class
- **module**: Shared across test module
- **session**: Shared across entire test session

```python
import pytest

@pytest.fixture(scope="session")
def flex_project():
    """Provide FLEx project for entire test session."""
    project = FLExProject()
    yield project
    project.Close()

@pytest.fixture(scope="function")
def clean_project(flex_project):
    """Provide clean project state for each test."""
    # Setup
    yield flex_project
    # Teardown - clean up test data
    _cleanup_test_data(flex_project)

@pytest.fixture
def sample_text(clean_project):
    """Provide a sample text for testing."""
    text = clean_project.TextCreate("Sample Text")
    yield text
    # Cleanup happens via clean_project fixture
```

### 4.2 Shared Fixtures (conftest.py)
Place commonly used fixtures in `conftest.py`:

```python
# tests/conftest.py
import pytest
from flexlibs_dev import FLExProject

@pytest.fixture(scope="session")
def db_project():
    """Provide FLEx project for testing."""
    project = FLExProject()
    project.Open("TestProject")
    yield project
    project.Close()

@pytest.fixture
def test_ws(db_project):
    """Provide default writing system."""
    return db_project.DefaultVernacularWritingSystem

@pytest.fixture
def sample_texts(db_project):
    """Provide sample texts for testing."""
    texts = []
    for i in range(3):
        text = db_project.TextCreate(f"Text_{i}")
        texts.append(text)

    yield texts

    # Cleanup
    for text in texts:
        db_project.TextDelete(text)
```

### 4.3 Parameterized Fixtures
```python
@pytest.fixture(params=["Narrative", "Procedural", "Expository"])
def genre(request):
    """Provide different genre types."""
    return request.param

def test_text_create_with_various_genres(db_project, genre):
    """Test text creation with different genres."""
    text = db_project.TextCreate("Test", genre=genre)
    assert db_project.TextGetGenre(text) == genre
    db_project.TextDelete(text)
```

---

## 5. TEST COVERAGE REQUIREMENTS

### 5.1 Coverage Targets
- **Overall Project**: >90% coverage
- **Per Cluster**: >90% coverage
- **Critical Methods**: 100% coverage (Create, Delete, Get, Set)
- **Error Paths**: All exception paths tested

### 5.2 Coverage Report
```bash
# Generate coverage report
pytest --cov=flexlibs_dev --cov-report=html --cov-report=term

# View HTML report
# Open htmlcov/index.html in browser

# Check coverage meets threshold
pytest --cov=flexlibs_dev --cov-fail-under=90
```

### 5.3 Coverage Configuration
```ini
# setup.cfg or pyproject.toml
[tool:pytest]
addopts = --cov=flexlibs_dev --cov-report=html --cov-report=term-missing

[coverage:run]
source = flexlibs_dev
omit =
    */tests/*
    */test_*.py
    */__pycache__/*

[coverage:report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
    if TYPE_CHECKING:
    @abstractmethod
```

---

## 6. TEST CATEGORIES

### 6.1 Unit Tests
Test individual methods in isolation:

```python
def test_text_create_with_valid_name(db_project):
    """Unit test for TextCreate method."""
    # Arrange
    name = "Genesis"

    # Act
    text = db_project.TextCreate(name)

    # Assert
    assert text is not None
    assert isinstance(text, IText)

    # Cleanup
    db_project.TextDelete(text)
```

### 6.2 Integration Tests
Test multiple methods working together:

```python
def test_complete_text_workflow(db_project):
    """Integration test for complete text operations."""
    # Create text
    text = db_project.TextCreate("Genesis", genre="Narrative")
    assert text is not None

    # Add paragraph
    para = db_project.ParagraphCreate(text, "In the beginning...")
    assert para is not None

    # Verify text has paragraph
    paras = db_project.TextGetParagraphs(text)
    assert len(list(paras)) == 1

    # Get paragraph text
    para_text = db_project.ParagraphGetText(para)
    assert para_text == "In the beginning..."

    # Cleanup
    db_project.TextDelete(text)
```

### 6.3 Error Tests
Test error conditions and exceptions:

```python
def test_text_create_raises_valueerror_when_name_empty(db_project):
    """Test TextCreate raises ValueError for empty name."""
    with pytest.raises(ValueError, match="cannot be empty"):
        db_project.TextCreate("")

def test_text_create_raises_keyerror_when_duplicate(db_project):
    """Test TextCreate raises KeyError for duplicate name."""
    text = db_project.TextCreate("Genesis")

    with pytest.raises(KeyError, match="already exists"):
        db_project.TextCreate("Genesis")

    db_project.TextDelete(text)

def test_text_delete_raises_error_when_not_found(db_project):
    """Test TextDelete raises error for non-existent text."""
    invalid_hvo = 99999999

    with pytest.raises(ObjectNotFoundError):
        db_project.TextDelete(invalid_hvo)
```

### 6.4 Edge Case Tests
Test boundary conditions and edge cases:

```python
def test_text_create_with_very_long_name(db_project):
    """Test text creation with maximum length name."""
    long_name = "A" * 255  # Maximum length
    text = db_project.TextCreate(long_name)
    assert db_project.TextGetName(text) == long_name
    db_project.TextDelete(text)

def test_text_create_with_unicode_characters(db_project):
    """Test text creation with Unicode characters."""
    unicode_name = "Génesis 创世记 Γένεση"
    text = db_project.TextCreate(unicode_name)
    assert db_project.TextGetName(text) == unicode_name
    db_project.TextDelete(text)

def test_paragraph_get_all_returns_empty_for_new_text(db_project):
    """Test getting paragraphs from empty text."""
    text = db_project.TextCreate("Empty")
    paras = list(db_project.TextGetParagraphs(text))
    assert len(paras) == 0
    db_project.TextDelete(text)
```

### 6.5 Performance Tests
```python
import time

def test_text_get_all_performance(db_project, many_texts):
    """Test TextGetAll performance with many texts."""
    start = time.time()
    texts = list(db_project.TextGetAll())
    elapsed = time.time() - start

    assert len(texts) >= 100
    assert elapsed < 1.0  # Should complete in under 1 second

@pytest.mark.slow
def test_create_thousand_paragraphs(db_project):
    """Test creating large number of paragraphs."""
    text = db_project.TextCreate("Large Text")

    start = time.time()
    for i in range(1000):
        db_project.ParagraphCreate(text, f"Paragraph {i}")
    elapsed = time.time() - start

    assert elapsed < 10.0  # Should complete in under 10 seconds
    db_project.TextDelete(text)
```

---

## 7. TEST DATA MANAGEMENT

### 7.1 Test Data Principles
- Use realistic test data
- Make test data obvious and readable
- Avoid production data in tests
- Clean up test data after tests

### 7.2 Factory Pattern for Test Data
```python
# tests/fixtures/data_fixtures.py
class TextFactory:
    """Factory for creating test texts."""

    _counter = 0

    @classmethod
    def create(cls, db_project, name=None, genre=None):
        """Create a test text with unique name."""
        if name is None:
            cls._counter += 1
            name = f"TestText_{cls._counter}"

        return db_project.TextCreate(name, genre=genre)

    @classmethod
    def create_batch(cls, db_project, count=3):
        """Create multiple test texts."""
        return [cls.create(db_project) for _ in range(count)]

# Usage in tests
def test_text_operations(db_project):
    text = TextFactory.create(db_project, name="Genesis")
    assert text is not None
```

### 7.3 Cleanup Strategy
```python
# Option 1: Explicit cleanup in test
def test_text_create(db_project):
    text = db_project.TextCreate("Test")
    try:
        assert text is not None
    finally:
        db_project.TextDelete(text)

# Option 2: Fixture cleanup
@pytest.fixture
def test_text(db_project):
    text = db_project.TextCreate("Test")
    yield text
    db_project.TextDelete(text)

# Option 3: Cleanup fixture
@pytest.fixture(autouse=True)
def cleanup_texts(db_project):
    """Auto-cleanup texts after each test."""
    yield
    # Delete all test texts
    for text in db_project.TextGetAll():
        if "Test" in db_project.TextGetName(text):
            db_project.TextDelete(text)
```

---

## 8. MOCKING & TEST DOUBLES

### 8.1 When to Mock
- External dependencies (file system, network)
- Expensive operations (don't mock FLEx in integration tests)
- Non-deterministic behavior
- Error conditions that are hard to trigger

### 8.2 Mocking Examples
```python
from unittest.mock import Mock, patch, MagicMock

def test_text_create_handles_com_exception(db_project):
    """Test TextCreate handles COM exceptions gracefully."""
    with patch.object(db_project.cache, 'CreateText') as mock_create:
        mock_create.side_effect = COMException("Database error")

        with pytest.raises(RuntimeError, match="FLEx operation failed"):
            db_project.TextCreate("Test")

def test_text_get_name_with_missing_ws(db_project):
    """Test TextGetName handles missing writing system."""
    text = Mock()
    text.Name = None

    result = db_project.TextGetName(text)
    assert result == ""
```

### 8.3 Spy Pattern
```python
def test_text_create_calls_prop_changed(db_project):
    """Test that TextCreate calls PropChanged."""
    with patch.object(db_project.cache, 'PropChanged') as mock_prop_changed:
        text = db_project.TextCreate("Test")

        # Verify PropChanged was called
        mock_prop_changed.assert_called()

        db_project.TextDelete(text)
```

---

## 9. PARAMETRIZED TESTS

### 9.1 Basic Parametrization
```python
@pytest.mark.parametrize("name,expected", [
    ("Genesis", "Genesis"),
    ("Exodus", "Exodus"),
    ("Leviticus", "Leviticus"),
])
def test_text_create_with_various_names(db_project, name, expected):
    """Test text creation with different names."""
    text = db_project.TextCreate(name)
    assert db_project.TextGetName(text) == expected
    db_project.TextDelete(text)
```

### 9.2 Multiple Parameters
```python
@pytest.mark.parametrize("name,genre,expected_genre", [
    ("Genesis", "Narrative", "Narrative"),
    ("Psalms", "Poetry", "Poetry"),
    ("Romans", "Epistle", "Epistle"),
    ("Test", None, None),
])
def test_text_create_with_genres(db_project, name, genre, expected_genre):
    """Test text creation with various genres."""
    text = db_project.TextCreate(name, genre=genre)
    assert db_project.TextGetGenre(text) == expected_genre
    db_project.TextDelete(text)
```

### 9.3 Error Condition Parameters
```python
@pytest.mark.parametrize("invalid_name", [
    "",
    None,
    " ",
    "A" * 300,  # Too long
])
def test_text_create_rejects_invalid_names(db_project, invalid_name):
    """Test TextCreate rejects invalid names."""
    with pytest.raises((ValueError, TypeError)):
        db_project.TextCreate(invalid_name)
```

---

## 10. TEST MARKERS

### 10.1 Standard Markers
```python
import pytest

@pytest.mark.slow
def test_large_batch_operation(db_project):
    """This test takes a long time."""
    pass

@pytest.mark.integration
def test_complete_workflow(db_project):
    """Integration test."""
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature(db_project):
    """This feature is not ready."""
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_python38_feature(db_project):
    """Uses Python 3.8+ features."""
    pass

@pytest.mark.xfail(reason="Known bug #123")
def test_known_issue(db_project):
    """This test is expected to fail."""
    pass
```

### 10.2 Custom Markers
```ini
# pytest.ini or setup.cfg
[tool:pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests
    requires_flex: marks tests that require FLEx installation
```

```python
# Usage
@pytest.mark.unit
def test_text_validation():
    pass

@pytest.mark.integration
@pytest.mark.requires_flex
def test_with_real_flex_project():
    pass
```

### 10.3 Running Specific Markers
```bash
# Run only unit tests
pytest -m unit

# Run all except slow tests
pytest -m "not slow"

# Run integration tests only
pytest -m integration

# Combine markers
pytest -m "integration and not slow"
```

---

## 11. CLUSTER-SPECIFIC TEST REQUIREMENTS

### 11.1 Required Tests per Cluster
Based on PROJECT_BOARD.md, each cluster must include:

1. **CRUD Operations**:
   - test_create_simple
   - test_create_with_all_parameters
   - test_create_duplicate_raises_error
   - test_delete
   - test_get_all
   - test_exists

2. **Get/Set Operations**:
   - test_get_property
   - test_set_property
   - test_get_set_roundtrip

3. **Error Conditions**:
   - test_invalid_input_raises_error
   - test_not_found_raises_error
   - test_type_error_for_wrong_type

4. **Integration**:
   - test_cluster_operations_integration

### 11.2 Example: Cluster 1.1 Tests
```python
# tests/test_cluster_1_1_text_ops.py

class TestTextCreate:
    """Tests for TextCreate method."""

    def test_text_create_simple(self, db_project):
        text = db_project.TextCreate("Genesis")
        assert text is not None
        db_project.TextDelete(text)

    def test_text_create_with_genre(self, db_project):
        text = db_project.TextCreate("Genesis", genre="Narrative")
        assert db_project.TextGetGenre(text) == "Narrative"
        db_project.TextDelete(text)

    def test_text_create_duplicate_raises_error(self, db_project):
        text = db_project.TextCreate("Genesis")
        with pytest.raises(KeyError):
            db_project.TextCreate("Genesis")
        db_project.TextDelete(text)


class TestTextDelete:
    """Tests for TextDelete method."""

    def test_text_delete(self, db_project):
        text = db_project.TextCreate("ToDelete")
        hvo = text.Hvo
        db_project.TextDelete(text)
        assert not db_project.TextExists("ToDelete")


class TestTextExists:
    """Tests for TextExists method."""

    def test_text_exists_returns_true_when_found(self, db_project):
        text = db_project.TextCreate("Genesis")
        assert db_project.TextExists("Genesis") is True
        db_project.TextDelete(text)

    def test_text_exists_returns_false_when_not_found(self, db_project):
        assert db_project.TextExists("NonExistent") is False


class TestTextIntegration:
    """Integration tests for text operations."""

    def test_text_operations_integration(self, db_project):
        # Create
        text = db_project.TextCreate("Genesis", genre="Narrative")

        # Verify exists
        assert db_project.TextExists("Genesis")

        # Get name
        name = db_project.TextGetName(text)
        assert name == "Genesis"

        # Update name
        db_project.TextSetName(text, "Genesis 1")
        assert db_project.TextGetName(text) == "Genesis 1"

        # Delete
        db_project.TextDelete(text)
        assert not db_project.TextExists("Genesis 1")
```

---

## 12. CONTINUOUS INTEGRATION

### 12.1 CI Configuration
```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11"]

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests
        run: |
          pytest --cov=flexlibs_dev --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

---

## 13. BEST PRACTICES SUMMARY

### ✅ DO
- Write tests first (TDD approach)
- Use descriptive test names
- Follow AAA pattern
- Test error conditions
- Use fixtures for setup
- Clean up test data
- Aim for >90% coverage
- Keep tests fast
- Make tests independent
- Use parametrization for similar tests

### ❌ DON'T
- Write tests that depend on each other
- Use production data
- Hardcode paths or values
- Write flaky tests
- Skip error testing
- Leave test data in database
- Mock everything (test real FLEx when possible)
- Write tests without assertions
- Commit failing tests
- Ignore coverage gaps

---

## 14. TESTING CHECKLIST

Before marking a cluster complete, verify:

- [ ] All specified tests from PROJECT_BOARD.md implemented
- [ ] Coverage >90% for cluster
- [ ] All happy paths tested
- [ ] All error conditions tested
- [ ] Edge cases tested
- [ ] Integration test passes
- [ ] Tests are independent
- [ ] Tests clean up properly
- [ ] All tests pass locally
- [ ] All tests pass in CI
- [ ] No flaky tests
- [ ] Test execution time <30 seconds for cluster

---

**End of Testing Guidelines**

For questions or clarifications, contact the QC team lead (Agent 5).
