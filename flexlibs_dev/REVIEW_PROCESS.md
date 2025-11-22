# Review Process

## Complete Data Access Initiative - Step-by-Step Code Review Process

**Version**: 1.0
**Last Updated**: 2025-11-22
**Reviewer**: Agent 5 - Quality Control & Standards Enforcement Specialist

---

## 🎯 Purpose

This document defines the systematic review process for all cluster implementations in the Complete Data Access initiative. Every cluster must pass through these review stages before being merged to the main branch.

---

## 📋 Review Stages

```
┌─────────────────┐
│ Agent Submits   │
│ Implementation  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Stage 1:        │
│ Automated       │◄─── Pre-commit hooks, CI/CD
│ Checks          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Stage 2:        │
│ Code Review     │◄─── Manual review by QC specialist
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Stage 3:        │
│ Testing         │◄─── Test execution and coverage
│ Verification    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Stage 4:        │
│ Integration     │◄─── Integration testing
│ Testing         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Stage 5:        │
│ Documentation   │◄─── Documentation completeness
│ Review          │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Stage 6:        │
│ Final           │◄─── Overall assessment
│ Approval        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Merge to Main   │
└─────────────────┘
```

---

## STAGE 1: AUTOMATED CHECKS

### 1.1 Pre-commit Validation
Before reviewing any code manually, ensure automated checks pass:

```bash
# On agent's branch
git checkout <agent-branch>

# Run pre-commit hooks
pre-commit run --all-files

# Expected output: All hooks should pass
```

### 1.2 Required Automated Checks
- [ ] **Black formatting**: Code is properly formatted
- [ ] **Flake8 linting**: No linting errors
- [ ] **Mypy type checking**: All type hints valid
- [ ] **Import sorting**: Imports properly organized
- [ ] **Trailing whitespace**: No trailing whitespace
- [ ] **YAML validation**: Config files are valid

### 1.3 CI/CD Pipeline
- [ ] All CI tests pass
- [ ] Build succeeds
- [ ] No warnings in build log

### 1.4 If Automated Checks Fail
**Action**: Request changes from agent

**Template Response**:
```markdown
## Stage 1: Automated Checks - FAILED ❌

The following automated checks failed:

- [ ] Black formatting
  - Error: Files not formatted according to Black standards
  - Fix: Run `black flexlibs_dev/`

- [ ] Flake8 linting
  - Error: [specific linting errors]
  - Fix: [specific fixes needed]

Please fix these issues and push updates. Re-review will begin after fixes are committed.
```

---

## STAGE 2: CODE REVIEW

### 2.1 Preparation
1. Check out the agent's branch
2. Open the implementation files
3. Have QC_CHECKLIST.md ready
4. Have CODING_STANDARDS.md ready

### 2.2 Review Methodology

#### Step 1: High-Level Review (15 minutes)
Review overall structure and approach:

```markdown
# High-Level Review Notes

## Cluster: [X.Y - Name]
## Reviewer: Agent 5
## Date: [YYYY-MM-DD]

### Architecture
- [ ] Code organization makes sense
- [ ] Files in correct directories
- [ ] Naming conventions followed
- [ ] No unnecessary files

### Approach
- [ ] Implementation approach is sound
- [ ] No obvious design flaws
- [ ] Follows established patterns
- [ ] Reuses existing helpers appropriately

### Completeness
- [ ] All methods from PROJECT_BOARD.md implemented
- [ ] All required signatures match spec
- [ ] No methods missing

**Initial Assessment**: PASS / NEEDS_WORK / MAJOR_ISSUES
```

#### Step 2: Method-by-Method Review (30-60 minutes)
For each method, check against QC_CHECKLIST.md:

```markdown
### Method: TextCreate(name, genre=None)

**Signature**: ✅ / ❌
- [ ] Type hints present
- [ ] Parameters named correctly
- [ ] Return type correct

**Implementation**: ✅ / ❌
- [ ] Logic is clear
- [ ] Error handling appropriate
- [ ] COM interop correct
- [ ] UndoableUnitOfWork used

**Documentation**: ✅ / ❌
- [ ] Docstring complete
- [ ] Parameters documented
- [ ] Returns documented
- [ ] Exceptions documented
- [ ] Example provided

**Issues Found**:
- [P0] Critical issue 1
- [P1] Important issue 2
- [P2] Minor issue 3

**Comments**:
[Detailed feedback]
```

#### Step 3: Cross-Cutting Concerns (15 minutes)
Review aspects that span multiple methods:

```markdown
### Cross-Cutting Review

**Consistency**:
- [ ] Similar methods follow same patterns
- [ ] Naming is consistent across cluster
- [ ] Error messages are consistent
- [ ] Return types consistent

**Error Handling**:
- [ ] All error paths covered
- [ ] Appropriate exception types
- [ ] Clear error messages
- [ ] No bare except clauses

**Performance**:
- [ ] No obvious bottlenecks
- [ ] Generators used appropriately
- [ ] No unnecessary database queries
- [ ] Caching used effectively

**Security**:
- [ ] Input validation present
- [ ] No injection vulnerabilities
- [ ] Resource cleanup proper
- [ ] Transaction handling correct
```

### 2.3 Code Review Checklist
Use the comprehensive QC_CHECKLIST.md, focusing on:

**Critical Items (Must Fix)**:
- [ ] Type hints on all methods
- [ ] Docstrings on all methods
- [ ] Error handling for all methods
- [ ] HVO-or-object pattern used correctly
- [ ] UndoableUnitOfWork for write operations
- [ ] No security vulnerabilities

**Important Items (Should Fix)**:
- [ ] Code follows CODING_STANDARDS.md
- [ ] Clear variable names
- [ ] Appropriate comments
- [ ] No code duplication
- [ ] Helper methods for complex logic

**Minor Items (Nice to Have)**:
- [ ] Additional examples in docstrings
- [ ] Performance optimizations
- [ ] Additional type aliases

### 2.4 Record Review Findings
Use AGENT_REVIEW_TEMPLATE.md to document findings.

---

## STAGE 3: TESTING VERIFICATION

### 3.1 Test Execution
```bash
# Switch to agent's branch
git checkout <agent-branch>

# Run all tests for the cluster
pytest tests/test_cluster_X_Y.py -v

# Run with coverage
pytest tests/test_cluster_X_Y.py --cov=flexlibs_dev/<cluster_module> --cov-report=html --cov-report=term
```

### 3.2 Test Review Checklist
- [ ] **All specified tests implemented**
  - Check against PROJECT_BOARD.md test list
  - Verify each method has tests

- [ ] **All tests pass**
  - No failures
  - No errors
  - No skipped tests (unless justified)

- [ ] **Coverage meets requirements**
  - Overall coverage >90%
  - Critical methods at 100%
  - No untested error paths

- [ ] **Test quality**
  - Tests follow AAA pattern
  - Clear test names
  - Tests are independent
  - Proper cleanup

- [ ] **Test categories complete**
  - Unit tests for each method
  - Integration test for cluster
  - Error condition tests
  - Edge case tests

### 3.3 Coverage Analysis
```bash
# Generate detailed coverage report
pytest --cov=flexlibs_dev/<cluster_module> --cov-report=html

# Review HTML report
# Open htmlcov/index.html

# Identify gaps
# Lines highlighted in red are not covered
```

### 3.4 Coverage Gap Review
For any lines not covered:

```markdown
### Coverage Gaps Analysis

**Uncovered Lines**: [line numbers]

**Reason for gap**:
- [ ] Justified (defensive code, rare error path)
- [ ] Needs test
- [ ] Dead code (should be removed)

**Action Required**:
[Description of what needs to be done]
```

---

## STAGE 4: INTEGRATION TESTING

### 4.1 Integration Test Execution
```bash
# Run integration tests
pytest tests/test_cluster_X_Y.py::test_integration -v

# Run all integration tests
pytest -m integration
```

### 4.2 Integration Checklist
- [ ] Integration test demonstrates realistic workflow
- [ ] Multiple methods work together correctly
- [ ] Data persists correctly
- [ ] No side effects between operations
- [ ] Cleanup works properly

### 4.3 Cross-Cluster Integration
If cluster depends on previous clusters:

```bash
# Run tests for dependent clusters
pytest tests/test_cluster_X_*.py -v

# Verify no regressions
```

### 4.4 Manual Integration Testing
Perform manual verification:

```markdown
### Manual Integration Test

**Test Scenario**: [Realistic workflow description]

**Steps**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Results**:
- [Expected result 1]
- [Expected result 2]

**Actual Results**:
- [Actual result 1]
- [Actual result 2]

**Status**: ✅ PASS / ❌ FAIL

**Issues Found**: [If any]
```

---

## STAGE 5: DOCUMENTATION REVIEW

### 5.1 Method Documentation
For each method:
- [ ] Docstring present and complete
- [ ] Purpose clearly stated
- [ ] Parameters documented with types
- [ ] Return value documented
- [ ] Exceptions documented
- [ ] Usage example provided (for complex methods)
- [ ] Related methods referenced

### 5.2 Module Documentation
- [ ] Module docstring present
- [ ] Cluster overview provided
- [ ] Usage examples included
- [ ] Public API clearly defined

### 5.3 API Documentation
If auto-generated docs exist:
- [ ] All methods appear in API docs
- [ ] Signatures are correct
- [ ] Examples render correctly
- [ ] Links work

### 5.4 User-Facing Documentation
If applicable:
- [ ] User guide updated
- [ ] Tutorial examples added
- [ ] Migration guide updated
- [ ] Breaking changes documented

### 5.5 Code Comments
- [ ] Complex logic explained
- [ ] "Why" comments present
- [ ] FLEx quirks documented
- [ ] TODOs have issue numbers
- [ ] No commented-out code

---

## STAGE 6: FINAL APPROVAL

### 6.1 Overall Assessment
Review all stages:

```markdown
# Final Review Summary

## Cluster: [X.Y - Name]
## Agent: [Agent Name/Number]
## Reviewer: Agent 5
## Review Date: [YYYY-MM-DD]

### Stage Results
- [x] Stage 1: Automated Checks - PASS ✅
- [x] Stage 2: Code Review - PASS ✅
- [x] Stage 3: Testing Verification - PASS ✅
- [x] Stage 4: Integration Testing - PASS ✅
- [x] Stage 5: Documentation Review - PASS ✅

### Quality Metrics
- **Test Coverage**: 94% (Target: >90%) ✅
- **Methods Implemented**: 8/8 (100%) ✅
- **Tests Written**: 12/9 (133%) ✅
- **Issues Found**: 3 (0 P0, 1 P1, 2 P2)
- **Issues Resolved**: 3/3 (100%) ✅

### Final Decision
**Status**: ✅ APPROVED / ⚠️ APPROVED WITH MINOR ITEMS / ❌ NEEDS WORK

**Recommendation**: MERGE / REQUEST CHANGES / BLOCK
```

### 6.2 Approval Criteria

#### ✅ APPROVED (Ready to Merge)
- All automated checks pass
- No P0 (critical) issues
- No P1 (high) issues
- Coverage >90%
- All tests pass
- Documentation complete
- Integration test passes

#### ⚠️ APPROVED WITH MINOR ITEMS
- All automated checks pass
- No P0 issues
- No P1 issues
- Minor P2 issues can be addressed in follow-up
- Coverage >90%
- All tests pass
- Documentation substantially complete

#### ❌ NEEDS WORK
- Automated checks fail
- P0 or P1 issues present
- Coverage <90%
- Tests failing
- Major documentation gaps
- Integration test fails

### 6.3 Final Approval Actions

#### If APPROVED:
1. Add approval comment to PR
2. Update PROJECT_BOARD.md cluster status to 🟢 Complete
3. Merge to main branch
4. Notify team
5. Update metrics

```bash
# Merge process
git checkout claude/expand-flextools-data-access-013mrWNEJ6GpYcbeRNdFuFBi
git merge <agent-branch> --no-ff
git push origin claude/expand-flextools-data-access-013mrWNEJ6GpYcbeRNdFuFBi
```

#### If NEEDS WORK:
1. Create detailed review report using AGENT_REVIEW_TEMPLATE.md
2. Post review report as comment
3. Request changes from agent
4. Set status to "Needs Work"
5. Wait for agent to address issues
6. Re-review when ready

---

## 🔄 RE-REVIEW PROCESS

### When Agent Addresses Feedback

1. **Check Updates**
   ```bash
   git fetch origin
   git checkout <agent-branch>
   git pull
   ```

2. **Review Changes**
   ```bash
   # See what changed
   git log --oneline -n 5
   git diff <previous-commit> HEAD
   ```

3. **Focus Re-Review**
   - Review only items that were flagged
   - Verify all requested changes made
   - Check for new issues introduced

4. **Update Review Report**
   ```markdown
   ## Re-Review #2 - [Date]

   ### Previous Issues Addressed
   - [x] Issue 1 - Fixed
   - [x] Issue 2 - Fixed
   - [ ] Issue 3 - Still present

   ### New Issues Found
   - [New issue 1]

   ### Status
   - [x] Stage 2: Code Review - PASS ✅
   - [x] Stage 3: Testing - PASS ✅
   ```

5. **Make Decision**
   - If all issues resolved: APPROVE
   - If issues remain: REQUEST CHANGES again
   - If new major issues: BLOCK

---

## 📊 REVIEW METRICS

Track these metrics for each review:

```markdown
### Review Metrics

**Time Spent**:
- Stage 1 (Automated): 5 min
- Stage 2 (Code Review): 45 min
- Stage 3 (Testing): 20 min
- Stage 4 (Integration): 15 min
- Stage 5 (Documentation): 10 min
- Total: 95 min

**Issues Found**:
- P0 (Critical): 0
- P1 (High): 1
- P2 (Medium): 3
- P3 (Low): 2
- Total: 6

**Review Rounds**: 2

**Time to Approval**: 2 days

**Code Quality Score**: 8.5/10
```

---

## 📝 REVIEW BEST PRACTICES

### For Reviewers (Agent 5)

#### DO:
- ✅ Be thorough but not nitpicky
- ✅ Explain why changes are needed
- ✅ Provide examples of better approaches
- ✅ Recognize good work
- ✅ Be consistent across reviews
- ✅ Review promptly (within 24 hours)
- ✅ Focus on important issues first

#### DON'T:
- ❌ Bikeshed (argue over trivial style choices)
- ❌ Request changes without explanation
- ❌ Approve code you don't understand
- ❌ Let personal preferences override standards
- ❌ Block on minor issues
- ❌ Rush reviews

### For Agents (Being Reviewed)

#### DO:
- ✅ Run all checks before submitting
- ✅ Self-review before requesting review
- ✅ Respond to feedback promptly
- ✅ Ask for clarification if needed
- ✅ Test your changes thoroughly
- ✅ Update tests when fixing issues

#### DON'T:
- ❌ Submit code with known issues
- ❌ Take feedback personally
- ❌ Argue over standards
- ❌ Make unrelated changes in review cycle
- ❌ Rush fixes without testing

---

## 🔍 COMMON REVIEW FINDINGS

### Frequent Issues to Watch For

1. **Missing Type Hints**
   ```python
   # Bad
   def TextCreate(self, name, genre=None):

   # Good
   def TextCreate(self, name: str, genre: Optional[str] = None) -> IText:
   ```

2. **Incomplete Error Handling**
   ```python
   # Bad
   try:
       text = self.cache.GetText(name)
   except:
       return None

   # Good
   try:
       text = self.cache.GetText(name)
   except AttributeError:
       raise ObjectNotFoundError(f"Text '{name}' not found")
   ```

3. **Missing Docstrings**
   ```python
   # Bad
   def TextGetName(self, text_or_hvo):
       pass

   # Good
   def TextGetName(self, text_or_hvo: Union[IText, int]) -> str:
       """
       Get the name of a text.

       Args:
           text_or_hvo: Text object or its HVO.

       Returns:
           The text name.
       """
       pass
   ```

4. **No UndoableUnitOfWork**
   ```python
   # Bad
   def TextCreate(self, name: str) -> IText:
       text = self.cache.CreateText()
       text.Name = name
       return text

   # Good
   def TextCreate(self, name: str) -> IText:
       with UndoableUnitOfWork(self.project, "Create Text"):
           text = self.cache.CreateText()
           text.Name = name
           return text
   ```

5. **Tests Missing Cleanup**
   ```python
   # Bad
   def test_text_create(db_project):
       text = db_project.TextCreate("Test")
       assert text is not None
       # No cleanup!

   # Good
   def test_text_create(db_project):
       text = db_project.TextCreate("Test")
       try:
           assert text is not None
       finally:
           db_project.TextDelete(text)
   ```

---

## 📋 REVIEW CHECKLIST SUMMARY

Quick checklist for reviewers:

### Before Review
- [ ] Agent's branch checked out
- [ ] All automated checks passed
- [ ] CI/CD pipeline green
- [ ] Review documents ready (QC_CHECKLIST, CODING_STANDARDS)

### During Review
- [ ] All methods implemented per spec
- [ ] Type hints present
- [ ] Docstrings complete
- [ ] Error handling appropriate
- [ ] Tests pass
- [ ] Coverage >90%
- [ ] Integration test passes
- [ ] Documentation complete
- [ ] No security issues
- [ ] Follows coding standards

### After Review
- [ ] Review report created
- [ ] Findings documented
- [ ] Priority assigned to issues
- [ ] Feedback provided to agent
- [ ] Status updated
- [ ] Metrics recorded

---

## 📞 ESCALATION

### When to Escalate
- Fundamental design disagreements
- Security vulnerabilities discovered
- Agent unresponsive to feedback
- Repeated quality issues
- Timeline blockers

### Escalation Process
1. Document the issue clearly
2. Attempt to resolve with agent first
3. If unresolved, escalate to project lead
4. Include all relevant context and history

---

## 🎓 CONTINUOUS IMPROVEMENT

### Learning from Reviews
After each review cycle, consider:

- What patterns of issues are emerging?
- Are standards clear enough?
- Do agents need more guidance?
- Can we automate more checks?
- Should we update templates or documentation?

### Updating Review Process
This process should evolve based on:
- Lessons learned
- Team feedback
- Changing requirements
- Tool improvements

---

**End of Review Process**

For questions or suggestions for improving this process, contact the QC team lead (Agent 5).
