---
name: llm-wiki-query
description: >-
  Answers questions using the LLM Wiki: reads wiki/index.md, drills into wiki pages,
  cites wiki links and sources. Optionally files valuable answers as new wiki pages.
  Project-local skill for this vault only (.cursor/skills/).
  Use when the user asks questions about wiki content, query, 요약, 비교,
  또는 위키 기반 질문.
disable-model-invocation: false
---

# LLM Wiki — Query

## Preconditions

- Read vault `AGENTS.md` for paths and conventions.

## Steps

1. **Scan `wiki/index.md`** — Locate relevant pages before deep reading.
2. **Read** needed pages under `wiki/` (and cited raw sources only if the wiki is insufficient).
3. **Answer** with citations: wiki links and, where relevant, original source titles/paths under `raw/sources/`.
4. **Preserve value** — For dense comparisons, analyses, or new connections: propose saving as a new `wiki/` page and updating `wiki/index.md`, or do so if the user explicitly asks.
5. **Log if substantial** — After non-trivial synthesis or multi-page reads, append one line to `wiki/log.md`: `## [YYYY-MM-DD] query | <short description>`.

## Done when

- The question is answered with traceability to wiki (and sources if used); log updated when warranted.
