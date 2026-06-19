---
tags: [ingest, agent, loop, pytorchkr]
date: 2026-06-19
sources:
  - raw/sources/2026-06-19-discuss-pytorchkr-loop-engineering-10796.md
assets:
  - raw/assets/loop_engineering_1.jpg
  - raw/assets/loop_engineering_2.jpg
  - raw/assets/loop_engineering_3.jpg
  - raw/assets/loop_engineering_4.jpg
  - raw/assets/loop_engineering_5.jpg
  - raw/assets/loop_engineering_6.jpg
url: https://discuss.pytorch.kr/t/loop-engineering/10796
author: jacey-dong
published: 2026-06-18
original_url: https://x.com/sairahul1/article/2064277888216555684
note: PyTorchKR 커뮤니티 게시물. GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.
---

# 루프 엔지니어링 학습 자료 (PyTorchKR)

> 출처: [PyTorchKR #10796](https://discuss.pytorch.kr/t/loop-engineering/10796) · jacey-dong · 2026-06-18 · 원문 [Loops: What Every AI Engineer Needs to Know in 2026](https://x.com/sairahul1/article/2064277888216555684) (sairahul1)

## 한 줄 요약

**[[루프 엔지니어링]]** 입문 학습 자료 — Discover→Plan→Execute→Verify→Iterate 5단계, 6가지 구성요소, 단일/플릿·오픈/클로즈드 루프, 4가지 루프 패턴, 토큰 비용·DeepSeek V4. *프롬프트 엔지니어 → 루프 엔지니어* 직무 전환.

## 핵심 내용

### 정의

에이전트가 **사람의 지속 개입 없이** 목표 달성까지 **Discover · Plan · Execute · Verify · Iterate** 피드백 사이클을 돌도록 **시스템을 설계**하는 방법론.

| 인용 | 내용 |
|------|------|
| Peter Steinberger (OpenClaw) | 에이전트에 프롬프트하는 **루프**를 설계 |
| Boris Cherny (Claude Code) | *"제 일은 루프를 작성하는 것"* |

기존: 개발자가 매 턴 프롬프트·검토·수정 → **사람이 루프**.  
전환: 전체 사이클을 시스템이 수행 → 개발자는 **목표 설정·결과 검토**.

### 6가지 구성요소

![루프 6구성요소](../../raw/assets/loop_engineering_1.jpg)

| # | 요소 | 역할 |
|---|------|------|
| 1 | **Automations** | 심장박동 — `/loop`, `/goal`, cron; 조건 충족까지 반복 |
| 2 | **Worktrees** | git worktree로 병렬 Execute 시 파일 충돌 방지 |
| 3 | **Skills** | `SKILL.md` + `VISION.md` / `ARCHITECTURE.md` / `RULES.md` |
| 4 | **Plugins·Connectors** | MCP — PR·Linear·CI·Slack 등 실환경 |
| 5 | **Sub-agents** | maker/checker 분리; Explore·Implement·Verify |
| 6 | **Memory** | markdown·Linear 등 **디스크** 상태 — 실행 간 지속 |

Claude Code·Codex 모두 제공 ([[출처/루프 엔지니어링 Addyo GeekNews]]와 동일 프레임).

### 5단계 사이클

![5단계 사이클](../../raw/assets/loop_engineering_2.jpg)

검증 통과 → 완료. 실패 → 1단계로.  
![프롬프트 vs 루핑](../../raw/assets/loop_engineering_3.jpg)

### 규모·유형

**단일 에이전트 루프** — 한 에이전트가 전체 DPEVI; 집중·단순 목표.

**플릿 루프** — Orchestrator → Specialist → Subagent 트리; Eval Gate로 품질.  
![단일 vs 플릿](../../raw/assets/loop_engineering_4.jpg)

| 유형 | 특성 | 실용성 |
|------|------|--------|
| **Open Loop** | 탐색적·넓은 행동 공간; Steinberger식 | 토큰 폭발 — 예산 무제한 소수 |
| **Closed Loop** | 사람이 E2E 경로·평가 기준·escalation 설계 | **오늘의 실무 선택**; 타이트→점진적 개방 |

![오픈 vs 클로즈드](../../raw/assets/loop_engineering_5.jpg)

### 4가지 루프 패턴 (의사코드)

공통 골격: **Goal → Action → Check → Fix → Repeat until done**

| 패턴 | 흐름 요약 |
|------|-----------|
| **Coding** | VISION+ARCHITECTURE → 계획 → 편집 → 테스트 → 실패 시 수정 루프 → 통과 시 요약 |
| **Research** | 질문 → 출처 검색·요약 → 대조·상충 비교 → 합성 → 신뢰도 임계값 |
| **Content** | 주제 정의 → 초안 → critic → 재작성 → 점수화 → 통과 시 게시 |
| **Sales outreach** | ICP → 리드 → enrich → 적격 판정 → 개인화 → 품질 검토 → 전송/escalation |

### 토큰 비용 (게시물 추정)

| 시나리오 | 토큰 |
|----------|------|
| 단일 에이전트·중간 코딩 | 50k–200k |
| Orchestrator + 전문가 3 | 500k–2M |
| 매일 스케줄 루프 | 주간 수백만 |

표준 API 가격이면 **일주일 진지한 루프 = 월 AI 예산 초과** 가능. 재시도·sub-agent·검증마다 누적.

**DeepSeek V4** 등 저가·장컨텍스트(1M) 모델이 **루프 대규모 실행** 비용 장벽 완화 후보로 언급 (게시물 내 EvoLink 링크 — 스펙은 별도 검증).

### 프롬프트 → 루프 엔지니어

![프롬프트 vs 루프 엔지니어](../../raw/assets/loop_engineering_6.jpg)

- 프롬프트 엔지니어: AI에게 **결과물 요청**
- 루프 엔지니어: **검증된 결과를 생산하는 시스템** 설계
- *하나의 신뢰할 수 있는 루프 > 천 개의 완벽한 프롬프트*

### 한계·경고

동일 루프도 사용자에 따라 **이해 가속** vs **이해 회피(com cognitive surrender)**. 루프는 구분 못 함 → 설계가 프롬프트보다 **더 어렵다**. Cherny: 작업이 쉬워진 게 아니라 **레버리지 포인트 이동**.

## GeekNews 출처와의 관계

| 항목 | Addyo #30336 | 본 PyTorchKR 글 |
|------|--------------|-----------------|
| 5+1 구성 | ✓ | ✓ (6요소 동일) |
| `/goal`·checker | ✓ | ✓ |
| DPEVI 5단계 | 간접 | **명시** |
| Fleet·Open/Closed | — | **추가** |
| 4 패턴 의사코드 | 예시 1 | **4종** |
| Fable 5 벤치 | [[출처/Fable 5 루프 설계 GeekNews]] | — |
| 토큰·DeepSeek | 간략 | **수치·V4** |

## 관련 위키

- [[루프 엔지니어링]] — 통합 개념
- [[출처/루프 엔지니어링 Addyo GeekNews]]
- [[출처/Fable 5 루프 설계 GeekNews]]
- [[Claude 프롬프트 엔지니어링]] · [[Anthropic]]

## 원본

- `raw/sources/2026-06-19-discuss-pytorchkr-loop-engineering-10796.md`
