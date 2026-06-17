---
tags: [entity, product, llmops, open-source]
sources:
  - raw/sources/2026-06-17-discuss-pytorchkr-tensorzero-llmops-10694.md
url: https://github.com/tensorzero/tensorzero
license: Apache-2.0
---

# TensorZero

오픈소스 **[[LLMOps]]** 플랫폼 — LLM **게이트웨이**, **관측**, **평가**, **최적화**, **실험**을 단일 스택으로 통합. 프로덕션 추론 데이터가 평가·미세조정으로 이어지는 **데이터 플라이휠**을 목표로 설계.

## 아키텍처 (5모듈)

| 모듈 | 요약 |
|------|------|
| Gateway | Rust; OpenAI SDK 호환; 다중 제공자·자체 호스팅 |
| Observability | 사용자 DB에 추론·피드백; OTLP·Prometheus |
| Evaluation | 추론 평가 + 워크플로 평가 (LLM judge) |
| Optimization | SFT·RLHF·GEPA·DICL |
| Experimentation | A/B·순차 검정·멀티턴 실험 |

## 게이트웨이

- `base_url`을 게이트웨이(예: `http://localhost:3000/openai/v1`)로 두고 `model`에 `tensorzero::model_name::...` 형식
- vLLM·SGLang·Ollama 등 자체 호스팅 백엔드 연결
- 저자 벤치: 10k+ QPS에서 p99 &lt;1ms 오버헤드 ([[출처/TensorZero LLMOps PyTorchKR]])

## 상용·생태

- **TensorZero Autopilot** — 관측·평가·최적화 자동화 **유료** (오픈소스와 별도)
- Apache 2.0, 자체 호스팅

## 관련

- [[LLMOps]]
- [[출처/TensorZero LLMOps PyTorchKR]]
- [[PyTorchKR]]

## 링크

- https://www.tensorzero.com
- https://github.com/tensorzero/tensorzero
