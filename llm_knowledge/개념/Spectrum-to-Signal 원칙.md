---
tags: [concept, training, reasoning, slm]
sources:
  - wiki/출처/VibeThinker-3B 소형 추론 모델 PyTorchKR.md
---

# Spectrum-to-Signal 원칙

**Spectrum-to-Signal Principle (SSP)** — [[Weibo AI]] VibeThinker 계열의 사후 학습 철학. SFT에서 **다양한 풀이 경로(스펙트럼)** 를 넓게 펼친 뒤, RL에서 **올바른 추론(신호)** 만 증폭한다.

## 직관

- 단일 정답 모방 SFT만으로는 RL 탐색 여지가 좁음
- 팔레트에 색을 넓게 펼쳐 두듯, **의도적 다양성** → 이후 강화학습이 신호를 선택·증폭

## VibeThinker-3B 파이프라인 (4단계)

1. **2단계 커리큘럼 SFT** — 쿼리 확장·다중 경로 증류·품질 필터; 2단계는 긴 추론(5K+ 토큰) 위주
2. **다중 도메인 RL (MGPO)** — Math → Code → STEM; on-policy; 64K 단일 컨텍스트
3. **오프라인 자기 증류** — learning-potential score로 교사 궤적 선별
4. **Instruct RL** — 사용자 지시·형식 정렬

## MGPO (MaxEnt-Guided Policy Optimization)

VibeThinker-1.5B에서 도입, 3B에서 계승.

- 프롬프트별 G회 롤아웃 → 경험적 정확도 \(p(q)\)
- \(p(q)\approx 0\) (너무 어려움) · \(p(q)\approx 1\) (포화) 보다 **중간 난이도**에 가중치
- \(w(q)=\exp(-\gamma D_{\mathrm{ME}}(p(q)\|p_0))\), \(p_0=0.5\) — 최대 엔트로피 근처 집중

## Long2Short (3B 차별)

- 1단계 MGPO로 정확도 확보 → 2단계에서 **정답 궤적 간** 길이 인식 보상 재분배 (영합 zero-sum)
- 짧고 정확한 풀이 선호; \(\lambda=0.2\)

## 3B vs 1.5B RL 설계 차이

- **점진적 컨텍스트 확장**(DeepScaleR 등)은 3B에서 **역효과** — 엄격한 SFT 품질 하에 높은 절단이 긴 추론 행동을 손상
- 3B는 **처음부터 64K** RL

## 관련

- [[VibeThinker-3B]] · [[Weibo AI]] · [[추론-지식 분리]] · [[CLR]]
- [[출처/VibeThinker-3B 소형 추론 모델 PyTorchKR]]
