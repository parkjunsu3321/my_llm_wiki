---
tags: [entity, tool, sdd, github]
sources:
  - wiki/출처/스펙 주도 개발 SDD GeekNews.md
url: https://github.com/github/spec-kit
---

# Spec-kit

GitHub의 **[[스펙 주도 개발]]** CLI — 다양한 코딩 어시스턴트용 작업 공간·슬래시 커맨드 생성. 세 도구 중 **가장 커스터마이즈 가능**.

## 워크플로

**Constitution → Specify → Plan → Tasks** (반복 가능)

| 단계 | 역할 |
|------|------|
| **Constitution** | 모든 변경에 적용되는 **불변** 고수준 원칙 (강력한 규칙 파일) |
| Specify | 기능 명세화 |
| Plan | 계획·연구 |
| Tasks | 작업 분해 |

산출물: bash 스크립트·템플릿·체크리스트. 명세당 **다수 MD** (spec, plan, tasks, data-model, research, api…).

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

## 실무 보고 (GeekNews)

- 10일 SpecKit+Claude Code: 테스트·빌드 실패 다수
- **subagent + sprint 단위** 반복이 신뢰도 개선
- TDD-first 단계에서 Claude 취약성 언급

## 관련

- [[스펙 주도 개발]] · [[출처/스펙 주도 개발 SDD GeekNews]]
- [[Kiro]] · [[Tessl]]
