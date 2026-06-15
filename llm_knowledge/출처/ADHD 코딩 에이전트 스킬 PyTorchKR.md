---
tags: [ingest, agent-skill, pytorchkr]
date: 2026-06-02
sources:
  - raw/sources/2026-06-02-discuss-pytorchkr-adhd-10481.md
url: https://discuss.pytorch.kr/t/adhd/10481
---

# ADHD: 코딩 에이전트 발산-수렴 스킬 (PyTorchKR)

> 출처: [PyTorchKR 게시물](https://discuss.pytorch.kr/t/adhd/10481) · 작성 9bow(박정환) · 2026-06-02

## 한 줄 요약

[[ADHD 스킬]]은 LLM의 **조기 수렴**을 구조적으로 막기 위해, 서로 맥락을 공유하지 않는 [[인지 프레임]]별 병렬 발산(Diverge) 후 별도 비평가가 수렴(Focus)하는 코딩 에이전트용 스킬이다.

## 핵심 내용

### 문제 인식

- 자기회귀 생성 → 첫 가설이 이후 추론을 끌어당김
- [[Chain-of-Thought]]: 첫 답에 묶임
- [[Tree-of-Thought]]: 폭은 넓히나 공유 맥락 위에서 고착이 가지에 번짐

### ADHD 접근

| 단계 | 역할 | 격리 |
|------|------|------|
| **Diverge** | N개 프레임 × 독립 Agent 병렬 호출 | 분기끼리 결과 비공유 → 앵커링 방지 |
| **Focus** | 별도 critic이 채점·군집·심화 | 생성기와 비평가를 별도 LLM 호출로 분리 |

비평 기준: 참신성, 실현 가능성, 적합성. 함정(trap) 아이디어 명시적 표시.

### 벤치마크 (저자 보고, LLM 채점)

6개 open-ended 엔지니어링 문제, 5/6 승. 특히 **함정 탐지 5.2×**, **참신성 2.9×** 개선. 방법론 한계는 원저장소 `documentation/evals.md` 참고.

### 설치·사용

```bash
npx skills add UditAkhourii/adhd
```

`/adhd "문제"` 또는 CLI·라이브러리(`adhd-agent`). MIT 라이선스.

## 관련 위키

- [[ADHD 스킬]] — 개념·동작 상세
- [[인지 프레임]] — Diverge 단위
- [[Udit Akhouri]] — 원저자
- [[adhd-agent]] — GitHub 프로젝트

## 원본

- `raw/sources/2026-06-02-discuss-pytorchkr-adhd-10481.md`
