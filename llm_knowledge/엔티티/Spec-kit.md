---
tags: [entity, tool, sdd, github]
sources:
  - raw/sources/2025-10-20-geeknews-sdd-tools-23776.md
  - raw/sources/2026-06-15-kakaopay-ifkakao-agentic-coding-spec-kit.md
  - raw/sources/2026-06-15-tsyang-sdd-context-engineering-224.md
url: https://github.com/github/spec-kit
---

# Spec-kit

GitHub의 **[[스펙 주도 개발]]** CLI — 다양한 코딩 어시스턴트용 작업 공간·슬래시 커맨드 생성. 세 도구 중 **가장 커스터마이즈 가능**.

## 설치·초기화

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init <PROJECT_NAME>   # 신규
specify init --here           # 기존 프로젝트 (브라운필드)
```

초기화 후 코딩 에이전트(Cursor 등) 선택 → Constitution·Specify 메뉴.

## 워크플로

**Constitution → Specify ↔ Clarify → Plan → Tasks → Analyze → Implement** (반복 가능)

| 단계 | 슬래시 커맨드 | 역할 |
|------|---------------|------|
| **Constitution** | (초기) | **불변** 고수준 원칙 → `constitution.md` |
| Specify | `/speckit.specify` | 기능 명세 — **what·why** (how는 Plan) ([[tsyang]]) |
| Clarify | (선택) | `[NEEDS CLARIFICATION]` 태그로 추측 방지 ([[tsyang]]) |
| Plan | `/speckit.plan` | constitution+spec → 계획; **게이트** (헌법 위반·과복잡 차단) |
| Tasks | `/speckit.tasks` | → `tasks.md`; `[P]` 병렬 작업 표시 ([[tsyang]]) |
| Analyze | `/speckit.analyze` | spec/plan/task **모순 분석** (implement 전) |
| Implement | `/speckit.implement` | tasks 중심 코드 생성·MCP 호출 |

**원칙**: plan/task/data-model 불만 → **직접 수정 금지**, `/speckit.specify`로 스펙 재정의 ([[출처/iFKakao Agentic Coding 카카오페이 Spec-kit]]). 실무 예외: tasks에 MCP URL 등 누락 — 스펙 일치 확인 후 프롬프트 보완.

산출물: bash 스크립트·템플릿·체크리스트. 명세당 **다수 MD** (spec, plan, tasks, data-model, research, api…).

### MCP 연동

Specify·Implement 단계에서 **Figma MCP**, 위키 MCP 등 사전 연결 → 디자인·기획 링크를 스펙에 반영 ([[카카오페이 AI 플랫폼]] 실전).

## SDD 수준

공식 narrative는 **spec-anchored** 지향처럼 보이나, **브랜치별 명세** 생성 → 실질 **spec-first**에 가깝다는 비판 (명세 = 변경 요청 수명).

## 특징

- 작업 공간에 산출물 직접 배치 → 수정·확장 용이
- "역할은 방향만이 아니라 **각 단계 검증·반영**" (GitHub 블로그)
- 브라운필드 도입 부담 큼

## 한계

- 작은 변경에도 MD·단계 **과다**
- 에이전트가 연구·헌법·기존 코드 맥락 **무시** 사례
- 튜토리얼 대부분 투두리스트 수준; 레거시 사례 부족

## 실무 보고

**GeekNews / Fowler** ([[출처/스펙 주도 개발 SDD GeekNews]])

- 10일 SpecKit+Claude Code: 테스트·빌드 실패 다수
- **subagent + sprint 단위** 반복이 신뢰도 개선
- TDD-first 단계에서 Claude 취약성 언급

**카카오페이 AI Platform** ([[출처/iFKakao Agentic Coding 카카오페이 Spec-kit]])

- [[에이전틱 코딩]] 후반 **검토·환각** → Spec-kit으로 **팀 일관성** 개선
- Implement는 **tasks 우선** — constitution 위반 시 tasks·spec 재점검
- 장점: 기획 Clarify, 보안·테스트 constitution 추적; 단점: 단계·토큰·소규모 수정 애매

**tsyang (Context Engineering)** ([[출처/스펙 주도 개발 SDD tsyang Context Engineering]])

- 6단계 + **Plan 게이트**, Clarify **`[NEEDS CLARIFICATION]`**, Task **`[P]`**
- [[컨텍스트 엔지니어링]]·[[Context Rot]] 관점 정리

## 관련

- [[스펙 주도 개발]] · [[컨텍스트 엔지니어링]] · [[에이전틱 코딩]] · [[카카오페이 AI 플랫폼]] · [[tsyang]]
- [[출처/스펙 주도 개발 SDD GeekNews]] · [[출처/iFKakao Agentic Coding 카카오페이 Spec-kit]] · [[출처/스펙 주도 개발 SDD tsyang Context Engineering]]
- [[Kiro]] · [[Tessl]]
