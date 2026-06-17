# OpenKB — Open LLM Knowledge Base (GitHub README)

- URL: https://github.com/VectifyAI/OpenKB
- Organization: VectifyAI
- License: Apache 2.0
- Language: Python
- Stars: ~2,079 (2026-06-17)
- Homepage: https://pageindex.ai
- Created: 2026-04-04

---

## What is OpenKB

**OpenKB (Open Knowledge Base)** is an open-source CLI system that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by **PageIndex** for vectorless long document retrieval.

Based on Andrej Karpathy's concept: LLMs generate summaries, concept pages, and cross-references, all maintained automatically. Knowledge compounds over time instead of being re-derived on every query.

### Why not traditional RAG?

Traditional RAG rediscovers knowledge from scratch on every query. Nothing accumulates. OpenKB compiles knowledge once into a persistent wiki, then keeps it current. Cross-references already exist. Contradictions are flagged. Synthesis reflects everything consumed.

Two layers:
- **Wiki foundation** — compile and maintain knowledge
- **Generators** — query / chat / Skill Factory

## Getting Started

```bash
pip install openkb
mkdir my-kb && cd my-kb
openkb init
openkb add paper.pdf
openkb add ~/papers/
openkb add https://arxiv.org/pdf/2509.11420
openkb query "What are the main findings?"
openkb chat
openkb skill new my-expert "Reason like an expert on <topic-from-your-docs>"
```

LLM via LiteLLM (OpenAI, Claude, Gemini). `.env`: `LLM_API_KEY=...`. Config: `.openkb/config.yaml`.

## Architecture

```
raw/
 ├─ Short docs ──→ markitdown ──→ LLM reads full text
 ├─ Long PDFs ──→ PageIndex ────→ LLM reads document trees
 │                                     ▼
 │                         Wiki Compilation (LLM)
 ▼                                     ▼
wiki/                                  ← foundation
 ├── index.md
 ├── log.md
 ├── AGENTS.md
 ├── sources/
 ├── summaries/
 ├── concepts/           ← cross-document synthesis
 ├── entities/           ← people, orgs, places, products
 ├── explorations/
 └── reports/
                ┌──────────┼──────────┐
                ▼          ▼          ▼
            query/chat  Skill Factory  (future)
```

### Short vs Long Documents

| | Short | Long (PDF ≥ 20 pages) |
|---|---|---|
| Convert | markitdown → Markdown | PageIndex → tree + summaries |
| Images | pymupdf inline | PageIndex |
| LLM reads | Full text | Document trees |

### Knowledge Compilation (on add)

1. Summary page
2. Read existing concept + entity pages
3. Create/update concepts (cross-document synthesis)
4. Create/update entity pages
5. Update index + log

Single source may touch 10–15 wiki pages.

## Commands

### Wiki Foundation

| Command | Description |
|---|---|
| `openkb init` | Initialize KB (interactive) |
| `openkb add <file/dir/URL>` | Add + compile. URL: PDF→PageIndex/markitdown; HTML→trafilatura→.md |
| `openkb remove <doc>` | Remove doc + wiki cleanup (`--dry-run`, `--keep-raw`, `--keep-empty`) |
| `openkb recompile [<doc>] [--all]` | Re-run compile on indexed docs; overwrites manual edits |
| `openkb watch` | Watch `raw/` auto-compile |
| `openkb lint` | Structural + knowledge health checks |
| `openkb list` | List indexed docs and concepts |
| `openkb status` | KB stats |
| `openkb feedback ["msg"]` | Prefilled GitHub issue |

### Generators

| Command | Output |
|---|---|
| `openkb query "..."` | Grounded answer + citations (`--save` → explorations) |
| `openkb chat` | Multi-turn session (`--resume`, `--list`, `--delete`) |
| `openkb skill new <name> "<intent>"` | Anthropic Skill at `output/skills/<name>/` + marketplace.json |
| `openkb skill validate [name]` | Structural lint (`--strict`) |
| `openkb skill eval <name>` | Trigger-accuracy eval (`--save`) |
| `openkb skill history/rollback` | Iteration workspace |

### Chat slash commands

`/help`, `/status`, `/list`, `/add`, `/skill new`, `/save`, `/clear`, `/lint`, `/exit`

## Skill Factory

Distills wiki subset into portable Anthropic Skill for Claude Code, Codex CLI, Gemini CLI, Cursor.

Output: `SKILL.md`, `references/`, optional `scripts/`. Auto-updates `.claude-plugin/marketplace.json`.

Install: `cp -r output/skills/<name> ~/.claude/skills/` or `npx skills@latest add <org>/<repo>`.

## Configuration (`.openkb/config.yaml`)

```yaml
model: gpt-5.4
language: en
pageindex_threshold: 20
# entity_types: optional override
# extra_headers: optional HTTP headers for LLM
```

OAuth providers (`chatgpt/*`, `github_copilot/*`) need no API key.

## PageIndex

Vectorless reasoning-based retrieval. Local OSS by default. Optional cloud via `PAGEINDEX_API_KEY` (OCR, faster indexing).

## Obsidian

Open `wiki/` as vault. Graph view, Web Clipper → `raw/`.

## Agent CLI Integration

- Claude Code: `/plugin marketplace add VectifyAI/OpenKB`
- Gemini CLI: `gemini skills install ... --path skills/openkb`
- Codex: symlink `skills/openkb` to `~/.agents/skills/`

Skill is read-only by default.

## vs Karpathy

| | Karpathy | OpenKB |
|---|---|---|
| Short docs | LLM direct | markitdown → LLM |
| Long docs | Context limits | PageIndex tree |
| Formats | Web clipper .md | PDF, Word, PPT, Excel, HTML, text, CSV, .md |
| Wiki compile | LLM agent | LLM agent |
| Q&A | Query over wiki | Wiki + PageIndex retrieval |

## Stack

PageIndex, markitdown, OpenAI Agents SDK, LiteLLM, Click, watchdog

## Roadmap

- Long doc handling for non-PDF
- Nested folder collections
- Hierarchical concept indexing
- Database-backed storage
- Web UI

## Topics (GitHub)

agents, ai, knowledge-base, llm, rag, retrieval
