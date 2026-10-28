# Delegate Work

**서브 에이전트 병렬 실행과 작업 위임을 조율하는 에이전트 스킬**입니다. 독립적인 조사·코딩·리뷰를 작업자에게 나누고, 파일 충돌을 방지하며 결과의 근거를 확인합니다.

[English](README.md) · [skills.sh](https://skills.sh/g-hyeong/delegate-work/delegate-work) · [스킬 본문](skills/delegate-work/SKILL.md) · [구체적인 예시](skills/delegate-work/references/examples.md) · [검증 기록](evals/VALIDATION.md)

멀티 에이전트 워크플로의 병렬 조사부터 범위가 명확한 작업 하나의 전체 위임까지 다룹니다. 작거나 서로 얽힌 작업은 직접 처리합니다. 모델 이름과 사고 수준을 고정하지 않고 현재 실행 환경이 실제로 제공하는 선택지에 맞춥니다.

## 설치

스킬을 사용할 프로젝트에서 실행합니다.

```bash
npx skills add g-hyeong/delegate-work --skill delegate-work
```

설치 중 사용할 에이전트를 선택할 수 있습니다. Codex와 Claude Code를 명시하려면 다음과 같이 실행합니다.

```bash
npx skills add g-hyeong/delegate-work --skill delegate-work -a codex -a claude-code
```

기본 설치 범위는 현재 프로젝트입니다. 사용자 전체 설치를 원할 때만 `-g`를 추가하고, 같은 이름의 기존 스킬을 덮어쓰는지 확인하세요. 현재 실행 요건과 옵션은 [설치 도구 문서](https://github.com/vercel-labs/skills#install-a-skill)를 참고하세요.

수동 설치는 `skills/delegate-work/` 폴더 전체를 사용하는 에이전트의 스킬 경로에 복사합니다. 참고자료와 라이선스 파일도 함께 보존합니다.

## 사용 예시

> delegate-work를 사용해서 이 설계안 세 개를 비교해 줘. 실행 환경이 지원하면 독립적인 자료 읽기를 나누고, 근거를 합쳐 하나의 추천으로 정리해 줘.

> delegate-work로 서로 무관한 오류들을 조사해 줘. 작업 범위와 파일 수정 담당을 나누고, 합친 결과가 맞는지 확인해 줘.

한 줄 오타 수정은 직접 처리하는 것이 의도한 동작입니다. 스킬이 있다고 매번 서브 에이전트를 쓰지는 않습니다.

## 주요 판단

- 독립 결과는 병렬로 처리하고, 선행 결과가 필요한 구간은 순차로 진행합니다.
- 크지만 범위가 명확한 작업은 한 작업자에게 통째로 맡길 수 있습니다.
- 가용 모델·사고 수준·맥락 상속 제약은 현재 도구에서 확인합니다. 확인할 수 없는 선택 옵션은 기본값을 따릅니다.
- 필요한 맥락과 권한 범위만 전달하고, 공유 파일은 한 명이 수정합니다.
- 작업자의 완료 선언을 그대로 믿지 않고 원래 요구사항과 검증 근거를 확인합니다.

## 실행 환경과 검증 범위

본문은 Agent Skills 형식의 영어 지침이며 특정 위임 도구 이름에 의존하지 않습니다. `agents/openai.yaml`은 선택적인 Codex UI 메타데이터입니다.

서브 에이전트 도구와 모델 접근 권한은 실행 환경이 제공해야 합니다. 이 스킬은 별도 엔진·API·계정·권한을 추가하지 않습니다. 위임을 지원하지 않는 환경에서는 허용된 작업을 직접 진행합니다.

**설치 가능 여부와 실제 위임 동작은 별개입니다.** 확인한 환경과 결과는 [검증 기록](evals/VALIDATION.md)에 구분해 남깁니다. 모든 에이전트에서의 동작이나 시간·토큰 절감률을 주장하지 않습니다.

## 유지보수

추가 패키지 없이 구조와 로컬 참조를 점검할 수 있습니다.

```bash
python3 scripts/check_package.py
```

[평가 사례](evals/cases.json)는 직접 처리, 작업 의존성, 공유 파일, 제한된 실행 환경, 부족한 검증 근거, 권한 경계를 다룹니다. 모의 판단 사례이며 성능 벤치마크가 아닙니다. 개선 제안에는 실제 문제와 재현 조건을 적고 비밀정보나 개인 대화는 포함하지 마세요.

## 배포와 라이선스

GitHub 저장소가 원본입니다. skills.sh는 CLI 설치 집계를 통해 목록과 순위에 반영합니다. 설치 횟수는 순사용자 수나 실제 작업 성공 횟수가 아닙니다. 기존 `DISABLE_TELEMETRY`, `DO_NOT_TRACK` 설정을 존중합니다. [등재 방식](https://skills.sh/docs/faq)

MIT 라이선스이며, 설치되는 스킬 폴더 안에도 라이선스 사본이 들어 있습니다. 참고한 자료와 적용 한계는 [출처 문서](skills/delegate-work/references/sources.md)에 정리했습니다.
