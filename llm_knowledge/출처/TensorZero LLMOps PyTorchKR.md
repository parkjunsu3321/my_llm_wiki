---
tags: [ingest, llmops, gateway, pytorchkr]
date: 2026-06-17
sources:
  - raw/sources/2026-06-17-discuss-pytorchkr-tensorzero-llmops-10694.md
assets:
  - raw/assets/tensorzero_1.png
  - raw/assets/tensorzero_2.png
url: https://discuss.pytorch.kr/t/tensorzero-llm-llmops/10694
author: 9bow(박정환)
published: 2026-06-17
note: PyTorchKR 커뮤니티 게시물. GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.
---

# TensorZero: 통합 LLMOps 플랫폼 (PyTorchKR)

> 출처: [PyTorchKR #10694](https://discuss.pytorch.kr/t/tensorzero-llm-llmops/10694) · 9bow · 2026-06-17 · 원저 [[TensorZero]]

## 한 줄 요약

**[[TensorZero]]** — 게이트웨이·관측·평가·최적화·실험을 **단일 오픈소스 스택**으로 묶는 [[LLMOps]] 플랫폼. Rust 게이트웨이, OpenAI SDK·OpenTelemetry 호환, 프로덕션 추론→피드백→평가→미세조정 **데이터 플라이휠**.

## 핵심 내용

### 문제

LLM 앱을 운영 단계까지 가면 **게이트웨이·관측·평가·최적화** 도구가 제각각 분리되고, 데이터 포맷·연동 방식이 달라 **한 곳에서 모은 신호를 다른 곳에 재사용하기 어렵다**는 마찰이 커짐.

### TensorZero 접근

- **다섯 기능**을 점진적 도입 가능한 단일 스택으로 제공
- 게이트웨이(Rust) + OpenAI SDK / OTLP / Prometheus 연동 → 기존 코드 변경 최소화
- **복리 효과**: 게이트웨이 추론·피드백 → 관측 DB → 평가·최적화 입력 → 프로덕션 신호로 모델·프롬프트 재개선

### 다섯 구성 요소

| 구성 | 역할 |
|------|------|
| **Gateway** | 통합 API로 주요 LLM 제공자·자체 호스팅 호출; tool use, JSON, 배치, 임베딩, 멀티모달, 캐싱; 라우팅·재시도·폴백·로드밸런싱 |
| **Observability** | 추론·피드백(지표·사람 수정)을 **사용자 소유 DB**에 저장; UI·프로그램 조회; OTLP·Prometheus |
| **Evaluation** | **추론 평가**(휴리스틱·LLM judge, 단위 테스트 비유) + **워크플로 평가**(통합 테스트 비유) |
| **Optimization** | 프로덕션 지표·피드백으로 프롬프트·모델·추론 전략 개선; SFT·RLHF·**GEPA**(자동 프롬프트 최적화)·**DICL** |
| **Experimentation** | A/B·라우팅·폴백·재시도; 멀티턴·순차 검정(sequential testing) |

연계 예: LLM judge를 다른 함수처럼 미세조정, 평가 데이터를 SFT에 재사용.

### LLM 게이트웨이

- Anthropic, Bedrock, SageMaker, Azure, DeepSeek, Fireworks, Vertex, Google AI Studio, Groq, Mistral, OpenAI, OpenRouter, SGLang, TGI, Together, vLLM, xAI, Ollama(OpenAI 호환) 등
- 저자 주장: **10k+ QPS, p99 &lt;1ms** 게이트웨이 오버헤드 (README §LLM Gateway; 실제 지연은 제공자 의존)
- OpenAI SDK: `base_url`·`model`만 게이트웨이로 변경

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:3000/openai/v1", api_key="not-used")
response = client.chat.completions.create(
    model="tensorzero::model_name::anthropic::claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Share a fun fact about TensorZero."}],
)
```

### 평가·최적화·플라이휠

- UI·CLI 평가 예: `docker compose run --rm evaluations --evaluation-name ... --dataset-name ... --variant-name ...`
- 과거 추론 **replay**로 새 프롬프트·모델·전략 비교
- **TensorZero Autopilot**: 관측 분석·평가 설정·자동 최적화 **유료** 제품 (오픈소스 본체와 구분)
- 저자 주장: 프런티어 스타트업~포춘 10대 사용, 전 세계 LLM API 지출 **약 1%** (출처·검증은 원문 확인)

### 라이선스

- **Apache 2.0** — 개인·상업 사용, 100% 자체 호스팅

## 관련 위키

- [[TensorZero]] · [[LLMOps]]
- [[PyTorchKR]]

## 원본·리소스

- `raw/sources/2026-06-17-discuss-pytorchkr-tensorzero-llmops-10694.md`
- PyTorchKR: https://discuss.pytorch.kr/t/tensorzero-llm-llmops/10694
- 공식: https://www.tensorzero.com
- GitHub: https://github.com/tensorzero/tensorzero
- Docs: https://github.com/tensorzero/tensorzero/tree/main/docs

## 도표 (원본 첨부)

![TensorZero 개요](../../raw/assets/tensorzero_1.png)

![데이터 플라이휠](../../raw/assets/tensorzero_2.png)
