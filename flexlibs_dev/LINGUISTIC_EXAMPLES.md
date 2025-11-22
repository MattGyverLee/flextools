# Linguistic Usage Examples

**Purpose**: Real-world code examples for linguists using the Complete Data Access API
**Audience**: Field linguists, lexicographers, language documentarians
**Prerequisites**: Basic Python knowledge, familiarity with FLEx

---

## Table of Contents

1. [Basic Text Management](#1-basic-text-management)
2. [Dictionary Development Workflow](#2-dictionary-development-workflow)
3. [Interlinear Text Creation](#3-interlinear-text-creation)
4. [Spelling Approval Workflow](#4-spelling-approval-workflow)
5. [Corpus Statistics](#5-corpus-statistics)
6. [Multi-Script Projects](#6-multi-script-projects)
7. [Genre-Based Text Organization](#7-genre-based-text-organization)
8. [Advanced Examples](#8-advanced-examples)

---

## 1. Basic Text Management

### 1.1 Creating a Text Corpus

**Scenario**: You're starting a new language documentation project and need to create texts for different genres.

```python
from flexlibs_dev.text_ops import TextCoreOperations

# Initialize
ops = TextCoreOperations(project)

# Create texts for different genres
texts_to_create = [
    ("Pig Story", "Narrative"),
    ("How to Make Sago", "Procedural"),
    ("Marriage Customs", "Hortatory"),
    ("Counting Song", "Song"),
    ("Creation Myth", "Narrative"),
]

created_texts = []
for name, genre in texts_to_create:
    try:
        text = ops.text_create(name, genre=genre)
        created_texts.append(text)
        print(f"✓ Created: {name} ({genre})")
    except ValueError as e:
        print(f"✗ Failed: {name} - {e}")

print(f"\nTotal texts created: {len(created_texts)}")
```

### 1.2 Listing All Texts with Metadata

**Scenario**: Generate a report of all texts in your corpus.

```python
from flexlibs_dev.text_ops import TextCoreOperations, TextAdvancedOperations

core_ops = TextCoreOperations(project)
adv_ops = TextAdvancedOperations(project)

print("Text Corpus Inventory")
print("=" * 60)

for i, text in enumerate(core_ops.text_get_all(), start=1):
    name = core_ops.text_get_name(text)
    genre = core_ops.text_get_genre(text)
    abbrev = adv_ops.text_get_abbreviation(text)
    para_count = adv_ops.text_get_paragraph_count(text)

    print(f"{i:3d}. {name:30s} [{abbrev:5s}]")
    print(f"      Genre: {genre:15s} Paragraphs: {para_count}")
    print()
```

**Output**:
```
Text Corpus Inventory
============================================================
  1. Pig Story                      [PigSt]
      Genre: Narrative        Paragraphs: 12

  2. How to Make Sago               [Sago ]
      Genre: Procedural       Paragraphs: 8

  3. Marriage Customs               [Marr ]
      Genre: Hortatory        Paragraphs: 15
```

### 1.3 Adding Paragraphs to a Text

**Scenario**: Transcribing a recorded text, adding each utterance as a paragraph.

```python
from flexlibs_dev.text_ops import ParagraphCRUDOperations

para_ops = ParagraphCRUDOperations(project)

# Get the text
text = core_ops.text_create("Fishing Story", genre="Narrative")

# Transcription (each line = one paragraph/utterance)
transcription = [
    "Yumi go long solwara.",
    "Mi lukim wanpela bikpela pis.",
    "Mi kilim dispela pis long spia.",
    "Mipela i kaikai gut.",
]

# Get vernacular writing system handle
ws_tpi = project.WSHandle("tpi")  # Tok Pisin

# Add each utterance as a paragraph
for i, utterance in enumerate(transcription, start=1):
    para = para_ops.paragraph_create(text, utterance, ws_handle=ws_tpi)
    print(f"Paragraph {i} added: {utterance}")

print(f"\nText '{core_ops.text_get_name(text)}' now has {len(transcription)} paragraphs")
```

---

## 2. Dictionary Development Workflow

### 2.1 Linking Wordforms to Lexicon

**Scenario**: After transcribing texts, you want to build dictionary entries from the wordforms.

```python
from flexlibs_dev.wordform_ops import wordform_crud

# Assuming FLEx has already parsed the text into wordforms
# (This happens automatically when you open a text in FLEx)

# Get all unapproved wordforms
print("Wordforms needing lexicon entries:")
print("=" * 60)

ws_tpi = project.WSHandle("tpi")

for wf in wordform_crud.wordform_get_all_unapproved():
    form = wordform_crud.wordform_get_form(wf, ws_tpi)
    count = wordform_crud.wordform_get_occurrence_count(wf)
    status = wordform_crud.wordform_get_spelling_status(wf)

    print(f"{form:20s} - {count:3d} occurrences - {status.name}")

    # High-frequency wordforms are probably correct
    if count >= 5:
        wordform_crud.wordform_approve_spelling(wf)
        print(f"  → Auto-approved (high frequency)")

        # TODO: Create lexicon entry (requires Phase 2 analysis operations)
        # entry = create_lexicon_entry_from_wordform(wf)
```

### 2.2 Finding All Occurrences of a Word

**Scenario**: You want to see all contexts where a word appears to determine its meaning.

```python
from flexlibs_dev.wordform_ops import wordform_crud, wordform_advanced

# Find a specific wordform
ws_tpi = project.WSHandle("tpi")
target_word = "pis"  # "fish" in Tok Pisin

wf = wordform_crud.wordform_find(target_word, ws_tpi)

if wf:
    # Get occurrence count
    count = wordform_advanced.wordform_get_occurrence_count(wf)
    print(f"'{target_word}' appears {count} times\n")

    # Get all occurrences (segments where it appears)
    occurrences = wordform_advanced.wordform_get_occurrences(wf)

    print("Contexts:")
    print("=" * 60)

    for i, segment in enumerate(occurrences, start=1):
        # Get the segment text (baseline)
        # NOTE: segment_get_baseline_text() is Phase 2 - not yet implemented
        # segment_text = segment_get_baseline_text(segment, ws_tpi)

        # Temporary workaround: get from paragraph
        para = segment.Owner
        para_text = para_ops.paragraph_get_text(para, ws_tpi)

        print(f"{i}. {para_text}")
        # TODO: Highlight the target word in context
else:
    print(f"Wordform '{target_word}' not found")
```

### 2.3 Batch Spelling Approval

**Scenario**: You've reviewed a list of correct spellings and want to approve them all.

```python
from flexlibs_dev.wordform_ops import wordform_crud

# List of approved spellings (e.g., from a wordlist review session)
approved_spellings = [
    "yumi", "lukim", "kaikai", "wara", "haus",
    "solwara", "pis", "spia", "bikpela", "gutpela"
]

ws_tpi = project.WSHandle("tpi")

print("Batch Approval Results:")
print("=" * 60)

approved_count = 0
missing_count = 0

for spelling in approved_spellings:
    wf = wordform_crud.wordform_find(spelling, ws_tpi)

    if wf:
        wordform_crud.wordform_approve_spelling(wf)
        count = wordform_crud.wordform_get_occurrence_count(wf)
        print(f"✓ {spelling:15s} - {count:3d} occurrences")
        approved_count += 1
    else:
        print(f"✗ {spelling:15s} - not found in corpus")
        missing_count += 1

print(f"\nApproved: {approved_count}, Not found: {missing_count}")
```

---

## 3. Interlinear Text Creation

### 3.1 Creating Text with Free Translations

**Scenario**: You're creating an interlinear text and need to add translations at the sentence level.

**NOTE**: This example shows the INTENDED workflow. Segment operations are Phase 2 and not yet implemented.

```python
# PHASE 2 EXAMPLE (not yet implemented)
from flexlibs_dev.text_ops import TextCoreOperations, ParagraphCRUDOperations
# from flexlibs_dev.segment_ops import SegmentOperations  # Phase 2

core_ops = TextCoreOperations(project)
para_ops = ParagraphCRUDOperations(project)

# Create text
text = core_ops.text_create("Genesis 1:1-3", genre="Scripture")

# Writing systems
ws_tpi = project.WSHandle("tpi")  # Tok Pisin (vernacular)
ws_eng = project.WSHandle("en")   # English (analysis)

# Add paragraph with vernacular text
baseline_text = "Long stat, God i mekim heven na graun."
para = para_ops.paragraph_create(text, baseline_text, ws_handle=ws_tpi)

# FLEx automatically parses the paragraph into segments
# (This happens in the FLEx UI or via parser)

# NOW: Add free translations to each segment
# segments = segment_ops.segment_get_all(para)  # Phase 2

# for segment in segments:
#     # Show the baseline
#     baseline = segment_ops.segment_get_baseline_text(segment, ws_tpi)
#     print(f"Vernacular: {baseline}")
#
#     # Linguist provides translation
#     translation = input("Translation: ")
#
#     # Set the free translation
#     segment_ops.segment_set_free_translation(segment, translation, ws_eng)
#     print()

print("PHASE 2 REQUIRED: Segment operations not yet implemented")
```

### 3.2 Word-by-Word Glossing

**Scenario**: Creating morpheme-by-morpheme glosses for linguistic analysis.

**NOTE**: This requires Analysis and Morpheme operations (Phase 2+).

```python
# FUTURE WORKFLOW EXAMPLE (Phase 2+)

# from flexlibs_dev.wordform_ops import wordform_crud
# from flexlibs_dev.analysis_ops import analysis_ops  # Phase 2
# from flexlibs_dev.morpheme_ops import morpheme_ops  # Phase 3

# # Get a wordform
# ws_tpi = project.WSHandle("tpi")
# wf = wordform_crud.wordform_find("lukim", ws_tpi)
#
# # Create an analysis
# analysis = analysis_ops.analysis_create(wf)
#
# # Add morphemes
# # lukim = luk (see) + -im (TR)
# morph1 = morpheme_ops.morpheme_create(analysis, "luk")
# morpheme_ops.morpheme_set_gloss(morph1, "see", ws_en)
# morpheme_ops.morpheme_set_category(morph1, "v")  # verb
#
# morph2 = morpheme_ops.morpheme_create(analysis, "im")
# morpheme_ops.morpheme_set_gloss(morph2, "TR", ws_en)  # transitive
# morpheme_ops.morpheme_set_category(morph2, "suffix")
#
# # Link to lexicon entry
# entry = project.LexiconFindEntry("luk")
# analysis_ops.analysis_link_to_entry(analysis, entry)
#
# # Approve the analysis
# analysis_ops.analysis_approve(analysis)

print("FUTURE: Morpheme-level operations planned for Phase 3")
```

---

## 4. Spelling Approval Workflow

### 4.1 Review Queue Dashboard

**Scenario**: Daily workflow - review unapproved wordforms and approve or correct them.

```python
from flexlibs_dev.wordform_ops import wordform_crud, wordform_advanced

ws_tpi = project.WSHandle("tpi")

# Get statistics
all_wordforms = list(wordform_crud.wordform_get_all())
unapproved = list(wordform_crud.wordform_get_all_unapproved())
correct = list(wordform_crud.wordform_get_all_with_status(
    wordform_crud.SpellingStatusStates.CORRECT
))
incorrect = list(wordform_crud.wordform_get_all_with_status(
    wordform_crud.SpellingStatusStates.INCORRECT
))

print("Wordform Spelling Status Dashboard")
print("=" * 60)
print(f"Total wordforms:     {len(all_wordforms):5d}")
print(f"Approved (correct):  {len(correct):5d}")
print(f"Incorrect:           {len(incorrect):5d}")
print(f"Needs review:        {len(unapproved):5d}")
print()

# Show high-priority items (frequent but unapproved)
print("High Priority Review (frequent wordforms):")
print("-" * 60)

review_items = []
for wf in unapproved:
    count = wordform_advanced.wordform_get_occurrence_count(wf)
    if count >= 3:  # Appears 3+ times
        form = wordform_crud.wordform_get_form(wf, ws_tpi)
        review_items.append((form, count, wf))

# Sort by frequency (most common first)
review_items.sort(key=lambda x: x[1], reverse=True)

for form, count, wf in review_items[:20]:  # Top 20
    print(f"{form:20s} - {count:3d} occurrences")
    # TODO: Show first occurrence context for review

print(f"\nShowing top {min(20, len(review_items))} of {len(review_items)} items")
```

### 4.2 Automated Approval by Frequency

**Scenario**: Auto-approve high-frequency wordforms (likely correct).

```python
from flexlibs_dev.wordform_ops import wordform_crud, wordform_advanced

FREQUENCY_THRESHOLD = 10  # Auto-approve if appears 10+ times

ws_tpi = project.WSHandle("tpi")

print(f"Auto-approving wordforms with {FREQUENCY_THRESHOLD}+ occurrences")
print("=" * 60)

auto_approved = []

for wf in wordform_crud.wordform_get_all_unapproved():
    count = wordform_advanced.wordform_get_occurrence_count(wf)

    if count >= FREQUENCY_THRESHOLD:
        form = wordform_crud.wordform_get_form(wf, ws_tpi)
        wordform_crud.wordform_approve_spelling(wf)
        auto_approved.append((form, count))
        print(f"✓ {form:20s} - {count:3d} occurrences")

print(f"\nAuto-approved {len(auto_approved)} wordforms")

# Review remaining unapproved wordforms manually
remaining = list(wordform_crud.wordform_get_all_unapproved())
print(f"Remaining for manual review: {len(remaining)}")
```

---

## 5. Corpus Statistics

### 5.1 Basic Corpus Metrics

**Scenario**: Generate basic statistics about your text corpus.

```python
from flexlibs_dev.text_ops import TextCoreOperations, TextAdvancedOperations

core_ops = TextCoreOperations(project)
adv_ops = TextAdvancedOperations(project)

print("Corpus Statistics")
print("=" * 60)

# Count texts
all_texts = list(core_ops.text_get_all())
text_count = len(all_texts)

# Count paragraphs across all texts
total_paragraphs = 0
for text in all_texts:
    para_count = adv_ops.text_get_paragraph_count(text)
    total_paragraphs += para_count

# Calculate averages
avg_paragraphs = total_paragraphs / text_count if text_count > 0 else 0

print(f"Total texts:          {text_count:5d}")
print(f"Total paragraphs:     {total_paragraphs:5d}")
print(f"Avg paragraphs/text:  {avg_paragraphs:5.1f}")
print()

# Genre distribution
from collections import Counter
genres = Counter()

for text in all_texts:
    genre = core_ops.text_get_genre(text)
    genres[genre or "(no genre)"] += 1

print("Genre Distribution:")
print("-" * 60)
for genre, count in genres.most_common():
    percentage = (count / text_count) * 100
    print(f"{genre:20s} - {count:3d} texts ({percentage:5.1f}%)")
```

### 5.2 Wordform Frequency Analysis

**Scenario**: Identify the most common words in your corpus.

```python
from flexlibs_dev.wordform_ops import wordform_crud, wordform_advanced

ws_tpi = project.WSHandle("tpi")

print("Wordform Frequency Analysis")
print("=" * 60)

# Collect all wordforms with their frequencies
wordforms_freq = []

for wf in wordform_crud.wordform_get_all():
    form = wordform_crud.wordform_get_form(wf, ws_tpi)
    count = wordform_advanced.wordform_get_occurrence_count(wf)
    wordforms_freq.append((form, count, wf))

# Sort by frequency
wordforms_freq.sort(key=lambda x: x[1], reverse=True)

# Calculate totals
total_tokens = sum(count for _, count, _ in wordforms_freq)
total_types = len(wordforms_freq)
type_token_ratio = total_types / total_tokens if total_tokens > 0 else 0

print(f"Total tokens (word occurrences):  {total_tokens:,}")
print(f"Total types (unique wordforms):   {total_types:,}")
print(f"Type/Token Ratio:                 {type_token_ratio:.4f}")
print()

# Top 50 most frequent wordforms
print("Top 50 Most Frequent Wordforms:")
print("-" * 60)
print(f"{'Rank':>4} {'Wordform':20} {'Count':>7} {'% of corpus':>12}")
print("-" * 60)

for i, (form, count, wf) in enumerate(wordforms_freq[:50], start=1):
    percentage = (count / total_tokens) * 100
    status = wordform_crud.wordform_get_spelling_status(wf)
    status_mark = "✓" if status == wordform_crud.SpellingStatusStates.CORRECT else "?"

    print(f"{i:4d} {status_mark} {form:18} {count:7,} {percentage:11.2f}%")

# Hapax legomena (words appearing only once)
hapax = [form for form, count, _ in wordforms_freq if count == 1]
print(f"\nHapax legomena (words appearing once): {len(hapax)}")
```

---

## 6. Multi-Script Projects

### 6.1 Working with Multiple Writing Systems

**Scenario**: Your language has both a Latin orthography and a traditional script.

```python
from flexlibs_dev.text_ops import TextCoreOperations, ParagraphCRUDOperations

core_ops = TextCoreOperations(project)
para_ops = ParagraphCRUDOperations(project)

# Writing systems
ws_latin = project.WSHandle("xyz-Latn")      # Latin script
ws_traditional = project.WSHandle("xyz-Xyzz") # Traditional script
ws_eng = project.WSHandle("en")              # English analysis

# Create text
text = core_ops.text_create("Proverb 1", genre="Proverb")

# Add paragraph in Latin orthography
para = para_ops.paragraph_create(
    text,
    "Kakamóri dònga tíyé.",  # Latin with tone marks
    ws_handle=ws_latin
)

# Also store in traditional script
para_ops.paragraph_set_text(
    para,
    "𐤊𐤀𐤊𐤀𐤌𐤏𐤓𐤉 𐤃𐤏𐤍𐤂𐤀 𐤈𐤉𐤉𐤄",  # Traditional script
    ws_handle=ws_traditional
)

# Retrieve in both scripts
latin_text = para_ops.paragraph_get_text(para, ws_handle=ws_latin)
traditional_text = para_ops.paragraph_get_text(para, ws_handle=ws_traditional)

print("Multi-Script Text:")
print(f"Latin:        {latin_text}")
print(f"Traditional:  {traditional_text}")

# Text name in different languages
core_ops.text_set_name(text, "Proverb 1", ws_handle=ws_eng)
core_ops.text_set_name(text, "Kakamóri wándé", ws_handle=ws_latin)

eng_name = core_ops.text_get_name(text, ws_handle=ws_eng)
vernac_name = core_ops.text_get_name(text, ws_handle=ws_latin)

print(f"\nText names:")
print(f"English:     {eng_name}")
print(f"Vernacular:  {vernac_name}")
```

### 6.2 Bilingual Dictionary Export

**Scenario**: Extract vernacular-English lexicon data from your corpus.

```python
# Using existing flexlibs methods (from Agent 4 review)

ws_tpi = project.WSHandle("tpi")  # Tok Pisin
ws_eng = project.WSHandle("en")   # English

print("Bilingual Dictionary Export (Tok Pisin - English)")
print("=" * 60)

entry_count = 0

for entry in project.LexiconAllEntries():
    # Get headword (main entry form)
    headword = project.LexiconGetLexemeForm(entry)

    # Get all senses
    for sense in entry.SensesOS:
        # Get gloss in English
        gloss = project.LexiconGetSenseGloss(sense, ws_eng)

        # Get definition if available
        definition = project.LexiconGetSenseDefinition(sense)

        # Get sense number (e.g., "1.2" for subsenses)
        sense_num = project.LexiconGetSenseNumber(sense)

        # Format output
        if sense_num == "1" or not sense_num:
            # Main sense
            print(f"\n{headword}")
        else:
            # Subsense
            print(f"  {sense_num}.")

        print(f"    {gloss}")

        if definition:
            # Wrap long definitions
            import textwrap
            wrapped = textwrap.fill(definition, width=70, initial_indent="    Def: ",
                                  subsequent_indent="         ")
            print(wrapped)

        entry_count += 1

print(f"\n\nTotal entries: {entry_count}")
```

---

## 7. Genre-Based Text Organization

### 7.1 Organizing Texts by Genre

**Scenario**: List all texts organized by genre for a corpus overview.

```python
from flexlibs_dev.text_ops import TextCoreOperations
from collections import defaultdict

core_ops = TextCoreOperations(project)

# Group texts by genre
texts_by_genre = defaultdict(list)

for text in core_ops.text_get_all():
    name = core_ops.text_get_name(text)
    genre = core_ops.text_get_genre(text) or "(Unclassified)"
    texts_by_genre[genre].append(name)

# Display organized by genre
print("Text Corpus by Genre")
print("=" * 60)

for genre in sorted(texts_by_genre.keys()):
    texts = texts_by_genre[genre]
    print(f"\n{genre} ({len(texts)} texts):")
    print("-" * 60)

    for i, text_name in enumerate(sorted(texts), start=1):
        print(f"  {i:2d}. {text_name}")

# Summary
total_texts = sum(len(texts) for texts in texts_by_genre.values())
print(f"\n\nTotal: {total_texts} texts in {len(texts_by_genre)} genres")
```

### 7.2 Creating a Text Collection

**Scenario**: Create a thematic collection (e.g., all texts about fishing).

```python
from flexlibs_dev.text_ops import TextCoreOperations

core_ops = TextCoreOperations(project)

# Create texts for a fishing text collection
fishing_texts = [
    "Fishing with Nets",
    "Spearfishing Technique",
    "Traditional Fish Traps",
    "Night Fishing Story",
    "The Big Catch",
]

print("Creating Fishing Text Collection")
print("=" * 60)

for text_name in fishing_texts:
    try:
        text = core_ops.text_create(text_name, genre="Procedural")
        print(f"✓ Created: {text_name}")

        # Set abbreviation for easy reference
        # (using TextAdvancedOperations - currently only has getter)
        # TODO: Need text_set_abbreviation() method

    except ValueError as e:
        print(f"✗ Failed: {text_name} - {e}")

print(f"\nCollection '{len(fishing_texts)}' texts created")

# Could also add custom field "Collection" or "Theme"
# (requires Phase 2 custom field support)
```

---

## 8. Advanced Examples

### 8.1 Data Quality Check

**Scenario**: Identify potential data quality issues in your corpus.

```python
from flexlibs_dev.text_ops import TextCoreOperations, TextAdvancedOperations
from flexlibs_dev.wordform_ops import wordform_crud, wordform_advanced

core_ops = TextCoreOperations(project)
adv_ops = TextAdvancedOperations(project)

print("Data Quality Report")
print("=" * 60)

# Check 1: Texts without genre
print("\n1. Texts without genre classification:")
no_genre_count = 0
for text in core_ops.text_get_all():
    genre = core_ops.text_get_genre(text)
    if not genre:
        name = core_ops.text_get_name(text)
        print(f"  - {name}")
        no_genre_count += 1

if no_genre_count == 0:
    print("  ✓ All texts have genres")

# Check 2: Empty texts (no paragraphs)
print("\n2. Empty texts (no paragraphs):")
empty_count = 0
for text in core_ops.text_get_all():
    para_count = adv_ops.text_get_paragraph_count(text)
    if para_count == 0:
        name = core_ops.text_get_name(text)
        print(f"  - {name}")
        empty_count += 1

if empty_count == 0:
    print("  ✓ All texts have content")

# Check 3: High-frequency unapproved wordforms
print("\n3. Frequent unapproved wordforms (likely typos or need approval):")
ws_tpi = project.WSHandle("tpi")

frequent_unapproved = []
for wf in wordform_crud.wordform_get_all_unapproved():
    count = wordform_advanced.wordform_get_occurrence_count(wf)
    if count >= 5:
        form = wordform_crud.wordform_get_form(wf, ws_tpi)
        frequent_unapproved.append((form, count))

frequent_unapproved.sort(key=lambda x: x[1], reverse=True)

for form, count in frequent_unapproved[:10]:
    print(f"  - {form:20s} ({count} occurrences)")

if not frequent_unapproved:
    print("  ✓ No high-frequency unapproved wordforms")

# Check 4: Wordforms marked as incorrect but still appear in texts
print("\n4. Incorrect wordforms still in texts:")
incorrect_count = 0
for wf in wordform_crud.wordform_get_all_with_status(
    wordform_crud.SpellingStatusStates.INCORRECT
):
    count = wordform_advanced.wordform_get_occurrence_count(wf)
    if count > 0:
        form = wordform_crud.wordform_get_form(wf, ws_tpi)
        print(f"  - {form:20s} ({count} occurrences)")
        incorrect_count += 1

if incorrect_count == 0:
    print("  ✓ No incorrect wordforms in texts")

print("\n" + "=" * 60)
print("Data Quality Check Complete")
```

### 8.2 Exporting Text for Analysis

**Scenario**: Export texts to a simple format for external analysis tools.

```python
from flexlibs_dev.text_ops import TextCoreOperations, ParagraphCRUDOperations
import csv

core_ops = TextCoreOperations(project)
para_ops = ParagraphCRUDOperations(project)

# Export to CSV for analysis in R, Excel, etc.
output_file = "corpus_export.csv"

ws_tpi = project.WSHandle("tpi")
ws_eng = project.WSHandle("en")

print(f"Exporting corpus to {output_file}")

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Header row
    writer.writerow(['TextID', 'TextName', 'Genre', 'ParaNum', 'VernacularText', 'Translation'])

    text_id = 0
    total_paragraphs = 0

    for text in core_ops.text_get_all():
        text_id += 1
        text_name = core_ops.text_get_name(text)
        genre = core_ops.text_get_genre(text)

        para_num = 0
        for para in para_ops.paragraph_get_all(text):
            para_num += 1
            total_paragraphs += 1

            # Get vernacular text
            vernac_text = para_ops.paragraph_get_text(para, ws_handle=ws_tpi)

            # Get translation (if available)
            # NOTE: Translation is at segment level (Phase 2)
            # For now, leave blank
            translation = ""

            # Write row
            writer.writerow([text_id, text_name, genre, para_num, vernac_text, translation])

print(f"✓ Exported {text_id} texts, {total_paragraphs} paragraphs")
print(f"  File: {output_file}")
```

### 8.3 Finding Texts with Media Files

**Scenario**: List all texts that have associated audio recordings.

```python
from flexlibs_dev.text_ops import TextCoreOperations, TextAdvancedOperations

core_ops = TextCoreOperations(project)
adv_ops = TextAdvancedOperations(project)

print("Texts with Audio Recordings")
print("=" * 60)

texts_with_media = []

for text in core_ops.text_get_all():
    media_files = adv_ops.text_get_media_files(text)

    if media_files:
        name = core_ops.text_get_name(text)
        media_count = len(media_files)
        texts_with_media.append((name, media_count, media_files))

        print(f"\n{name}")
        print(f"  {media_count} media file(s):")

        for media in media_files:
            # Get media file path
            # (actual path access depends on ICmMedia structure)
            # file_path = media.MediaFileRA.AbsoluteInternalPath
            print(f"    - [Media file]")

if not texts_with_media:
    print("No texts with media files found")
else:
    print(f"\n\nTotal: {len(texts_with_media)} texts with media")
```

---

## 9. Language-Specific Examples

### 9.1 Tonal Language (Yoruba)

**Scenario**: Working with tone-marked text in Yoruba.

```python
from flexlibs_dev.text_ops import TextCoreOperations, ParagraphCRUDOperations
from flexlibs_dev.wordform_ops import wordform_crud

core_ops = TextCoreOperations(project)
para_ops = ParagraphCRUDOperations(project)

ws_yor = project.WSHandle("yo")  # Yoruba

# Create text with tone marks
text = core_ops.text_create("Àlọ́ Àkúkọ", genre="Narrative")  # "First Story"

# Yoruba text with three tone levels: á (high), a (mid), à (low)
yoruba_text = """
Ní àkókò kan, ọba kan wà tí ó ní ọmọ méjì.
Ọmọ àkọ́kọ́ náà jẹ́ ọlọ́gbọ́n, ṣùgbọ́n ọmọ kejì jẹ́ aláìgbọ́n.
"""

para = para_ops.paragraph_create(text, yoruba_text.strip(), ws_handle=ws_yor)

print("Yoruba text created with tone marks")
print("Text:", core_ops.text_get_name(text))
print("Content:", para_ops.paragraph_get_text(para, ws_handle=ws_yor))

# Tone marks are preserved in Unicode
# Each wordform will retain its tone marks
wf = wordform_crud.wordform_find("ọlọ́gbọ́n", ws_yor)
if wf:
    form = wordform_crud.wordform_get_form(wf, ws_yor)
    print(f"\nWordform with tones: {form}")
    print("Unicode code points:", " ".join(f"U+{ord(c):04X}" for c in form))
```

### 9.2 Polysynthetic Language (Greenlandic)

**Scenario**: Handling very long wordforms in Greenlandic (Kalaallisut).

```python
from flexlibs_dev.wordform_ops import wordform_crud, wordform_advanced

ws_kal = project.WSHandle("kl")  # Greenlandic

# Very long wordform (not uncommon in Greenlandic)
long_wordform = "tusaatsiarunnanngittualuujunga"
# Roughly: "I can't hear very well"

# Create wordform
wf = wordform_crud.wordform_create(long_wordform, ws_kal)

print(f"Wordform: {long_wordform}")
print(f"Length: {len(long_wordform)} characters")

# In actual use, this would be analyzed into morphemes:
# tusaa-tsiaq-unnanngit-ssuaq-uu-junga
# hear-try.to-cannot-really-be-1SG.IND

# Phase 2+ would support morpheme breakdown
print("\nMorpheme analysis (requires Phase 2+):")
print("  tusaa-    (hear)")
print("  -tsiaq-   (try to)")
print("  -unnanngit- (cannot)")
print("  -ssuaq-   (really)")
print("  -uu-      (be)")
print("  -junga    (1SG.IND)")
```

### 9.3 Multilingual Project (Papua New Guinea)

**Scenario**: Project with multiple languages and English glosses.

```python
from flexlibs_dev.text_ops import TextCoreOperations, ParagraphCRUDOperations

core_ops = TextCoreOperations(project)
para_ops = ParagraphCRUDOperations(project)

# Writing systems for multiple languages
ws_tpi = project.WSHandle("tpi")  # Tok Pisin
ws_meu = project.WSHandle("meu")  # Motu
ws_eng = project.WSHandle("en")   # English

# Create texts in different languages
texts = [
    ("Pig Story", "tpi", "Stori bilong pik", "Narrative"),
    ("Fishing Trip", "meu", "Lau henuala", "Narrative"),
    ("How to Cook Sago", "tpi", "Wanem pasin bilong kukim sago", "Procedural"),
]

print("Creating multilingual corpus")
print("=" * 60)

for name_eng, lang_code, name_vernac, genre in texts:
    # Create text
    text = core_ops.text_create(name_eng, genre=genre)

    # Set vernacular name
    ws = project.WSHandle(lang_code)
    core_ops.text_set_name(text, name_vernac, ws_handle=ws)

    # Display
    eng_name = core_ops.text_get_name(text, ws_handle=ws_eng)
    vernac_name = core_ops.text_get_name(text, ws_handle=ws)

    print(f"Created: {eng_name}")
    print(f"  Vernacular: {vernac_name} ({lang_code})")
    print(f"  Genre: {genre}")
    print()
```

---

## Conclusion

These examples demonstrate the practical use of the Complete Data Access API for real-world linguistic workflows. As Phase 2 implementations are completed (segment operations, analysis operations, translation support), many more workflows will become possible.

### Key Takeaways for Linguists:

1. **Writing Systems**: Always specify `ws_handle` for multilingual projects
2. **Generators**: Use `for ... in ...` patterns for memory-efficient iteration
3. **Error Handling**: Use try/except for robust scripts
4. **Batch Processing**: Process unapproved wordforms, text collections systematically
5. **Data Quality**: Regular checks help maintain corpus integrity

### Next Steps:

- Explore existing flexlibs methods (39 methods, see EXISTING_FUNCTIONS_REVIEW.md)
- Await Phase 2 implementations (segment, analysis, translation operations)
- Contribute feedback on linguistic edge cases and requirements

For questions or feature requests, contact the development team or consult the LINGUISTICS_REVIEW.md document.
