---
name: update-notion
description: >-
  Updates existing Notion pages via MCP: find page by URL/title/search, read
  current markdown, apply notion-format, replace or patch content, verify write
  access, return page URL. Use when the user runs /update_notion, update_notion,
  asks to update/refresh Notion content, 노션 업데이트, 노션 갱신, or 노션 내용
  수정 (distinct from add_it which creates new IT Issue pages). Project-local
  skill for this vault only (.cursor/skills/).
disable-model-invocation: true
---

# Update Notion Page

기존 Notion 페이지 **본문·메타를 갱신**한다. 새 IT Issue **생성**은 `add-it` 스킬을 사용한다.

## Command

`/update_notion [대상] [내용/지시]`

Examples:

- `/update_notion 루프 에이전트 관련 내용 업데이트` — 검색 후 전체 갱신
- `/update_notion https://app.notion.com/p/382c47ea… PyTorchKR 반영`
- `update_notion` (직전 대화·ingest 결과를 본문 소스로 사용)
- `노션 IT Issue 루프 엔지니어링 페이지 갱신해줘`

## Config

`.cursor/skills/update-notion/config.json`:

| Key | 용도 |
|-----|------|
| `itIssueDatabaseId` | IT Issue DB (검색 힌트) |
| `studyDatabaseId` | 스터디 DB (검색 힌트) |
| `addItConfigPath` | `add-it` config 참조 |
| `notionFormatSkillPath` | 포맷 스킬 경로 |

## Preconditions

1. **Notion MCP** — 대상 페이지가 integration과 **공유**되어 있어야 한다.
2. Connection capability: **Read + Update content** (필요 시 Insert).
3. 사용자 편집 권한은 DB/페이지 **워크스페이스 Can edit** 공유에 의존 (`add-it`과 동일).

## Workflow

When invoked:

1. **Read** `config.json` · **`.cursor/skills/notion-format/SKILL.md`** (본문 구조 필수).
2. **Resolve target page** (우선순위):
   - 사용자가 **Notion URL** 또는 `page_id`(UUID) 제공 → 해당 페이지
   - 사용자가 **제목·키워드** 제공 → `post-search`로 검색, 후보 1건 선택 (복수면 사용자에게 확인)
   - `/add_it` 직후·명시적 “방금 페이지” → 직전 `page_id` 재사용
   - IT Issue·스터디 문맥 → 검색 쿼리에 DB 힌트 포함
3. **Read current state** — `retrieve-page-markdown` (`page_id`).
   - 갱신 전 기존 구조·참고 URL·작성일 파악
   - 사용자가 “덧붙이기”만 요청한 경우 전체 replace 하지 않음
4. **Choose update mode**

| 사용자 의도 | MCP | 동작 |
|-------------|-----|------|
| 업데이트·갱신·정리·반영 (기본) | `update-page-markdown` · `type: replace_content` | notion-format으로 **전체 본문 재작성**; 기존 유용 섹션은 병합 |
| 일부 수정·섹션 추가 | `update-page-markdown` · `type: update_content` | `content_updates` find-and-replace (최대 100건) |
| 덧붙이기·append | `patch-block-children` | 기존 children 유지, 하단 append |
| 제목만 | `patch-page` · `properties` | DB title / `이름` 속성 |

**기본값은 `replace_content`.** 사용자가 “일부만”“append”를 명시하지 않으면 전체 갱신.

5. **Write content** — `notion-format` 준수:
   - 💡 blue callout 한 줄 요약 (갱신 사유·날짜 반영)
   - 📚 참고 문서 — **클릭 가능 URL** + Wiki·스킬 `code` 경로
   - heading_2/3 · divider · gray/red/purple/yellow callout
   - 하단 *작성일: YYYY-MM-DD · …* (갱신일 표기)
6. **Patch meta** (필요 시) — `patch-page`: `icon.emoji`, `cover.external` (주제 유지 또는 개선).
7. **Verify write access** — `patch-page`로 무해한 icon 갱신 시도 → connection 쓰기 OK 확인.
8. **Respond** with:
   - 페이지 제목
   - Notion URL
   - 갱신 모드 (replace / patch / append)
   - 권한 상태 한 줄

## Content sources

갱신 본문 소스 우선순위:

1. 사용자가 붙인 텍스트·명시적 지시
2. 직전 대화 (ingest·query·정리 결과)
3. LLM Wiki `wiki/` 페이지 (Vault ingest 후 Notion 동기화 시)
4. 기존 Notion markdown + 변경분 병합

Wiki → Notion 동기화 시 `wiki/출처/`·`wiki/개념/` frontmatter의 `url`, `sources`를 참고 문서에 반영.

## MCP notes

- **`update-page-markdown`** — enhanced Markdown (`<callout>`, `---`, `##`). 대부분의 IT Issue·스터디 갱신에 **권장**.
- **`patch-block-children`** — append·레거시 블록 JSON 필요 시. 15블록 단위 분할.
- **`delete-a-block`** — replace 대신 children 전부 교체할 때만 (비권장; replace_content가 단순).
- 403/404 → integration 공유·capability 안내. 429 → 잠시 후 재시도.

## Rules

- **새 IT Issue 페이지 생성 금지** — 생성 요청이면 `add-it`으로 라우팅.
- plain paragraph 나열 금지 — `notion-format` 최소 구조 유지.
- 참고 URL은 **link annotation** 필수.
- 검색 결과가 **2건 이상**이고 모호하면 사용자에게 선택 요청 (임의 덮어쓰기 금지).
- 갱신 후 **URL 필수 전달**.
- Notion API로 사용자별 share/invite 시도하지 않음 (미지원).
- 기존 참고 문서·핵심 섹션은 **삭제하지 말고 병합** (replace 시에도).

## add-it vs update-notion

| | add-it | update-notion |
|---|--------|---------------|
| 대상 | IT Issue DB **신규** 페이지 | **기존** 페이지 |
| 트리거 | `/add_it`, IT issue 등록 | `/update_notion`, 노션 업데이트·갱신 |
| 본문 | `post-page` + blocks | `update-page-markdown` (기본) |

## Done when

- [ ] 대상 `page_id` 확인됨
- [ ] 갱신 전 `retrieve-page-markdown`으로 현재 내용 확인
- [ ] notion-format 구조로 본문 반영
- [ ] connection 쓰기 검증 (또는 실패 원인 보고)
- [ ] 사용자에게 URL·갱신 요약 전달

## Example (replace_content)

```
1. post-search query="루프 에이전트"
2. retrieve-page-markdown page_id=382c47ea-...
3. update-page-markdown type=replace_content
   - 상단 callout에 "PyTorchKR #10796 반영" 추가
   - 참고 문서에 discuss.pytorch.kr URL
   - DPEVI·Open/Closed 섹션 추가
4. patch-page icon 🔁 (write verify)
5. Respond URL
```
