# PROTOCOL-AGENT2

## 목적

이 문서는 승인된 에이전트 추상화 확장을 기록한다.
다중 에이전트 조직은 역할 흐름 외에도 Agent Contract, Capability/Permission Matrix, Shared Agent State, Agent Logs를 명확하게 가진다.

## 1. Agent Contract

모든 Agent는 공통적으로 다음 추상 필드를 가진다.

```text
agent_id
role
capability
permission
input_schema
output_schema
allowed_channels
blocked_channels
state_reference
trace_id
```

공통 입력은 다음과 같다.

- 사용자 요청 또는 정규화된 목표
- 프로젝트 상태 요약
- 관련 Task 컨텍스트
- 관련 Protocol 컨텍스트
- 허용된 Permission 범위

공통 출력은 다음과 같다.

- task_id
- agent_id
- summary
- changes
- verification evidence
- remaining risks
- issues
- artifacts

## 2. Capability와 Permission 분리

Capability는 Agent가 기술적으로 수행할 수 있는 능력이다.
Permission은 실제로 해당 프로젝트에서 허용되는 행동 범위이다.

예:

```text
Developer
Capability:
- 파일 읽기
- 파일 수정
- 테스트 실행

Permission:
- /root/** 읽기 허용
- /root/agents/** 쓰기 허용
- /root/protocol/** 읽기 허용
- /root/state/** 쓰기 허용
- production 배포 금지
- 외부 API Key 접근 금지
```

역할별 관점:

```text
Role           Capability                       Permission
Secretary      receive/report                  user interface only
Orchestrator   plan/decompose/assign/verify    workflow orchestration only
Planner        requirements decomposition      project planning scope
Researcher    information gathering          internal docs and public facts only
Developer      code implementation             repository files inside allowed scope
Tester         verification execution          allowed test scope only
Reviewer       review and acceptance check     review evidence only
Security       review risks                     restricted access to security evidence
Documenter     documentation generation        doc and artifact write scope
```

## 3. Shared Agent State

Agent는 실행 시 다음 상태를 참조할 수 있다.

```text
project_id
project_name
goal
requirements
constraints
decisions
current_tasks
completed_tasks
artifacts
issues
risks
```

추가로 다음 상태 정보도 포함할 수 있다.

```text
conversation history
project state
relevant task state
protocol version
verification evidence
```

중요 원칙:

- 전체 대화 기록을 한 번에 Agent에게 전달하지 않는다.
- Project State는 Conversation History와 별도로 관리한다.
- Agent는 필요한 최소 상태만 참조한다.

## 4. Agent Logs

Agent의 수행 기록은 다음 항목을 기준으로 남긴다.

```text
message_id
task_id
trace_id
sender
receiver
message_type
status
timestamp
payload_summary
verification_note
```

기본 로그 흐름:

```text
Secretary request
Orchestrator assignment
Specialist result
Orchestrator verification
Secretary report
```

## 5. 통신 제약

```text
User -> Secretary Agent
Secretary Agent -> Orchestrator Agent
Orchestrator Agent -> Specialist Agent
Specialist Agent -> Orchestrator Agent
Orchestrator Agent -> Secretary Agent
Secretary Agent -> User
```

기본 원칙:

- User는 Specialist에게 직접 지시하지 않는다.
- Specialist는 사용자에게 직접 응답하지 않는다.
- Specialist는 기본적으로 Specialist끼리 직접 통신하지 않는다.
- Agent는 검증된 결과만 완료로 보고한다.
