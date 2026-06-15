---
tags: [concept, claude, api]
sources:
  - raw/sources/2026-05-30-discuss-pytorchkr-claude-prompt-engineering-10447.md
---

# effort 파라미터

Claude API의 **지능 ↔ 토큰 소비** 트레이드오프를 조정하는 파라미터. [[Claude Opus 4.8]]에서 특히 중요해졌으며, [[adaptive thinking]]과 함께 사고 깊이를 제어한다.

## 레벨 (Opus 4.8 기준)

| 값 | 용도 |
|----|------|
| `max` | 최고 지능. diminishing returns·overthinking 주의 |
| `xhigh` | **코딩·에이전트** 작업 기본 추천 |
| `high` | 균형. 지능 중요 작업의 최소 기준선 |
| `medium` | 비용 민감 |
| `low` | 짧고 범위 명확, 지연 민감 |

## 동작 특성

- Opus 4.8은 **낮은 effort를 엄격히 준수** — low/medium은 요청 범위만, "기대 이상" 안 함
- 추론이 얕으면 프롬프트 튜닝보다 **effort 올리기**가 정석
- 도구 호출을 늘리고 싶을 때도 high/xhigh가 레버

## API 예시

```python
output_config={"effort": "high"}  # max, xhigh, medium, low
thinking={"type": "adaptive"}
```

## Sonnet 4.6

기본 effort `high` (Sonnet 4.5와 다름). 대부분 `medium`, 대용량·지연 민감은 `low` 검토.

## 관련

- [[adaptive thinking]]
- [[Claude 프롬프트 엔지니어링]]
- [[엔티티/Claude Opus 4.8]]
