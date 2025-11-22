# FlexTools Complete Data Access - Quick Reference

## 📊 At a Glance

**Total Methods**: ~290
**Total Clusters**: 40
**Timeline**: 24 weeks (6 months)
**Current Status**: Planning Phase

---

## 🎯 Milestones

| Milestone | Week | Key Deliverable |
|-----------|------|-----------------|
| **M0** | 2 | Foundation Ready (Test framework, CI/CD) |
| **M1** | 8 | Beta 1 - Text & Corpus CRUD |
| **M2** | 14 | Beta 2 - Interlinear & Analysis |
| **M3** | 18 | RC 1 - Phase 1 Complete |
| **M4** | 20 | v2.4.0 Stable Release |
| **M5** | 24 | Beta 3 - Grammar & Morphology |
| **M6** | 30 | v2.5.0 Stable Release |
| **M7** | 34 | Complete Coverage (all 290 methods) |

---

## 📋 Phase Summary

### Phase 0: Foundation (Weeks 1-2) - 0 methods
Setup development environment, testing framework, CI/CD, templates

### Phase 1: Texts & Interlinear (Weeks 3-8) - 73 methods
**Priority: HIGH** - Most requested features
- Text CRUD (8 methods)
- Text advanced (6 methods)
- Paragraph CRUD (8 methods)
- Paragraph advanced (5 methods)
- Segment operations (9 methods)
- Wordform CRUD (10 methods)
- Wordform advanced (6 methods)
- Analysis CRUD (11 methods)
- MorphBundle operations (10 methods)

**Deliverable**: Beta 1 Release - Full text corpus manipulation

### Phase 2: Grammar & Morphology (Weeks 9-14) - 88 methods
**Priority: MEDIUM-HIGH** - Project setup & linguistic analysis
- POS CRUD (10 methods)
- POS advanced (6 methods)
- Grammatical categories (7 methods)
- Phoneme CRUD (10 methods)
- Phoneme advanced (6 methods)
- Natural classes (9 methods)
- Phonological environment (7 methods)
- Allomorphs (10 methods)
- Morphology rules (11 methods)
- Inflection & features (12 methods)

**Deliverable**: Beta 2 Release - Grammar configuration & morphological analysis

### Phase 3: Lists & Media (Weeks 15-18) - 60 methods
**Priority: MEDIUM** - Configuration & resources
- Custom list CRUD (10 methods)
- List item operations (10 methods)
- List hierarchy (6 methods)
- Media files (9 methods)
- External links (6 methods)
- Enhanced WS operations (8 methods)
- Publications & filters (11 methods)

**Deliverable**: RC 1 Release - Complete Phase 1, ready for production

### Phase 4: Specialized (Weeks 19-24) - 80 methods
**Priority: LOW-MEDIUM** - Domain-specific features
- Scripture books (8 methods)
- Scripture sections (7 methods)
- Scripture notes & BT (8 methods)
- Discourse charts (6 methods)
- Chart details (7 methods)
- Anthropology (8 methods)
- Time/seasons (6 methods)
- Notebook records (8 methods)
- Events & research (7 methods)
- Advanced phonology (7 methods)
- Advanced morphology (6 methods)
- Lexical relations (6 methods)
- Remaining features (12 methods)

**Deliverable**: v2.6.0 Release - Complete coverage of FLEx data model

---

## 🚀 Quick Start for Contributors

### 1. Pick a Cluster
Choose from available clusters in PROJECT_BOARD.md

### 2. Set Up
```bash
git checkout -b feature/cluster-X.Y-name
```

### 3. Implement
Follow the template:
1. Write tests first (TDD)
2. Implement methods with docstrings
3. Follow Pythonic naming conventions
4. Handle errors properly

### 4. Quality Check
```bash
pytest --cov=flexlibs
black flexlibs/
flake8 flexlibs/
mypy flexlibs/
```

### 5. Submit
```bash
git push origin feature/cluster-X.Y-name
# Create PR with cluster number in title
```

---

## 📐 Design Principles

### ✅ DO
- Use **PascalCase** for method names: `TextCreate()`, `LexiconGetSenseGloss()`
- Start with **area prefix**: Text, Lexicon, Wordform, Phoneme, etc.
- Provide **sensible defaults**: `wsHandle=None` uses default WS
- Return **Python types** when simple: `str`, `int`, `bool`
- Return **generators** for large collections
- Return **None** for "not found" (not exceptions)
- Validate parameters before .NET calls
- Provide **helpful error messages**

### ❌ DON'T
- Use snake_case (use PascalCase instead)
- Use .NET-style getter/setter patterns
- Require too many parameters
- Raise exceptions for normal "not found" cases
- Load entire collections into memory
- Forget to document parameters and return values

---

## 📚 Example Method

```python
def TextCreate(self, name, genre=None):
    """
    Create a new text in the project.

    Args:
        name (str): The name of the text. Must be unique.
        genre (str, optional): The genre/type of the text.
                              Defaults to None.

    Returns:
        IText: The newly created text object.

    Raises:
        ValueError: If name is empty or text already exists.
        FlexToolsPermissionError: If modifications not allowed.

    Example:
        >>> text = project.TextCreate("Story 1", "Narrative")
        >>> print(project.TextGetName(text))
        Story 1

    See Also:
        - TextDelete: Delete an existing text
        - TextExists: Check if a text exists
        - TextGetAll: Get all texts in the project

    Version:
        Added in flexlibs 2.4.0
    """
    # Validate
    if not name or not isinstance(name, str) or not name.strip():
        raise ValueError("Text name must be a non-empty string")

    if self.TextExists(name):
        raise ValueError(f"Text '{name}' already exists in project")

    # Import
    from SIL.LCModel import ITextRepository
    from SIL.LCModel.Core.Text import TsStringUtils

    # Implement
    try:
        textRepo = self.project.ServiceLocator.GetInstance(ITextRepository)
        text = textRepo.Create()

        wsHandle = self.GetDefaultAnalysisWS()[1]
        tsName = TsStringUtils.MakeString(name, wsHandle)
        text.Name.set_String(wsHandle, tsName)

        if genre:
            tsGenre = TsStringUtils.MakeString(genre, wsHandle)
            text.Genre = tsGenre

        self.lp.TextsOC.Add(text)
        return text

    except Exception as e:
        raise FlexToolsAPIError(f"Failed to create text '{name}': {e}", e)
```

---

## 📊 Progress Tracking

### By Phase
- Phase 0: ⚪⚪⚪ (0/3 clusters)
- Phase 1: ⚪⚪⚪⚪⚪⚪⚪⚪⚪ (0/9 clusters)
- Phase 2: ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪ (0/10 clusters)
- Phase 3: ⚪⚪⚪⚪⚪⚪⚪ (0/7 clusters)
- Phase 4: ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪ (0/13 clusters)

### By Priority
- Critical (Foundation): 0% (0/3)
- High (Texts/Interlinear): 0% (0/9)
- Medium-High (Grammar): 0% (0/10)
- Medium (Lists/Media): 0% (0/7)
- Low-Medium (Specialized): 0% (0/13)

### Overall
**0 of 290 methods complete (0%)**

---

## 🎯 Success Metrics

### Code Quality
- Test coverage: Target >90%
- Performance overhead: <5% vs direct .NET
- Documentation: 100% of methods

### User Adoption
- Beta testers: Target 5+ users
- Module migrations: Track existing modules using new API
- Community feedback: Positive reception

### Delivery
- On-time milestone delivery
- No critical bugs in releases
- Backward compatibility maintained

---

## 📞 Support

- **Issues**: GitHub Issues
- **Questions**: GitHub Discussions
- **Documentation**: See PROJECT_BOARD.md
- **Templates**: See implementation plan document

---

**Last Updated**: 2025-11-22
**Next Action**: Set up development environment (Cluster 0.1)
