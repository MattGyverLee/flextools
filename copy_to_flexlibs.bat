@echo off
REM ==============================================================================
REM Copy FlexLibs Development Files from FlexTools to FlexLibs Repository
REM ==============================================================================
REM Source: D:\Github\flextools\flexlibs_dev
REM Target: D:\Github\flexlibs
REM ==============================================================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo FlexTools to FlexLibs Copy Utility
echo ========================================
echo.

REM Define source and target directories
set "SOURCE_ROOT=D:\Github\flextools\flexlibs_dev"
set "TARGET_ROOT=D:\Github\flexlibs"

REM Check if source directory exists
if not exist "%SOURCE_ROOT%" (
    echo ERROR: Source directory not found: %SOURCE_ROOT%
    echo Please verify the path and try again.
    pause
    exit /b 1
)

REM Check if target directory exists
if not exist "%TARGET_ROOT%" (
    echo ERROR: Target directory not found: %TARGET_ROOT%
    echo Please verify the path and try again.
    pause
    exit /b 1
)

echo Source: %SOURCE_ROOT%
echo Target: %TARGET_ROOT%
echo.
echo This will copy all Python files and documentation from flexlibs_dev to flexlibs.
echo Python cache files (__pycache__) will be excluded.
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause > nul

echo.
echo Starting copy operation...
echo.

REM Create target subdirectories if they don't exist
echo Creating directory structure...
if not exist "%TARGET_ROOT%\core" mkdir "%TARGET_ROOT%\core"
if not exist "%TARGET_ROOT%\grammar_ops" mkdir "%TARGET_ROOT%\grammar_ops"
if not exist "%TARGET_ROOT%\morphology_ops" mkdir "%TARGET_ROOT%\morphology_ops"
if not exist "%TARGET_ROOT%\paragraph_segment_ops" mkdir "%TARGET_ROOT%\paragraph_segment_ops"
if not exist "%TARGET_ROOT%\phonology_ops" mkdir "%TARGET_ROOT%\phonology_ops"
if not exist "%TARGET_ROOT%\tests" mkdir "%TARGET_ROOT%\tests"
if not exist "%TARGET_ROOT%\text_ops" mkdir "%TARGET_ROOT%\text_ops"
if not exist "%TARGET_ROOT%\wordform_ops" mkdir "%TARGET_ROOT%\wordform_ops"

REM Copy root level files (excluding __pycache__)
echo.
echo [1/9] Copying root level files...
copy /Y "%SOURCE_ROOT%\*.py" "%TARGET_ROOT%\" > nul 2>&1
copy /Y "%SOURCE_ROOT%\*.md" "%TARGET_ROOT%\" > nul 2>&1
echo   - Root files copied

REM Copy core module
echo [2/9] Copying core module...
xcopy "%SOURCE_ROOT%\core\*.py" "%TARGET_ROOT%\core\" /Y /Q > nul 2>&1
echo   - core module copied

REM Copy grammar_ops module
echo [3/9] Copying grammar_ops module...
xcopy "%SOURCE_ROOT%\grammar_ops\*.py" "%TARGET_ROOT%\grammar_ops\" /Y /Q > nul 2>&1
echo   - grammar_ops module copied

REM Copy morphology_ops module
echo [4/9] Copying morphology_ops module...
xcopy "%SOURCE_ROOT%\morphology_ops\*.py" "%TARGET_ROOT%\morphology_ops\" /Y /Q > nul 2>&1
echo   - morphology_ops module copied

REM Copy paragraph_segment_ops module
echo [5/9] Copying paragraph_segment_ops module...
xcopy "%SOURCE_ROOT%\paragraph_segment_ops\*.py" "%TARGET_ROOT%\paragraph_segment_ops\" /Y /Q > nul 2>&1
echo   - paragraph_segment_ops module copied

REM Copy phonology_ops module
echo [6/9] Copying phonology_ops module...
xcopy "%SOURCE_ROOT%\phonology_ops\*.py" "%TARGET_ROOT%\phonology_ops\" /Y /Q > nul 2>&1
echo   - phonology_ops module copied

REM Copy tests module
echo [7/9] Copying tests module...
xcopy "%SOURCE_ROOT%\tests\*.py" "%TARGET_ROOT%\tests\" /Y /Q > nul 2>&1
echo   - tests module copied

REM Copy text_ops module
echo [8/9] Copying text_ops module...
xcopy "%SOURCE_ROOT%\text_ops\*.py" "%TARGET_ROOT%\text_ops\" /Y /Q > nul 2>&1
echo   - text_ops module copied

REM Copy wordform_ops module
echo [9/9] Copying wordform_ops module...
xcopy "%SOURCE_ROOT%\wordform_ops\*.py" "%TARGET_ROOT%\wordform_ops\" /Y /Q > nul 2>&1
echo   - wordform_ops module copied

echo.
echo ========================================
echo Copy operation completed successfully!
echo ========================================
echo.
echo Files have been copied from:
echo   %SOURCE_ROOT%
echo.
echo To:
echo   %TARGET_ROOT%
echo.
echo Summary of copied modules:
echo   - core (validators, types, constants, exceptions, resolvers)
echo   - grammar_ops (POS CRUD, POS advanced, grammatical categories)
echo   - morphology_ops (allomorph ops, inflection features, morph rules)
echo   - paragraph_segment_ops (paragraph advanced, segment ops)
echo   - phonology_ops (phoneme CRUD, phoneme advanced, natural classes, environments)
echo   - text_ops (text core, text advanced, paragraph CRUD)
echo   - wordform_ops (wordform CRUD, wordform advanced)
echo   - tests (integration tests)
echo   - Documentation files (*.md)
echo.
echo Next steps:
echo   1. Navigate to D:\Github\flexlibs
echo   2. Review the copied files
echo   3. Run tests to verify everything works
echo   4. Commit the changes to Git
echo.

pause
