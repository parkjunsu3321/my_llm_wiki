---
tags: [ingest, slm, reasoning, pytorchkr]
date: 2026-06-17
sources:
  - raw/sources/2026-06-17-discuss-pytorchkr-vibethinker-3b-10748.md
assets:
  - raw/assets/vibethinker_1.png
  - raw/assets/vibethinker_2.png
  - raw/assets/vibethinker_3.png
  - raw/assets/vibethinker_4.png
url: https://discuss.pytorch.kr/t/vibethinker-3b-3b-feat-weibo-ai/10748
author: 9bow(박정환)
published: 2026-06-17
note: PyTorchKR 커뮤니티 게시물. GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.
---

# VibeThinker-3B: 3B 파라미터 프론티어급 추론 (PyTorchKR)

> 출처: [PyTorchKR #10748](https://discuss.pytorch.kr/t/vibethinker-3b-3b-feat-weibo-ai/10748) · 9bow · 2026-06-17 · 원저 [[Weibo AI]] 기술 보고서

## 한 줄 요약

[[Weibo AI]]의 **[[VibeThinker-3B]]** — Qwen2.5-Coder-3B 기반 3B SLM이 [[Spectrum-to-Signal 원칙]] 사후 학습으로 AIME26 **94.3**, LiveCodeBench v6 **80.2** 등 **검증 가능한 추론**에서 DeepSeek V3.2(671B)·Kimi K2.5(1T)급 성능. [[추론-지식 분리]] 가설·[[CLR]] test-time scaling.

## 핵심 내용

### 문제·가설

- 프론티어 추론은 스케일링 법칙으로 **초대형 모델**에 집중; SLM(≤3B)은 긴 호흡 추론에 약하다는 통념
- [[VibeThinker-3B]] 전작 VibeThinker-1.5B가 “작은 모델도 추론 가능”을 입증했으나 상한은 미지
- **파라미터 압축-커버리지 가설**: 검증 가능 추론(탐색·제약·오류 수정·다단계 조합)은 **압축 가능(parameter-dense)**; 개방형 지식·롱테일 대화는 **넓은 커버리지(parameter-expansive)** → GPQA-Diamond 격차와 정합

### 사후 학습 파이프라인 (SSP 계승)

Qwen2.5-Coder-3B → 4단계:

| 단계 | 내용 |
|------|------|
| **1. 2단계 커리큘럼 SFT** | 다중 도메인 스펙트럼 구축 — 쿼리 확장·다중 경로 증류·3단계 품질 필터; 2단계는 5K+ 토큰 긴 추론 위주 |
| **2. 다중 도메인 RL** | **MGPO**로 Math→Code→STEM 순차; **처음부터 64K** 단일 컨텍스트(3B에서는 점진 확장 역효과); **Long2Short**로 정확도 유지하며 토큰 절감 |
| **3. 오프라인 자기 증류** | 도메인별 RL 체크포인트 → **learning-potential score** 우선 증류 |
| **4. Instruct RL** | 형식·지시 준수; 규칙 검증기 + 루브릭 보상 |

[[Spectrum-to-Signal 원칙]]: SFT에서 다양한 풀이 **스펙트럼** → RL에서 올바른 **신호** 증폭.

### CLR (test-time scaling)

- K=32 후보 궤적 → 핵심 **claim** M=5 추출 → self-verifier 이진 판정
- 신뢰도 \(r_k = (\frac{1}{M}\sum v_{k,m})^M\) — 하나라도 실패 시 급격히 감점
- 답 군집 후 신뢰도 가중 합으로 최종 선택; 파라미터 갱신 없이 Pass@1 향상

### 벤치마크 (vLLM, temp 1.0, top-p 0.95)

**소형·중형 대비**

| 영역 | 대표 점수 |
|------|-----------|
| 수학 | AIME25 91.4, AIME26 **94.3**, HMMT25 89.3, BruMO25 93.8, IMO-AnswerBench 76.4 |
| 코드 | LiveCodeBench v6 **80.2**, OJBench 38.6 |
| 지시 | IFEval 93.4, IFBench 74.5 |

**최상위 대비 + CLR**

- CLR 적용 시 AIME26 **97.1**, BruMO25 **99.2**, IMO-AnswerBench **80.6** — GLM-5·Gemini 3 Pro·GPT-5 구간
- **OOD**: 2026-04~05 LeetCode 콘테스트 128문제 중 123 통과 (**96.1%**)

**한계**: GPQA-Diamond 70.2→72.9(CLR) — 지식 집약 과제는 대형 모델 격차

### 사용

- MIT · `WeiboAI/VibeThinker-3B` · `transformers>=4.54.0` · vLLM 0.10.1 / SGLang 권장
- 수학·코딩·STEM(검증 가능)에 적합; 광범위 개방형 지식은 대형 범용 모델 유리

## 관련 위키

- [[VibeThinker-3B]] · [[Weibo AI]]
- [[Spectrum-to-Signal 원칙]] · [[추론-지식 분리]] · [[CLR]]
- [[PyTorchKR]]

## 원본·리소스

- `raw/sources/2026-06-17-discuss-pytorchkr-vibethinker-3b-10748.md`
- PyTorchKR: https://discuss.pytorch.kr/t/vibethinker-3b-3b-feat-weibo-ai/10748
- Hugging Face: https://huggingface.co/WeiboAI/VibeThinker-3B
- GitHub: https://github.com/WeiboAI/VibeThinker

## 도표 (원본 첨부)

![SSP 파이프라인](../../raw/assets/vibethinker_1.png)

![IMO-AnswerBench 파라미터 효율](../../raw/assets/vibethinker_2.png)

![벤치마크 비교](../../raw/assets/vibethinker_3.png)

![추가 벤치마크](../../raw/assets/vibethinker_4.png)
