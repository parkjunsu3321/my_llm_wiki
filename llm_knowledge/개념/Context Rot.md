---
tags: [concept, agent, context]
sources:
  - wiki/출처/스펙 주도 개발 SDD tsyang Context Engineering.md
  - wiki/출처/iFKakao Agentic Coding 카카오페이 Spec-kit.md
---

# Context Rot

**Context Rot (맥락 부식)** — [[바이브 코딩]]·저구조 [[에이전틱 코딩]]에서 **작업을 바꿀 때마다 이전 맥락이 사라져** 프로젝트 일관성이 무너지는 현상.

## 증상

- AI가 **기존 코드와 다른 패턴**으로 생성
- **이전 결정과 모순**되는 구현
- 같은 수정을 **반복 요청**
- 수동 **컨텍스트 노동** (맥락을 매번 다시 입력)

## 전형적 패턴 (tsyang)

데미지 시스템 → 적 AI → UI를 **별도 프롬프트**로 지시하면, 각 단계는 그럴듯하나 **데미지 로직이 서로 다름** — 마치 팀원 간 소통 없이 짠 코드 조각 모음.

## 완화

| 접근 | 메커니즘 |
|------|----------|
| **[[스펙 주도 개발]]** | 모든 작업이 **동일 spec·constitution** 참조 |
| **[[Spec-kit]]** | constitution → specify → plan → tasks 파이프라인 |
| **[[루프 엔지니어링]]** | memory·루프로 맥락 지속 |
| 정적 가이드 | 부분 완화 (`AGENTS.md` 등); 기능 단위 한계 |

## 관련

- [[바이브 코딩]] · [[컨텍스트 엔지니어링]] · [[스펙 주도 개발]]
