---
tags: [entity, model, claude]
sources:
  - raw/sources/2026-05-30-discuss-pytorchkr-claude-prompt-engineering-10447.md
---

# Claude Opus 4.8

[[Anthropic]] 최상위 Claude 모델. 장기 호흡 에이전트, 지식 노동, 비전, 메모리에 강점. 모델 문자열: `claude-opus-4-8`.

## 프롬프팅 특성 (vs 이전 Opus)

| 항목 | 특성 |
|------|------|
| [[effort 파라미터]] | 가장 중요한 레버 |
| thinking | **기본 OFF**, adaptive 명시 필요 |
| 지시 | **literal** — 범위 명시 없으면 일반화 안 함 |
| 도구 | 추론 선호 > 도구 (high/xhigh로 보완) |
| 톤 | 직접적·의견 분명, 이모지 절제 |
| 서브에이전트 | 기본적으로 더 적게 생성 |
| 코딩 | 인터랙티브(다중 턴)에서 토큰↑ |

4.7 프롬프트는 대체로 그대로 동작하나, **default 변화** 미이해 시 어긋남.

## 관련

- [[Claude 프롬프트 엔지니어링]]
- [[adaptive thinking]]
- [[overtriggering]]
- [[출처/Claude 프롬프트 엔지니어링 Anthropic 가이드 PyTorchKR]]
