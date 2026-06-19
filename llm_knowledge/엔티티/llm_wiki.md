---
tags: [entity, app, knowledge-management, open-source]
sources:
  - raw/sources/2026-06-19-discuss-pytorchkr-llm-wiki-karpathy-10139.md
url: https://github.com/nashsu/llm_wiki
license: GPL-3.0
---

# llm_wiki

[nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) — Karpathy [[LLM Wiki]] 패턴의 **크로스플랫폼 데스크톱 앱**. 문서(PDF/DOCX/PPTX/MD)를 **영속 위키**로 컴파일; RAG의 매번-from-scratch 검색 대안.

## 핵심 기능

- **2단계 CoT ingest** — 분석 → 위키 생성·index/log/overview·리뷰·리서치 쿼리
- **4신호 지식 그래프** — wikilink·source overlap·Adamic-Adar·type affinity; Louvain·Graph Insights
- **검색** — BM25/CJK + LanceDB 벡터 + 2-hop 그래프 확장 + 토큰 예산
- **Deep Research** — Tavily; 빈 곳·인사이트 카드에서 트리거
- **Lint · Review · Chat** — 위키 건강·인간 검토·인용 `[n]` 답변
- **`purpose.md`** — 위키 의도에 따른 ingest/query 분기

## 스택

Tauri v2 · Rust · React 19 · sigma.js · LanceDB · shadcn/ui

## 통합

- Obsidian 볼트(동일 폴더)
- Chrome Web Clipper (MV3, port 19827)

## 비교

| | llm_wiki | [[obsidian-second-brain]] | 이 Vault |
|--|----------|---------------------------|----------|
| 형태 | GUI 앱 | CLI 스킬 | Obsidian + Cursor 스킬 |
| 갱신 | append + overview | **rewrite** | append (Karpathy) |
| 그래프 | 내장 | 없음 | Obsidian |

## 관련

- [[출처/LLM Wiki 데스크톱 앱 PyTorchKR]]
- [[LLM Wiki]] · [[PyTorchKR]]
