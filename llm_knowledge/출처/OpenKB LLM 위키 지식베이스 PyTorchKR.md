---
tags: [ingest, openkb, wiki, rag, pytorchkr]
date: 2026-06-17
sources:
  - raw/sources/2026-05-06-discuss-pytorchkr-openkb-llm-10058.md
url: https://discuss.pytorch.kr/t/openkb-llm/10058
author: 9bow(박정환)
published: 2026-05-06
note: PyTorchKR 커뮤니티 게시물. GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.
---

# OpenKB: LLM 위키 지식베이스 자동 컴파일 (PyTorchKR)

> 출처: [PyTorchKR #10058](https://discuss.pytorch.kr/t/openkb-llm/10058) · 9bow · 2026-05-06 · 원저 [[OpenKB]] · [GitHub](https://github.com/VectifyAI/OpenKB)

## 한 줄 요약

**[[OpenKB]]** — Andrej Karpathy [[LLM Wiki]] 아이디어를 구현한 **오픈소스 CLI**. PDF·Word·MD 등 문서를 LLM이 **요약·개념·교차 링크 위키**로 컴파일. 전통 RAG의 매 쿼리 재발견 대신 **누적형 지식 그래프**; LiteLLM·Obsidian `[[wikilinks]]`·PageIndex(장문 PDF) 지원.

## 핵심 문제: RAG vs 위키 컴파일

| | 전통 RAG | [[LLM Wiki]] / OpenKB |
|--|----------|------------------------|
| 지식 축적 | 매 쿼리마다 **재발견** | 한 번 컴파일 → **재사용** |
| 교차 참조 | 수동·부재 | 문서 간 **자동 wikilink** |
| 모순 | 미탐지 | `openkb lint`로 **건강 검사** |
| 구조 | 청크·벡터 DB | **개념 페이지** 중심 위키 |

Karpathy 논지: LLM이 문서를 그때그때 검색하는 것보다 **지식을 위키로 지속 컴파일·갱신**하는 방식이 더 강력하다.

## 아키텍처

```
raw/ → (짧은 문서: markitdown → LLM 전문)
     → (긴 PDF 20p+: PageIndex 트리 → LLM 트리 읽기)
     → 위키 컴파일 (LLM)
wiki/  index · log · AGENTS.md · sources · summaries · concepts · explorations · reports
```

- 문서 1건 추가 시 보통 **10~15개 위키 페이지** 갱신
- **concepts/** — 여러 문서를 아우르는 교차 합성 (핵심)
- 장문 PDF: PageIndex **계층 요약 트리**로 컨텍스트 창 제한 우회

## 주요 기능

| 기능 | 명령·역할 |
|------|-----------|
| 문서 추가 | `openkb add` — PDF·docx·MD·PPT·HTML·Excel·txt |
| 질의 | `openkb query` · `--save`로 explorations 저장 |
| 대화 | `openkb chat` · `--resume` 세션 재개 |
| 건강 검사 | `openkb lint` — 모순·공백·orphan·구식 콘텐츠 |
| 감시 | `openkb watch` — `raw/` 자동 ingest |
| LLM | LiteLLM — OpenAI·Claude·Gemini 등 |
| 출력 | 순수 MD + `[[wikilinks]]` — Obsidian 호환 |

## 설치·사용

```bash
pip install openkb
mkdir my-kb && cd my-kb && openkb init
openkb add paper.pdf
# .env: LLM_API_KEY=...  /  .openkb/config.yaml 모델 지정
openkb query "주요 발견은?"
openkb lint && openkb watch
```

Python API: `KnowledgeBase("./my-kb").add()` · `.query()` · `.chat()`.

## 이 Vault·유사 도구와의 관계

| 도구 | 포지션 |
|------|--------|
| **이 Vault** | Karpathy [[LLM Wiki]] 패턴 — Cursor ingest/query/lint 스킬 |
| **[[OpenKB]]** | 동일 철학의 **독립 CLI** + markitdown·PageIndex·watch |
| **[[obsidian-second-brain]]** | Karpathy 위 **self-rewriting** 계층 (재작성·reconcile) |
| **seCall** | 한국어 llm wiki; 커뮤니티에서 CJK 검색 강점 ([[PyTorchKR]] 댓글) |

OpenKB는 벡터 DB RAG를 **완전 대체**하기보다 **공존·보완** 가능 (커뮤니티 의견).

## 커뮤니티 댓글

- **CJK 한계**: 해외 llm wiki 구현체는 형태소·토크나이저 부재로 CJK 검색이 약함 — OpenKB도 해당 이슈 가능
- **한국어 대안**: [seCall](https://github.com/hang-in/seCall) (Rust, 대화→로컬 위키)
- **logicutils**와의 연동은 미검증 (댓글)

## 관련 (글 내 더 읽어보기)

Graphify · Cognee · RAG Web UI · WeKnora · ApeRAG · Advanced RAG Cookbooks · legalize-kr · Karpathy LLM 영상

## 관련 위키

- [[OpenKB]] · [[VectifyAI]] · [[LLM Wiki]] · [[자기 갱신 위키]] · [[obsidian-second-brain]] · [[PyTorchKR]]
- [[출처/OpenKB GitHub README VectifyAI]] — 공식 README (entities·Skill Factory)

## 원본·리소스

- `raw/sources/2026-05-06-discuss-pytorchkr-openkb-llm-10058.md`
- PyTorchKR: https://discuss.pytorch.kr/t/openkb-llm/10058
- GitHub: https://github.com/VectifyAI/OpenKB
