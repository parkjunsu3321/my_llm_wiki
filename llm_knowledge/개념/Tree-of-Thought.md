---
tags: [concept, llm, reasoning]
sources:
  - raw/sources/2026-06-02-discuss-pytorchkr-adhd-10481.md
---

# Tree-of-Thought (ToT)

하나의 문제에 대해 **여러 추론 가지를 트리 형태로 탐색**하는 방식이다. CoT보다 탐색 폭이 넓다.

## ADHD 맥락에서의 한계

가지는 늘리지만 **하나의 공유 맥락** 위에서 분기하므로, 초기 고착이 가지들 사이에 그대로 번질 수 있다.

## ADHD와의 차이

| | ToT | ADHD |
|---|-----|------|
| 맥락 | 공유 트리 | 프레임별 **완전 격리** |
| 비평 | 트리 내 pruning | **별도 critic LLM 호출** |

## 관련

- [[Chain-of-Thought]]
- [[ADHD 스킬]]
- [[인지 프레임]]
