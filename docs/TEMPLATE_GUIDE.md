# LaTeX Template Guide

Easy-Paper is designed for LaTeX-first manuscript editing. It does not convert the canonical manuscript into Markdown unless the user explicitly asks for a separate draft artifact.

## Default Manuscript Model

```text
paper-project/
|-- main.tex
|-- references.bib
|-- figures/
|-- tables/
`-- plan/
```

If a project uses split chapters, Easy-Paper should follow the existing `\input{}` or `\include{}` structure instead of flattening it.

## Elsevier CAS Template

The first template profile included with Easy-Paper is based on an Elsevier CAS single-column paper.

Expected markers:

```latex
\documentclass[a4paper,fleqn]{cas-sc}
\usepackage[authoryear,longnamesfirst]{natbib}
\bibliographystyle{cas-model2-names}
\bibliography{references}
```

Preferred citation commands:

```latex
\citep{key}
\citet{key}
```

Section commands:

```latex
\section{Introduction}
\subsection{Study context}
\subsubsection{Data preparation}
```

Do not introduce `\chapter` in this template.

## Compile Commands

For simple builds:

```bash
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

When BibTeX is needed:

```bash
xelatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

If output goes to a build directory, adapt the BibTeX target accordingly.

## Safe Editing Rules

- Keep the document class.
- Keep journal class files and `.bst` files.
- Keep existing labels unless the surrounding object is removed by user request.
- Keep figure paths relative to the paper project.
- Keep math environments syntactically intact.
- Keep table layout unless the task is explicitly table formatting.
- Add bibliography entries only after metadata verification.

## Adding a New Template

Create a new reference file under `references/`, for example:

```text
references/latex-ieee-template.md
references/latex-chinese-thesis.md
references/latex-nature-template.md
```

Include:

- document class;
- citation style;
- section commands;
- special front matter;
- bibliography commands;
- compile command;
- prohibited edits;
- known fragile environments.

Then add a row in `SKILL.md` under the routing table.
