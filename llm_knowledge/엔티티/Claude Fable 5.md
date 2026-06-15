---
tags: [entity, model, anthropic]
sources:
  - raw/sources/2026-06-11-geeknews-fable5-loop-engineering-30390.md
---

# Claude Fable 5

[[Anthropic]]의 **Mythos-class** 모델. 내부 작업 방식을 바꾼 것으로 소개되며, **장시간·자율적** 에이전트 과제에 맞춘다.

## 이 Vault에서의 특징 (GeekNews 검증, 2026-06-11)

직접 프롬프팅·미세 조종보다 **[[루프 엔지니어링]]**과 궁합이 좋다.

| 과제 | vs Opus 4.7 | 관찰 |
|------|-------------|------|
| Parameter Golf (ML) | **~6×** 학습 파이프라인 개선 | 구조적 변경·회복력; quantization regression 극복 |
| Continual Learning Bench (memory) | 검증 커버리지 **73%** vs median **~17%** | fail→distill 파이프라인 완주 경향 |

[[Claude Managed Agents]] harness + Outcomes rubric + memory filesystem과 함께 평가됨.

## 관련

- [[루프 엔지니어링]]
- [[Claude Managed Agents]]
- [[Claude Opus 4.8]] — Vault 내 다른 Claude 최상위 계열 (4.8은 프롬프트 가이드 중심)
- [[출처/Fable 5 루프 설계 GeekNews]]
- [[Anthropic]]
