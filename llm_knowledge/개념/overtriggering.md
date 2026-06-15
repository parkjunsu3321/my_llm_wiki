---
tags: [concept, prompt-engineering, claude]
sources:
  - raw/sources/2026-05-30-discuss-pytorchkr-claude-prompt-engineering-10447.md
---

# overtriggering (과잉 발동)

이전 Claude 세대용 **공격적 시스템 프롬프트**가 최신 모델(Opus 4.5/4.6+)에서 **의도보다 과하게 동작**을 유발하는 현상.

## 원인

- 최신 모델은 시스템 프롬프트에 **더 민감**
- 지시 따르기·자율성 향상 → "anti-laziness" 보정이 불필요·해로움
- `"CRITICAL: You MUST use this tool"` → 도구·스킬 **과다 호출**

## 대칭 개념: undertriggering

구 세대에서 도구가 안 쓰여서 넣었던 강한 표현이, 신 세대에서는 overtriggering으로 바뀜.

## 해법

| Before | After |
|--------|-------|
| CRITICAL / MUST | 평범한 "Use this tool when..." |
| anti-laziness 블록 | **제거** (새 모델은 이미 능동적) |
| "3번마다 진행 요약" | Opus 4.8은 기본 품질 좋음 → 스캐폴딩 제거 |
| "고심각도만 보고" (리뷰) | coverage 단계와 filter 단계 **분리** |

## 마이그레이션 메시지

[[Claude 프롬프트 엔지니어링]] 핵심: 모델과 싸우지 말고, **강점을 방해하는 보정을 걷어낸다**.

## 관련

- [[Claude 프롬프트 엔지니어링]]
- [[엔티티/Claude Opus 4.8]]
