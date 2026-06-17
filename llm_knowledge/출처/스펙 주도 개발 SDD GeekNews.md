---
tags: [ingest, agent, geeknews, sdd]
date: 2026-06-15
sources:
  - raw/sources/2025-10-20-geeknews-sdd-tools-23776.md
url: https://news.hada.io/topic?id=23776
original_url: https://martinfowler.com/articles/exploring-gen-ai/sdd-tools.html
author: Birgitta Böckeler
---

# 스펙 주도 개발(SDD) — Kiro, Spec-Kit, Tessl (GeekNews)

> 출처: [GeekNews #23776](https://news.hada.io/topic?id=23776) · GN+ xguru · 2025-10-20 · 원문 [Martin Fowler — Understanding SDD tools](https://martinfowler.com/articles/exploring-gen-ai/sdd-tools.html)

## 한 줄 요약

**[[스펙 주도 개발]]** = AI 코딩에서 코드 전에 **명세(spec)** 를 진실 공급원으로 두는 접근. **spec-first → spec-anchored → spec-as-source** 세 단계. [[Kiro]]·[[Spec-kit]]·[[Tessl]] 비교 — 작은 수정에 과한 프로세스·마크다운 리뷰 피로·에이전트 비준수 한계; MDD 교훈과 LLM 비결정성.

## 핵심 내용

### SDD 정의

- 코드 작성 **전** 명세 우선(documentation first)
- 명세 = 개발자·AI 공통 **single source of truth**
- GitHub: *유지보수 = 명세의 진화; 코드는 최종 단계*
- Tessl: *명세가 주요 산출물, 구조화·테스트 가능한 의도 → 에이전트가 코드 생성*

### 세 구현 수준

| 수준 | 설명 |
|------|------|
| **spec-first** | 잘 구조화된 명세를 먼저 쓰고 AI 워크플로에 사용 |
| **spec-anchored** | 기능 완료 후에도 명세를 유지·진화시킴 |
| **spec-as-source** | 명세만 편집, 코드는 생성물(`GENERATED FROM SPEC`) |

모든 SDD는 spec-first이지만, anchored/as-source를 **지향하지 않는** 도구도 많음.

### spec vs memory bank

| | 명세(spec) | 메모리 뱅크 / steering / constitution |
|--|------------|--------------------------------------|
| 범위 | **특정 기능** 생성·변경 작업 | 코드베이스 **전역** AI 컨텍스트 |
| 예 | PRD급 기능 명세 | `AGENTS.md`, product.md, constitution |

### 도구 비교

| | [[Kiro]] | [[Spec-kit]] | [[Tessl]] |
|--|----------|--------------|-----------|
| 배포 | VS Code 기반 | CLI + 슬래시 커맨드 | CLI (+ MCP) |
| 워크플로 | 요구사항 → 설계 → 작업 (3 MD) | Constitution → Specify → Plan → Tasks | spec-as-source 실험 |
| SDD 수준 | 주로 **spec-first** | spec-first (브랜치별 명세) | **spec-anchored** 명시, as-source 탐구 |
| 특징 | GIVEN/WHEN/THEN, steering | 헌법(불변 원칙), 8+ MD 파일 | `@generate`, 1:1 spec↔code |

### 한계·비판 (원문 + HN)

- **규모 불일치**: 작은 버그 → 16개 acceptance criteria, 4 user stories (Kiro); spec-kit도 과도한 MD 산출
- **리뷰 피로**: 코드보다 마크다운 리뷰가 더 번거로움
- **통제 착각**: 큰 컨텍스트 ≠ 모든 지시 준수; 헌법 과잉·연구 무시·중복 생성
- **기능 vs 기술 명세** 분리 혼란
- **MDD 재현**: spec-as-source는 UML/MDD와 유사 — LLM이 생성기·DSL 제약은 줄이지만 **비결정성**·**비유연성** 위험
- **Verschlimmbesserung**: 워크플로가 기존 문제(과부하·환각)를 증폭할 수 있음

### 실무 코멘트 (GeekNews)

- SE에서 배운 요구사항 명세를 마크다운으로 — 실용적
- README/document-driven development와 유사 ([#15502](https://news.hada.io/topic?id=15502))
- SpecKit 2주 실험: 테스트 실패·빌드 깨짐; subagent 단위 반복이 더 신뢰적
- cofounder: **spec as source** 올인 — 명세가 진짜 소스면 실행 가능한 형식 언어에 가까워야

## 관련 위키

- [[스펙 주도 개발]] — 개념·수준·MDD 비교
- [[Kiro]] · [[Spec-kit]] · [[Tessl]]
- [[Claude 프롬프트 엔지니어링]] — 명세·프롬프트 구조
- [[루프 엔지니어링]] — 반복 워크플로 (대비: SDD는 사전 명세 중심)

## 원본

- `raw/sources/2025-10-20-geeknews-sdd-tools-23776.md`
- GeekNews: https://news.hada.io/topic?id=23776
- Fowler: https://martinfowler.com/articles/exploring-gen-ai/sdd-tools.html
