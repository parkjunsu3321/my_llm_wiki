---
tags: [concept, claude, reasoning]
sources:
  - raw/sources/2026-05-30-discuss-pytorchkr-claude-prompt-engineering-10447.md
---

# adaptive thinking

Claude Opus 4.6·Sonnet 4.6의 **동적 사고** 모드. [[effort 파라미터]]와 질의 복잡도를 보고 언제·얼마나 추론할지 결정한다.

## 설정

```python
thinking={"type": "adaptive"}
```

- 쉬운 질의 → 바로 응답
- 복잡한 질의 → 깊은 추론
- Anthropic 내부 평가: 확장 사고(budget_tokens)보다 일관되게 우수

## Opus 4.8 주의

- **기본적으로 thinking OFF** — adaptive를 **명시**해야 켜짐
- 과도한 사고 시: *"Thinking adds latency and should only be used when it will meaningfully improve answer quality..."*

## 마이그레이션

`budget_tokens` 기반 extended thinking → `adaptive` + effort로 이전.

## 팁

- "think thoroughly" > 손짜기 단계별 계획
- few-shot에 `` 패턴 포함 → 추론 일반화
- Opus 4.5 (thinking off): "think" 단어가 의도치 않은 사고 유발 → consider/evaluate 대체

## 관련

- [[effort 파라미터]]
- [[Claude 프롬프트 엔지니어링]]
- [[Chain-of-Thought]]
