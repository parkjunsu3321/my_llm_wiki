---
tags: [ingest, agent, geeknews, loop]
date: 2026-06-10
sources:
  - raw/sources/2026-06-10-geeknews-loop-engineering-30336.md
url: https://news.hada.io/topic?id=30336
original_url: https://addyo.substack.com
referrer: pytorchkr
---

# 루프 엔지니어링 — 에이전트를 프롬프트하는 시스템 (GeekNews)

> 출처: [GeekNews #30336](https://news.hada.io/topic?id=30336) · GN+ neo · 2026-06-10 · 원문 [Addy Osmani (Substack)](https://addyo.substack.com) · PyTorchKR 경유

## 한 줄 요약

**[[루프 엔지니어링]]** = 매 턴 직접 프롬프트 대신, 에이전트를 대신 찌르는 **시스템** 설계. Automations·Worktrees·Skills·Connectors·Sub-agents + **Memory** — Claude Code·Codex 모두 탑재. *build the loop, stay the engineer.*

## 핵심 내용

### 개념 진화

프롬프트 → 컨텍스트 → harness → **루프** (harness·factory model **상위**)

| 인용 | 내용 |
|------|------|
| Peter Steinberger | 에이전트에 프롬프트하는 **루프**를 설계 |
| Boris Cherny | *"내 일은 루프를 작성하는 것"* |

### 5+1 구성요소

| 요소 | 역할 | Claude Code / Codex |
|------|------|---------------------|
| Automations | 스케줄·triage | `/loop`, hooks, cron / Automations 탭 |
| Worktrees | 병렬 격리 | `--worktree`, `isolation: worktree` / 내장 |
| Skills | intent 외부화 | `SKILL.md` (동일 포맷) |
| Connectors | MCP 연동 | 이슈·DB·Slack |
| Sub-agents | maker/checker | `.claude/agents/` / `.codex/agents/` |
| Memory | 디스크 상태 | markdown·Linear·state file |

### 핵심 primitive

- **`/loop`** — 주기 재실행
- **`/goal`** — 검증 가능 정지 조건까지 반복; **별도 모델**이 완료 판정 (self-grade 방지)

### 예시 루프

매일 automation → triage skill → worktree별 sub-agent(초안+리뷰) → connector(PR·티켓) → **state file**로 이어하기.

### 사람이 남는 일

- **검증** — verifier sub-agent도 "done"은 주장
- **이해** — comprehension debt
- **판단** — cognitive surrender 방지

직접 프롬프트와 **균형**; 같은 루프도 사람에 따라 치료제/가속제.

## 후속 검증

- [[출처/Fable 5 루프 설계 GeekNews]] — 동일 개념을 [[Claude Fable 5]] + CMA로 벤치 (~6× ML, 73% memory)

## 관련 위키

- [[루프 엔지니어링]] — 통합 개념
- [[Claude 프롬프트 엔지니어링]]
- [[Anthropic]]

## 원본

- `raw/sources/2026-06-10-geeknews-loop-engineering-30336.md`
