#!/usr/bin/env python3
"""Small scholarly search helper for Easy-Paper.

This is not a systematic-review engine. It provides quick OpenAlex and Crossref
triage with enough metadata to start an evidence map.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from typing import Any


USER_AGENT = "Easy-Paper/0.1 (mailto optional; scholarly metadata triage)"


def fetch_json(url: str, headers: dict[str, str] | None = None) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def inverted_index_to_text(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, word_positions in index.items():
        for pos in word_positions:
            positions.append((pos, word))
    return " ".join(word for _, word in sorted(positions))


def openalex_search(query: str, limit: int, year: str | None, min_citations: int) -> list[dict[str, Any]]:
    params = {"search": query, "per-page": str(limit), "sort": "cited_by_count:desc"}
    filters = []
    if year:
        if "-" in year:
            start, end = year.split("-", 1)
            filters.append(f"from_publication_date:{start}-01-01")
            filters.append(f"to_publication_date:{end}-12-31")
        else:
            filters.append(f"publication_year:{year}")
    if min_citations:
        filters.append(f"cited_by_count:>{min_citations - 1}")
    if filters:
        params["filter"] = ",".join(filters)
    email = os.environ.get("OPENALEX_EMAIL")
    if email:
        params["mailto"] = email
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = fetch_json(url)
    records = []
    for item in data.get("results", []):
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        ids = item.get("ids") or {}
        records.append(
            {
                "source": "openalex",
                "id": item.get("id"),
                "title": item.get("title") or item.get("display_name"),
                "year": item.get("publication_year"),
                "authors": [
                    a.get("author", {}).get("display_name")
                    for a in item.get("authorships", [])
                    if a.get("author", {}).get("display_name")
                ],
                "venue": source.get("display_name"),
                "doi": ids.get("doi", "").replace("https://doi.org/", "") or None,
                "url": ids.get("doi") or item.get("id"),
                "citations": item.get("cited_by_count"),
                "abstract": inverted_index_to_text(item.get("abstract_inverted_index")),
                "oa_pdf": primary.get("landing_page_url") if primary.get("is_oa") else None,
            }
        )
    return records


def crossref_search(query: str, limit: int, year: str | None) -> list[dict[str, Any]]:
    params = {"query.bibliographic": query, "rows": str(limit), "sort": "is-referenced-by-count", "order": "desc"}
    if year:
        if "-" in year:
            start, end = year.split("-", 1)
            params["filter"] = f"from-pub-date:{start},until-pub-date:{end}"
        else:
            params["filter"] = f"from-pub-date:{year},until-pub-date:{year}"
    mailto = os.environ.get("CROSSREF_MAILTO") or os.environ.get("OPENALEX_EMAIL")
    if mailto:
        params["mailto"] = mailto
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = fetch_json(url)
    records = []
    for item in data.get("message", {}).get("items", []):
        title = " ".join(item.get("title") or [])
        authors = []
        for author in item.get("author", []):
            name = " ".join(part for part in [author.get("given"), author.get("family")] if part)
            if name:
                authors.append(name)
        year_value = None
        for key in ("published-print", "published-online", "created", "issued"):
            parts = item.get(key, {}).get("date-parts")
            if parts and parts[0]:
                year_value = parts[0][0]
                break
        records.append(
            {
                "source": "crossref",
                "id": item.get("DOI"),
                "title": title,
                "year": year_value,
                "authors": authors,
                "venue": " ".join(item.get("container-title") or []),
                "doi": item.get("DOI"),
                "url": item.get("URL"),
                "citations": item.get("is-referenced-by-count"),
                "abstract": re.sub("<[^>]+>", "", item.get("abstract") or ""),
                "oa_pdf": None,
            }
        )
    return records


def bibtex_key(record: dict[str, Any]) -> str:
    first_author = record.get("authors", ["source"])[0] if record.get("authors") else "source"
    family = re.sub(r"[^A-Za-z0-9]", "", first_author.split()[-1]).lower() or "source"
    year = str(record.get("year") or "nd")
    title_word = ""
    for word in re.findall(r"[A-Za-z0-9]+", record.get("title") or ""):
        if len(word) > 3:
            title_word = word.lower()
            break
    return f"{family}{year}{title_word}"[:48]


def to_bibtex(records: list[dict[str, Any]]) -> str:
    entries = []
    for record in records:
        key = bibtex_key(record)
        authors = " and ".join(record.get("authors") or [])
        lines = [
            f"@article{{{key},",
            f"  title = {{{record.get('title') or ''}}},",
            f"  author = {{{authors}}},",
        ]
        if record.get("venue"):
            lines.append(f"  journal = {{{record['venue']}}},")
        if record.get("year"):
            lines.append(f"  year = {{{record['year']}}},")
        if record.get("doi"):
            lines.append(f"  doi = {{{record['doi']}}},")
        if record.get("url"):
            lines.append(f"  url = {{{record['url']}}},")
        lines.append("}")
        entries.append("\n".join(lines))
    return "\n\n".join(entries)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--source", choices=["openalex", "crossref", "both"], default="openalex")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--year", help="YYYY or YYYY-YYYY")
    parser.add_argument("--min-citations", type=int, default=0)
    parser.add_argument("--format", choices=["json", "bibtex"], default="json")
    parser.add_argument("--output")
    args = parser.parse_args()

    records: list[dict[str, Any]] = []
    if args.source in {"openalex", "both"}:
        records.extend(openalex_search(args.query, args.limit, args.year, args.min_citations))
    if args.source in {"crossref", "both"}:
        if records:
            time.sleep(0.25)
        records.extend(crossref_search(args.query, args.limit, args.year))

    seen = set()
    deduped = []
    for record in records:
        key = (record.get("doi") or record.get("title") or "").lower()
        if not key or key in seen:
            continue
        seen.add(key)
        deduped.append(record)

    output = to_bibtex(deduped) if args.format == "bibtex" else json.dumps(deduped, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(output + "\n")
    else:
        sys.stdout.write(output + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
