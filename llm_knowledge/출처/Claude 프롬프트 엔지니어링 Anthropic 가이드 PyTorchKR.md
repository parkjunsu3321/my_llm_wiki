---
tags: [ingest, prompt-engineering, anthropic, pytorchkr]
date: 2026-05-30
sources:
  - raw/sources/2026-05-30-discuss-pytorchkr-claude-prompt-engineering-10447.md
url: https://discuss.pytorch.kr/t/claude-anthropic/10447
---

# Claude 프롬프트 엔지니어링: Anthropic 공식 가이드 (PyTorchKR)

> 출처: [PyTorchKR 게시물](https://discuss.pytorch.kr/t/claude-anthropic/10447) · 9bow(박정환) · 2026-05-30  
> 원문: Anthropic [Prompting best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices)

## 한 줄 요약

[[Claude 프롬프트 엔지니어링]]은 모델 세대별 **기본값 변화**를 전제로, 명확한 지시·[[effort 파라미터]]·[[adaptive thinking]]·에이전트 하니스 설계를 한 레퍼런스로 정리한 [[Anthropic]] 가이드이다.

## 핵심 주제

### Opus 4.8 전용

- **effort**가 핵심 레버 (xhigh=코딩·에이전트, low=범위 고정 작업)
- thinking 기본 OFF → adaptive 명시 필요
- literal instruction following, 도구보다 추론 선호
- 코드 리뷰: 필터 지시가 recall을 낮춰 보이게 함 → coverage 단계 분리

### 세대 공통 + 마이그레이션

- Golden rule: 맥락 없는 동료 테스트
- few-shot + XML 태그, 긴 문서는 상단 배치
- **Prefill 폐지** (4.6+)
- "CRITICAL/MUST" → [[overtriggering]] (4.5/4.6+)
- anti-laziness 프롬프트 **제거** 권장 (새 모델은 이미 능동적)

### 에이전트

- 장기 호흡·상태 추적·안전 확인
- overengineering 억제 스니펫
- 병렬 도구 호출, 서브에이전트 위임 기준

## 관련 위키

- [[개념/Claude 프롬프트 엔지니어링]]
- [[개념/effort 파라미터]]
- [[개념/adaptive thinking]]
- [[개념/overtriggering]]
- [[엔티티/Anthropic]]
- [[엔티티/Claude Opus 4.8]]
- [[엔티티/PyTorchKR]]

## 원본

- `raw/sources/2026-05-30-discuss-pytorchkr-claude-prompt-engineering-10447.md`
