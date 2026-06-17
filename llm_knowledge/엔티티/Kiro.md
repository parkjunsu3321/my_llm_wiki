---
tags: [entity, tool, sdd, aws]
sources:
  - raw/sources/2025-10-20-geeknews-sdd-tools-23776.md
---

# Kiro

AWS의 **[[스펙 주도 개발]]** 도구 — Kiro·[[Spec-kit]]·[[Tessl]] 중 **가장 단순·경량**. VS Code 기반 배포.

## SDD 수준

주로 **spec-first**. spec-anchored(기능 수명 동안 명세 유지) 사례는 드묾.

## 워크플로

**요구사항 → 설계 → 작업** — 각 단계 하나의 마크다운.

| 단계 | 내용 |
|------|------|
| Requirements | user story(As a…), GIVEN/WHEN/THEN acceptance criteria |
| Design | 아키텍처, 데이터 모델, 에러 처리, 테스트 전략 등 |
| Tasks | 요구사항 번호 추적 작업 목록, 단계별 실행 UI |

## Steering (메모리 뱅크)

Kiro 용어 **steering** — 전역 컨텍스트. 기본 생성: `product.md`, `structure.md`, `tech.md`.

## 한계 (Fowler 평가)

- 작은 버그 수정에 **과한** 요구사항·AC 확장
- 코드 삭제·롤백 예측 불가 (사용자 보고)
- MD 리뷰 부담은 spec-kit보다 적지만 여전히 존재

## 관련

- [[스펙 주도 개발]] · [[출처/스펙 주도 개발 SDD GeekNews]]
- [[Spec-kit]] · [[Tessl]]
