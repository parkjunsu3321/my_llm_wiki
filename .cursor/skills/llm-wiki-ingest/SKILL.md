---
name: llm-wiki-ingest
description: >-
  LLM Wiki ingest — URL·문서를 raw/sources에 저장하고 wiki(출처·개념·엔티티·index·log)를
  갱신한 뒤 git commit·push로 GitHub에 동기화. 사용자가 ingest·흡수·위키에 추가·URL 넣어줘
  등을 요청할 때 사용.
---

# LLM Wiki Ingest

Karpathy [[LLM Wiki]] 패턴. 위키 루트: `llm_knowledge/`. Git 저장소 루트: `my_llm_wiki/` (한 단계 상위).

## 레이아웃

| 레이어 | 경로 | 규칙 |
|--------|------|------|
| 원본 | `llm_knowledge/raw/sources/` | immutable; **HTML 덤프 금지** — 본문 텍스트만 |
| 첨부 | `llm_knowledge/raw/assets/` | 이미지 등; 덮어쓰기 금지 |
| 위키 | `llm_knowledge/{출처,개념,엔티티}/` | LLM 생성·유지 |
| 색인 | `llm_knowledge/index.md`, `log.md` | ingest 후 **반드시** 갱신 |

## Ingest 절차

1. **원본 확보** — URL fetch 또는 사용자 파일. HTML이면 article 본문만 추출.
2. **raw 저장** — `llm_knowledge/raw/sources/YYYY-MM-DD-{slug}.md`
3. **출처 페이지** — `llm_knowledge/출처/{제목}.md` (frontmatter: tags, date, sources, url, author, published, note)
4. **개념·엔티티** — 새 주제면 생성, 기존이면 **갱신·교차 링크**
5. **index.md** — 개요·출처 요약·개념·엔티티 섹션 반영
6. **log.md** — append-only: `## [YYYY-MM-DD] ingest | {한 줄 설명}`
7. **GitHub sync** — 아래 절차 **필수** (ingest 완료의 일부)

## GitHub sync (ingest 후 필수)

ingest로 변경·추가된 파일만 커밋하고 `origin/main`에 push한다.

### Git 실행 (Windows)

PATH에 `git`이 없을 수 있다. 먼저 PATH, 없으면 전체 경로:

```powershell
$git = if (Get-Command git -ErrorAction SilentlyContinue) { "git" } else { "C:\Program Files\Git\cmd\git.exe" }
Set-Location "C:\Users\JUNSOO\Desktop\my_llm_wiki"   # repo root
```

### 커밋·push

```powershell
& $git add llm_knowledge/raw/ llm_knowledge/출처/ llm_knowledge/개념/ llm_knowledge/엔티티/ llm_knowledge/index.md llm_knowledge/log.md
# 교차 링크로 갱신된 다른 wiki 파일도 git status로 확인 후 add

& $git commit -m "ingest | {제목} ({출처 식별})"
& $git push origin main
& $git status
```

### 커밋 메시지 형식

- `ingest | OpenKB PyTorchKR #10058`
- `ingest | token-router GeekNews #30547`
- `ingest-fix | …` — raw/sources 수정 등

### 제외

- **`llm_knowledge/.obsidian/`** — 로컬 Obsidian 설정; 커밋하지 않음
- `.env`, credentials — 절대 커밋 금지

### log.md

GitHub sync 성공 시 log 항목 끝에 `, GitHub sync` 추가 (예: 기존 ingest 로그 패턴).

### 실패 시

- push 실패 → 원인(인증·네트워크·충돌) 보고; rebase/force push는 사용자 요청 없이 하지 않음
- 커밋할 변경 없음 → push 생략하고 사용자에게 알림

## 출처 페이지 템플릿

```markdown
---
tags: [ingest, ...]
date: YYYY-MM-DD
sources:
  - raw/sources/...
url: ...
author: ...
published: ...
note: PyTorchKR/GeekNews 등 GPT 정리 글일 경우 명시
---

# {제목}

> 출처: [링크](url) · 작성자 · 날짜

## 한 줄 요약
...
```

## 품질

- wikilink `[[개념/...]]`, `[[엔티티/...]]` 적극 연결
- 기존 페이지와 **중복 개념 통합** (새 페이지 남발 금지)
- ingest 완료 응답에 **커밋 해시·push 결과** 포함
