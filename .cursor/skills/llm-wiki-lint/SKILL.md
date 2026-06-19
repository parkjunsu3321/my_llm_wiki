---
name: llm-wiki-lint
description: >-
  Health-checks the LLM Wiki: contradictions, stale claims, orphan pages, missing
  concept pages, weak cross-links, optional web-fill gaps. Applies fixes in wiki/
  and summarizes in wiki/log.md.
  Project-local skill for this vault only (.cursor/skills/).
  Use when the user asks for lint, 린트, 점검, 위키 정리, or wiki maintenance.
disable-model-invocation: false
---

# LLM Wiki — Lint

## Preconditions

- Read vault `AGENTS.md` for paths and conventions.
- **Do not** modify `raw/sources/` or `raw/assets/`.

## Checks

1. **Contradictions** — Conflicting claims across `wiki/` pages; reconcile or document uncertainty.
2. **Stale claims** — Older summaries superseded by newer ingests; update or mark dated.
3. **Orphans** — Pages with no inbound `[[links]]` from index or other pages (fix links or merge).
4. **Missing pages** — Important terms used repeatedly without a dedicated page (create stub or full page).
5. **Cross-links** — Obvious missing `[[wikilinks]]` between related notes.
6. **Gaps** — Optional: suggest web searches or new sources; do not fabricate facts.

## Steps

1. Use `wiki/index.md` and grep/link patterns as needed to traverse `wiki/`.
2. Apply edits only under `wiki/` (and keep `index.md` consistent).
3. **Append `wiki/log.md`** — `## [YYYY-MM-DD] lint | <what changed / findings>`.

## Done when

- Report is clear (what was fixed vs suggested); log documents the pass.
