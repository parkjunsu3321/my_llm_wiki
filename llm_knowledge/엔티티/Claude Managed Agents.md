---
tags: [entity, product, anthropic, agent]
sources:
  - raw/sources/2026-06-11-geeknews-fable5-loop-engineering-30390.md
---

# Claude Managed Agents (CMA)

[[Anthropic]]의 **에이전트 harness + 호스팅 sandbox** 제품. 장시간 자율 작업(특히 [[Claude Fable 5]])에 맞춘 실행 환경.

## 주요 primitive

| 기능 | 설명 |
|------|------|
| **Outcomes** | goal/rubric 기반 **self-correction loop**. grader sub-agent 자동 생성, 기준 충족 시에만 작업 종료 |
| **Sandbox** | self-hosted GPU 등 (Parameter Golf: 8×H100) |
| **Memory** | 세션 간 공유 **mounted filesystem** — [[루프 엔지니어링]]의 outer loop |

Claude Code의 `/goal`과 유사한 “루프 레시피”를 특정 작업에 적용하는 층.

## Parameter Golf 사용 예 ([[출처/Fable 5 루프 설계 GeekNews]])

- 9개 체크 가능 rubric (baseline, 실험 20회 등), 최대 8시간
- Outcomes grader가 **독립 context**에서 판정 → self-critique보다 신뢰
- Fable 5 vs Opus 4.7 비교 벤치 플랫폼

## 관련

- [[루프 엔지니어링]]
- [[Claude Fable 5]]
- [[Anthropic]]
- [[출처/Fable 5 루프 설계 GeekNews]]
