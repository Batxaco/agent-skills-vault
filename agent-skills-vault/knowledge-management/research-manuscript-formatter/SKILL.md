---
name: research-manuscript-formatter
domain: knowledge-management
submodule: research-manuscript-formatter
version: 1.0.0
status: production
maintainer: Principal AI Agent Architect
description: Conversational academic manuscript reformatter and compilation engine for peer-review reconciliation, journal guideline compliance, and camera-ready LaTeX/PDF bundle synthesis.
---

# Research Manuscript Formatter (`skill.md`)

## 1. Operational Scope & Invocation Boundaries
* **Trigger Type:** Interactive Conversational Trigger.
* **Context of Invocation:** Initiated during peer-review preparation, revision passes, or final submission staging.
* **Scope & Boundaries:**
  - Guides interactive reconciliation of author guidelines, target journal formatting (e.g., Elsevier, Springer, IEEE, AGU), strict word counts, and section-by-section layout structures.
  - Invocations operate strictly on designated manuscript markdown nodes within the Obsidian vault and synchronized remote knowledge bases.
  - Out of scope: Automated copy-editing of non-academic prose, code refactoring outside reproducible manuscript appendices, and unverified citation generation.

## 2. Input Specifications & Schema Validation Rules
The engine mandates strict YAML frontmatter at the root of every parsed manuscript (`*.md`). Any missing required field halts downstream processing.

### Frontmatter Schema Definition
```yaml
manuscript:
  title: "Manuscript Title"
  target_journal: "elsevier_cas_single_column" # Options: elsevier_*, springer_*, ieee_*, agu_*
  version: "2.1.0"
  word_count_limits:
    abstract: 250
    main_text: 6500
  authors:
    - name: "Author Name"
      affiliation: "Department, Institution"
      email: "author@domain.org"
      corresponding: true
  dependencies:
    bibtex_source: "references/library.bib"
    figure_dir: "assets/figures"
    drive_assets:
      - folder_id: "1dbxgaYMkfFR_TP7_HtBOoX8NfVLPXzn0"
        mount_point: "assets/remote_data"
      - folder_id: "1v3Ll4stfmgiR7KNQqHGF-Ej6Ap7pFu4b"
        mount_point: "assets/remote_figures"
  sections:
    - id: "sec_intro"
      path: "sections/01_introduction.md"
    - id: "sec_methods"
      path: "sections/02_methods.md"
    - id: "sec_results"
      path: "sections/03_results.md"
    - id: "sec_discussion"
      path: "sections/04_discussion.md"