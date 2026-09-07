# Literature Retrieval

Use this reference when collecting, screening, or verifying papers for Easy-Paper.

## Source Priority

1. User-provided papers, PDFs, BibTeX, DOI lists, notes, CNKI exports, or Zotero/EndNote records.
2. Identifier lookup by DOI, PMID, PMCID, arXiv ID, title, or OpenAlex ID.
3. OpenAlex broad search for cross-disciplinary discovery and citation counts.
4. Crossref for DOI metadata and journal/publisher records.
5. Semantic Scholar for citation graph, related papers and abstracts when available.
6. Domain databases: PubMed/PMC/Europe PMC for biomedical work, arXiv for CS/math/physics, CORE/Unpaywall for open-access full text.
7. Web search only as a fallback for official landing pages or search strategy support.

For CNKI, WanFang, VIP, Google Scholar, IEEE Xplore, ScienceDirect or other gated platforms, do not bypass access controls. Provide search strings and process user-exported metadata, abstracts, PDFs, or RIS/BibTeX files.

## Retrieval Contract

Before searching, record:

```markdown
## Retrieval Contract
- Research topic:
- Target section:
- Needed claim types:
- Inclusion criteria:
- Exclusion criteria:
- Year range:
- Required sources:
- Access constraints:
```

## Search Log

Every query that feeds the paper must be logged in `plan/literature/retrieval-log.md`:

```markdown
### YYYY-MM-DD HH:MM - <database>
- Query:
- Endpoint or interface:
- Parameters:
- Result count:
- Selected IDs:
- Access date:
- Warnings:
```

## Candidate Triage

Use a table like this:

```markdown
| Source ID | Title | Year | Venue | DOI/ID | Citations | OA/full text | Decision | Reason |
|---|---:|---:|---|---|---:|---|---|---|
```

Decision values:

- `keep-primary`: central to the argument.
- `keep-supporting`: useful for background or comparison.
- `method-reference`: useful for methods or metrics.
- `style-only`: useful only for structure/rhetorical pattern; not cited for claims.
- `exclude`: weak, irrelevant, duplicate, unverifiable, or outside scope.

## Evidence Map

Use `plan/evidence-map.md` for claim-level mapping:

```markdown
| Evidence ID | Source ID | Citation key | Verified? | Source type | What was read | Usable fact | Supported claim | Citation slot | Risk |
|---|---|---|---|---|---|---|---|---|---|
```

Rules:

- `Supported claim` must be a sentence that could appear in the manuscript.
- `Citation slot` must be specific, such as `Introduction P2 method landscape`.
- `What was read` must distinguish title/abstract/metadata/full text/user notes.
- If only title/abstract was read, do not claim details from methods, results or limitations.
- If a paper contributes only style, do not cite it as evidence.

## Verification

Separate two questions:

1. **Existence**: Does the source exist and does the metadata match?
2. **Support**: Does the source support this exact claim?

Record existence checks in `plan/review/citation-verification.md`.
Record support checks in `plan/review/evidence-coverage.md`.

Suggested verification fields:

```markdown
| Citation key | DOI/ID | Crossref | OpenAlex | Semantic Scholar | Metadata match | Claim support | Verdict |
|---|---|---|---|---|---|---|---|
```

Verdicts:

- `verified-supported`
- `verified-but-indirect`
- `metadata-only`
- `needs-full-text`
- `not-supported`
- `unverified-do-not-use`

## BibTeX Rules

- Add a new BibTeX entry only after metadata is available from a reliable source.
- Prefer DOI-based entries for journal articles.
- Keep citation keys stable and human-readable, such as `wei2021typhoon`.
- Do not change existing citation keys unless all `.tex` references are updated.
- For author-year `natbib`, make sure author and year fields are present.

## Search Script

Easy-Paper includes `scripts/scholarly_search.py` for simple OpenAlex/Crossref lookup and BibTeX skeleton output. It is intentionally small; for heavy systematic search, use specialized tools or direct database exports.
