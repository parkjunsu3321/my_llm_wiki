---
name: add-it
description: >-
  Creates a page in the Notion IT Issue database from user-provided content,
  applies notion-format styling (callouts, headings, reference URLs), verifies
  write access, and returns the page URL. Use when the user runs /add_it,
  add_it, or asks to register an IT issue in Notion. For updating existing
  pages use update-notion instead. Project-local skill for this vault only
  (.cursor/skills/).
disable-model-invocation: true
---

# Add IT Issue (Notion)

`/add_it` 또는 `add_it`로 IT 이슈 내용을 Notion **IT Issue** DB에 페이지로 등록한다.

## Command

`/add_it [내용]`

Examples:

- `/add_it VPN 접속 불가 — 재부팅 후에도 동일`
- `add_it` (직전 대화·붙여넣은 텍스트를 본문으로 사용)

## Config

`.cursor/skills/add-it/config.json`:

| Key | Value |
|-----|-------|
| `databaseId` | IT Issue DB ID |
| `dataSourceId` | IT Issue data source ID |
| `titleProperty` | `이름` (title) |
| `databaseUrl` | DB 링크 |

## Preconditions

1. **Notion MCP** 연결이 IT Issue DB에 접근 가능해야 한다. (DB가 MCP integration과 공유되어 있어야 함)
2. **권한 상속 (1회 설정 권장):** Notion에서 IT Issue DB → **Share** → 워크스페이스 전체 **Can edit**.  
   Notion API는 **사용자/그룹별 페이지 공유 권한을 프로그래밍으로 부여할 수 없다.**  
   DB가 워크스페이스 편집 권한으로 공유되어 있으면, 새로 만든 하위 페이지도 멤버가 편집할 수 있다.
3. MCP connection이 DB에 **Read + Insert + Update content** capability를 갖도록 Developer portal에서 설정한다.

## Workflow

When invoked:

1. **Read** `config.json`.
2. **Parse input**
   - 사용자가 제목을 명시했으면 그대로 사용.
   - 없으면 본문 첫 줄(또는 첫 80자)을 제목으로, 나머지를 본문으로.
   - 본문이 없고 한 줄만 있으면 제목만 채우고 본문 블록은 생략 가능.
3. **Read** `.cursor/skills/notion-format/SKILL.md` — 본문은 **Notion 포맷 템플릿**으로 작성 (plain paragraph 나열 금지).
4. **Create page** — Notion MCP `post-page`:
   - `parent`: `{ "database_id": "<databaseId>" }`
   - `properties`: `{ "이름": { "title": [{ "text": { "content": "<title>" } }] } }`
   - `icon` / `cover`: `patch-page`로 설정 (notion-format 참고)
   - 본문: `patch-block-children`으로 callout · divider · heading_2/3 · bullets · 참고 URL 섹션 append
5. **Grant / verify edit access** (API 한계 내에서 최대한 수행):
   - **Connection 권한:** DB parent가 integration과 공유되어 있으면 **자식 페이지는 connection에 자동 상속**된다. 별도 API 호출 불필요.
   - **쓰기 확인:** `retrieve-a-page`로 생성된 `page_id` 조회 후, `patch-page`로 무해한 갱신(예: `icon` emoji `📋`)을 시도해 connection의 **수정 권한**을 검증한다. 실패 시 사용자에게 DB connection 공유 상태를 안내한다.
   - **사용자 편집 권한:** 위 Preconditions 2(DB 워크스페이스 Can edit)에 의존. API로 사용자 invite 불가 — 미설정이면 사용자에게 1회 UI 설정을 안내한다.
6. **Respond** with:
   - 생성된 페이지 제목
   - Notion URL (`url` 필드)
   - 권한 상태 한 줄 (connection 쓰기 OK / DB 공유 설정 확인 필요)

## Body format

본문 블록·색상·참고 URL 형식은 **`notion-format` 스킬**을 따른다.

필수 포함:
- 💡 blue callout (한 줄 요약)
- 📚 참고 문서 (URL 있으면 link annotation)
- 섹션별 heading_2 + divider
- 활용 예/주의는 gray·red callout

## Rules

- 제목(`이름`)은 비우지 않는다. 비어 있으면 `IT Issue YYYY-MM-DD HH:mm` 같은 기본 제목을 쓴다.
- **제목만 채우고 본문 생략 금지** — 내용이 짧아도 notion-format 최소 구조는 유지.
- Notion API로 사용자별 share/invite는 시도하지 않는다 (미지원).
- 페이지 생성 후 URL을 반드시 사용자에게 전달한다.
- 실패 시 Notion 오류 메시지와 함께 DB connection 공유·capability 점검 방법을 안내한다.

## Done when

- IT Issue DB에 새 페이지가 생성되었다.
- Connection이 해당 페이지에 쓰기 가능함을 확인(또는 실패 원인을 보고)했다.
- 사용자에게 페이지 URL과 권한 상태를 전달했다.

## Related

- **기존 페이지 갱신** → `.cursor/skills/update-notion/SKILL.md` (`/update_notion`)
