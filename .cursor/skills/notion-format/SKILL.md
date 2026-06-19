---
name: notion-format
description: >-
  Formats Notion pages with callouts, headings, dividers, and reference links.
  Use when creating or rewriting Notion pages (IT Issue, 스터디, add_it,
  update_notion, Notion MCP patch-block-children). Project-local skill for
  this vault only (.cursor/skills/).
disable-model-invocation: false
---

# Notion 문서 포맷

Notion MCP로 페이지·본문을 작성·갱신할 때 **아래 템플릿**을 따른다.  
IT Issue(`add_it`), 스터디 DB, 기타 Notion 페이지 모두 동일.

## 페이지 메타

1. **아이콘** — 주제에 맞는 emoji (`patch-page` → `icon.emoji`)
2. **커버** (선택) — `patch-page` → `cover.external.url` (Unsplash 등)
3. **제목** — DB `title` / `이름` 속성. 비우지 않음.

## 본문 구조 (순서)

| # | 블록 | 용도 |
|---|------|------|
| 1 | **callout** (blue_background, 💡) | 한 줄 요약 |
| 2 | **divider** | |
| 3 | **heading_2** 📚 참고 문서 | 출처·링크 목록 (있으면 상단 배치) |
| 4 | bulleted_list_item × N | **볼드 라벨** + 설명 + 클릭 URL |
| 5 | **divider** | 섹션 구분 |
| 6 | **heading_2** ✨/🔧/⚖️ + 번호·제목 | 대주제 (Loop Agent, 루프 엔지니어링 등) |
| 7 | paragraph / callout / bullets | 본문 |
| 8 | **heading_3** 1️⃣/2️⃣ | 소주제 |
| 9 | **callout** (gray_background) | 활용 예·개념 카드 |
| 10 | **callout** (red_background) | 주의·중지·한계 |
| 11 | **callout** (purple/yellow_background) | 핵심 정의·비교 |
| 12 | paragraph (italic) | `작성일: YYYY-MM-DD · …` |

## 참고 문서 섹션 (필수 — URL 있으면)

- GeekNews, 원문, Notion 스터디, Wiki 경로, 스킬 경로 등 **모든 참고 URL** 포함
- 형식: **볼드 라벨** · 설명 → `link.url` 로 클릭 가능하게
- 로컬 경로만 있는 항목은 `code` annotation

```json
{
  "type": "bulleted_list_item",
  "bulleted_list_item": {
    "rich_text": [
      { "type": "text", "text": { "content": "GeekNews #30336" }, "annotations": { "bold": true } },
      { "type": "text", "text": { "content": " — 루프 엔지니어링 → " } },
      { "type": "text", "text": { "content": "https://news.hada.io/topic?id=30336", "link": { "url": "https://news.hada.io/topic?id=30336" } } }
    ]
  }
}
```

## 강조 규칙

- **볼드** — 라벨, 핵심 용어
- `code` — 명령, 경로, sentinel (`/loop`, `SKILL.md`)
- *이탤릭* — 슬로건, 작성일, 보조 설명

## 콜아웃 색·아이콘 가이드

| color | icon 예 | 용도 |
|-------|--------|------|
| blue_background | 💡 | 상단 한 줄 요약 |
| gray_background | 📊 ✅ 🔁 🧠 | 활용 예, inner/outer 루프 |
| red_background | 🛑 | 중지, 위험, 한계 |
| purple_background | 🎯 | 핵심 정의 |
| yellow_background | 🔀 | 비교·대조 |

## MCP 블록 타입

`patch-block-children` / `post-page` children:

- `callout`, `divider`, `heading_2`, `heading_3`, `paragraph`, `bulleted_list_item`

한 번에 15블록 이하로 나눠 append. paragraph 2000자 초과 시 분할.

## 기존 페이지 갱신 시

전체 워크플로: **`update-notion` 스킬** (`.cursor/skills/update-notion/SKILL.md`).

1. `retrieve-page-markdown` — 현재 본문 확인
2. **`update-page-markdown` · `replace_content`** (기본) — notion-format으로 전체 재작성
3. 덧붙이기만 요청 시 — `patch-block-children` append
4. `patch-page` — icon·cover + connection 쓰기 검증

## 참고 예시

- IT Issue: https://app.notion.com/p/382c47eae79381c0af5ce07d79a63a55
- 스터디 · 루프 에이전트: https://app.notion.com/p/380c47eae79381c8a60fed98360ada7b

## Done when

- 상단 요약 callout + (URL 있으면) 참고 문서 섹션
- heading/divider/callout로 시각 계층
- 참고 URL 클릭 가능
- 페이지 URL 사용자에게 전달
