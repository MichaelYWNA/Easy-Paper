# Easy-Paper Workflow

Easy-Paper follows a staged workflow so that every manuscript change can be traced back to a reason, evidence source and validation result.

## Stage 1: Project Intake

Goal: understand the LaTeX project before editing.

Actions:

- Identify the project root.
- Identify the canonical manuscript, usually `main.tex`.
- Identify bibliography files and citation style.
- Extract section hierarchy, citation keys, labels, references and figure paths.
- Record compile commands if known.

Recommended command:

```bash
python scripts/latex_project_inspect.py "path/to/paper-project" --json "path/to/paper-project/plan/latex-project-inspection.json"
```

Output:

- `plan/latex-project-inspection.json`
- updated project notes if the user wants persistent tracking

## Stage 2: Literature Pool

Goal: gather the sources that may support the paper.

Accepted inputs:

- PDFs supplied by the user;
- BibTeX or RIS exports;
- DOI, PMID, PMCID, arXiv ID or OpenAlex ID lists;
- CNKI, WanFang, VIP or Google Scholar exported records;
- OpenAlex or Crossref search results.

For online retrieval, record a reproducible query log:

```markdown
### YYYY-MM-DD HH:MM - OpenAlex
- Query:
- Endpoint:
- Parameters:
- Result count:
- Selected IDs:
- Access date:
- Warnings:
```

## Stage 3: Evidence Map

Goal: convert sources into claim-level evidence.

Use:

```markdown
| Evidence ID | Source ID | Citation key | Verified? | Source type | What was read | Usable fact | Supported claim | Citation slot | Risk |
|---|---|---|---|---|---|---|---|---|---|
```

Rules:

- A source is not useful just because it is related.
- A source must support a concrete claim.
- If only the abstract was read, do not cite details from the methods or results.
- If a source only teaches structure or style, mark it `style-only` and do not cite it as evidence.

## Stage 4: Reference Style Map

Goal: learn writing moves without copying wording.

Use:

```markdown
## Pattern P01: operational problem before method landscape

- Source papers:
- Section type:
- Writing move:
- Why it works:
- Safe adaptation rule:
- Forbidden reuse:
```

Good style patterns include:

- problem -> method family -> limitation -> gap -> contribution;
- observation -> exception -> bounded interpretation;
- result table -> trend -> adverse case -> operational meaning;
- method component -> role -> interface with next component.

## Stage 5: Revision Ledger

Goal: revise the user's manuscript paragraph by paragraph and sentence by sentence.

Recommended command:

```bash
python scripts/latex_revision_sheet.py "path/to/main.tex" --output "path/to/paper-project/plan/revision-ledger.md"
```

Every target paragraph should record:

- location;
- paragraph role;
- current main claim;
- evidence IDs;
- reference style move;
- problems;
- revision strategy;
- post-revision logic;
- LaTeX risk.

Every target sentence should record:

- original function;
- issue;
- evidence IDs;
- source pattern, not wording;
- revised sentence;
- logic check;
- remaining risk.

## Stage 6: LaTeX Patch

Goal: write approved revisions back to `.tex` safely.

Rules:

- Read the full surrounding section before editing.
- Preserve commands, equations, figures, tables, labels, cross-references and citation keys.
- Do not add packages unless the template requires it.
- Do not rename assets casually.
- Escape LaTeX special characters in new prose.

## Stage 7: Review and Verification

Before claiming completion, check:

- citations in `.tex` exist in `.bib`;
- new references have DOI or stable metadata where possible;
- every strong claim has an evidence-map row;
- revised paragraphs follow the section argument;
- LaTeX compile logs do not show fatal errors;
- unresolved risks are recorded.

Recommended review files:

```text
plan/review/evidence-coverage.md
plan/review/citation-verification.md
plan/review/logic-review.md
plan/review/latex-build.md
```

## Modes

| Mode | When to use | Main output |
|---|---|---|
| `diagnose` | user wants comments only | review notes and revision ledger |
| `literature-first` | evidence is missing | candidate list, retrieval log and evidence map |
| `revise-section` | one section or subsection | targeted `.tex` patch and review |
| `revise-paper` | many sections or whole paper | task packets, section passes and final checks |
| `compile-fix` | LaTeX fails to build | minimal compile-safe patch |
