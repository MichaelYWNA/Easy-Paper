# Easy-Paper Extension Points

Use this reference when modifying Easy-Paper itself.

## Design Goals

Easy-Paper should stay modular:

- `SKILL.md` keeps routing, boundaries and core workflow.
- `references/` holds detailed operating modes.
- `scripts/` holds deterministic helpers.
- `assets/` can hold reusable project templates or icons.
- `agents/openai.yaml` holds UI metadata.

Avoid adding large examples or generic writing advice to `SKILL.md`.

## Where To Add Future Features

| Need | File to modify |
|---|---|
| New database or retrieval source | `references/literature-retrieval.md`; optionally `scripts/scholarly_search.py` |
| New LaTeX journal template | new `references/latex-<template>.md` and route from `SKILL.md` |
| New revision ledger columns | `references/evidence-led-revision.md` and `scripts/latex_revision_sheet.py` |
| Stronger compile checks | add or update `scripts/latex_compile_check.py` |
| Plagiarism/integrity report | add `references/integrity-review.md` |
| Chinese thesis template | add `references/latex-chinese-thesis.md` |
| Zotero/RIS/BibTeX import | add `scripts/import_references.py` |

## Version Notes

Record meaningful changes here:

```markdown
## Version
- 0.1.0 (2026-09-07): Initial Easy-Paper workflow for LaTeX evidence-guided revision.
```

## Validation Checklist

After changing Easy-Paper:

```powershell
python "C:\Users\We_married dream\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "C:\Users\We_married dream\.codex\skills\easy-paper"
python "C:\Users\We_married dream\.codex\skills\easy-paper\scripts\latex_project_inspect.py" "D:\The_Second_Semester_Term_Of_Sophomore\Marine_Paper\STANDARD_converted_latex7"
python "C:\Users\We_married dream\.codex\skills\easy-paper\scripts\latex_revision_sheet.py" "D:\The_Second_Semester_Term_Of_Sophomore\Marine_Paper\STANDARD_converted_latex7\main.tex" --output "C:\Users\We_married dream\Documents\Codex\2026-09-07\github\work\easy-paper-smoke-ledger.md"
```
