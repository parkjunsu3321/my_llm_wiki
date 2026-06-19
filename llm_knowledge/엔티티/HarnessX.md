---
tags: [entity, agent, harness, paper]
sources:
  - raw/sources/2026-06-19-discuss-pytorchkr-harnessx-xiaomi-10740.md
url: https://arxiv.org/abs/2606.14249
---

# HarnessX

Xiaomi 연구진의 **Composable, Adaptive, and Evolvable Agent Harness Foundry**. 에이전트 **[[에이전트 하네스|하네스]]**를 1급 객체로 두고 실행 트레이스에서 자동 개선.

논문: [arXiv:2606.14249](https://arxiv.org/abs/2606.14249)

## 3층

1. **Compose** — $\mathcal{H}=(\mathcal{M},\mathcal{C})$, Processor 조합
2. **Adapt** — [[AEGIS]] 진화 엔진
3. **Evolve** — cross-harness GRPO **하네스–모델 공진화**

## 실험 하이라이트

- 5 벤치 · 3 모델 패밀리 · pass@2
- 평균 **+14.5%**, 최대 **+44%** (Qwen3.5-9B · ALFWorld)
- **역스케일링** — 약한 모델·낮은 베이스라인일수록 harness 편집 이득 큼
- **변형 격리** — GAIA GPT-5.4 Global 정체 → +13.6%

## 한계

진화셋=평가셋(held-out 없음), Opus 4.6 메타만 검증, 조직적으로 harness·모델 공동 통제 필요.

## 관련

- [[출처/HarnessX PyTorchKR]]
- [[AEGIS]] · [[에이전트 하네스]]
- [[PyTorchKR]]
