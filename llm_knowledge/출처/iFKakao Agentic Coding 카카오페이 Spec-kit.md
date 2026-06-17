---
tags: [ingest, agent, sdd, kakaopay]
date: 2026-06-15
sources:
  - raw/sources/2026-06-15-kakaopay-ifkakao-agentic-coding-spec-kit.md
url: https://tech.kakaopay.com/post/ifkakao-agentic-coding/
author: wayne (카카오페이 AI 플랫폼팀)
event: if(kakao)25
---

# SDD (Spec-kit) 에이전트 코딩 실전기 — 카카오페이

> 출처: [카카오페이 기술 블로그](https://tech.kakaopay.com/post/ifkakao-agentic-coding/) · wayne · AI 플랫폼팀 · if(kakao)25 연계

## 한 줄 요약

[[카카오페이 AI 플랫폼]]팀이 [[에이전틱 코딩]]으로 AI Platform을 구축했으나 후반 **무분별한 코드 생성·환각·검토 시간 증가**로 [[Spec-kit]] 기반 [[스펙 주도 개발]]을 도입. Constitution → Specify ↔ Clarify → Plan → Tasks → Analyze → Implement 파이프라인, Figma·위키 MCP 연동, **스펙 불일치 시 직접 수정 대신 specify 재정의** 원칙.

## 핵심 내용

### 배경: 에이전틱 코딩의 한계

- AI Platform(모델 배포·사용) 구축에 [[에이전틱 코딩]] 적극 활용 → 초·중·후기 단계별 협업 전략으로 개발 기간 단축
- 엔터프라이즈 환경: 후반으로 갈수록 **막 생성되는 코드** 억제용 프롬프트 부담
- **AI 생성 코드 검토·수정 시간**이 직접 코딩보다 길어짐
- 업계 공통: 스펙 정의 후 단계별 수행 방식으로 전환 → Spec-kit 도입

### Spec-kit vs 기존 에이전틱 코딩

| | 기존 | Spec-kit |
|--|------|----------|
| 입력 | 개발자 프롬프트 | **스펙 정의** |
| 중간 | — | Spec-kit이 AI 프롬프트 자동 생성 |
| 역할 | 지시·코드 생성 | **스펙 정의·검증**, AI는 구현 |

### 전체 파이프라인

```
constitution → specify ↔ clarify → plan → tasks → analyze → implement
```

| 단계 | 슬래시 커맨드 | 역할 |
|------|---------------|------|
| Constitution | (초기) | 시스템 **최상위 규칙** — 코드 스타일, 테스트, 문서화 |
| Specify | `/speckit.specify` | 이번 개발 **구체 스펙** (요구사항 많이, 정리는 도구) |
| Clarify | (선택) | 스펙 모호성 제거, 기획 누락 발견 (최대 5질문) |
| Plan | `/speckit.plan` | constitution+spec 기반 **개발 계획** |
| Tasks | `/speckit.tasks` | spec+plan → **구체 작업** (tasks.md) |
| Analyze | `/speckit.analyze` | constitution 기준 spec/plan/task **모순 분석** |
| Implement | `/speckit.implement` | tasks 중심 **코드 생성** (MCP 호출 포함) |

**SDD 원칙**: 마음에 안 드는 plan/task/data-model은 **직접 수정하지 말고** `/speckit.specify`로 스펙 재정의 → AI가 일관되게 수정. (실무 예외: tasks에 MCP 주소 누락 등 — 스펙과 일치 확인 후 프롬프트 보완)

### 설정

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init <PROJECT_NAME>      # 신규
specify init --here              # 기존 프로젝트
```

에이전트 선택 후 Constitution·Specify 등 메뉴 사용.

### MCP·협업 팁

- Specify 단계: **Figma MCP**, **위키 MCP** 등 클립 아이콘으로 미리 연결
- 피그마 디자인 링크 누락 → specify 보완 요청 예시
- Implement 시 tasks에 정의된 MCP까지 **자동 호출** 관찰
- constitution vs tasks: implement는 **tasks에 더 집중** — constitution 위반 시 tasks 재점검

### 장단점 (저자 경험)

**장점**

- 팀 **일관성·체계적 협업** (엔터프라이즈 핵심)
- 기획자와 Clarify/스펙 문서 공동 검토
- constitution에 보안·테스팅 명시 → tasks 반영 여부 추적
- [[바이브 코딩]] 대비: 긴 대화·맥락 상실·스타일 불일치 완화

**단점**

- 단계 많음 → 초심자 진입 장벽
- **간단한 수정**은 specify vs agent 모드 판단 애매
- 파이프라인마다 **MD·토큰** 대량 (문서화 장점이기도)

### 개발자 역할 변화

> 코드 작성자 → **스펙 검증·테스트 설계자**

## 리뷰어 코멘트

- **will.109**: Spec-kit 상호작용·산출물이 다른 도구에도 귀감
- **geuru.geon**: 계획 시간 > 코딩 시간; Spec-kit + Figma MCP로 컨텍스트 발산 방지

## 관련 위키

- [[스펙 주도 개발]] · [[Spec-kit]] · [[에이전틱 코딩]]
- [[카카오페이 AI 플랫폼]]
- [[출처/스펙 주도 개발 SDD GeekNews]] — Fowler 도구 비교·한계
- [[Claude 프롬프트 엔지니어링]] · [[루프 엔지니어링]]

## 참고 (원문)

- `raw/sources/2026-06-15-kakaopay-ifkakao-agentic-coding-spec-kit.md`
- [카카오페이 기술 블로그](https://tech.kakaopay.com/post/ifkakao-agentic-coding/)
