---
tags: [ingest, agent, harness, paper, pytorchkr]
date: 2026-06-19
sources:
  - raw/sources/2026-06-19-discuss-pytorchkr-harnessx-xiaomi-10740.md
assets:
  - raw/assets/harnessx_1.png
  - raw/assets/harnessx_2.jpeg
  - raw/assets/harnessx_3.jpeg
  - raw/assets/harnessx_4.jpeg
  - raw/assets/harnessx_5.jpeg
  - raw/assets/harnessx_6.png
  - raw/assets/harnessx_7.png
url: https://discuss.pytorch.kr/t/harnessx-feat-xiaomi/10740
author: 9bow(박정환)
published: 2026-06-19
paper_url: https://arxiv.org/abs/2606.14249
note: PyTorchKR 커뮤니티 게시물. GPT 정리본; held-out 미검증 등 한계는 원문 확인.
---

# HarnessX: 에이전트 하네스 진화 (PyTorchKR)

> 출처: [PyTorchKR #10740](https://discuss.pytorch.kr/t/harnessx-feat-xiaomi/10740) · 9bow · 2026-06-19 · 논문 [arXiv:2606.14249](https://arxiv.org/abs/2606.14249) · Xiaomi

## 한 줄 요약

**[[HarnessX]]** — [[에이전트 하네스]]를 **직렬화·조합·교체 가능한 1급 객체**로 두고, 실행 트레이스로 **AEGIS** 적응 + **cross-harness GRPO** 공진화. 5 벤치 평균 **+14.5%**(최대 **+44%**); 약한 모델일수록 이득 큼.

## 핵심 내용

### 문제: 정적·뒤엉킨 하네스

에이전트 성능은 기반 모델만이 아니라 **하네스**(프롬프트·도구·메모리·제어 흐름)에 크게 의존. 현재 하네스는 (1) **수동·정적**, (2) 프롬프트·도구·재시도·메모리가 **한 코드 경로에 뒤섞임**, (3) 하네스 개선과 **모델 학습이 분리**되어 trajectory가 버려짐.

LangChain/LlamaIndex/Smolagents는 부품, LangGraph/AutoGen/CrewAI는 오케스트레이션, Claude Code/Cursor는 **고정된** 제품화 하네스 — 모두 **하네스 자체의 자동 진화**까지는 못 감.

### HarnessX 3층

![HarnessX 개요](../../raw/assets/harnessx_1.png)

| 층 | 역할 |
|----|------|
| **Compose** | 타입 있는 프리미티브 + 치환 대수로 하네스 조합 |
| **Adapt (AEGIS)** | 실행 트레이스 근거 자동 진화 |
| **Evolve (공진화)** | 동일 트레이스를 GRPO 학습 신호로 재활용 |

### 1급 객체 하네스

$\mathcal{H}=(\mathcal{M},\mathcal{C})$ — **모델 설정** $\mathcal{M}$ + **하네스 설정** $\mathcal{C}=(\mathbf{P},\mathbf{S})$.

- $\mathbf{P}$: 8 lifecycle hook별 **Processor** 파이프라인
- $\mathbf{S}$: 도구 레지스트리·트레이서·워크스페이스·샌드박스·플러그인 등 **공유 슬롯**

`agent = model_config.agentic(harness_config)` — 모델·하네스 **독립 교체**.

**Processor** — `process(event) → AsyncIterator[Event]`; 결과 5종: pass-through / transform / split / intercept / interrupt. `_singleton_group`, `_order`, `_after`로 조합 제어.

**9차원 택소노미** D1–D9: 모델·컨텍스트·메모리·도구·실행환경·평가·제어·관측·학습 브릿지. AEGIS는 주로 **D2(컨텍스트)·D4(도구)** 편집.

### AEGIS (Operational Mirror)

하네스 진화 ≈ **기호 공간 RL**: 설정=state, 타입 있는 edit=action, 트레이스+검증=reward.

![AEGIS 루프](../../raw/assets/harnessx_4.jpeg)

| 단계 | 역할 |
|------|------|
| **Digester** | ~10M 토큰 트레이스 → 구조화 증거(~10K) |
| **Planner** | 적응 지형 — 과소 탐험 방어 |
| **Evolver** | 후보 하네스 + change manifest + smoke test |
| **Critic + 게이트** | 보상 해킹 방어; **seesaw constraint**(회귀 편집 거부) |

원칙: *LLM은 제안, 타입·결정론적 게이트가 출시 결정.*

**변형 겹리(variant isolation)** — 최대 K개 하네스 변형, 작업별 최고 변형으로 **앙상블 라우팅**. GAIA GPT-5.4: Global 정체 $0.0\%$ → 격리 **+13.6%**.

### Harness–Model 공진화

![공진화 루프](../../raw/assets/harnessx_5.jpeg)

공유 **replay buffer**: rollout → 검증 → buffer → AEGIS($\mathcal{H}_{t+1}$) + **cross-harness GRPO**($\mathcal{M}_{t+1}$).

- GRPO 그룹 = **같은 task id**의 모든 트레이스 (하네스 버전 무관)
- 하네스 변형이 **구조화된 탐험 연산자** — 추가 rollout 없이 모델 갱신
- GAIA/WebShop **scaffolding ceiling** 돌파: 평균 **+4.7%** 추가

### 실험 (요약)

- **5 벤치**: GAIA, ALFWorld, WebShop, $\tau^3$-Bench, SWE-bench Verified
- **작업 모델**: Claude Sonnet 4.6, GPT-5.4, Qwen3.5-9B · **메타**: Opus 4.6 고정
- **15/15 설정 중 14개 개선**, 평균 **+14.5%**, 최대 **Qwen ALFWorld +44%** (53→97%)
- **역스케일링**: 베이스라인 낮을수록 향상 큼
- 세 병리 **실측**: 보상 해킹(GAIA R10–12), 망각(τ³ R7), 과소 탐험(ALFWorld R4–7)

### 한계

- **Held-out eval 없음** — 진화셋=평가셋, 과적합 가능
- 이산·텍스트 행동 공간만; 메타 에이전트는 Opus 4.6만 검증
- 공진화는 하네스·모델 **공동 통제** 필요

## 관련 위키

- [[HarnessX]] · [[AEGIS]] · [[에이전트 하네스]]
- [[루프 엔지니어링]] — harness → loop 개념 층
- [[Claude Managed Agents]] · [[Claude Fable 5]] — 제품화 harness
- [[PyTorchKR]]

## 원본

- `raw/sources/2026-06-19-discuss-pytorchkr-harnessx-xiaomi-10740.md`
