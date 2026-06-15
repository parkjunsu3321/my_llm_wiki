---
tags: [concept, llm, reasoning]
sources:
  - raw/sources/2026-06-02-discuss-pytorchkr-adhd-10481.md
---

# Chain-of-Thought (CoT)

LLM이 중간 추론 단계를 순차적으로 생성하는 **사고의 사슬** 방식이다.

## ADHD 맥락에서의 한계

자기회귀 생성으로 **첫 가설이 이후 전체 사슬을 지배**하기 쉽다. "몇 가지 방법 제안" 요청에서도 조기 수렴(premature convergence)이 발생한다.

## 관련

- [[Tree-of-Thought]] — 가지 탐색으로 폭 확장
- [[ADHD 스킬]] — 프레임별 격리 병렬 + 별도 critic
- [[인지 프레임]]
