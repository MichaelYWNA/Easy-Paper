# LaTeX Project Intake

Use this reference when starting work on a LaTeX paper project or when the user points to a new folder.

## Intake Goals

Before editing, determine:

- project root;
- canonical manuscript file;
- bibliography file and style;
- document class and important packages;
- section hierarchy;
- figure/table locations;
- build command;
- existing plan/review files;
- whether the user wants diagnosis only or direct LaTeX edits.

## First Commands

Prefer deterministic inspection before reading large files:

```powershell
python "<skill>/scripts/latex_project_inspect.py" "<paper-project>" --json "<paper-project>/plan/latex-project-inspection.json"
python "<skill>/scripts/latex_revision_sheet.py" "<paper-project>/main.tex" --output "<paper-project>/plan/revision-ledger.md"
```

If `plan/` does not exist, create it and its `review/`, `task-packets/`, and `chapter-blueprints/` subfolders.

## Required Project Files

Create or update these files as needed:

```text
plan/project-overview.md
plan/easy-paper-progress.md
plan/evidence-map.md
plan/reference-style-map.md
plan/revision-ledger.md
plan/review/evidence-coverage.md
plan/review/citation-verification.md
plan/review/logic-review.md
plan/review/latex-build.md
```

Do not fill them with generic placeholders if the task is narrow. Record only what is known and mark missing items as `Unknown` or `Needs user/source`.

## Main Manuscript Detection

Use this priority:

1. user-specified `.tex`;
2. `main.tex`;
3. a `.tex` file containing `\begin{document}`;
4. ask the user only if multiple plausible roots remain.

## Edit Mode

Classify the current request:

| Mode | Trigger | Output |
|---|---|---|
| `diagnose` | "review", "find problems", "tell me how to revise" | comments and ledgers only |
| `revise-section` | one section, subsection or paragraph | targeted `.tex` patch + ledger |
| `revise-paper` | whole paper, multiple sections, major restructuring | task packets, section passes, `.tex` patches |
| `literature-first` | missing evidence, user asks to find papers | retrieval log + evidence map before edits |
| `compile-fix` | LaTeX errors, formatting, references | compile log review + minimal fix |

When the request is ambiguous but the user clearly wants action, choose the smallest edit mode that can satisfy it.

## Progress Entry

Append a short entry to `plan/easy-paper-progress.md`:

```markdown
## YYYY-MM-DD - <task>

- Scope:
- Input files:
- Output files:
- Evidence used:
- Edits made:
- Verification:
- Remaining risk:
```

## Do Not

- Do not assume the PDF output is canonical when `.tex` exists.
- Do not rewrite the entire paper just because the file is available.
- Do not create a new project structure that fights the user's template.
- Do not delete existing plan/review files from earlier work.
