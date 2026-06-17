---
tags: [entity, tool, wiki, rag, open-source, python]
sources:
  - raw/sources/2026-05-06-discuss-pytorchkr-openkb-llm-10058.md
url: https://github.com/VectifyAI/OpenKB
author: VectifyAI
---

# OpenKB

**VectifyAI**의 오픈소스 **CLI + Python API** — 다양한 문서를 LLM이 **위키 형태 지식 베이스**로 자동 컴파일. Andrej Karpathy [[LLM Wiki]] 패턴의 **독립 구현체**.

## 핵심 가치

- 전통 RAG: 매 쿼리 **재발견** → OpenKB: **누적·교차 참조** 위키
- 문서 추가 시 summaries + **concepts**(교차 합성) + index/log 갱신
- 출력: 순수 Markdown + `[[wikilinks]]` — **Obsidian** 그래프 뷰

## 파이프라인

| 입력 | 처리 |
|------|------|
| 짧은 문서 | markitdown → LLM **전문** 읽기 |
| 긴 PDF (20p+) | **PageIndex** 계층 트리 → LLM 트리 읽기 |
| 공통 | LLM **위키 컴파일** → `wiki/` |

## CLI

| 명령 | 역할 |
|------|------|
| `openkb init` | KB 초기화 |
| `openkb add` | 문서·디렉터리 추가 |
| `openkb query` | 질의 (`--save` → explorations) |
| `openkb chat` | 멀티턴 (`--resume`) |
| `openkb lint` | 모순·orphan·구식 콘텐츠 |
| `openkb watch` | `raw/` 감시 자동 업데이트 |

## 스택

- **LiteLLM** — OpenAI·Claude·Gemini 등
- **markitdown** — PDF·docx·PPT·HTML·Excel·MD
- **PageIndex** — 장문 PDF 트리 인덱싱
- 설정: `.env` (`LLM_API_KEY`) · `.openkb/config.yaml`

## 디렉터리 (`wiki/`)

`index.md` · `log.md` · `AGENTS.md` · `sources/` · `summaries/` · **`concepts/`** · `explorations/` · `reports/`

## 한계·비교

- **CJK 검색**: 해외 llm wiki 계열 공통 약점 — 형태소·토크나이저 부재 ([[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]] 댓글)
- **vs 벡터 RAG**: 대체가 아닌 **공존** 가능
- **vs [[obsidian-second-brain]]**: Karpathy **append+compile** vs **self-rewriting**
- **vs 이 Vault**: 동일 [[LLM Wiki]] 철학; OpenKB는 markitdown·PageIndex·watch 내장 CLI

## 관련

- [[LLM Wiki]] · [[obsidian-second-brain]] · [[PyTorchKR]]
- [[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]]

## 링크

- https://github.com/VectifyAI/OpenKB
- `pip install openkb`
