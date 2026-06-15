---
tags: [ingest, agent, sdd, context]
date: 2026-06-15
url: https://tsyang.tistory.com/224
author: tsyang
blog: 게임 클라 개발
---

# 스펙 주도 개발 (SDD) — Context Engineering 관점 (tsyang)

> 출처: [tsyang 티스토리](https://tsyang.tistory.com/224) · 게임 클라 개발 · AI코딩 카테고리

## 한 줄 요약

[[컨텍스트 엔지니어링]] 관점에서 **[[스펙 주도 개발]]** = 스펙이 곧 AI에 줄 **구조화된 맥락**; [[바이브 코딩]]의 **[[Context Rot]]** 방지. `CLAUDE.md`/`AGENTS.md`는 정적 가이드, SDD 스펙은 기능 단위 설계·게이트·검증 포함. **SDD 방법론은 유행이 지나도 Spec 산출물은 남을 것** (TDD↔Test 비유).

## 핵심 내용

### Context Engineering

- AI 코딩에서 **맥락(Context) 품질**이 결과를 좌우
- [[Claude 프롬프트 엔지니어링]] = **어떻게 말하느냐**; 컨텍스트 엔지니어링 = **무엇을 알려주느냐**
- 예: "적 AI 만들어줘" vs NavMesh·FSM·OverlapSphere·서버 판정 등 **프로젝트 제약** 전달

### 맥락의 역사 (3단계)

| 방식 | 맥락 위치 | 한계 |
|------|-----------|------|
| **전통 개발** | 사람 머릿속·구두 | 문서 노후, 버스 팩터, 온보딩 지연 (사람은 암묵 추론 가능) |
| **[[바이브 코딩]]** | 최소화·즉석 프롬프트 | 소규모 강점; 확대 시 패턴 불일치·결정 모순·**[[Context Rot]]** |
| **SDD** | **스펙 = 맥락** | 작업 전환해도 동일 스펙 참조 → 일관성 |

### Context Rot

- 작업마다 AI는 그 작업만 잘함; **전환 시 이전 맥락 증발**
- 예: 데미지 시스템 → 적 AI → UI — 각각 다른 데미지 로직
- "컨텍스트 노동": 수동으로 맥락 반복 입력
- → [[스펙 주도 개발]]이 정면 대응

### 방법론 비교 (무엇을 먼저?)

| | 1차 산출물 | → | 결과 |
|--|------------|---|------|
| Traditional | Code | → | Docs (나중·없음) |
| TDD | Test | → | Code |
| **SDD** | **Spec** | → | Code |

코드는 스펙의 **표현(expression)**.

### CLAUDE.md / AGENTS.md vs SDD 스펙

| | 정적 가이드 (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`) | SDD 스펙 |
|--|--------------------------------------------------------|----------|
| 역할 | 팀 위키급 배경·컨벤션 | **기능 단위** 요구·제약·체크리스트 |
| 단계 | 없음 — "알아서 해줘" | 명세→명확화→계획→구현 |
| 검증 | 위반해도 넘어감 | Plan **게이트**, Clarify 태그 |

→ [[개념/스펙 주도 개발#spec vs 전역 컨텍스트]] 메모리 뱅크와 기능 명세 구분과 정합

### Spec-kit 6단계 (tsyang 정리)

1. **Constitution** — 프로젝트 불변 원칙 (예: 테스트 선행, 구조 제한)
2. **Specify** — **what·why** (how는 Plan까지 미룸)
3. **Clarify** — 애매함에 `[NEEDS CLARIFICATION]` 강제 (추측 방지)
4. **Plan** — how; 헌법 위반·과복잡·테스트 없음 → **게이트**
5. **Task** — 실행 단위; `[P]` 병렬 가능 표시
6. **Implement** — 헌법+명세+제약+계획+작업 목록 위에서 코드

※ 카카오페이 실전에는 **Analyze** 단계 추가 ([[출처/iFKakao Agentic Coding 카카오페이 Spec-kit]])

### SDD vs Spec (방법론 vs 산출물)

- SDD **방법론** 전체를 모든 팀이 따를 가능성 낮음
- **TDD : Test :: SDD : Spec** — 방법론은 선택, **Spec은 표준화**될 가능성
- 핵심: *"AI에게 코드를 잘 짜게 하려면, 코드가 아니라 **스펙**을 잘 짜야 한다."*

## 관련 위키

- [[컨텍스트 엔지니어링]] · [[Context Rot]] · [[스펙 주도 개발]] · [[바이브 코딩]]
- [[Spec-kit]] · [[Claude 프롬프트 엔지니어링]]
- [[출처/스펙 주도 개발 SDD GeekNews]] · [[출처/iFKakao Agentic Coding 카카오페이 Spec-kit]]

## 원본·참고

- 글: https://tsyang.tistory.com/224
- GitHub spec-kit (글 내 링크)
- SDD 소개 영상 (글 내 링크)
