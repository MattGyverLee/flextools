# Testing Guidelines

## Complete Data Access Initiative - Testing Standards & Requirements

**Version**: 1.0
**Last Updated**: 2025-11-22
**Framework**: pytest
**Coverage Target**: >90%

---

## 🎯 Testing Philosophy

1. **Comprehensive Coverage**: Every method tested, every path validated
2. **Independence**: Tests don't depend on each other
3. **Clarity**: Tests serve as documentation
4. **Speed**: Fast enough to run frequently
5. **Reliability**: No flaky tests

---

## 1. TESTING FRAMEWORK

### Tools
- **Test Framework**: pytest 7.0+
- **Coverage**: pytest-cov
- **Mocking**: unittest.mock or pytest-mock

### Installation
```bash
pip install pytest pytest-cov pytest-mock
```

### Running Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=flexlibs_dev --cov-report=html

# Specific test
pytest tests/test_text_ops.py::test_text_create

# Stop on first failure
pytest -x

# Verbose
pytest -v
```

---

## 2. TEST ORGANIZATION

### Directory Structure
```
flexlibs_dev/
├── text_ops/
│   └── text_operations.py
└── tests/
    ├── conftest.py
    ├── test_text_ops.py
    └── test_integration.py
```

### Test Naming
- Files: `test_<module_name>.py`
- Functions: `test_<feature>_<condition>`
- Classes: `Test<Feature>` (if grouping)

---

## 3. TEST STRUCTURE

### AAA Pattern (Arrange-Act-Assert)
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
    
    # Cleanup
    db_project.TextDelete(text)
```

### Test Naming Convention
```python
# Good
def test_text_create_with_valid_name():
    pass

def test_text_create_raises_valueerror_when_name_empty():
    pass

# Bad
def test_text1():
    pass

def test_error():
    pass
```

---

## 4. FIXTURES

### Fixture Scope
- **function**: New instance per test (default)
- **class**: Shared across test class
- **module**: Shared across test module
- **session**: Shared across entire session

```python
import pytest

@pytest.fixture(scope="session")
def flex_project():
    """Provide FLEx project for entire test session."""
    project = FLExProject()
    yield project
    project.Close()

@pytest.fixture
def sample_text(flex_project):
    """Provide a sample text for testing."""
    text = flex_project.TextCreate("Sample Text")
    yield text
    flex_project.TextDelete(text)
```

### Shared Fixtures (conftest.py)
```python
# tests/conftest.py
import pytest

@pytest.fixture(scope="session")
def db_project():
    """Provide FLEx project for testing."""
    project = FLExProject()
    yield project
    project.Close()

@pytest.fixture
def test_ws(db_project):
    """Provide default writing system."""
    return db_project.DefaultVernacularWritingSystem
```

### Parametrized Fixtures
```python
@pytest.fixture(params=["Narrative", "Procedural", "Expository"])
def genre(request):
    return request.param

def test_text_create_with_various_genres(db_project, genre):
    text = db_project.TextCreate("Test", genre=genre)
    assert db_project.TextGetGenre(text) == genre
    db_project.TextDelete(text)
```

---

## 5. TEST COVERAGE

### Coverage Targets
- **Overall**: >90%
- **Per Cluster**: >90%
- **Critical Methods**: 100%
- **Error Paths**: All tested

### Generate Reports
```bash
# HTML report
pytest --cov=flexlibs_dev --cov-report=html

# Terminal report
pytest --cov=flexlibs_dev --cov-report=term-missing

# Fail if below threshold
pytest --cov=flexlibs_dev --cov-fail-under=90
```

---

## 6. TEST CATEGORIES

### Unit Tests
```python
def test_text_create_with_valid_name(db_project):
    """Unit test for TextCreate method."""
    text = db_project.TextCreate("Genesis")
    assert text is not None
    db_project.TextDelete(text)
```

### Integration Tests
```python
def test_complete_text_workflow(db_project):
    """Integration test for complete text operations."""
    text = db_project.TextCreate("Genesis", genre="Narrative")
    para = db_project.ParagraphCreate(text, "In the beginning...")
    paras = list(db_project.TextGetParagraphs(text))
    assert len(paras) == 1
    db_project.TextDelete(text)
```

### Error Tests
```python
def test_text_create_raises_valueerror_when_name_empty(db_project):
    """Test TextCreate raises ValueError for empty name."""
    with pytest.raises(ValueError, match="cannot be empty"):
        db_project.TextCreate("")
```

### Edge Case Tests
```python
def test_text_create_with_very_long_name(db_project):
    """Test text creation with maximum length name."""
    long_name = "A" * 255
    text = db_project.TextCreate(long_name)
    assert db_project.TextGetName(text) == long_name
    db_project.TextDelete(text)

def test_text_create_with_unicode_characters(db_project):
    """Test text creation with Unicode characters."""
    unicode_name = "Génesis 创世记 Γένεση"
    text = db_project.TextCreate(unicode_name)
    assert db_project.TextGetName(text) == unicode_name
    db_project.TextDelete(text)
```

---

## 7. PARAMETRIZED TESTS

```python
@pytest.mark.parametrize("name,expected", [
    ("Genesis", "Genesis"),
    ("Exodus", "Exodus"),
    ("Leviticus", "Leviticus"),
])
def test_text_create_with_various_names(db_project, name, expected):
    text = db_project.TextCreate(name)
    assert db_project.TextGetName(text) == expected
    db_project.TextDelete(text)

@pytest.mark.parametrize("invalid_name", [
    "",
    None,
    " ",
    "A" * 300,  # Too long
])
def test_text_create_rejects_invalid_names(db_project, invalid_name):
    with pytest.raises((ValueError, TypeError)):
        db_project.TextCreate(invalid_name)
```

---

## 8. TEST MARKERS

```python
import pytest

@pytest.mark.slow
def test_large_batch_operation():
    pass

@pytest.mark.integration
def test_complete_workflow():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass
```

### Running Specific Markers
```bash
# Run only unit tests
pytest -m unit

# Skip slow tests
pytest -m "not slow"

# Run integration tests
pytest -m integration
```

---

## 9. CLUSTER REQUIREMENTS

### Required Tests per Cluster (from PROJECT_BOARD.md)

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

4. **Integration**:
   - test_cluster_operations_integration

---

## 10. BEST PRACTICES

### ✅ DO
- Write tests first (TDD)
- Use descriptive names
- Follow AAA pattern
- Test error conditions
- Use fixtures
- Clean up test data
- Aim for >90% coverage
- Keep tests fast
- Make tests independent

### ❌ DON'T
- Write dependent tests
- Use production data
- Hardcode paths
- Write flaky tests
- Skip error testing
- Leave test data
- Mock everything
- Skip assertions
- Commit failing tests
- Ignore coverage gaps

---

## 11. TESTING CHECKLIST

Before marking cluster complete:

- [ ] All specified tests implemented
- [ ] Coverage >90%
- [ ] All happy paths tested
- [ ] All error conditions tested
- [ ] Edge cases tested
- [ ] Integration test passes
- [ ] Tests are independent
- [ ] Tests clean up properly
- [ ] All tests pass locally
- [ ] All tests pass in CI
- [ ] No flaky tests
- [ ] Execution time <30s

---

**End of Testing Guidelines**
