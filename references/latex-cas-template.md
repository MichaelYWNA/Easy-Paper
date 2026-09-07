# User LaTeX Template: Elsevier CAS Marine Paper

This reference captures the current template observed at:

`D:\The_Second_Semester_Term_Of_Sophomore\Marine_Paper\STANDARD_converted_latex7`

Use it when the user asks Easy-Paper to work on this paper or a closely related copy.

## Template Facts

- Canonical manuscript: `main.tex`
- Bibliography: `references.bib`
- Document class: `\documentclass[a4paper,fleqn]{cas-sc}`
- Citation package: `\usepackage[authoryear,longnamesfirst]{natbib}`
- Bibliography style: `\bibliographystyle{cas-model2-names}`
- Bibliography command: `\bibliography{references}`
- Current citation style: author-year `\citep{...}` and compatible `natbib` commands.
- Current language: English.
- Field: engineering / ocean-wave forecasting research article.
- Main manuscript organization:
  - `Introduction`
  - `Study area and data`
  - `Methodology`
  - `Experimental design`
  - `Results and discussion`
  - `Conclusions`

## Existing Project Norms

The project already uses `plan/` as the memory and audit layer. Preserve and extend this pattern rather than replacing it.

Important existing conventions:

- `main.tex` remains the canonical manuscript.
- Reference papers are style and structure evidence only unless independently verified as sources for a claim.
- Do not import external findings, data, experimental details or citations into the manuscript without evidence.
- Preserve technical meaning, data, equations, labels, references, figures, tables, numbering and cross-references.
- Keep conclusions bounded to validated station-event-horizon combinations.

## Build Command

The project README records this Windows XeLaTeX command:

```powershell
& 'D:\Latex\bin\windows\xelatex.exe' -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
& 'D:\Latex\bin\windows\xelatex.exe' -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

If using BibTeX after adding references, run:

```powershell
& 'D:\Latex\bin\windows\xelatex.exe' -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
bibtex build/main
& 'D:\Latex\bin\windows\xelatex.exe' -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
& 'D:\Latex\bin\windows\xelatex.exe' -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

Adapt if the project uses another build directory or if `latexmk` is available.

## Editing Rules For This Template

- Use `\section`, `\subsection`, and `\subsubsection`; do not introduce `\chapter`.
- Keep `\begin{abstract}`, `\begin{highlights}`, `\begin{keywords}` and `\maketitle` intact.
- Keep figure paths relative to the project root, usually under `figures/`.
- Keep `\captionof{figure}` blocks if they are already used for centered figure layouts.
- Keep `table`, `longtable`, `resizebox`, `minipage`, math environments and labels intact unless explicitly revising them.
- Preserve existing abbreviations such as PPH-VMD-GRU-LSTM, VMD, GRU, LSTM, Longdong, Hualien, Kong-rey, Morakot and Gaemi.
- Preserve horizon language: 1--4 h is the main operational window; 6 h is a longer-lead degradation/stress check unless new evidence changes this.

## Current Evidence Caution

The observed `references.bib` currently contains a small verified set of entries. When revising Introduction, Study Area, Methodology or Discussion, expect citation coverage to be a limiting factor and record any missing support in `plan/review/evidence-coverage.md`.

## Reference-Paper Use

For this marine-paper template, reference papers may safely inform:

- how typhoon-wave studies introduce operational risk;
- how station/event validation matrices are described;
- how decomposition-recurrent hybrid methods are positioned;
- how global metrics and peak-stage errors are separated;
- how limitations and boundary claims are phrased.

They must not supply:

- new station facts;
- new typhoon event data;
- new model components;
- new experimental settings;
- new performance numbers;
- new citations not verified for this manuscript.
