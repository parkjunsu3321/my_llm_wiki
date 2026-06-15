---
tags: [concept, prompt-engineering, claude]
sources:
  - raw/sources/2026-05-30-discuss-pytorchkr-claude-prompt-engineering-10447.md
---

# Claude 프롬프트 엔지니어링

[[Anthropic]]이 Claude 최신 모델군용으로 정리한 **프롬프트·에이전트 설계** 가이드. "마법 주문 찾기"에서 **모델 기본 동작 이해 + 필요한 부분만 명시**로 무게중심이 이동했다.

대상: Opus 4.8/4.7/4.6, Sonnet 4.6, Haiku 4.5.

## 패러다임 전환

| 과거 | 현재 |
|------|------|
| 모호한 프롬프트 → 모델이 의도 추측 | **literal** 지시 따르기 |
| 더 공격적인 프롬프트 | 세대별 default 이해, **과잉 보정 제거** |
| prefill로 형식 강제 | Structured Outputs·시스템 프롬프트 |

Golden rule: *"맥락 없는 동료에게 프롬프트를 보여주고 따라하게 해보라. 헷갈리면 Claude도 헷갈린다."*

## 주제별 요약

### 기초

- 명확·직접 지시 + 수식어 (`Go beyond the basics`)
- 지시 **이유** 설명 → 일반화
- few-shot 3~5개, XML 태그 (`<instructions>`, `<example>`)
- system role, 긴 문서(20k+) 상단 + `<documents>` + 인용 grounding

### Opus 4.8

- [[effort 파라미터]] — 추론 깊이·도구 사용의 1차 레버
- [[adaptive thinking]] — 기본 OFF, 명시 설정
- literalism, 톤·진행 업데이트·서브에이전트 default 변화

### 출력·도구·사고

- 형식: **하지 말 것** < **할 것** 지시
- 도구: `<default_to_action>`, `<use_parallel_tool_calls>`
- 사고: effort + adaptive; "think thoroughly" > 단계별 계획

### 에이전트 시스템

- 장기 호흡, compaction·메모리 인지
- 위험 행동 전 확인
- overengineering 억제, 파일 열기 전 추측 금지
- 프롬프트 체이닝·자기 교정 (필요 시)
- **[[루프 엔지니어링]]** — rubric/Outcomes·memory outer loop ([[Claude Fable 5]] 검증, [[출처/Fable 5 루프 설계 GeekNews]])

### 마이그레이션 (4.6+)

1. adaptive thinking + effort (budget_tokens 대체)
2. prefill 제거
3. anti-laziness·CRITICAL 표현 **덜어내기** → [[overtriggering]] 방지
4. Sonnet 4.6: 기본 effort `high` → workload별 조정

## 관련

- [[출처/Claude 프롬프트 엔지니어링 Anthropic 가이드 PyTorchKR]]
- [[effort 파라미터]]
- [[adaptive thinking]]
- [[overtriggering]]
- [[엔티티/Claude Opus 4.8]]
