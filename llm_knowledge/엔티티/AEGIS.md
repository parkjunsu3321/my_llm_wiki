---
tags: [entity, agent, harness]
sources:
  - raw/sources/2026-06-19-discuss-pytorchkr-harnessx-xiaomi-10740.md
---

# AEGIS

**[[HarnessX]]**의 하네스 **적응(adapt)** 엔진. 실행 트레이스를 근거로 타입 있는 편집으로 $\mathcal{C}$를 진화.

## Operational Mirror

기호 공간에서 harness 진화 ≈ RL: configuration=state, edit=action, trace+verifier=reward.

## 4단계 (+ 게이트)

| 단계 | 역할 | 방어 대상 |
|------|------|-----------|
| Digester | 트레이스→증거 압축 | 컨텍스트 폭발 |
| Planner | 적응 지형 | **과소 탐험** |
| Evolver | 후보 + manifest | — |
| Critic | 명세 vs 증거 | **보상 해킹** |
| 결정론적 게이트 | seesaw constraint | **파국적 망각** |

## 변형 겹리

충돌 편집 시 **fork** → K개 변형 · 작업별 앙상블 라우팅.

## 관련

- [[HarnessX]] · [[에이전트 하네스]]
- [[출처/HarnessX PyTorchKR]]
