---
tags: [ingest, agent, geeknews, fable]
date: 2026-06-11
sources:
  - raw/sources/2026-06-11-geeknews-fable5-loop-engineering-30390.md
url: https://news.hada.io/topic?id=30390
original_url: https://x.com/RLanceMartin
---

# Fable 5로 루프 설계하기 (GeekNews)

> 출처: [GeekNews #30390](https://news.hada.io/topic?id=30390) · GN+ neo · 2026-06-11 · 원문 [Lance Martin (X)](https://x.com/RLanceMartin)

## 한 줄 요약

[[Claude Fable 5]]는 직접 조종보다 **[[루프 엔지니어링]]**(self-correction + memory)으로 쓸 때 강하다 — Parameter Golf에서 Opus 4.7 대비 **~6×** 파이프라인 개선, memory 벤치에서 검증 커버리지 **73%** vs Opus **~17%**.

## 핵심 내용

### 두 가지 루프

| 루프 | 역할 | primitive 예 |
|------|------|----------------|
| **Self-correction** | rubric/goal 피드백 → 실행·수정 반복 | Claude Code `/goal`, [[Claude Managed Agents]] **Outcomes** |
| **Memory** | 세션 간 outer loop, 기록 검색·재사용 | CMA mounted filesystem memory |

bcherny: *"자신의 일은 루프를 작성하는 것."* — 대화형 프롬프팅보다 **실험 환경 설계**에 가깝다.

### Parameter Golf (ML 엔지니어링)

- 16MB 모델, 8×H100, 10분 내 학습 — `train_gpt.py` 단일 파일 autoresearch형 챌린지
- [[Claude Managed Agents]] + self-hosted 8×H100 sandbox
- **9개 rubric** (baseline, 실험 20회 등), 최대 8시간; **Outcomes grader** sub-agent가 종료 허용
- **Self-critique < verifier sub-agent** (독립 context window)
- **Fable 5**: 구조적 변경·회복력, ~6× 개선 / **Opus 4.7**: 스칼라 튜닝 반복

### Continual Learning Bench (memory)

- pgasawa 팀 **Continual Learning Bench 1.0** — stateful 온라인 개선 측정
- SQL DB 순차 Q&A, 질문마다 별도 세션 + 공유 memory
- Memory 파이프라인: **fail → investigate → verify → distill → consult**
- Sonnet 4.6 ≈ fail / Opus 4.7 ≈ verify (median 17%) / **Fable 5** ≈ distill (최대 73%)

## 후속 검증

- [[출처/루프 엔지니어링 Addyo GeekNews]] — 동일 개념의 개론 (5+1 구성요소, build the loop stay the engineer)

## 관련 위키

- [[루프 엔지니어링]] — 개념·기법 상세
- [[Claude Fable 5]] — Mythos-class 모델
- [[Claude Managed Agents]] — harness·Outcomes·sandbox
- [[Anthropic]]

## 원본

- `raw/sources/2026-06-11-geeknews-fable5-loop-engineering-30390.md`
