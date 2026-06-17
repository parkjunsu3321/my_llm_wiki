---
tags: [concept, llm, ops, production]
sources:
  - raw/sources/2026-06-17-discuss-pytorchkr-tensorzero-llmops-10694.md
---

# LLMOps

**LLM Operations** — LLM 애플리케이션을 **프로토타입에서 프로덕션·지속 개선**까지 운영하기 위한 도구·프로세스 묶음. 게이트웨이, 관측, 평가, 최적화, 실험이 흔한 축.

## 전형적 구성

| 영역 | 역할 |
|------|------|
| **게이트웨이** | 다중 모델 제공자·자체 호스팅을 통합 API로 호출 |
| **관측(Observability)** | 추론·피드백·지표 기록·트레이싱 |
| **평가(Evaluation)** | 품질·회귀 검증 (휴리스틱·LLM judge) |
| **최적화** | 프롬프트·모델·전략 개선 (SFT·RLHF·자동 프롬프트 튜닝 등) |
| **실험** | A/B·라우팅·폴백 비교 |

## 운영 마찰

도구가 **분리**되면 데이터 포맷·연동이 달라, 한 시스템에서 모은 프로덕션 신호를 평가·학습 파이프라인에 **그대로 재사용하기 어렵다** ([[출처/TensorZero LLMOps PyTorchKR]]).

## 통합 스택 예

**[[TensorZero]]** — 위 다섯 기능을 오픈소스 단일 스택 + 게이트웨이 추론→DB→평가→최적화 **플라이휠** ([[출처/TensorZero LLMOps PyTorchKR]]).

## 관련

- [[TensorZero]]
- [[에이전틱 코딩]] — 프로덕션 전 단계; LLMOps는 배포 후 순환
- [[카카오페이 AI 플랫폼]] — AI Platform·LLMOps 인프라 언급
