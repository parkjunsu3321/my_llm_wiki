---
tags: [ingest, obsidian, second-brain, agent-skill, pytorchkr]
date: 2026-06-17
sources:
  - raw/sources/2026-06-16-discuss-pytorchkr-obsidian-second-brain-10730.md
assets:
  - raw/assets/obsidian-second-brain_1.png
  - raw/assets/obsidian-second-brain_2.png
url: https://discuss.pytorch.kr/t/obsidian-second-brain-obsidian-vault-ai/10730
author: 9bow(박정환)
published: 2026-06-16
note: PyTorchKR 커뮤니티 게시물. GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.
---

# obsidian-second-brain: Obsidian Vault AI 세컨드 브레인 (PyTorchKR)

> 출처: [PyTorchKR #10730](https://discuss.pytorch.kr/t/obsidian-second-brain-obsidian-vault-ai/10730) · 9bow · 2026-06-16 · 원저 [[Eugeniu Ghelbur]] · [GitHub](https://github.com/eugeniughelbur/obsidian-second-brain)

## 한 줄 요약

[[obsidian-second-brain]] — Obsidian 볼트를 **스스로 갱신되는 AI-first 세컨드 브레인**으로 만드는 크로스 CLI 스킬. Andrej Karpathy [[LLM Wiki]] 패턴 위에 **자동 유지보수·재작성** 계층 추가. Claude Code·Codex·Gemini·OpenCode, 40+ 슬래시 명령, 4개 예약 에이전트.

## 핵심 문제

- Claude 세션은 매번 리셋 — 맥락 재설명, 대화 소멸
- Obsidian 노트는 쌓이기만 함 — 6개월 전 결정 망각·중복 판단
- **append-only** 지식 베이스는 규모가 커지면 오래된·모순된 사실이 뒤섞임

## Karpathy LLM Wiki vs obsidian-second-brain

| | [[LLM Wiki]] (Karpathy) | [[obsidian-second-brain]] |
|--|-------------------------|---------------------------|
| 새 출처 | 새 페이지 덧붙이기 + 상호 참조 | **기존 페이지 재작성** (인물·주장·사실 갱신) |
| 모순 | 표시 → 사용자 해결 | `/obsidian-reconcile` **자동 조정** |
| 패턴 | 질문할 때만 | `/obsidian-synthesize` **종합 페이지** 자동 생성 |
| 실행 | 요청 시 | **4개 예약 에이전트** (야간·주간·모순·볼트 상태) |
| 형식 | 사람 읽기 위키 | **AI-first**: `## For future Claude` + LLM 검색용 frontmatter |

한 문장: Karpathy 위키 = LLM과 **함께** 관리하는 KB · obsidian-second-brain = **스스로** 관리하는 KB.

## 주요 슬래시 명령

| 명령 | 역할 |
|------|------|
| `/obsidian-save` | 회의 후 결정·인물·작업·아이디어 → 적절한 노트 저장 |
| `/obsidian-ingest` | 음성(Whisper)·화이트보드·유튜브·웹·X → 볼트 흡수; **기존 페이지 갱신** |
| `/obsidian-challenge` | 큰 결정 전 — 과거 실패·번복 결정을 찾아 반박 |
| `/obsidian-reconcile` | 모순 자동 해결 |
| `/obsidian-synthesize` | 출처 가로지르는 패턴 → 종합 페이지 |
| `/obsidian-daily` | 캘린더·밀린 작업·야간 변경 → 오늘 노트 |
| `/research-deep` | Perplexity·Grok — **열린 웹** 리서치 |
| `/notebooklm` | Gemini File Search — **자신의 볼트** 리서치 |
| `/obsidian-architect` | (v0.10) 코드베이스 스캔 → 아키텍처 노트 (The Architect) |

**리서치**: 중요 주제는 `/research-deep` + `/notebooklm` **병행** — 두 트랙 간 모순이 통찰 지점.

## 예약 에이전트 (4종)

야간: 하루 마감 · 모순 조정 · 패턴 종합 · 고아 노트 연결 · 인덱스 재생성.

## v0.10 "The Architect"

- `/obsidian-architect` — 유지보수되는 아키텍처 노트
- 키 없는 웹 리서치 · Google Calendar · 환각 방지 가드 · 테스트·CI

## 배포

- **MIT** · `npx skills add eugeniughelbur/obsidian-second-brain` (패턴상)
- GitHub: https://github.com/eugeniughelbur/obsidian-second-brain
- 블로그: Eugeniu Ghelbur — The AI Operator (Substack)

## 이 Vault와의 관계

이 Obsidian Vault는 Karpathy [[LLM Wiki]] 패턴(`raw/sources/` + `wiki/` + ingest/query/lint 스킬)을 따른다. GUI 구현은 [[llm_wiki]]; [[obsidian-second-brain]]은 동일 볼트에 **재작성·reconcile·synthesize·스케줄 에이전트**를 더하는 **상위/대안 스킬**로 볼 수 있음.

## 관련 (글 내 더 읽어보기)

- claude-obsidian — Claude Code + Obsidian 자동 정리 위키
- Obsidian Skills — 로컬 KB ↔ AI 에이전트
- OpenKB — LLM이 문서→위키 컴파일
- Open Knowledge Format(OKF) — Google AI 에이전트 지식 공유 표준

## 관련 위키

- [[obsidian-second-brain]] · [[Eugeniu Ghelbur]] · [[LLM Wiki]] · [[PyTorchKR]]
- [[루프 엔지니어링]] — 예약 에이전트·자동화 (대비: 지식 볼트 유지보수)

## 도표 (원본 첨부)

![Karpathy LLM Wiki vs obsidian-second-brain 비교](../../raw/assets/obsidian-second-brain_1.png)

![append-only vs self-rewriting 요약](../../raw/assets/obsidian-second-brain_2.png)

## 원본·리소스

- `raw/sources/2026-06-16-discuss-pytorchkr-obsidian-second-brain-10730.md`
- PyTorchKR: https://discuss.pytorch.kr/t/obsidian-second-brain-obsidian-vault-ai/10730
- GitHub: https://github.com/eugeniughelbur/obsidian-second-brain
- 첨부: `raw/assets/obsidian-second-brain_1.png`, `obsidian-second-brain_2.png`
