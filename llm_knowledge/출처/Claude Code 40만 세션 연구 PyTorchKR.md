---
tags: [ingest, anthropic, claude-code, agentic-coding, research, pytorchkr]
date: 2026-06-19
sources:
  - raw/sources/2026-06-19-discuss-pytorchkr-claude-code-40-10794.md
assets:
  - raw/assets/claude_code_40_1.jpeg
  - raw/assets/claude_code_40_2.png
  - raw/assets/claude_code_40_3.png
  - raw/assets/claude_code_40_4.png
  - raw/assets/claude_code_40_5.png
  - raw/assets/claude_code_40_6.png
  - raw/assets/claude_code_40_7.png
  - raw/assets/claude_code_40_8.png
  - raw/assets/claude_code_40_9.png
  - raw/assets/claude_code_40_10.png
url: https://discuss.pytorch.kr/t/anthropic-claude-code-40/10794
author: 9bow(박정환)
published: 2026-06-19
paper_url: https://www.anthropic.com/research/claude-code-expertise
note: PyTorchKR GPT 정리본; 원문 Anthropic 연구 보고서 병행 확인.
---

# Claude Code 40만 세션 연구 (PyTorchKR)

> 출처: [PyTorchKR #10794](https://discuss.pytorch.kr/t/anthropic-claude-code-40/10794) · 9bow · 2026-06-19 · Anthropic [Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise) (2026-06-16)

## 한 줄 요약

Anthropic **~40만** [[Claude Code]] 대화형 세션(23.5만 사용자·7개월) 분석 — **사람=무엇을(plan ~70%)**, **Claude=어떻게(exec ~80%)**. 성공은 **코딩 실력**보다 **과제별 도메인 전문성**; 직군 간 검증 성공률은 **5%p 이내**. *Coding is a leading case.*

![연구 개요](../../raw/assets/claude_code_40_1.jpeg)

## 연구 설계

| 항목 | 내용 |
|------|------|
| 기간 | 2025-10 ~ 2026-04 (7개월) |
| 규모 | ~40만 interactive 세션, ~23.5만 사용자 |
| 도구 | **Clio** (프라이버시 보존 집계 분석) |
| 분류기 | 주로 **Claude Sonnet 4.6** |
| 포함 | CLI, claude.ai, Claude Code 데스크톱 |
| 제외 | headless `claude -p`, 서드파티 IDE 자동화 |

배경: GitHub 에이전트 활동 프로젝트 비율 2025말 이후 **2배+**; Claude Code 사용자 **주당 ~20h** 도구 켜 둠.

## 네 가지 핵심 발견

1. **분업** — 사람은 계획, Claude는 실행; 전문성↑ → 프롬프트당 Claude 행동·출력↑  
2. **직업 < 전문성** — 코딩 세션 검증 성공: SWE ~34% vs 타 직군 ~29% (**5%p**)  
3. **전문성↔성공** — novice 검증 성공 **15%** → intermediate+ **28–33%**; 이득 대부분은 **초보→중급**  
4. **과제 가치↑** — 추정 프리랜스 가치 평균 **+27%**; 디버깅 비중 **33→19%**

> *Coding agents are not substituting for domain expertise—the more understanding a worker brings to an agent, the more quality work the agent is able to do.*

## 9가지 작업 모드

| 모드 | 비중 | |
|------|------|--|
| fixing | 26% | |
| building | 25% | |
| operating | 17% | |
| communicating | 10% | |
| understanding / planning | 각 7% | |
| orchestrating / analyzing | 각 3% | |
| testing | 2% | |

코드 직접 다루기(build+fix+test+orch) **~56%**. **48%** 기존 코드 수정, **14%** greenfield, **~20%** 코드베이스 미접촉.

![9 work modes](../../raw/assets/claude_code_40_2.png)

## 분업·위임

- 평균 **~4 turns**/세션; 프롬프트 1개 → **~10 actions**, **~2,400 words** 출력  
- *People decide what to build, and the agent decides how to build it.*

![plan vs exec decisions](../../raw/assets/claude_code_40_3.png)

## [[도메인 전문성 (에이전틱 코딩)|도메인 전문성]] (과제별)

5단계(novice→expert): 지시 정밀도·검증 요청·누가 누구를 교정하는지. **직책과 무관·task-specific** — Rust 처음인 시니어 SWE는 Rust에선 novice; 도메인 규칙을 아는 비개발자는 그 과제에선 expert.

| 수준 | 프롬프트당 actions | 출력(words) |
|------|-------------------|-------------|
| novice | ~5 | ~600 |
| expert | ~12 | ~3,200 |

회귀(통제 변수): 전문성 +1단계 → actions **+9%**, output **+13%** (p&lt;0.001).

![expertise vs output](../../raw/assets/claude_code_40_6.png)

## 성공 척도

- **Judged success** — 대화 전체 판정(성공/부분/실패/목표 없음)  
- **Verified success** — 판정 성공 + git·테스트·명시 확인 등 **확실한 증거**

Novice: verified **15%**, partial **77%**. Intermediate+: verified **28–33%**, partial **91–92%**.

곤경(trouble) 후 verified 성공: novice **4%** → expert **15%**; abandoned novice **19%** vs others **5–7%**.

![success by expertise](../../raw/assets/claude_code_40_7.png)

## 직군별

10대 SOC 직군 모두 코딩 세션 verified success가 SWE와 **7%p 이내**. 관리 직군 **37%** vs SWE **34%**(측정 편향 가능).

![occupation success rates](../../raw/assets/claude_code_40_9.png)

## 7개월 트렌드

- fixing **33→19%**; operating **14→21%**; communicating+analyzing **~10→20%**  
- 증폭 vs 대체: **코딩 구현**은 대체 쪽, **도메인 판단·검증·steering**은 증폭

![task composition shift](../../raw/assets/claude_code_40_8.png)

## 한계·시사

- 실제 배포·폐기·경제 가치 **미측정**; non-interactive 사용 **제외**  
- 분류기·모델 해석 의존 (텔레메트리와 교차검증은 일치)  
- **개발자 시사**: 차별화 → *무엇을 왜 풀지* + 에이전트 **검증·조종**; 코딩은 다른 지식 노동의 **선행 사례**

## 관련 위키

- [[Claude Code]] · [[Anthropic]] · [[에이전틱 코딩]] · [[도메인 전문성 (에이전틱 코딩)]]
- [[루프 엔지니어링]] · [[HarnessX]] · [[PyTorchKR]]

## 원본

- `raw/sources/2026-06-19-discuss-pytorchkr-claude-code-40-10794.md`
