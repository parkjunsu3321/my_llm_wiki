---
tags: [concept, knowledge-management, obsidian]
sources:
  - raw/sources/2026-06-16-discuss-pytorchkr-obsidian-second-brain-10730.md
  - raw/sources/2026-05-06-discuss-pytorchkr-openkb-llm-10058.md
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

## RAG vs 위키 컴파일

Karpathy 논지: LLM이 문서를 **그때그때 검색(RAG)** 하는 것보다 지식을 **위키로 지속 컴파일**하는 방식이 더 강력하다.

| | 전통 RAG | LLM Wiki |
|--|----------|----------|
| 지식 | 매 쿼리 **재발견** | **누적**·재사용 |
| 교차 참조 | 수동·부재 | **wikilink** 자동 |
| 모순 | 미탐지 | **lint**·사람/에이전트 해결 |
| 구조 | 청크·벡터 | **개념 페이지** 그래프 |

벡터 RAG와 **완전 대체 관계는 아님** — 공존·보완 가능 ([[OpenKB]]·[[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]]).

## 구현체

| 구현 | 특징 |
|------|------|
| **이 Vault** | Cursor `llm-wiki-ingest/query/lint` 스킬 |
| **[[OpenKB]]** | CLI; markitdown·PageIndex·watch; LiteLLM |
| **[[obsidian-second-brain]]** | Karpathy + **self-rewriting**·예약 에이전트 |
| **seCall** | Rust; 대화→로컬 위키; CJK 강점 (커뮤니티) |

## 관련

- [[OpenKB]] · [[obsidian-second-brain]] · [[Eugeniu Ghelbur]]
- [[출처/obsidian-second-brain Obsidian 세컨드 브레인 PyTorchKR]] · [[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]]
- [[Context Rot]] — 세션 맥락 소멸; 위키·세컨드 브레인이 대응
