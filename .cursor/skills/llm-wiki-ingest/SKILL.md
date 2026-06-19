---
name: llm-wiki-ingest
description: >-
  Integrates new sources from raw/sources into the Obsidian LLM Wiki under wiki/.
  Updates entity/concept pages, cross-links, wiki/index.md and wiki/log.md.
  Syncs wiki/ to GitHub (llm_knowledge/) after ingest.
  Project-local skill for this vault only (.cursor/skills/).
  Use when the user asks to ingest, import, process sources, 반영, 인제스트,
  원본 반영, or adds files under raw/sources/.
disable-model-invocation: false
---

# LLM Wiki — Ingest

## Preconditions

- Read vault `AGENTS.md` for paths and immutable rules.
- **Never edit or delete** existing files under `raw/sources/` or `raw/assets/`.
- **Creating new** files under `raw/sources/` and `raw/assets/` is required for ingest (see below).
- Read `.cursor/skills/llm-wiki-ingest/config.json` for GitHub sync settings.

## Three-layer rule (mandatory)

Every ingest must populate **all applicable layers** before wiki work is considered done:

| Layer | Path | Ingest duty |
|-------|------|-------------|
| 원본 | `raw/sources/` | **Create** one immutable snapshot per source (URL fetch or user file). |
| 첨부 | `raw/assets/` | **Download/save** figures, charts, screenshots referenced in the source. Do not overwrite existing files. |
| 위키 | `wiki/` | Summaries, concepts, entities — always **`sources:` → `raw/sources/...`**. |

**Forbidden shortcut:** fetching a URL and writing only `wiki/` without `raw/sources/` (and assets when images exist).

## Steps

### 1. Acquire or identify sources

- **User placed file** in `raw/sources/` → ingest that file.
- **URL-only request** (no raw file yet) → **first** snapshot the content into `raw/sources/`:
  - Filename: `YYYY-MM-DD-<origin>-<slug>-<id>.md` (match existing vault style).
  - YAML frontmatter: `title`, `source_url`, `author`, `published`, `fetched`, optional `assets`, `note`.
  - Body: **plain markdown/text only** — Discourse `raw`, GeekNews `.md`, blog HTML→text. **Never store raw HTML** (`<!DOCTYPE`, `<html>`, etc.) in `raw/sources/`.
  - For HTML pages: extract article text (`html-to-text.py`, WebFetch, or readability) before writing. Prefer native markdown endpoints (e.g. `news.hada.io/topic/N.md`, Discourse `.json` → `raw` field).
  - Helper scripts (optional): `backfill-raw-sources.py`, `fix-html-raw-sources.py`, `save-discourse-source.py`, `fetch-discourse-images.py`.
- If a snapshot already exists for the same URL, **do not rewrite it** — ingest from the existing file.

### 2. Assets (when the source has figures)

- List images from the source (Discourse JSON, page HTML, etc.).
- Save content figures to `raw/assets/<slug>_N.png` (skip emoji/icons/OG cards).
- Use `curl.exe -L` on Windows if `curl` alias fails.
- Record paths in raw frontmatter `assets:` and wiki frontmatter `assets:`.

### 3. Read source + assets

- Read each `raw/sources/` file; use `raw/assets/` when images clarify content (text first, then images if needed).

### 4. Integrate into `wiki/`

- Create or update summary pages under `wiki/출처/`.
- **Every** `wiki/출처/` page **must** include:

```yaml
sources:
  - raw/sources/<same-file>.md
assets:   # omit if none
  - raw/assets/...
```

- Embed figures in `wiki/출처/` when assets exist: `![caption](../../raw/assets/file.png)` (from `wiki/출처/`).
- Update or create entity/concept pages; **`sources:` should list `raw/sources/`**, not only `wiki/출처/`.
- Add `[[wikilinks]]`; surface contradictions if any.

### 5. Update `wiki/index.md`

- Add/update entries by category.

### 6. Append `wiki/log.md`

- One block per source or batch, e.g. `## [YYYY-MM-DD] ingest | <title>`.
- For backfills: `## [YYYY-MM-DD] ingest-fix | raw/sources backfill — …`.

### 7. Push to GitHub

- Sync `wiki/` → `llm_knowledge/` (skip only if user says not to push).

## GitHub sync (post-ingest)

Settings live in `.cursor/skills/llm-wiki-ingest/config.json`:

| Key | Default |
|-----|---------|
| `remoteUrl` | `https://github.com/parkjunsu3321/my_llm_wiki.git` |
| `localRepoPath` | `C:\Users\user\Documents\my_llm_wiki` |
| `destFolder` | `llm_knowledge` |
| `branch` | `main` |
| `wikiSource` | `wiki` |

Run from vault root (PowerShell):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".cursor/skills/llm-wiki-ingest/sync-push.ps1" -CommitMessage "ingest | <title or batch summary>"
```

## Done when (checklist)

- [ ] `raw/sources/` snapshot exists for each ingested source (body is text/markdown, not HTML dump).
- [ ] `raw/assets/` contains files when the source had content images; wiki embeds or lists them (no phantom paths).
- [ ] `wiki/출처/` has `sources:` → `raw/sources/...` and an **원본** section with the raw path.
- [ ] Entity/concept pages cite `raw/sources/` in frontmatter where applicable.
- [ ] `wiki/index.md` and `wiki/log.md` updated.
- [ ] `wiki/` synced to GitHub (or push failure reported).

## Lint cross-check

If user reports missing raw/assets, run `llm-wiki-lint` or compare: every `wiki/출처/` ingest page ↔ file in `raw/sources/`.
