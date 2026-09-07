# Contributing

Thanks for helping improve Easy-Paper.

## Good Contributions

- Add a new LaTeX template guide under `references/`.
- Improve citation verification or evidence-map fields.
- Add import support for BibTeX, RIS, Zotero exports, CNKI exports or DOI lists.
- Improve scripts without removing provenance, safety checks or academic-integrity boundaries.
- Add examples that teach evidence-guided original writing.

## Boundaries

Do not add features that:

- rewrite a reference paper sentence by sentence into a new manuscript;
- bypass plagiarism detection or academic review;
- fabricate citations, DOI metadata, data, experiments or results;
- remove evidence provenance or verification requirements.

## Validation

Run:

```bash
python scripts/latex_project_inspect.py path/to/paper-project
python scripts/latex_revision_sheet.py path/to/main.tex --output work/revision-ledger-smoke.md
python scripts/scholarly_search.py "typhoon wave height forecasting" --source openalex --limit 3
```

If you are editing the skill itself inside Codex, also run the Codex skill validator if available:

```bash
python path/to/quick_validate.py path/to/easy-paper
```
