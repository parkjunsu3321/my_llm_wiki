---
tags: [ingest, openkb, wiki, github, vectifyai]
date: 2026-06-17
sources:
  - raw/sources/2026-06-17-github-vectifyai-openkb-readme.md
url: https://github.com/VectifyAI/OpenKB
author: VectifyAI
published: 2026-04-04
note: 공식 GitHub README·저장소 메타. PyTorchKR #10058 요약과 병행 참고.
---

# OpenKB GitHub README (VectifyAI)

> 출처: [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) · Apache 2.0 · Python · ~2.1k★ (2026-06-17) · [[VectifyAI]]

## 한 줄 요약

**[[OpenKB]]** — 문서→**위키 foundation** + **generator**(query·chat·**Skill Factory**) 2계층 CLI. **PageIndex**로 장문 PDF vectorless 검색, **markitdown** 다형식 변환, **LiteLLM** 멀티 프로바이더. Karpathy [[LLM Wiki]] 아이디어의 **공식 구현**.

## 2계층 모델

| 계층 | 역할 | 대표 명령 |
|------|------|-----------|
| **Wiki foundation** | compile·유지 | `init` · `add` · `remove` · `recompile` · `watch` · `lint` |
| **Generators** | wiki→산출물 | `query` · `chat` · **`skill new`** |

전통 RAG는 매 쿼리 **재발견**; OpenKB는 **한 번 컴파일** 후 교차참조·lint·합성이 누적.

## wiki/ 구조 (공식)

`index` · `log` · `AGENTS.md` · `sources/` · `summaries/` · **`concepts/`** · **`entities/`** · `explorations/` · `reports/`

- **concepts/** — 교차 문서 합성
- **entities/** — person·organization·place·product·work·event 등 (PyTorchKR 글에는 없던 레이어)
- 문서 1건 → 보통 **10~15 페이지** 갱신

## 문서 처리

| | 짧은 문서 | 긴 PDF (≥20p, `pageindex_threshold`) |
|--|-----------|--------------------------------------|
| 변환 | markitdown | PageIndex 트리+요약 |
| LLM 입력 | 전문 | **문서 트리** |
| 이미지 | pymupdf inline | PageIndex |

`openkb add`는 **URL** 지원 — PDF vs HTML(trafilatura) 자동 판별.

## Wiki foundation 명령 (README 기준)

- `remove` — wiki·이미지·registry·PageIndex 상태 정리 (`--dry-run`)
- `recompile` — 인덱싱 없이 compile 재실행; **수동 편집 덮어씀** (`--all`, `--refresh-schema`)
- `list` · `status` · `feedback` (GitHub issue)

## Generators

### query · chat

- `query` — 인용 포함 grounded 답변, `--save` → explorations
- `chat` — 멀티턴; `/add` `/skill new` `/save` `/lint` 등 슬래시 명령

### Skill Factory (신규)

`openkb skill new <name> "<intent>"` — wiki 일부를 **Anthropic Skill** 폴더로 distill.

- 출력: `output/skills/<name>/` (`SKILL.md`, `references/`, optional `scripts/`)
- `.claude-plugin/marketplace.json` 자동 갱신
- `skill validate` · `skill eval` · `skill history/rollback`
- Claude Code·Codex·Gemini CLI·**Cursor** 설치 가능

## 설정

`.openkb/config.yaml`: `model`, `language`, `pageindex_threshold`, optional `entity_types`, `extra_headers`.

`.env`: `LLM_API_KEY`, optional `PAGEINDEX_API_KEY` (cloud OCR·대용량).

## 에이전트·Obsidian 연동

- Obsidian: `wiki/` 볼트 + Web Clipper→`raw/`
- Claude Code: `/plugin marketplace add VectifyAI/OpenKB`
- Gemini: `gemini skills install ... --path skills/openkb`
- Codex: `skills/openkb` symlink
- 내장 skill은 **read-only** (add/remove/lint --fix 자동 실행 안 함)

## Karpathy vs OpenKB (공식 표)

| | Karpathy | OpenKB |
|--|----------|--------|
| 장문 | context rot | **PageIndex** |
| 형식 | web clipper .md | PDF·Office·HTML·CSV 등 |
| Q&A | wiki query | wiki + PageIndex retrieval |

## 스택·로드맵

PageIndex · markitdown · OpenAI Agents SDK · LiteLLM · Click · watchdog

로드맵: 비-PDF 장문 · nested folder · concept 계층 인덱스 · DB 엔진 · **Web UI**

## PyTorchKR 글과의 차이

| 항목 | PyTorchKR #10058 | GitHub README |
|------|------------------|---------------|
| entities/ | 미언급 | **공식 레이어** |
| Skill Factory | 없음 | **skill new/validate/eval** |
| remove/recompile | 없음 | **문서·스키마 재컴파일** |
| URL add | 없음 | PDF/HTML 자동 |
| PageIndex Cloud | 없음 | `PAGEINDEX_API_KEY` |

## 관련 위키

- [[OpenKB]] · [[VectifyAI]] · [[LLM Wiki]] · [[obsidian-second-brain]]
- [[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]] — 커뮤니티 요약·CJK·seCall 댓글

## 원본·리소스

- `raw/sources/2026-06-17-github-vectifyai-openkb-readme.md`
- https://github.com/VectifyAI/OpenKB
- PageIndex: https://github.com/VectifyAI/PageIndex
