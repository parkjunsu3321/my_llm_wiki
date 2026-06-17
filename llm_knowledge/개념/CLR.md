---
tags: [concept, inference, test-time-scaling, reasoning]
sources:
  - wiki/출처/VibeThinker-3B 소형 추론 모델 PyTorchKR.md
---

# CLR

**Claim-Level Reliability Assessment (CLR)** — [[VibeThinker-3B]]의 **추론 시점 확장(test-time scaling)** 기법. 궤적 전체가 아니라 **핵심 주장(claim)** 만 검증해 Pass@1을 끌어올린다.

## 절차

1. 문제당 **K=32** 후보 궤적 생성 (표준 샘플링)
2. 각 궤적에서 최종 답 + **M=5** 핵심 claim 추출
3. 모델 **self-verifier**가 claim 반증/검증 → \(v_{k,m}\in\{0,1\}\)
4. 신뢰도 \(r_k = (\frac{1}{M}\sum_m v_{k,m})^M\) — 지수 M으로 단일 실패 시 급격히 감점
5. 동치 답 군집 → **신뢰도 가중 합** 최대 답 선택

## 특징

- **파라미터 갱신 없음** — inference-only
- 장황한 전체 궤적 대신 핵심 논리만 → **토큰 효율** + 정확도 향상
- AIME26 94.3 → **97.1**, BruMO25 93.8 → **99.2** (저자 보고)

## 관련

- [[VibeThinker-3B]] · [[추론-지식 분리]]
- [[출처/VibeThinker-3B 소형 추론 모델 PyTorchKR]]
