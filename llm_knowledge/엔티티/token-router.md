---
tags: [entity, tool, skill, github, token]
sources:
  - raw/sources/2026-06-17-geeknews-token-router-30547.md
url: https://github.com/sleeplesshan/token-router
license: MIT
author: sleeplesshan
---

# token-router

MIT 오픈소스 **[[하이브리드 컨텍스트 라우팅]]** 스킬·스크립트. Ollama **Gemma 4 2B**(기본)로 로컬 triage → Python **raw slice** → Codex·Claude Code 클라우드 추론.

## 아키텍처

```
질문 + 대용량 파일/지침
  → Ollama (라인 좌표 JSON)
  → router.py (원문 slice)
  → 클라우드 에이전트 (추론만)
```

## 모드

| 모드 | 대상 |
|------|------|
| `error_log` | 대용량 로그 |
| `heavy_code` | 대형·레거시 소스 |
| `agent_context` | CLAUDE.md, AGENTS.md, GEMINI.md, .cursorrules, agent-context/*.md |

## 사용·배포

- 독립 Python 스크립트 또는 **OpenAI Codex 스킬** 등록
- Claude Code: compact `CLAUDE.md` bootstrap + reference 파일 `agent_context` 라우팅
- 모델 변경: `OLLAMA_MODEL=qwen2.5-coder:7b python3 scripts/router.py ...` (댓글: JSON 안정성↑)

## 저자 벤치 (Show GN #30547)

- 2,000줄 로그: 41,711 → 131 토큰 (99.69%)
- 2,155줄 코드: 7,520 → 70 토큰 (99.06%)

실환경·모델·파일 유형에 따라 다를 수 있음.

## 관련

- [[하이브리드 컨텍스트 라우팅]] · [[컨텍스트 엔지니어링]]
- [[출처/token-router 하이브리드 컨텍스트 라우터 GeekNews]]

## 링크

- https://github.com/sleeplesshan/token-router
- https://news.hada.io/topic?id=30547
