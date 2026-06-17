# 위키 색인

> LLM이 ingest/query 후 이 파일을 갱신한다. 카테고리 예시: 개요, 출처 요약, 개념, 엔티티, 분석.

## 개요

- [[개념/스펙 주도 개발]] — spec=Context; Context Rot·Spec-kit (출처 5·6·7)
- [[개념/컨텍스트 엔지니어링]] — 무엇을 알려주느냐; SDD·바이브 대비 (출처 7)
- [[개념/에이전틱 코딩]] — AI 코드 생성; SDD 전환 동기 (출처 6)
- [[개념/루프 엔지니어링]] — 5+1 구성요소·/goal; Fable 5 벤치 (출처 3·4)
- [[개념/Claude 프롬프트 엔지니어링]] — Anthropic 공식 가이드; effort·adaptive thinking·에이전트 설계 (출처 2)
- [[개념/ADHD 스킬]] — 코딩 에이전트용 병렬 발산-수렴 아이디에이션 (출처 1)
- [[개념/Spectrum-to-Signal 원칙]] — SLM SFT 스펙트럼→RL 신호; MGPO (출처 8)
- [[개념/추론-지식 분리]] — 검증 가능 추론 vs 개방형 지식; SLM·대형 역할 (출처 8)
- [[개념/LLM Wiki]] — Karpathy raw/wiki 레이어; RAG vs 위키 컴파일; OpenKB·seCall (출처 9·12)
- [[개념/자기 갱신 위키]] — rewrite·reconcile·synthesize; append 한계 (출처 9)
- [[개념/LLMOps]] — 게이트웨이·관측·평가·최적화·실험; 프로덕션 플라이휠 (출처 10)
- [[개념/하이브리드 컨텍스트 라우팅]] — 로컬 triage·원문 slice·클라우드 추론; token-router (출처 11)

## 출처 요약

- [[출처/스펙 주도 개발 SDD tsyang Context Engineering]] — Context Rot·CLAUDE.md vs spec·TDD 비유 (tsyang, ingest 2026-06-15)
- [[출처/iFKakao Agentic Coding 카카오페이 Spec-kit]] — Spec-kit 파이프라인·MCP·팀 SDD 실전 (카카오페이, ingest 2026-06-15)
- [[출처/스펙 주도 개발 SDD GeekNews]] — Fowler SDD; Kiro·Spec-kit·Tessl; MDD·한계 (2025-10-20, ingest 2026-06-15)
- [[출처/Fable 5 루프 설계 GeekNews]] — Parameter Golf·Continual Learning Bench; Fable vs Opus (2026-06-11)
- [[출처/루프 엔지니어링 Addyo GeekNews]] — 5+1·Automations·/goal; build the loop stay the engineer (2026-06-10)
- [[출처/Claude 프롬프트 엔지니어링 Anthropic 가이드 PyTorchKR]] — Opus 4.8·마이그레이션·에이전트 프롬프트 스니펫 (2026-05-30)
- [[출처/ADHD 코딩 에이전트 스킬 PyTorchKR]] — Diverge/Focus, 벤치마크, 설치법 (2026-06-02)
- [[출처/VibeThinker-3B 소형 추론 모델 PyTorchKR]] — 3B 프론티어 추론·SSP·CLR·벤치마크 (2026-06-17)
- [[출처/obsidian-second-brain Obsidian 세컨드 브레인 PyTorchKR]] — 자기 갱신 Vault·43+ 명령·예약 에이전트 (2026-06-16)
- [[출처/TensorZero LLMOps PyTorchKR]] — 통합 게이트웨이·관측·평가·최적화·실험; Rust·OpenAI SDK (2026-06-17)
- [[출처/token-router 하이브리드 컨텍스트 라우터 GeekNews]] — Gemma 2B triage·raw slice·~99% 토큰 절감 (2026-06-17)
- [[출처/OpenKB LLM 위키 지식베이스 PyTorchKR]] — Karpathy 위키 컴파일 CLI; markitdown·PageIndex·lint·watch (2026-05-06, ingest 2026-06-17)
- [[출처/OpenKB GitHub README VectifyAI]] — 공식 README; entities·Skill Factory·recompile·agent 연동 (2026-06-17)

## 개념

### 프롬프트·Claude

- [[개념/Claude 프롬프트 엔지니어링]] — 세대별 default, 기초·도구·에이전트·마이그레이션
- [[개념/effort 파라미터]] — 지능↔토큰 다이얼; xhigh=코딩·에이전트
- [[개념/adaptive thinking]] — 동적 사고; 4.8은 기본 OFF
- [[개념/overtriggering]] — CRITICAL/anti-laziness 보정의 역효과

### 에이전트·루프

- [[개념/스펙 주도 개발]] — spec-first/anchored/as-source, constitution·steering, spec=Context
- [[개념/컨텍스트 엔지니어링]] — 맥락 설계; 프롬프트 엔지니어링과 구분; slice 라우팅
- [[개념/Context Rot]] — 바이브 코딩 맥락 부식
- [[개념/에이전틱 코딩]] — 프롬프트 기반 AI 코딩; 환각·일관성 한계
- [[개념/바이브 코딩]] — 구조 없는 대화형 코딩; SDD 대비
- [[개념/루프 엔지니어링]] — 5+1, /goal·/loop, memory, comprehension debt

### 아이디에이션·추론

- [[개념/ADHD 스킬]] — 조기 수렴 해결, Diverge/Focus
- [[개념/인지 프레임]] — Diverge 단위 관점
- [[개념/Chain-of-Thought]] — 순차 추론; 고착 취약
- [[개념/Tree-of-Thought]] — 트리 탐색; 공유 맥락 한계

### SLM·추론 모델

- [[개념/Spectrum-to-Signal 원칙]] — VibeThinker SFT→RL; MGPO·Long2Short
- [[개념/추론-지식 분리]] — parameter-dense vs expansive
- [[개념/CLR]] — claim-level test-time scaling

### 지식·Obsidian

- [[개념/LLM Wiki]] — Karpathy 3레이어; RAG vs compile; OpenKB·seCall
- [[개념/자기 갱신 위키]] — self-rewriting vs append-only

### LLM 운영

- [[개념/LLMOps]] — 게이트웨이·관측·평가·최적화·실험; 데이터 플라이휠

### 컨텍스트·토큰

- [[개념/하이브리드 컨텍스트 라우팅]] — local triage + raw slice + cloud reasoning

## 엔티티

### SDD 도구

- [[엔티티/Kiro]] — AWS; 3단 MD 워크플로
- [[엔티티/Spec-kit]] — GitHub; Clarify·Analyze·Implement·MCP
- [[엔티티/Tessl]] — spec-anchored/as-source 베타
- [[엔티티/카카오페이 AI 플랫폼]] — AI Platform·Spec-kit 실전 사례
- [[엔티티/tsyang]] — 게임 클라 블로그; SDD·Context Engineering

### Claude·커뮤니티

- [[엔티티/Anthropic]] — Claude 제작사
- [[엔티티/Claude Fable 5]] — Mythos-class; 루프 설계·장시간 작업
- [[엔티티/Claude Managed Agents]] — CMA harness·Outcomes·sandbox
- [[엔티티/Claude Opus 4.8]] — 최상위 모델; literal·effort 중심
- [[엔티티/PyTorchKR]] — 한국 PyTorch 커뮤니티 (출처 6건)
- [[엔티티/TensorZero]] — 오픈소스 LLMOps; 게이트웨이·플라이휠
- [[엔티티/VibeThinker-3B]] — Weibo AI 3B 추론 SLM; AIME·LiveCodeBench
- [[엔티티/Weibo AI]] — VibeThinker 시리즈 연구팀
- [[엔티티/obsidian-second-brain]] — Obsidian 자기 갱신 세컨드 브레인 스킬
- [[엔티티/Eugeniu Ghelbur]] — obsidian-second-brain·The AI Operator
- [[엔티티/Udit Akhouri]] — ADHD 저자
- [[엔티티/adhd-agent]] — ADHD GitHub/npm (MIT)
- [[엔티티/token-router]] — Ollama triage·raw slice; Codex·Claude Code 토큰 절감 (MIT)

### 지식·위키

- [[엔티티/OpenKB]] — VectifyAI; foundation+generator CLI; PageIndex·Skill Factory
- [[엔티티/VectifyAI]] — OpenKB·PageIndex 제작 조직
