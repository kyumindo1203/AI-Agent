# PROTOCOL-AGENT1

## 목적

이 문서는 다중 에이전트 조직에서 각 에이전트 역할의 추상적 분담과 책임 경계를 기록한다.

## 조직 흐름

```text
User -> Secretary Agent -> Orchestrator Agent -> Specialist Agents -> Orchestrator Agent -> Secretary Agent -> User
```

## 에이전트 역할

### Secretary Agent

Secretary Agent는 조직의 단일 사용자 인터페이스 역할을 수행한다.
사용자 요청을 수신하고, 사용자의 의도를 파악하며, 필요한 경우 추가 질문을 하고,
승인 흐름을 관리하며, 최종 결과를 사용자에게 보고한다.

Secretary Agent는 직접 Specialist를 배치하거나 작업을 분해하고, 검증하거나,
재시도 계획을 수립하거나, Specialist 작업을 직접 수행하지 않는다.

### Orchestrator Agent

Orchestrator Agent는 전체 워크플로우를 조율한다.
사용자 목표를 분석하고, 프로젝트 상태를 생성·관리하며, 작업을 분해하고,
Task를 Specialist에게 배분하고, 의존성 순서를 결정하며,
결과 검증, 재시도, 재계획, 완료 판단을 수행한다.

### Specialist Agents

Specialist Agent는 명확한 역할 범위를 가진 전문 에이전트이다.

- Planner
- Researcher
- Developer
- Tester
- Reviewer
- Security
- Documenter

Specialist는 Orchestrator로부터 Task를 받으며, 결과를 Orchestrator에게 제출한다.
기본적으로 사용자에게 직접 응답하지 않으며, Specialist 간 직접 통신도 허용하지 않는다.

## 통신 원칙

```text
Secretary -> Orchestrator
Orchestrator -> Specialist
Specialist -> Orchestrator
Orchestrator -> Secretary
```

기본적으로 Specialist 간 직접 통신은 Orchestrator 중재 없이 허용하지 않는다.

## 제약 사항

- User는 Specialist에게 직접 지시하지 않는다.
- Secretary는 사용자와 조직의 유일한 외부 인터페이스이다.
- Specialist는 자신의 Capability와 Permission 범위를 넘지 않는다.
- 결과는 검증된 경우에만 완료로 보고한다.
- 보안 위험, 사용자 승인 필요, 또는 중요한 리스크가 있는 작업은 Secretary와 Orchestrator를 통해 승인 및 검증 절차를 수행한다.
