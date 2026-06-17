---
tags: [entity, tool, obsidian, agent-skill, second-brain]
sources:
  - wiki/출처/obsidian-second-brain Obsidian 세컨드 브레인 PyTorchKR.md
url: https://github.com/eugeniughelbur/obsidian-second-brain
---

# obsidian-second-brain

[[Eugeniu Ghelbur]]의 **크로스 CLI 스킬** — Obsidian Vault를 **자기 갱신(self-rewriting) AI-first 세컨드 브레인**으로 운영. Andrej Karpathy [[LLM Wiki]] 패턴의 확장.

## 지원 CLI

Claude Code · Codex CLI · Gemini CLI · OpenCode — **단일 코드베이스**.

## Karpathy 대비 차별

- 덧붙이기 → **재작성** (인물·주장·사실 갱신)
- 모순 표시 → `/obsidian-reconcile` **자동 조정**
- 패턴은 질의 시 → `/obsidian-synthesize` **자동 종합**
- 요청 시만 → **4 예약 에이전트** (야간·주간·모순·볼트 상태)

## AI-first 노트 형식

- `## For future Claude` 프리앰블
- LLM 검색용 YAML frontmatter

## 명령 (43+, v0.10)

| 카테고리 | 예 |
|----------|-----|
| 흡수·저장 | `/obsidian-save`, `/obsidian-ingest` (Whisper·영상·웹·X) |
| 품질 | `/obsidian-reconcile`, `/obsidian-synthesize`, `/obsidian-challenge` |
| 일과 | `/obsidian-daily`, 야간 에이전트 |
| 리서치 | `/research-deep` (웹), `/notebooklm` (볼트) |
| v0.10 | `/obsidian-architect` — 코드→아키텍처 노트 |

## v0.10 "The Architect"

키 없는 웹 리서치 · Google Calendar · 환각 가드 · 테스트·CI.

## 배포

- **라이선스**: MIT
- **GitHub**: https://github.com/eugeniughelbur/obsidian-second-brain

## 관련

- [[LLM Wiki]] · [[Eugeniu Ghelbur]] · [[PyTorchKR]]
- [[출처/obsidian-second-brain Obsidian 세컨드 브레인 PyTorchKR]]
- [[루프 엔지니어링]] — 스케줄·자동화 워크플로
