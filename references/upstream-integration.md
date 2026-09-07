# Upstream Integration Map

Easy-Paper combines ideas from four GitHub projects without copying their prose into manuscripts.

## 1. ai-skill-scholar

Source: `https://github.com/dsebastien/ai-skill-scholar`

Use its pattern for:

- OpenAlex-first scholarly discovery when the user needs broad, no-key searching.
- Citation count, venue, year, DOI/arXiv/PMID and open-access URL triage.
- Two-pass literature review: wide search, then human/agent screening, then shortlist reading.
- Persistent review sessions with candidate, shortlist, fetch plan and synthesis artifacts.

Easy-Paper adaptation:

- Store candidates in `plan/literature/candidates.json`.
- Store accepted sources in `plan/literature/shortlist.json`.
- Convert accepted sources into `plan/evidence-map.md`, not directly into manuscript prose.

## 2. scientific-agent-skills / paper-lookup

Source: `https://github.com/K-Dense-AI/scientific-agent-skills`

Use its pattern for:

- Choosing the right scholarly database for the task instead of querying every source.
- Recording retrieval provenance: endpoint, parameters, identifiers, access date, and warnings.
- Treating API output as untrusted external data.
- Recognizing that HTTP success does not guarantee valid scholarly content.
- Using OpenAlex, Crossref, Semantic Scholar, PubMed/PMC, Europe PMC, arXiv, bioRxiv, medRxiv, CORE and Unpaywall according to domain and access needs.

Easy-Paper adaptation:

- Record every automated query in `plan/literature/retrieval-log.md`.
- For Chinese databases such as CNKI, WanFang and VIP, provide search strategies and process user-exported metadata or abstracts; do not bypass access controls or invent unavailable records.
- Prefer DOI or stable identifiers; otherwise mark the source as metadata-only or unverifiable.

## 3. OpenDraft

Source: `https://github.com/federicodeponte/opendraft`

Use its pattern for:

- Multi-phase pipeline: research, structure, citation management, compose, QA, export.
- Separating citation existence verification from claim-support verification.
- Maintaining a citation database and citation summary before writing.
- Running coherence, voice and fact-check passes after composition.

Easy-Paper adaptation:

- For revision work, replace "compose from scratch" with "read target LaTeX segment -> revise with evidence -> write back".
- Keep two verification tracks:
  - `plan/review/citation-verification.md`: does the source exist and match the BibTeX?
  - `plan/review/evidence-coverage.md`: does the source actually support the sentence or paragraph?
- Use full-paper generation only when the user asks for drafting and provides enough research material.

## 4. academic-research-skills

Source: `https://github.com/Imbad0202/academic-research-skills`

Use its pattern for:

- Research-question scoping, source verification, synthesis, editor review and ethics review.
- Evidence grading and source-quality hierarchy.
- Devil's-advocate checks against confirmation bias, cherry-picking, unsupported causality and logical gaps.
- Explicit AI-assistance and attribution integrity review.

Easy-Paper adaptation:

- Add an `Integrity Gate` before any reference-informed rewrite.
- Add a `Logic Gate` after each section-level revision.
- Add a `Style Origin Note` when a paragraph's structure is inspired by one or more reference papers, while ensuring the final wording is original.

## Integration Rule

When a user says "use other papers to revise mine", Easy-Paper must translate that into:

1. identify the writing move used by the source papers;
2. identify the evidence or claim type needed in the user's own paper;
3. write an original sentence using the user's data, method, and verified sources;
4. cite the source only if it supports the claim, not because its wording was influential.
