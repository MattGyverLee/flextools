# Agent Review Report Template

## Code Review Report - Cluster [X.Y]

**Cluster**: [X.Y - Cluster Name]
**Agent**: [Agent Name/Number]
**Reviewer**: Agent 5 - QC Specialist
**Review Date**: [YYYY-MM-DD]
**Review Round**: [#1, #2, etc.]
**Branch**: [agent-branch-name]

---

## 📊 EXECUTIVE SUMMARY

**Overall Status**: ✅ APPROVED / ⚠️ APPROVED WITH MINOR ITEMS / ❌ NEEDS WORK

**Recommendation**: MERGE / REQUEST CHANGES / BLOCK

**Summary**:
[2-3 sentence summary of the review outcome and key findings]

### Quick Stats
- **Methods Implemented**: [X/Y] ([%]%)
- **Tests Written**: [X/Y] ([%]%)
- **Test Coverage**: [%]% (Target: >90%)
- **Issues Found**: [Total] (P0: [X], P1: [Y], P2: [Z], P3: [W])
- **Time Spent on Review**: [X] hours
- **Code Quality Score**: [X]/10

---

## ✅ STAGE 1: AUTOMATED CHECKS

**Status**: ✅ PASS / ❌ FAIL

### Pre-commit Hooks
- [ ] Black formatting
- [ ] Flake8 linting
- [ ] Mypy type checking
- [ ] Import sorting (isort)
- [ ] Trailing whitespace
- [ ] YAML validation

### CI/CD Pipeline
- [ ] All tests pass in CI
- [ ] Build succeeds
- [ ] No warnings

### Issues Found
[List any automated check failures, or "None" if all passed]

**Stage 1 Result**: ✅ PASS / ❌ FAIL

---

## 📝 STAGE 2: CODE REVIEW

**Status**: ✅ PASS / ⚠️ PASS WITH ITEMS / ❌ FAIL

### 2.1 Implementation Completeness

#### Methods Implemented
All methods from PROJECT_BOARD.md:

- [x] Method1(params) → ReturnType
- [x] Method2(params) → ReturnType
- [x] Method3(params) → ReturnType
- [ ] Method4(params) → ReturnType (MISSING)

**Completeness**: [X/Y] methods ([%]%)

### 2.2 Method-by-Method Review

#### Method: [MethodName](params)

**Signature**: ✅ PASS / ❌ FAIL
- [ ] Type hints present and correct
- [ ] Parameters named appropriately
- [ ] Return type correct
- [ ] Optional parameters have defaults

**Implementation**: ✅ PASS / ⚠️ ISSUES / ❌ FAIL
- [ ] Logic is clear and maintainable
- [ ] Error handling appropriate
- [ ] COM interop correct
- [ ] UndoableUnitOfWork used for writes
- [ ] PropChanged called when needed
- [ ] No code duplication
- [ ] Performance considerations addressed

**Documentation**: ✅ PASS / ⚠️ ISSUES / ❌ FAIL
- [ ] Docstring present and complete
- [ ] Purpose clearly stated
- [ ] All parameters documented
- [ ] Return value documented
- [ ] Exceptions documented
- [ ] Example provided (if complex)
- [ ] Related methods referenced

**Issues**:
- [Priority] Issue description
  - **Location**: File:Line
  - **Problem**: [Detailed description]
  - **Solution**: [Recommended fix]
  - **Example**: [Code example if applicable]

---

[Repeat for each method]

---

### 2.3 Code Quality Assessment

#### Strengths ✨
- [Strength 1]
- [Strength 2]
- [Strength 3]

#### Areas for Improvement 📈
- [Area 1]
- [Area 2]
- [Area 3]

#### Code Organization
- [ ] Files properly organized
- [ ] Imports correctly ordered
- [ ] Helper methods appropriately placed
- [ ] No circular dependencies

#### Naming & Style
- [ ] Methods use PascalCase (FlexTools convention)
- [ ] Variables use snake_case
- [ ] Constants use UPPER_SNAKE_CASE
- [ ] Names are clear and descriptive

#### Error Handling
- [ ] All error paths covered
- [ ] Specific exception types used
- [ ] Error messages are clear and actionable
- [ ] No bare except clauses

#### Type Safety
- [ ] All methods have type hints
- [ ] Type hints are accurate
- [ ] Union types used correctly
- [ ] Optional types for nullable values

#### Performance
- [ ] No obvious bottlenecks
- [ ] Generators used for large collections
- [ ] No unnecessary database queries
- [ ] Caching utilized appropriately

**Stage 2 Result**: ✅ PASS / ⚠️ PASS WITH ITEMS / ❌ FAIL

---

## 🧪 STAGE 3: TESTING VERIFICATION

**Status**: ✅ PASS / ⚠️ PASS WITH ITEMS / ❌ FAIL

### 3.1 Test Completeness

#### Tests from PROJECT_BOARD.md
- [x] test_feature_1
- [x] test_feature_2
- [x] test_feature_3
- [ ] test_feature_4 (MISSING)

**Test Completeness**: [X/Y] tests ([%]%)

### 3.2 Test Execution Results

```
================== Test Results ==================
Total Tests: [X]
Passed: [X]
Failed: [X]
Skipped: [X]
Errors: [X]
Duration: [X]s
==================================================
```

#### Failed Tests
[List any failed tests with details, or "None - All tests pass ✅"]

1. **test_name**
   - **Error**: [Error message]
   - **Cause**: [Root cause]
   - **Fix Needed**: [Description]

### 3.3 Code Coverage

```
================== Coverage Report ================
Module Coverage: [X]%
Line Coverage: [X]/[Y] lines
Branch Coverage: [X]%
==================================================
```

**Coverage Target**: >90%
**Actual Coverage**: [X]%
**Status**: ✅ MEETS TARGET / ❌ BELOW TARGET

#### Coverage Gaps
[List any significant gaps, or "None - Coverage target met ✅"]

**File**: [filename]
- Lines [X-Y]: [Reason for gap]
- **Action Required**: [Add tests / Justified gap / Remove dead code]

### 3.4 Test Quality Review

#### Test Structure
- [ ] Tests follow AAA pattern
- [ ] Clear, descriptive test names
- [ ] Tests are independent
- [ ] Proper cleanup in tests
- [ ] Fixtures used appropriately

#### Test Categories
- [ ] Unit tests for each method
- [ ] Integration test for cluster
- [ ] Error condition tests
- [ ] Edge case tests
- [ ] Parametrized tests where appropriate

#### Test Issues Found
[List any test quality issues, or "None ✅"]

**Stage 3 Result**: ✅ PASS / ⚠️ PASS WITH ITEMS / ❌ FAIL

---

## 🔗 STAGE 4: INTEGRATION TESTING

**Status**: ✅ PASS / ❌ FAIL

### 4.1 Integration Test Execution

**Test Name**: test_[cluster]_integration

**Result**: ✅ PASS / ❌ FAIL

**Test Scenario**:
[Description of integration test workflow]

**Results**:
[Test output or description of results]

### 4.2 Cross-Cluster Integration

**Dependencies**: [List dependent clusters]

**Integration Status**:
- [ ] Works with Cluster [X.Y]
- [ ] Works with Cluster [X.Y]
- [ ] No regressions in dependent clusters

### 4.3 Manual Testing

**Manual Test Scenario**: [Description]

**Steps Performed**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Results**: [Description]

**Actual Results**: [Description]

**Status**: ✅ PASS / ❌ FAIL

**Stage 4 Result**: ✅ PASS / ❌ FAIL

---

## 📚 STAGE 5: DOCUMENTATION REVIEW

**Status**: ✅ PASS / ⚠️ PASS WITH ITEMS / ❌ FAIL

### 5.1 Method Documentation

**Docstring Completeness**: [X/Y] methods ([%]%)

#### Docstring Quality
- [ ] All methods have docstrings
- [ ] Purpose clearly stated
- [ ] Parameters documented with types
- [ ] Return values documented
- [ ] Exceptions documented
- [ ] Examples provided (where needed)
- [ ] See Also sections present

#### Documentation Issues
[List any documentation issues, or "None ✅"]

### 5.2 Code Comments

- [ ] Complex logic explained
- [ ] "Why" comments present (not just "what")
- [ ] FLEx quirks documented
- [ ] TODOs have issue references
- [ ] No commented-out code

### 5.3 Module Documentation

- [ ] Module docstring present
- [ ] Cluster overview clear
- [ ] Usage examples included
- [ ] Public API clearly defined

**Stage 5 Result**: ✅ PASS / ⚠️ PASS WITH ITEMS / ❌ FAIL

---

## 🎯 STAGE 6: FINAL ASSESSMENT

### Stage Summary

| Stage | Status | Result |
|-------|--------|--------|
| 1. Automated Checks | ✅/❌ | PASS/FAIL |
| 2. Code Review | ✅/⚠️/❌ | PASS/ISSUES/FAIL |
| 3. Testing | ✅/⚠️/❌ | PASS/ISSUES/FAIL |
| 4. Integration | ✅/❌ | PASS/FAIL |
| 5. Documentation | ✅/⚠️/❌ | PASS/ISSUES/FAIL |

### Overall Metrics

**Quality Score Breakdown**:
- Code Quality: [X]/10
- Test Quality: [X]/10
- Documentation: [X]/10
- Adherence to Standards: [X]/10
- **Overall**: [X]/10

**Coverage Metrics**:
- Methods: [X/Y] ([%]%)
- Tests: [X/Y] ([%]%)
- Coverage: [%]% (Target: >90%)

**Issue Summary**:
- P0 (Critical): [X] issues
- P1 (High): [X] issues
- P2 (Medium): [X] issues
- P3 (Low): [X] issues
- **Total**: [X] issues

---

## 🔍 DETAILED ISSUES

### Priority 0 (Critical) - Must Fix Before Merge

#### P0-1: [Issue Title]
- **File**: [filename:line]
- **Method**: [method name]
- **Severity**: Critical
- **Category**: [Security/Data Corruption/Breaking Change]

**Problem**:
[Detailed description of the issue]

**Impact**:
[Why this is critical]

**Recommended Fix**:
```python
# Before (problematic)
[problematic code]

# After (fixed)
[fixed code]
```

**Verification**:
[How to verify the fix]

---

[Repeat for each P0 issue]

---

### Priority 1 (High) - Should Fix Before Merge

#### P1-1: [Issue Title]
- **File**: [filename:line]
- **Method**: [method name]
- **Severity**: High
- **Category**: [Error Handling/Type Safety/Testing]

**Problem**:
[Description]

**Recommended Fix**:
[Fix description or code example]

---

[Repeat for each P1 issue]

---

### Priority 2 (Medium) - Should Fix (Can Address in Follow-up)

#### P2-1: [Issue Title]
- **File**: [filename:line]
- **Severity**: Medium
- **Category**: [Code Quality/Performance/Documentation]

**Problem**:
[Description]

**Recommended Fix**:
[Fix description]

---

[Repeat for each P2 issue]

---

### Priority 3 (Low) - Nice to Have

#### P3-1: [Issue Title]
- **File**: [filename:line]
- **Severity**: Low
- **Category**: [Style/Optimization/Enhancement]

**Suggestion**:
[Description]

---

[Repeat for each P3 issue]

---

## ✨ POSITIVE FEEDBACK

### What Went Well
- [Positive observation 1]
- [Positive observation 2]
- [Positive observation 3]

### Exemplary Code
[Highlight any particularly well-written code or clever solutions]

```python
# Example of excellent implementation
[code snippet]
```

**Why this is excellent**:
[Explanation]

---

## 📋 ACTION ITEMS

### Required Actions (Before Merge)
- [ ] Fix P0 issue: [Issue description]
- [ ] Fix P1 issue: [Issue description]
- [ ] Add missing tests: [Test descriptions]
- [ ] Improve coverage in [area]
- [ ] Update documentation for [methods]

### Optional Actions (Can be Follow-up)
- [ ] Address P2 issue: [Issue description]
- [ ] Consider P3 suggestion: [Suggestion]
- [ ] Optimize [area] for performance

### Reviewer Actions
- [ ] Update PROJECT_BOARD.md status
- [ ] Record review metrics
- [ ] Schedule follow-up review if needed

---

## 💬 REVIEWER COMMENTS

### General Comments
[Any general observations, suggestions, or feedback]

### Questions for Agent
[Any questions or clarifications needed]

### Recommendations
[High-level recommendations for this or future work]

---

## 🎯 DECISION

### Final Recommendation

**Status**: ✅ APPROVED / ⚠️ APPROVED WITH MINOR ITEMS / ❌ NEEDS WORK

**Rationale**:
[Explanation of the decision]

### Next Steps

#### If APPROVED ✅:
1. Merge to main branch
2. Update PROJECT_BOARD.md
3. Mark cluster as 🟢 Complete
4. Notify team
5. Move to next cluster

#### If APPROVED WITH MINOR ITEMS ⚠️:
1. Create follow-up issues for P2/P3 items
2. Merge to main branch
3. Update PROJECT_BOARD.md
4. Track minor items separately

#### If NEEDS WORK ❌:
1. Agent addresses all P0 and P1 issues
2. Update tests and documentation
3. Re-run automated checks
4. Request re-review
5. Expected time to resolution: [estimate]

---

## 📅 REVIEW TIMELINE

- **Submission Date**: [YYYY-MM-DD]
- **Review Start**: [YYYY-MM-DD]
- **Review Completed**: [YYYY-MM-DD]
- **Total Review Time**: [X] hours
- **Turnaround Time**: [X] days

---

## 📎 ATTACHMENTS

### Coverage Report
[Link to HTML coverage report]

### Test Output
[Link to or embed test output]

### Related Documents
- QC_CHECKLIST.md
- CODING_STANDARDS.md
- TESTING_GUIDELINES.md
- PROJECT_BOARD.md - Cluster [X.Y]

---

## 🔄 REVISION HISTORY

### Review Round 1 - [YYYY-MM-DD]
- Initial review completed
- [X] issues found
- Status: [APPROVED/NEEDS WORK]

### Review Round 2 - [YYYY-MM-DD]
- [X] issues resolved
- [X] new issues found
- Status: [APPROVED/NEEDS WORK]

---

## ✍️ SIGNATURES

**Reviewed By**: Agent 5 - QC Specialist
**Date**: [YYYY-MM-DD]
**Signature**: [Agent 5]

**Agent Response**: [To be filled by agent]
**Date**: [YYYY-MM-DD]

---

**End of Review Report**

---

## 📌 NOTES FOR USING THIS TEMPLATE

### Instructions
1. Copy this template for each cluster review
2. Fill in all sections as you review
3. Be specific with file names and line numbers
4. Provide code examples for issues
5. Be constructive and educational in feedback
6. Update status as issues are resolved

### Priority Guidelines
- **P0**: Security, data corruption, breaking changes, critical bugs
- **P1**: Missing error handling, type safety issues, significant bugs
- **P2**: Code quality, performance, minor bugs, documentation gaps
- **P3**: Style, optimizations, suggestions, enhancements

### Approval Guidelines
- **APPROVED**: 0 P0, 0 P1, coverage >90%, all tests pass
- **APPROVED WITH MINOR ITEMS**: 0 P0, 0 P1, minor P2/P3 items only
- **NEEDS WORK**: Any P0 or P1 issues, or coverage <90%

---

**Template Version**: 1.0
**Last Updated**: 2025-11-22
**Maintained By**: Agent 5 - QC Specialist
