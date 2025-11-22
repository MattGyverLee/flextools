# GitHub Issues for MattGyverLee/flextools

Create these issues on your fork: https://github.com/MattGyverLee/flextools/issues

---

## Issue 1: [Phase 0] Set up Development Infrastructure
**Labels**: `infrastructure`, `phase-0`, `priority-critical`
**Assignee**: TBD
**Milestone**: M0 - Foundation Ready

### Description
Set up the complete development infrastructure for the Complete Data Access initiative as outlined in Cluster 0.1 of PROJECT_BOARD.md.

### Tasks
- [ ] Set up flexlibs development repository structure
- [ ] Configure Python development environment (3.9-3.13)
- [ ] Set up virtual environment with dependencies
- [ ] Install and configure python-net
- [ ] Set up test FLEx projects (small, medium, large)
- [ ] Configure git workflow and branching strategy
- [ ] Create development documentation

### Dependencies
None

### Acceptance Criteria
- [ ] Virtual environment activates successfully
- [ ] python-net installed and working
- [ ] Test FLEx projects accessible
- [ ] Git branching strategy documented

---

## Issue 2: [Phase 0] Testing & CI/CD Framework
**Labels**: `testing`, `ci-cd`, `phase-0`, `priority-critical`
**Assignee**: TBD
**Milestone**: M0 - Foundation Ready

### Description
Implement comprehensive testing framework and CI/CD pipeline as outlined in Cluster 0.2.

### Tasks
- [ ] Set up pytest test framework
- [ ] Create test fixtures for FLEx projects
- [ ] Configure pytest-cov for coverage reporting
- [ ] Set up CI/CD pipeline (GitHub Actions)
- [ ] Configure automated testing on commit
- [ ] Set up code quality tools (black, flake8, mypy)
- [ ] Create test data generators
- [ ] Set up performance benchmarking tools

### Dependencies
- Issue #1 (Development Infrastructure)

### Acceptance Criteria
- [ ] pytest runs successfully
- [ ] Coverage reports generated (target >90%)
- [ ] CI/CD pipeline runs on every push
- [ ] All quality checks pass

---

## Issue 3: [Cluster 1.1] Core Text Operations
**Labels**: `feature`, `phase-1`, `text-operations`, `priority-high`
**Assignee**: TBD
**Milestone**: M1 - Beta 1 (Text CRUD)
**Branch**: `claude/cluster-text-ops-1.1-1.3-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Implement 8 core text CRUD operations for FLEx text management.

### Methods to Implement
- [ ] `TextCreate(name, genre=None)` → IText
- [ ] `TextDelete(text_or_hvo)` → None
- [ ] `TextExists(name)` → bool
- [ ] `TextGetAll()` → Generator[IText]
- [ ] `TextGetName(text_or_hvo, wsHandle=None)` → str
- [ ] `TextSetName(text_or_hvo, name, wsHandle=None)` → None
- [ ] `TextGetGenre(text_or_hvo)` → str
- [ ] `TextSetGenre(text_or_hvo, genre)` → None

### Tests Required
- [ ] test_text_create_simple
- [ ] test_text_create_with_genre
- [ ] test_text_delete
- [ ] test_text_exists
- [ ] test_text_get_all
- [ ] test_text_get_set_name
- [ ] test_text_get_set_genre

### Status
✅ **IMPLEMENTED** - Code available on branch, ready for FLEx API integration

### Dependencies
- Issue #2 (Testing Framework)

### Acceptance Criteria
- [ ] All 8 methods implemented with FLEx API integration
- [ ] All tests passing
- [ ] Code coverage >90%
- [ ] Documentation complete

---

## Issue 4: [Cluster 1.2] Advanced Text Operations
**Labels**: `feature`, `phase-1`, `text-operations`, `priority-high`
**Assignee**: TBD
**Milestone**: M1 - Beta 1
**Branch**: `claude/cluster-text-ops-1.1-1.3-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Implement 6 advanced text operations for content and media management.

### Methods to Implement
- [ ] `TextGetContents(text_or_hvo)` → IStText
- [ ] `TextGetParagraphs(text_or_hvo)` → List[IStTxtPara]
- [ ] `TextGetParagraphCount(text_or_hvo)` → int
- [ ] `TextGetMediaFiles(text_or_hvo)` → List[ICmMedia]
- [ ] `TextAddMediaFile(text_or_hvo, filepath)` → ICmMedia
- [ ] `TextGetAbbreviation(text_or_hvo, wsHandle=None)` → str

### Status
✅ **IMPLEMENTED** - Code available on branch, ready for FLEx API integration

### Dependencies
- Issue #3 (Core Text Operations)

---

## Issue 5: [Cluster 1.3] Paragraph CRUD Operations
**Labels**: `feature`, `phase-1`, `paragraph-operations`, `priority-high`
**Assignee**: TBD
**Milestone**: M1 - Beta 1
**Branch**: `claude/cluster-text-ops-1.1-1.3-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Implement 8 paragraph CRUD operations.

### Methods to Implement
- [ ] `ParagraphCreate(text_or_hvo, content, wsHandle=None)` → IStTxtPara
- [ ] `ParagraphDelete(paragraph_or_hvo)` → None
- [ ] `ParagraphGetAll(text_or_hvo)` → Generator[IStTxtPara]
- [ ] `ParagraphGetText(para_or_hvo, wsHandle=None)` → str
- [ ] `ParagraphSetText(para_or_hvo, text, wsHandle=None)` → None
- [ ] `ParagraphGetSegments(para_or_hvo)` → List[ISegment]
- [ ] `ParagraphGetSegmentCount(para_or_hvo)` → int
- [ ] `ParagraphInsertAt(text_or_hvo, index, content, wsHandle=None)` → IStTxtPara

### Status
✅ **IMPLEMENTED** - Code available on branch, ready for FLEx API integration

### Dependencies
- Issue #4 (Advanced Text Operations)

---

## Issue 6: [Cluster 1.4] Paragraph Advanced Operations
**Labels**: `feature`, `phase-1`, `paragraph-operations`, `priority-high`
**Assignee**: TBD
**Milestone**: M1 - Beta 1
**Branch**: `claude/cluster-para-seg-ops-1.4-1.5-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Implement 5 advanced paragraph operations for translations and notes.

### Methods to Implement
- [ ] `ParagraphGetTranslations(para_or_hvo)` → Dict[str, str]
- [ ] `ParagraphSetTranslation(para_or_hvo, text, wsHandle)` → None
- [ ] `ParagraphGetNotes(para_or_hvo)` → List[INote]
- [ ] `ParagraphAddNote(para_or_hvo, content)` → INote
- [ ] `ParagraphGetStyleName(para_or_hvo)` → str

### Status
✅ **IMPLEMENTED** - Code available on branch, ready for FLEx API integration

### Dependencies
- Issue #5 (Paragraph CRUD)

---

## Issue 7: [Cluster 1.5] Segment Operations
**Labels**: `feature`, `phase-1`, `segment-operations`, `priority-high`
**Assignee**: TBD
**Milestone**: M1 - Beta 1
**Branch**: `claude/cluster-para-seg-ops-1.4-1.5-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Implement 9 segment operations for interlinear text analysis.

### Methods to Implement
- [ ] `SegmentGetAll(paragraph_or_hvo=None)` → Generator[ISegment]
- [ ] `SegmentGetAnalyses(segment_or_hvo)` → List[IAnalysis]
- [ ] `SegmentGetBaselineText(segment_or_hvo, wsHandle=None)` → str
- [ ] `SegmentSetBaselineText(segment_or_hvo, text, wsHandle=None)` → None
- [ ] `SegmentGetFreeTranslation(segment_or_hvo, wsHandle=None)` → str
- [ ] `SegmentSetFreeTranslation(segment_or_hvo, text, wsHandle=None)` → None
- [ ] `SegmentGetLiteralTranslation(segment_or_hvo, wsHandle=None)` → str
- [ ] `SegmentSetLiteralTranslation(segment_or_hvo, text, wsHandle=None)` → None
- [ ] `SegmentGetNotes(segment_or_hvo)` → List[INote]

### Status
✅ **IMPLEMENTED** - Code available on branch, ready for FLEx API integration

⚠️ **LINGUISTICS REVIEW NOTE**: These segment operations are CRITICAL for interlinear glossing workflows. Priority for FLEx API integration.

### Dependencies
- Issue #6 (Paragraph Advanced)

---

## Issue 8: [Cluster 1.6] Wordform CRUD Operations
**Labels**: `feature`, `phase-1`, `wordform-operations`, `priority-high`
**Assignee**: TBD
**Milestone**: M1 - Beta 1
**Branch**: `claude/cluster-wordform-ops-1.6-1.7-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Implement 10 wordform CRUD operations for lexical management.

### Methods to Implement
- [ ] `WordformGetAll()` → Generator[IWfiWordform]
- [ ] `WordformCreate(form, wsHandle)` → IWfiWordform
- [ ] `WordformDelete(wordform_or_hvo)` → None
- [ ] `WordformExists(form, wsHandle)` → bool
- [ ] `WordformFind(form, wsHandle)` → IWfiWordform
- [ ] `WordformGetForm(wordform_or_hvo, wsHandle=None)` → str
- [ ] `WordformSetForm(wordform_or_hvo, form, wsHandle)` → None
- [ ] `WordformGetSpellingStatus(wordform_or_hvo)` → SpellingStatusStates
- [ ] `WordformSetSpellingStatus(wordform_or_hvo, status)` → None
- [ ] `WordformGetAnalyses(wordform_or_hvo)` → List[IWfiAnalysis]

### Status
✅ **IMPLEMENTED** - Code available on branch, ready for FLEx API integration

### Dependencies
- Issue #7 (Segment Operations)

---

## Issue 9: [Cluster 1.7] Wordform Advanced Operations
**Labels**: `feature`, `phase-1`, `wordform-operations`, `priority-medium`
**Assignee**: TBD
**Milestone**: M1 - Beta 1
**Branch**: `claude/cluster-wordform-ops-1.6-1.7-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Implement 6 advanced wordform operations for occurrence tracking and status management.

### Methods to Implement
- [ ] `WordformGetOccurrenceCount(wordform_or_hvo)` → int
- [ ] `WordformGetOccurrences(wordform_or_hvo)` → List[ISegment]
- [ ] `WordformGetChecksum(wordform_or_hvo)` → int
- [ ] `WordformGetAllWithStatus(status)` → Generator[IWfiWordform]
- [ ] `WordformGetAllUnapproved()` → Generator[IWfiWordform]
- [ ] `WordformApproveSpelling(wordform_or_hvo)` → None

### Status
✅ **IMPLEMENTED** - Code available on branch, ready for FLEx API integration

### Dependencies
- Issue #8 (Wordform CRUD)

---

## Issue 10: [Synthesis] Refactor to Modular Architecture
**Labels**: `refactoring`, `architecture`, `priority-high`
**Assignee**: TBD
**Branch**: `claude/synthesis-refactor-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Refactor implemented clusters to use shared utilities and eliminate code duplication.

### Work Completed
✅ Created core utilities module with:
- Type definitions and protocols
- Resolver functions (6 types)
- Validation utilities (5 functions)
- Custom exception hierarchy (8 classes)
- Shared constants and enums

✅ Refactored 7 feature modules to use core utilities
✅ Created 29 integration tests (all passing)
✅ Eliminated ~220 lines of duplicate code
✅ Created architecture documentation

### Tasks
- [ ] Review SYNTHESIS_REVIEW_REQUEST.md
- [ ] QC Agent review and approval
- [ ] Merge to main development branch

### Dependencies
- Issues #3-9 (All cluster implementations)

---

## Issue 11: [QC] Quality Control Review of Phase 1 Implementation
**Labels**: `quality-control`, `review`, `priority-critical`
**Assignee**: TBD
**Branch**: Multiple branches

### Description
Comprehensive QC review of all Phase 1 implementations before FLEx API integration.

### QC Framework Created
✅ QC_CHECKLIST.md - 10-section review checklist
✅ CODING_STANDARDS.md - Python standards with PascalCase convention
✅ TESTING_GUIDELINES.md - pytest standards, >90% coverage requirement
✅ REVIEW_PROCESS.md - 6-stage review process
✅ .pre-commit-config.yaml - Automated quality checks

### Reviews Needed
- [ ] Agent 1: Text Operations (Clusters 1.1-1.3)
- [ ] Agent 2: Paragraph/Segment Operations (Clusters 1.4-1.5)
- [ ] Agent 3: Wordform Operations (Clusters 1.6-1.7)
- [ ] Agent 7: Synthesis & Refactoring
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Code quality checks (Black, Flake8, Mypy)

### Acceptance Criteria
- [ ] All P0 and P1 issues resolved
- [ ] >90% test coverage achieved
- [ ] All automated checks passing
- [ ] Approval for FLEx API integration

---

## Issue 12: [Linguistics] Linguistic Review and Recommendations
**Labels**: `linguistics`, `review`, `documentation`, `priority-high`
**Assignee**: TBD
**Branch**: `claude/linguistics-review-013mrWNEJ6GpYcbeRNdFuFBi`

### Description
Expert linguistic review of Complete Data Access API for field linguistics and language documentation use cases.

### Review Completed
✅ LINGUISTICS_REVIEW.md - Comprehensive linguistic assessment
✅ LINGUISTIC_EXAMPLES.md - Real-world usage examples

### Key Findings

**APPROVE WITH CONDITIONS** ⚠️

**Strengths:**
- Excellent writing system support
- Well-designed wordform operations
- Good text management
- Correct linguistic terminology

**Critical Gaps (Phase 2 Required):**
- Missing segment translation operations (P0)
- Incomplete analysis operations (P0)
- No translation type distinction (P0)

### Recommendations for Phase 2
- [ ] Implement 10 segment operations for interlinear glossing
- [ ] Expand analysis operations (7 methods needed)
- [ ] Add translation operations (5 methods)
- [ ] Test with tonal languages, polysynthetic languages, non-Latin scripts
- [ ] Add "Linguistic Note" sections to documentation

### Dependencies
- All Phase 1 implementations

### Acceptance Criteria
- [ ] Phase 2 gaps addressed
- [ ] Cross-linguistic testing completed
- [ ] Documentation includes linguistic examples
- [ ] Workflow examples provided

---

## Issue 13: [Documentation] Complete API Documentation
**Labels**: `documentation`, `priority-high`
**Assignee**: TBD
**Milestone**: M1 - Beta 1

### Description
Generate comprehensive API documentation for all implemented methods.

### Tasks
- [ ] Generate API reference documentation
- [ ] Create migration guide from existing flexlibs
- [ ] Write integration examples
- [ ] Update README with new capabilities
- [ ] Create video tutorials for major areas
- [ ] Add linguistic workflow examples
- [ ] Document FLEx API integration patterns

### Documents to Create
- [ ] API_REFERENCE.md - Complete method reference
- [ ] MIGRATION_GUIDE.md - From flexlibs v1.x to v2.4
- [ ] INTEGRATION_GUIDE.md - FLEx API integration patterns
- [ ] WORKFLOWS.md - Common linguistic workflows
- [ ] FAQ.md - Frequently asked questions

### Dependencies
- All Phase 1 implementations
- Issue #11 (QC Review)
- Issue #12 (Linguistics Review)

---

## Issue 14: [FLEx Integration] FLEx API Integration for Phase 1 Methods
**Labels**: `flex-integration`, `priority-critical`
**Assignee**: TBD
**Milestone**: M1 - Beta 1

### Description
Replace NotImplementedError placeholders with actual FLEx LCM API integration using python.NET.

### Scope
Integrate 42 methods across:
- Text operations (14 methods)
- Paragraph operations (13 methods)
- Segment operations (9 methods)
- Wordform operations (16 methods)

### Tasks
- [ ] Set up FLEx LCM API access via python.NET
- [ ] Implement core resolvers with actual FLEx object retrieval
- [ ] Implement all TODO-marked integration points
- [ ] Test with real FLEx projects (small, medium, large)
- [ ] Verify UndoableUnitOfWork patterns for write operations
- [ ] Performance testing and optimization
- [ ] Error handling for FLEx-specific errors

### Acceptance Criteria
- [ ] All 42 methods working with real FLEx projects
- [ ] All tests passing with FLEx integration
- [ ] Performance benchmarks met
- [ ] No data corruption in test projects
- [ ] Error messages clear and actionable

---

## Issue 15: [Release] Prepare v2.4.0-beta1 Release
**Labels**: `release`, `milestone`
**Assignee**: TBD
**Milestone**: M1 - Beta 1

### Description
Prepare and release Beta 1 with Phase 1 complete (Text & Interlinear operations).

### Tasks
- [ ] Verify all Phase 1 methods implemented and tested
- [ ] Update version to v2.4.0-beta1
- [ ] Create comprehensive changelog
- [ ] Update requirements.txt
- [ ] Create release notes
- [ ] Tag release in git
- [ ] Package and test installation
- [ ] Announce beta to community for feedback

### Dependencies
- Issue #14 (FLEx Integration)
- Issue #13 (Documentation)
- Issue #11 (QC Review)

### Acceptance Criteria
- [ ] All 42 methods functional
- [ ] >90% test coverage
- [ ] Documentation complete
- [ ] Release notes published
- [ ] Beta testers identified

---

## Summary

**Total Issues Created**: 15
- Phase 0 (Foundation): 2 issues
- Phase 1 (Implementation): 7 issues
- Quality & Review: 3 issues
- Integration & Release: 3 issues

**Current Status**:
- ✅ 42 methods implemented (placeholder/skeleton)
- ✅ 29 integration tests passing
- ✅ QC framework established
- ✅ Linguistics review complete
- ✅ Code refactored to modular architecture
- ⏳ Awaiting FLEx API integration
- ⏳ Awaiting QC approval

**Next Steps**:
1. Create these issues on https://github.com/MattGyverLee/flextools/issues
2. Prioritize Phase 0 infrastructure setup
3. Begin FLEx API integration for Phase 1 methods
4. QC review and approval process
5. Beta 1 release preparation
