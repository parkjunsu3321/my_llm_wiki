---
tags: [concept, knowledge-management, obsidian]
sources:
  - raw/sources/2026-06-16-discuss-pytorchkr-obsidian-second-brain-10730.md
  - raw/sources/2026-06-19-discuss-pytorchkr-llm-wiki-karpathy-10139.md
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

# LLM Wiki

**Andrej Karpathy**가 제안한 패턴 — LLM과 **함께** 유지하는 지식 위키. 이 Vault(`AGENTS.md`)가 동일 구조를 따른다.

**구현체:** Karpathy [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · 데스크톱 [[llm_wiki]] · CLI [[obsidian-second-brain]] · Cursor 스킬(이 Vault).

## 세 레이어 (이 Vault)

| 레이어 | 경로 | 규칙 |
|--------|------|------|
| 원본 (immutable) | `raw/sources/` | 사용자 큐레이션; LLM **수정·삭제 금지** |
| 첨부 | `raw/assets/` | 원본 보조; LLM 덮어쓰기 금지 |
| 위키 | `wiki/` | 요약·개념·엔티티·색인; LLM **생성·유지** |

필수: `wiki/index.md`, `wiki/log.md` (append-only).

nashsu [[llm_wiki]]는 여기에 **`purpose.md`·`schema.md`·`overview.md`** 와 `queries/`·`synthesis/` 등을 추가.

## 워크플로 (이 Vault)

| 작업 | 스킬 |
|------|------|
| 원본 → 위키 | `llm-wiki-ingest` |
| 위키 질문 | `llm-wiki-query` |
| 건강 점검 | `llm-wiki-lint` |

[[llm_wiki]] 앱은 동일 역할을 GUI·2단 ingest·내장 그래프·Deep Research로 수행.

## Karpathy vs [[llm_wiki]] vs [[obsidian-second-brain]]

| | LLM Wiki (gist/이 Vault) | [[llm_wiki]] 앱 | [[obsidian-second-brain]] |
|--|--------------------------|-----------------|---------------------------|
| 새 출처 | **append** + wikilink | append + overview | **rewrite** |
| ingest | 1단( gist ) / 스킬 | **2단 CoT** | `/obsidian-ingest` |
| 모순 | 표시 → 사람 | Review + Lint | `/obsidian-reconcile` |
| purpose | (Vault: 사용자 방향) | **`purpose.md`** | 볼트 맥락 |
| UI | 에디터·Obsidian | **데스크톱 앱** | CLI 슬래시 |

두 접근은 **배타적이지 않음** — Karpathy 레이어 + nashsu 앱 ingest + obsidian-second-brain 유지보수를 같은 볼트에 결합 가능.

## 관련

- [[출처/LLM Wiki 데스크톱 앱 PyTorchKR]] · [[출처/obsidian-second-brain Obsidian 세컨드 브레인 PyTorchKR]]
- [[llm_wiki]] · [[obsidian-second-brain]] · [[Eugeniu Ghelbur]] · [[자기 갱신 위키]]
- [[Context Rot]] — 세션 맥락 소멸; 위키·세컨드 브레인이 대응
