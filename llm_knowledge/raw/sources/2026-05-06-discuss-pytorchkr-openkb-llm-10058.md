# OpenKB: LLM이 문서를 자동으로 위키 형태의 지식 베이스로 컴파일하는 오픈소스 도구

- URL: https://discuss.pytorch.kr/t/openkb-llm/10058
- 게시판: 읽을거리&정보공유
- 태그: rag, wiki, document-retrieval, knowledge-base, llm, python, wiki-style
- 작성: 9bow(박정환), 2026-05-06 06:30
- GitHub: https://github.com/VectifyAI/OpenKB

---

## OpenKB 소개

Andrej Karpathy는 LLM이 문서를 그때그때 검색하는 것을 넘어, 지식을 일종의 위키(wiki)로 지속적으로 컴파일하고 업데이트하는 방식이 훨씬 강력할 것이라고 이야기한 바 있다. 전통적인 RAG(Retrieval-Augmented Generation) 방식은 매 쿼리마다 지식을 새로 발견한다. 이전에 분석한 내용이 축적되지 않고, 여러 문서에 걸친 교차 참조도 자동으로 만들어지지 않으며, 모순도 감지되지 않는다.

OpenKB는 이 아이디어를 실현한 오픈소스 커맨드라인 도구다. PDF, Word, Markdown, PowerPoint, HTML, Excel 등 다양한 형식의 문서를 투입하면, LLM이 그 문서들을 요약 페이지, 개념 페이지, 교차 참조가 있는 위키 형태의 지식 베이스로 자동 컴파일한다. 한 번 컴파일된 지식은 이후 쿼리에서 재발견 없이 바로 활용되며, 새 문서가 추가될 때마다 기존 위키가 풍부해지는 누적 구조를 가진다. LiteLLM을 통해 OpenAI, Claude, Gemini 등 다양한 LLM 프로바이더를 지원하며, 생성된 위키는 순수 마크다운 파일이라 Obsidian 등 로컬 도구에서도 열 수 있다.

OpenKB의 특징적인 점은 짧은 문서와 긴 문서를 다르게 처리한다는 것이다. 짧은 문서는 전체 텍스트를 LLM이 직접 읽지만, 20페이지 이상의 긴 PDF는 PageIndex 트리 인덱싱을 사용해 계층적 요약 트리를 만들고 LLM이 전체 텍스트 대신 트리를 읽는다. 덕분에 수백 페이지짜리 기술 문서도 정확하게 처리하면서 컨텍스트 창 제한을 우회할 수 있다.

## OpenKB의 아키텍처

```
raw/  # <- 다양한 문서들이 위치하는 곳
 │
 ├─ 짧은 문서 ──→ markitdown ──→ LLM이 전체 텍스트 읽기
 │                                     │
 ├─ 긴 PDF ──→ PageIndex ────→ LLM이 문서 트리 읽기
 │                                     │
 │                                     ▼
 │                          위키 컴파일 (LLM 사용)
 │                                     │
 ▼                                     ▼
wiki/
 ├── index.md            지식 베이스 개요
 ├── log.md              운영 타임라인
 ├── AGENTS.md           위키 스키마 (LLM 지침)
 ├── sources/            전문 변환본
 ├── summaries/          문서별 요약
 ├── concepts/           교차 문서 합성  ← 핵심
 ├── explorations/       저장된 쿼리 결과
 └── reports/            린트 리포트
```

문서 하나가 추가될 때 LLM은 요약 페이지를 생성하고, 기존 개념 페이지들을 읽어 새 지식으로 업데이트하거나 새 개념 페이지를 만들며, 인덱스와 로그를 갱신한다. 문서 하나가 보통 10~15개의 위키 페이지에 영향을 미치며, 각 문서가 고립된 섬이 아니라 전체 지식 그래프의 일부로 연결된다.

## OpenKB의 주요 기능

- **다양한 형식 지원**: PDF, Word(.docx), Markdown, PowerPoint, HTML, Excel, 일반 텍스트를 markitdown을 통해 처리. 이미지, 표, 그림도 네이티브 멀티모달로 추출·이해.
- **위키 컴파일**: LLM이 여러 문서를 아우르는 요약, 개념 페이지, 교차 링크를 자동 관리. 시간이 지날수록 지식이 풍부해지는 누적 구조.
- **쿼리와 대화**: `openkb query`로 일회성 질문, `openkb chat`으로 멀티턴 대화. 세션 저장·재개 가능.
- **Lint 건강 검사**: `openkb lint` — 모순, 공백, 고아 페이지(orphan), 오래된 콘텐츠 탐지.
- **감시 모드**: `openkb watch` — `raw/` 모니터링 후 새 파일 추가 시 자동 위키 업데이트.
- **Obsidian 호환**: `[[wikilinks]]` 포함 순수 마크다운; Obsidian 그래프 뷰·브라우징 가능.

## OpenKB 설치 및 사용법

```bash
# 설치
pip install openkb

# 지식 베이스 초기화
mkdir my-kb && cd my-kb
openkb init

# 문서 추가 및 위키 컴파일
openkb add paper.pdf
openkb add ~/papers/        # 디렉토리 전체 추가
openkb add research.docx

# LLM API 키 설정 (.env)
# LLM_API_KEY=your_api_key
# init 시 또는 .openkb/config.yaml에서 모델 지정
# 예: anthropic/claude-sonnet-4-6, gpt-5.4
```

```bash
# 질문하기
openkb query "이 논문들의 주요 발견은 무엇인가요?"

# 답변을 위키에 저장
openkb query "트랜스포머 아키텍처의 핵심 혁신은?" --save

# 대화형 채팅 (세션 유지)
openkb chat
openkb chat --resume

# 지식 베이스 건강 검사
openkb lint

# 자동 업데이트 모드
openkb watch
```

```python
from openkb import KnowledgeBase

kb = KnowledgeBase("./my-kb")
kb.add("research_paper.pdf")
answer = kb.query("이 논문의 핵심 방법론은?")
session = kb.chat()
session.ask("이전 질문과 연결해서 설명해줘")
```

## 더 읽어보기 (글 내 링크)

- Graphify — 코드베이스 지식 그래프
- Cognee — 지식 그래프 + 벡터 검색
- RAG Web UI — RAG KB 웹 UI
- WeKnora — 텐센트 LLM 문서 이해·RAG
- ApeRAG — GraphRAG + 멀티모달
- Advanced RAG Cookbooks (Athina.AI)
- Karpathy LLM 심층 분석 영상
- legalize-kr — 법령·판례 Git 정리

## 커뮤니티 댓글 (요약)

- **d9ng**: 해외 llm wiki 구현체의 약점은 CJK 형태소 검색(토크나이저 부재). OpenKB는 다문서 형식 지원이 장점. 한국어 llm wiki로는 seCall(hang-in)이 현재까지 가장 나음.
- **Cyp**: 벡터 DB RAG 문제를 크게 개선할 여지. 완전 대체는 아니나 공존·응용 가능.
- **requests.selenium**: 추상적 설명보다 구현체를 보니 이해가 쉬움.
- **Honey-Be**: logicutils와의 궁합 궁금.

---

참고: PyTorchKR 게시물은 GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.
