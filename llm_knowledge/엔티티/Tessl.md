---
tags: [entity, tool, sdd]
sources:
  - raw/sources/2025-10-20-geeknews-sdd-tools-23776.md
---

# Tessl

**Tessl Framework** — **[[스펙 주도 개발]]** CLI (비공개 베타). MCP 서버 겸용. [[Spec-kit]]처럼 작업 공간 생성.

## SDD 수준

세 도구 중 **spec-anchored를 명시**하고 **spec-as-source** 탐구.

- 명세 = 유지·편집하는 **주요 산출물**
- 코드 상단: `// GENERATED FROM SPEC - DO NOT EDIT`
- 현재 **1 spec : 1 code file** (베타, 다파일 매핑 가능성)

## 명세 구조

- `@generate`, `@test` 태그
- API 섹션: 외부 노출 **최소 인터페이스**만 명세에 정의
- `tessl build` → JS 등 코드 생성

## 관찰

- 낮은 추상화 → LLM 해석 단계·오류 감소 기대
- 동일 spec에서 **재생성 시 비결정성** 관찰
- 명세를 더 구체화하는 반복 → "완전 명세" 함정 (MDD와 유사)

## 관련

- [[스펙 주도 개발]] · MDD(모델 주도 개발)와 개념상 유사
- [[출처/스펙 주도 개발 SDD GeekNews]]
- [[Kiro]] · [[Spec-kit]]
