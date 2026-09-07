# Evidence-Led Paragraph and Sentence Revision

Use this reference when revising the user's manuscript with reference papers.

## Integrity Gate

Before revising, classify each reference-paper use:

| Use | Allowed? | Notes |
|---|---|---|
| Structure pattern | yes | Example: problem -> method family -> gap -> contribution |
| Rhetorical move | yes | Example: narrowing claim scope after negative results |
| Technical evidence | yes, if verified | Cite only when it supports the user's claim |
| Short quote for analysis | limited | Keep brief; do not paste into final manuscript |
| Continuous wording reuse | no | Do not patchwrite or paraphrase sentence-by-sentence |
| Imported results/data | no by default | Only if independently relevant and cited |

If the user asks for plagiarism, patchwriting or "降重" of someone else's prose, refuse that operation and offer this workflow instead.

## Paragraph Pass

For every target paragraph, create or update a row in `plan/revision-ledger.md`:

```markdown
### <Section ID>.P<paragraph number>

- Location:
- Paragraph role:
- Current main claim:
- Evidence IDs:
- Reference style move:
- Problems:
- Revision strategy:
- Post-revision logic:
- LaTeX risk:
```

Paragraph roles:

- `context`
- `problem`
- `method-landscape`
- `limitation`
- `gap`
- `method-definition`
- `method-rationale`
- `data-description`
- `experiment-design`
- `result-observation`
- `result-interpretation`
- `discussion-boundary`
- `conclusion`
- `transition`

## Sentence Pass

For each sentence that needs attention, add:

```markdown
| Sentence ID | Original function | Issue | Evidence IDs | Source pattern, not wording | Revised sentence | Logic check | Risk |
|---|---|---|---|---|---|---|---|
```

Issue values:

- `unsupported-claim`
- `overclaim`
- `weak-transition`
- `scope-drift`
- `method-ambiguity`
- `result-logic`
- `citation-needed`
- `citation-mismatch`
- `style-only`
- `keep`

Rules:

- Do not rewrite accurate sentences just to increase edit count.
- Do not use synonyms as the main method. Change the sentence because the claim, logic, evidence or fit needs it.
- Preserve the user's research subject, data, methods, metrics and limitations.
- When evidence is missing, write `Needs evidence` instead of inventing support.
- When a claim is stronger than the evidence, narrow it with conditions such as `in the tested cases`, `within the validated horizon`, or `the results suggest`.

## Reference Style Map

Store reusable patterns in `plan/reference-style-map.md`:

```markdown
## Pattern <ID>: <short name>

- Source papers:
- Section type:
- Writing move:
- Why it works:
- Safe adaptation rule:
- Forbidden reuse:
```

Example safe adaptation:

```markdown
- Writing move: Introduce the operational problem before listing model families.
- Safe adaptation rule: Use the user's own field problem and cite sources that support that field problem.
- Forbidden reuse: Do not reuse the source paper's exact wording, data, or method sequence.
```

## Applying Edits

When writing back to `.tex`:

1. Read the surrounding section, not just the target sentence.
2. Preserve all LaTeX commands and labels unless the task requires changing them.
3. Keep citation commands compatible with the template.
4. Make the smallest coherent patch.
5. Re-read the changed section to ensure the new sentence fits the previous and next paragraphs.

## Section-Level Logic Review

After a section pass, write `plan/review/logic-review.md`:

```markdown
## <Section>
- Claim chain:
- Evidence chain:
- Transitions:
- Unsupported or weakened claims:
- Contradictions:
- Boundary language:
- Verdict:
```

Verdict values:

- `pass`
- `pass-with-risks`
- `revise`
- `blocked-needs-evidence`
