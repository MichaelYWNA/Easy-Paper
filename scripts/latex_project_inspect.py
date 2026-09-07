#!/usr/bin/env python3
"""Inspect a LaTeX paper project and emit a compact JSON summary."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SECTION_RE = re.compile(r"^\\(part|chapter|section|subsection|subsubsection)\*?\{(.+?)\}")
CITE_RE = re.compile(r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear)\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|autoref|cref|Cref)\{([^}]+)\}")
PACKAGE_RE = re.compile(r"\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}")
DOC_CLASS_RE = re.compile(r"\\documentclass(?:\[[^\]]*\])?\{([^}]+)\}")
BIB_STYLE_RE = re.compile(r"\\bibliographystyle\{([^}]+)\}")
BIB_RE = re.compile(r"\\bibliography\{([^}]+)\}")
GRAPHICSPATH_RE = re.compile(r"\\graphicspath\{(.+)\}")
INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "utf-8-sig", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace")


def find_main_tex(root: Path) -> Path | None:
    preferred = root / "main.tex"
    if preferred.exists():
        return preferred
    candidates = sorted(root.rglob("*.tex"))
    document_candidates: list[Path] = []
    for candidate in candidates:
        try:
            text = read_text(candidate)
        except OSError:
            continue
        if "\\begin{document}" in text:
            document_candidates.append(candidate)
    if len(document_candidates) == 1:
        return document_candidates[0]
    return candidates[0] if len(candidates) == 1 else None


def split_csv_like(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def find_missing_figures(root: Path, figures: list[str]) -> list[str]:
    missing: list[str] = []
    search_dirs = [root, root / "figures"]
    extensions = ["", ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg"]
    for figure in figures:
        normalized = figure.replace("/", "\\")
        found = False
        raw = Path(normalized)
        for base in search_dirs:
            for ext in extensions:
                candidate = base / (str(raw) + ext if not raw.suffix else str(raw))
                if candidate.exists():
                    found = True
                    break
            if found:
                break
        if not found:
            missing.append(figure)
    return missing


def inspect_project(root: Path) -> dict[str, Any]:
    root = root.resolve()
    main_tex = find_main_tex(root)
    if main_tex is None:
        return {
            "project_root": str(root),
            "error": "No unambiguous LaTeX main file found",
            "tex_files": [str(path.relative_to(root)) for path in sorted(root.rglob("*.tex"))],
        }

    text = read_text(main_tex)
    lines = text.splitlines()
    document_class = None
    packages: list[str] = []
    sections: list[dict[str, Any]] = []
    labels: list[str] = []
    refs: list[str] = []
    cite_keys: list[str] = []
    figures: list[str] = []
    bibliography_files: list[str] = []
    bibliography_style = None
    graphicspath = None

    class_match = DOC_CLASS_RE.search(text)
    if class_match:
        document_class = class_match.group(1)

    for match in PACKAGE_RE.finditer(text):
        packages.extend(split_csv_like(match.group(1)))

    style_match = BIB_STYLE_RE.search(text)
    if style_match:
        bibliography_style = style_match.group(1)

    bib_match = BIB_RE.search(text)
    if bib_match:
        for item in split_csv_like(bib_match.group(1)):
            bibliography_files.append(item if item.endswith(".bib") else f"{item}.bib")

    gp_match = GRAPHICSPATH_RE.search(text)
    if gp_match:
        paths = re.findall(r"\{([^{}]+)\}", gp_match.group(1))
        graphicspath = paths or gp_match.group(1)

    for idx, line in enumerate(lines, start=1):
        sec_match = SECTION_RE.match(line.strip())
        if sec_match:
            sections.append({"line": idx, "level": sec_match.group(1), "title": sec_match.group(2)})
        labels.extend(LABEL_RE.findall(line))
        refs.extend(REF_RE.findall(line))
        for cite_group in CITE_RE.findall(line):
            cite_keys.extend(split_csv_like(cite_group))
        figures.extend(INCLUDEGRAPHICS_RE.findall(line))

    bib_entries: dict[str, int] = {}
    known_keys: set[str] = set()
    for bib_name in bibliography_files:
        bib_path = root / bib_name
        if bib_path.exists():
            bib_text = read_text(bib_path)
            entries = re.findall(r"@\w+\s*\{\s*([^,\s]+)", bib_text)
            known_keys.update(entries)
            bib_entries[bib_name] = len(entries)
        else:
            bib_entries[bib_name] = -1

    return {
        "project_root": str(root),
        "main_tex": str(main_tex),
        "document_class": document_class,
        "packages": sorted(set(packages)),
        "bibliography_style": bibliography_style,
        "bibliography_files": bibliography_files,
        "bibliography_entry_counts": bib_entries,
        "graphicspath": graphicspath,
        "section_count": len(sections),
        "sections": sections,
        "citation_key_count": len(set(cite_keys)),
        "citation_keys": sorted(set(cite_keys)),
        "missing_citation_keys": sorted(set(cite_keys) - known_keys) if known_keys else sorted(set(cite_keys)),
        "label_count": len(set(labels)),
        "reference_count": len(set(refs)),
        "undefined_refs_by_static_scan": sorted(set(refs) - set(labels)),
        "figures": figures,
        "missing_figures_by_static_scan": find_missing_figures(root, figures),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", help="LaTeX project root")
    parser.add_argument("--json", dest="json_path", help="Optional output JSON path")
    args = parser.parse_args()

    result = inspect_project(Path(args.project))
    output = json.dumps(result, indent=2, ensure_ascii=False)
    if args.json_path:
        path = Path(args.json_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output + "\n", encoding="utf-8")
    print(output)
    return 0 if "error" not in result else 2


if __name__ == "__main__":
    raise SystemExit(main())
