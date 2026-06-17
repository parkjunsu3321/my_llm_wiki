---
tags: [concept, knowledge-management, obsidian]
sources:
  - raw/sources/2026-06-16-discuss-pytorchkr-obsidian-second-brain-10730.md
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
---

# LLM Wiki

**Andrej Karpathy**가 제안한 패턴 — LLM과 **함께** 유지하는 지식 위키. 이 Vault(`AGENTS.md`)가 동일 구조를 따른다.

## 세 레이어 (이 Vault)

| 레이어 | 경로 | 규칙 |
|--------|------|------|
| 원본 (immutable) | `raw/sources/` | 사용자 큐레이션; LLM **수정·삭제 금지** |
| 첨부 | `raw/assets/` | 원본 보조; LLM 덮어쓰기 금지 |
| 위키 | `wiki/` | 요약·개념·엔티티·색인; LLM **생성·유지** |

필수: `wiki/index.md`, `wiki/log.md` (append-only).

## 워크플로 (이 Vault)

| 작업 | 스킬 |
|------|------|
| 원본 → 위키 | `llm-wiki-ingest` |
| 위키 질문 | `llm-wiki-query` |
| 건강 점검 | `llm-wiki-lint` |

## Karpathy vs [[obsidian-second-brain]]

| | LLM Wiki | obsidian-second-brain |
|--|----------|------------------------|
| 새 출처 | **append** + wikilink | **rewrite** 기존 페이지 |
| 모순 | 표시 → 사람 해결 | `/obsidian-reconcile` |
| 패턴 | query 시 | `/obsidian-synthesize` |
| 트리거 | 사용자 ingest/query | + **예약 에이전트** |
| 노트 | 사람 읽기 | **AI-first** (`For future Claude`) |

두 접근은 **배타적이지 않음** — Karpathy 레이어 구조 + obsidian-second-brain 유지보수 명령을 같은 볼트에 결합 가능.

## 관련

- [[obsidian-second-brain]] · [[Eugeniu Ghelbur]]
- [[출처/obsidian-second-brain Obsidian 세컨드 브레인 PyTorchKR]]
- [[Context Rot]] — 세션 맥락 소멸; 위키·세컨드 브레인이 대응
