---
tags: [entity, tool, wiki, rag, open-source, python]
sources:
  - raw/sources/2026-05-06-discuss-pytorchkr-openkb-llm-10058.md
  - raw/sources/2026-06-17-github-vectifyai-openkb-readme.md
url: https://github.com/VectifyAI/OpenKB
author: VectifyAI
license: Apache-2.0
---

# OpenKB

**[[VectifyAI]]**의 오픈소스 **CLI + Python API** — 문서를 LLM이 **위키 foundation**으로 컴파일하고, **generator**로 query·chat·Skill을 만든다. Karpathy [[LLM Wiki]] 패턴의 **공식 구현체** (~2.1k★, Python, Apache 2.0).

## 2계층

| 계층 | 역할 |
|------|------|
| **Wiki foundation** | compile·유지 — summaries, concepts, **entities**, index, log |
| **Generators** | wiki→답변·대화·**Anthropic Skill** |

## 파이프라인

| 입력 | 처리 |
|------|------|
| 짧은 문서 | markitdown → LLM **전문** |
| URL | PDF→PageIndex/markitdown; HTML→trafilatura→.md |
| 긴 PDF (≥20p) | **PageIndex** 트리 → LLM 트리 읽기 |
| 공통 | LLM 위키 컴파일 → `wiki/` |

## wiki/ 디렉터리

`index.md` · `log.md` · `AGENTS.md` · `sources/` · `summaries/` · **`concepts/`** · **`entities/`** · `explorations/` · `reports/`

- **entities/** — person·organization·place·product·work·event 등
- 문서 1건 → 보통 **10~15 페이지** 갱신

## CLI — Wiki foundation

| 명령 | 역할 |
|------|------|
| `openkb init` | KB 초기화 |
| `openkb add` | 파일·디렉터리·**URL** 추가+compile |
| `openkb remove` | 문서·wiki·PageIndex 상태 제거 |
| `openkb recompile` | compile 재실행 (수동 편집 덮어씀) |
| `openkb watch` | `raw/` 감시 |
| `openkb lint` | 구조+지식 건강 검사 |
| `openkb list` · `status` | 목록·통계 |

## CLI — Generators

| 명령 | 역할 |
|------|------|
| `openkb query` | 인용 grounded 답변 (`--save`) |
| `openkb chat` | 멀티턴; `/add` `/skill new` `/lint` 등 |
| `openkb skill new` | wiki→`output/skills/` Anthropic Skill |
| `openkb skill validate/eval/history/rollback` | Skill 품질·반복 |

## 스택·설정

- **LiteLLM** · **markitdown** · **PageIndex** · OpenAI Agents SDK · Click · watchdog
- `.openkb/config.yaml`: model, language, pageindex_threshold, entity_types, extra_headers
- `.env`: `LLM_API_KEY`, optional `PAGEINDEX_API_KEY`

## 에이전트·Obsidian

- Obsidian: `wiki/` 볼트, `[[wikilinks]]`, Web Clipper→`raw/`
- Claude Code plugin · Gemini skills · Codex symlink — **read-only** skill
- Skill Factory 출력은 Cursor 등에 `npx skills add`로 공유 가능

## 비교

- **vs 벡터 RAG**: 대체가 아닌 **공존** ([[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]])
- **vs [[obsidian-second-brain]]**: compile+append vs **self-rewriting**
- **vs 이 Vault**: 동일 [[LLM Wiki]] 철학; OpenKB는 markitdown·PageIndex·Skill Factory 내장
- **CJK**: 형태소 검색 약점 — seCall 등 한국어 대안 ([[PyTorchKR]] 댓글)

## 관련

- [[VectifyAI]] · [[LLM Wiki]] · [[obsidian-second-brain]] · [[PyTorchKR]]
- [[출처/OpenKB GitHub README VectifyAI]] · [[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]]

## 링크

- https://github.com/VectifyAI/OpenKB
- `pip install openkb`
