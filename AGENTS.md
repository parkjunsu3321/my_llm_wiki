# LLM Wiki — 이 Vault 규칙

Karpathy의 [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 패턴을 이 Obsidian Vault에 적용한다.

**실행 절차는 프로젝트 스킬로 분리되어 있다.** Vault 루트의 `.cursor/skills/`:

| 작업 | 스킬 디렉터리 |
|------|----------------|
| 원본 → 위키 반영 | `llm-wiki-ingest` |
| 위키 기반 질문·답변 | `llm-wiki-query` |
| 위키 건강 점검 | `llm-wiki-lint` |
| Notion IT Issue **등록** | `add-it` |
| Notion 페이지 **갱신** | `update-notion` |
| Notion 본문 포맷 | `notion-format` |

사용자가 ingest / 질문 / lint / add_it / update_notion / 노션 정리를 요청하면 해당 스킬을 적용한다. 스킬 라우팅 규칙: `.cursor/rules/llm-wiki-skills.mdc`, `.cursor/rules/notion-skills.mdc`.

## 디렉터리 (세 레이어)

| 레이어            | 경로             | 규칙                                                 |
| -------------- | -------------- | -------------------------------------------------- |
| 원본 (immutable) | `raw/sources/` | 사용자가 넣는 기사·논문·노트 원본. **LLM은 이 안 파일을 수정·삭제하지 않는다.** |
| 첨부             | `raw/assets/`  | 클리핑 이미지 등 원본 보조 파일. LLM이 덮어쓰지 않는다.                 |
| 위키             | `wiki/`        | 요약·개념·엔티티·색인. **LLM이 생성·유지한다.**                    |

Vault 루트의 다른 경로는 기본적으로 수정하지 않는다.

## 필수 파일

- `wiki/index.md` — 카테고리별 목록 + 링크 + 한 줄 요약(선택: 날짜, 출처 수).
- `wiki/log.md` — append-only. 형식:

```markdown
## [YYYY-MM-DD] ingest | 문서 제목
## [YYYY-MM-DD] query | 한 줄 요약
## [YYYY-MM-DD] lint | 한 줄 요약
```

## 위키 작성 규칙

- Obsidian 호환 마크다운, 내부 링크 `[[…]]`는 Vault 설정에 맞출 것.
- 새 페이지 파일명은 Vault 안에서 한 스타일로 통일(한글 제목 허용, 특수문자 최소화).
- 선택: YAML frontmatter(`tags`, `date`, `sources` 등).

## 사용자 역할

원본 큐레이션, 질문 방향, 강조점 결정. 교차 참조·색인·일괄 갱신은 LLM이 담당.
