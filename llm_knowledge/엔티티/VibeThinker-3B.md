---
tags: [entity, model, slm, reasoning]
sources:
  - raw/sources/2026-06-17-discuss-pytorchkr-vibethinker-3b-10748.md
url: https://huggingface.co/WeiboAI/VibeThinker-3B
---

# VibeThinker-3B

[[Weibo AI]]의 **3B** dense 추론 특화 소형 언어 모델(SLM). 기반: **Qwen2.5-Coder-3B**. [[Spectrum-to-Signal 원칙]] 4단계 사후 학습.

## 성능 요약 (저자 보고)

| 벤치마크 | Pass@1 | 비고 |
|----------|--------|------|
| AIME26 | 94.3 (97.1 + [[CLR]]) | DeepSeek V3.2(671B)급 |
| LiveCodeBench v6 | 80.2 | 소형·중형 베이스라인 상회 |
| LeetCode OOD (2026-04~05) | 96.1% (123/128) | GPT-5.2·Claude 4.6 등 대비 |
| GPQA-Diamond | 70.2 (72.9 + CLR) | 지식 집약 — 대형 모델 격차 |

## 학습·추론

- **MGPO** RL, 64K 단일 컨텍스트, Long2Short 효율 단계
- 평가 권장: temperature **1.0**, top-p **0.95**, top-k **-1**
- `max_new_tokens` 최대 102400 (긴 CoT)

## 전작·계열

- **VibeThinker-1.5B** — SSP·MGPO 최초 실증 (“Tiny Model, Big Logic”)
- VibeThinker-3B — “어느 정도 파라미터면 프론티어 추론 등급?” 질문에 답

## 배포

- **라이선스**: MIT
- **Hugging Face**: `WeiboAI/VibeThinker-3B`
- **GitHub**: [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker)
- **런타임**: `transformers>=4.54.0`, vLLM 0.10.1 또는 SGLang≥0.4.9.post6

## 관련

- [[Weibo AI]] · [[Spectrum-to-Signal 원칙]] · [[추론-지식 분리]] · [[CLR]]
- [[출처/VibeThinker-3B 소형 추론 모델 PyTorchKR]]
