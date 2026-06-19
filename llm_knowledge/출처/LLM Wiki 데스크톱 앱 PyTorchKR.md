---
tags: [ingest, knowledge-management, obsidian, rag, pytorchkr]
date: 2026-06-19
sources:
  - raw/sources/2026-06-19-discuss-pytorchkr-llm-wiki-karpathy-10139.md
assets:
  - raw/assets/llm_wiki_karpathy_1.png
  - raw/assets/llm_wiki_karpathy_2.jpeg
  - raw/assets/llm_wiki_karpathy_3.jpeg
  - raw/assets/llm_wiki_karpathy_4.jpeg
  - raw/assets/llm_wiki_karpathy_5.jpeg
  - raw/assets/llm_wiki_karpathy_6.jpeg
  - raw/assets/llm_wiki_karpathy_7.jpeg
  - raw/assets/llm_wiki_karpathy_8.jpeg
  - raw/assets/llm_wiki_karpathy_9.jpeg
  - raw/assets/llm_wiki_karpathy_10.png
  - raw/assets/llm_wiki_karpathy_11.png
  - raw/assets/llm_wiki_karpathy_12.png
url: https://discuss.pytorch.kr/t/llm-wiki-feat-karpathy-llm-wiki/10139
author: 9bow(박정환)
published: 2026-06-17
repo_url: https://github.com/nashsu/llm_wiki
note: PyTorchKR 커뮤니티 게시물. GPT 정리본; 원문·GPL 라이선스 확인 권장.
---

# LLM Wiki 데스크톱 앱 (PyTorchKR)

> 출처: [PyTorchKR #10139](https://discuss.pytorch.kr/t/llm-wiki-feat-karpathy-llm-wiki/10139) · 9bow · 2026-06-17 · [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) · Karpathy [llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## 한 줄 요약

[[llm_wiki]] — Andrej Karpathy [[LLM Wiki]] 패턴을 **Tauri 데스크톱 앱**으로 구현. RAG 대신 **영속 위키** + **2단계 CoT ingest** + **4신호 지식 그래프** + Obsidian·Chrome Clipper 통합. GPL-3.0.

![LLM Wiki 앱 개요](../../raw/assets/llm_wiki_karpathy_1.png)

## RAG vs 위키 컴파일

| | RAG | LLM Wiki |
|--|-----|----------|
| 질의마다 | 원본 청크 재검색·재추론 | **이미 컴파일된 위키** 조회 |
| 관계·모순·공백 | 청크 단위라 파악 어려움 | `[[wikilinks]]`·그래프·Lint로 드러남 |
| 비용 | 반복 토큰 | ingest 시 1회 + 점진 갱신 |

Karpathy gist는 **패턴**; nashsu 프로젝트는 **설치형 제품**(위키·그래프·검색·Lint·Review·Deep Research).

## 3계층 + purpose·schema

Karpathy **Raw / Wiki / Schema**에 더해:

- **`purpose.md`** — 위키 존재 이유·핵심 질문·가설; ingest·query마다 LLM이 읽어 **같은 PDF도 목적에 따라 다르게** 분류
- **`schema.md`** — 페이지 타입·구조 규칙

![3계층 아키텍처](../../raw/assets/llm_wiki_karpathy_3.jpeg)

디렉터리(`wiki/entities`, `concepts`, `sources`, `queries`, `synthesis`, `comparisons`, `overview.md` 등)는 Git·Obsidian 볼트로 **그대로** 공유 가능.

## 2단계 인제스트

Karpathy 원안(단일 호출) → **Analysis + Generation** 분리:

1. **Step 1** — 엔티티·개념·주장·기존 위키 연결·모순·구조 추천
2. **Step 2** — 출처·엔티티·개념 페이지, `index.md`/`log.md`/`overview.md`, 리뷰 항목, Deep Research 쿼리

부가: SHA256 **증분 캐시**, 디스크 **인제스트 큐**, 실패 **3회 재시도**, 폴더 경로 분류 힌트.

## 4신호 관련도 · 그래프

| 신호 | 가중치 |
|------|--------|
| Direct `[[wikilink]]` | ×3.0 |
| Source overlap (`sources[]`) | ×4.0 |
| Adamic-Adar | ×1.5 |
| Type affinity | ×1.0 |

sigma.js + Louvain **커뮤니티**(응집도 &lt;0.15 경고). **Graph Insights**: Surprising Connections, 고립 페이지, Sparse communities, Bridge nodes → Deep Research 트리거.

![지식 그래프](../../raw/assets/llm_wiki_karpathy_4.jpeg)

## 검색 · Deep Research

파이프라인: (1) 토큰/BM25 + CJK bigram → (1.5) LanceDB **벡터** (recall 58.2→71.4%) → (2) 그래프 2-hop 확장 → (3) 토큰 예산(위키 60%·채팅 20%·인덱스 5%·시스템 15%) → (4) `[1]` 인용 조립.

**Deep Research**: Tavily 웹 검색 → 새 위키 페이지 → 2단계 ingest 재진입. `purpose.md`·`overview.md` 기반 도메인 맞춤 쿼리.

![Deep Research](../../raw/assets/llm_wiki_karpathy_8.jpeg)

## 스택 · 통합

- **Tauri v2 + Rust**, React 19, LanceDB(embedded), OpenAI/Anthropic/Google/Ollama/Custom
- **Obsidian** — 동일 디렉터리·`.obsidian/` 자동 생성
- **Chrome Web Clipper** — Readability + Turndown, localhost:19827, 다중 위키 프로젝트

![Obsidian 호환](../../raw/assets/llm_wiki_karpathy_9.jpeg)

## 이 Vault와의 관계

| | nashsu [[llm_wiki]] | 이 Obsidian Vault |
|--|---------------------|-------------------|
| 레이어 | raw/wiki/schema + purpose | `raw/sources/` + `wiki/` + `AGENTS.md` |
| ingest | 앱 내 2단 CoT | Cursor `llm-wiki-ingest` 스킬 |
| query/lint | 앱 Chat·Lint | `llm-wiki-query` / `llm-wiki-lint` |
| 그래프 | 내장 sigma.js | Obsidian graph + wikilink |
| 갱신 | append + overview | append (Karpathy); [[obsidian-second-brain]]은 rewrite |

**상호 보완** — nashsu 앱은 GUI·그래프·Deep Research; 이 Vault는 에이전트 스킬·GitHub sync(`my_llm_wiki`).

## 설치·라이선스

- Releases: macOS `.dmg`, Windows `.msi`, Linux `.deb`/`.AppImage`
- 빌드: Node 20+, Rust 1.70+, `npm run tauri build`
- **GPL-3.0** — 파생물도 GPL

## 관련 위키

- [[LLM Wiki]] · [[llm_wiki]] · [[obsidian-second-brain]] · [[자기 갱신 위키]]
- [[PyTorchKR]]

## 원본

- `raw/sources/2026-06-19-discuss-pytorchkr-llm-wiki-karpathy-10139.md`
