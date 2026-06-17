---
tags: [ingest, geeknews, agent, token, context]
date: 2026-06-17
sources:
  - raw/sources/2026-06-17-geeknews-token-router-30547.md
url: https://news.hada.io/topic?id=30547
original_url: https://github.com/sleeplesshan/token-router
author: sleeplesshan
published: 2026-06-17
note: GeekNews Show GN. 벤치·모델 권장은 저자·댓글 기준; 실환경 검증 권장.
---

# token-router: 하이브리드 컨텍스트 라우터 (GeekNews)

> 출처: [GeekNews #30547](https://news.hada.io/topic?id=30547) · sleeplesshan · 2026-06-17 · [[token-router]] (MIT)

## 한 줄 요약

**[[token-router]]** — Ollama **Gemma 4 2B**로 대용량 로그·코드·에이전트 지침에서 **관련 라인 좌표**만 로컬 탐색 → **원문 slice**(요약 없음) → Codex·Claude Code 등 **클라우드 추론**. [[하이브리드 컨텍스트 라우팅]]; 저자 벤치 **~99% 입력 토큰 절감**.

## 핵심 내용

### 문제

- 2,000줄+ 로그·대형 소스를 클라우드에 통째로 넣으면 **입력 토큰·지연** 폭증
- 소형 모델 **요약**은 에러 한 줄·변수 정의 누락 시 클라우드 AI **맥락 상실**
- 매 턴 주입되는 긴 `CLAUDE.md`·`AGENTS.md`·`.cursorrules`도 비용·노이즈 — 단, **이미 주입된 root 지침**은 사후 절감 불가 → root는 짧게, 긴 규칙은 reference 파일로 분리 후 라우팅 권장

### 해결 (3단계)

| 단계 | 역할 |
|------|------|
| **Local Triage** | Ollama Gemma 4 2B — 질문에 맞는 **라인 번호(좌표)** 탐색 |
| **Raw Slicing** | Python — 디스크에서 **원문 그대로** 해당 구간 추출 (요약 금지) |
| **Cloud Reasoning** | Codex·Claude Code — 고밀도 slice + 파일 구조 지도만으로 디버깅·코딩 |

### 모드

- `error_log` — 대용량 로그
- `heavy_code` — 레거시·대형 소스
- `agent_context` — `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `agent-context/*.md` 등에서 **현재 작업 관련 라인**만

### 저자 벤치 (본인 PC)

| 케이스 | 결과 |
|--------|------|
| 인프라 로그 2,000줄 | 41,711 → **131** 토큰 (**99.69%**, 5.37s) |
| 레거시 버그 코드 2,155줄 | 7,520 → **70** 토큰 (**99.06%**, 4.46s) |

### 실무 기능

- triage 후 **VRAM 즉시 해제** (PC 버벅임 완화)
- slice가 좁으면 클라우드가 **역요청**으로 범위 확장 (프롬프트 안전장치)
- 대용량 파일 **스트리밍** (키워드·파일 끝 스캔)
- Claude Code용 compact `CLAUDE.md` bootstrap 포함

### 댓글 (hshim)

- Gemma 2B가 JSON 좌표 출력 시 **문법 오류** 간헐 → `qwen2.5-coder:7b`·Gemma 4B로 **오류율 감소**
- `OLLAMA_MODEL=qwen2.5-coder:7b python3 scripts/router.py ...`

## 관련 위키

- [[token-router]] · [[하이브리드 컨텍스트 라우팅]] · [[컨텍스트 엔지니어링]]
- [[에이전틱 코딩]] · [[Claude 프롬프트 엔지니어링]]

## 원본·리소스

- `raw/sources/2026-06-17-geeknews-token-router-30547.md`
- GeekNews: https://news.hada.io/topic?id=30547
- GitHub: https://github.com/sleeplesshan/token-router
