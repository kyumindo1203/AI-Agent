# pre-PROTOCOL-README

## 1. 이해한 문서 원칙

현재 워크스페이스에는 다음 두 개의 원칙 문서가 존재한다.

- ReadMe/AGENT_CONSTITUTION.md
- ReadMe/TASK_PROTOCOL.md

이 문서들은 모두 에이전트 조직 운영을 위한 헌법과 통신/작업 프로토콜을 정의한다.

핵심 수용 원칙은 다음과 같다.

1. 사용자에게 최종 결과를 직접 전달하는 것은 기본적으로 비서 Agent가 담당한다.
2. 전문 Agent는 사용자에게 직접 답변하지 않는다.
3. Agent 간 통신은 구조화된 메시지와 Task 기반으로 이루어져야 한다.
4. 모든 작업은 검증을 거쳐야 하며, 중요 결정은 반드시 검증한다.
5. 높은 위험도 또는 비가역적 행동은 반드시 사용자 승인 절차를 거쳐야 한다.
6. 템플릿은 중복 생성하지 않고 최상위 공통 템플릿으로 통합한다.
7. 실패와 불확실성은 숨기지 않고 명시적으로 보고한다.
8. 로그와 감사 기록은 추적 가능성을 확보한다.

---

## 2. 이해한 조직 계층 구조

기본 조직 구조는 다음 계층으로 이해한다.

```text
USER
  ↓
SECRETARY AGENT
  ↓
ORCHESTRATOR AGENT
  ↓
SPECIALIST AGENTS
  ├─ Planner
  ├─ Researcher
  ├─ Developer
  ├─ Tester
  ├─ Reviewer
  └─ Security
```

Secretary Agent는 사용자와 직접 소통하는 통로이며,
Orchestrator Agent는 전체 Task 흐름을 관리하고, 각 Agent에게 작업을 분배한다.
Specialist Agent는 실제 작업만 수행하고 결과를 Orchestrator 또는 Secretary 흐름에 맞게 보고한다.

---

## 3. 이해한 Task 및 Message 프로토콜

Task는 다음 핵심 요소를 가진다.

- task_id
- parent_task_id
- title
- objective
- background
- inputs
- allowed_resources
- constraints
- dependencies
- assigned_agent
- priority
- acceptance_criteria
- expected_output
- status

Message는 다음 기본 구조로 구조화한다.

```json
{
  "message_id": "unique-id",
  "task_id": "task-id",
  "sender": "agent-name",
  "receiver": "agent-name",
  "message_type": "task",
  "priority": "normal",
  "context": {},
  "task": {},
  "constraints": [],
  "expected_output": {},
  "status": "pending"
}
```

메시지 타입은 REQUEST, TASK, RESULT, QUESTION, REPORT, REVIEW_REQUEST,
REVIEW_RESULT, ERROR, APPROVAL_REQUEST, APPROVAL_RESULT, STATUS, CANCEL로 구분한다.

---

## 4. 이해한 제약 사항

다음 항목은 구현을 설계할 때 반드시 반영한다.

1. 파일을 수정하거나 생성할 때 목적을 명확히 해야 한다.
2. 중요한 변경은 기존 상태를 보존할 수 있어야 한다.
3. 위험한 행동은 사용자 승인 절차를 통해서만 실행할 수 있다.
4. 중요 파일 삭제, 대규모 구조 변경, 외부 서비스 실데이터 전송, 비용 발생 API 사용, 계정/인증 정보 변경, 운영 배포, 복구 불가 데이터 변경은 별도 승인 절차가 필요하다.
5. 다른 Agent 권한을 임의로 대여하거나, 초과 권한을 행사할 수 없다.
6. Agent가 불필요한 Agent 호출, 반복적인 작업, 비용 증가, 자원 낭비를 하지 않는다.
7. Agent는 실패 원인, 현재 상태, 시도한 해결 방법, 남은 필요한 항목을 정확히 보고해야 한다.
8. 템플릿은 각 Agent 디렉터리에 중복 생성하지 않고, 최상위 공통 templates로 배치한다.

---

## 5. 설계 방향

문서 원칙에 따라, 최종적으로는 다음 구조를 설계한다.

```text
/workspaces/AI-Agent/
├─ templates/
│  ├─ task/
│  │  └─ task_template.json
│  ├─ message/
│  │  ├─ message_template.json
│  │  ├─ request_template.json
│  │  ├─ result_template.json
│  │  ├─ review_request_template.json
│  │  ├─ review_result_template.json
│  │  ├─ approval_request_template.json
│  │  └─ approval_result_template.json
│  ├─ error/
│  │  └─ error_template.json
│  └─ report/
│     └─ report_template.md
├─ agents/
│  ├─ secretary/
│  ├─ orchestrator/
│  ├─ planner/
│  ├─ researcher/
│  ├─ developer/
│  ├─ tester/
│  ├─ reviewer/
│  └─ security/
├─ protocols/
│  ├─ task_protocol.md
│  ├─ message_protocol.md
│  ├─ review_protocol.md
│  └─ approval_protocol.md
├─ workflow/
│  ├─ planning/
│  ├─ execution/
│  ├─ review/
│  └─ reporting/
├─ logs/
│  ├─ audit/
│  └─ execution/
├─ config/
│  ├─ agent_roles.yaml
│  └─ environment.yaml
└─ README.md
```

핵심 아이디어는 다음과 같다.

- templates는 최상위 공통 템플릿 저장소다.
- 각 Agent는 해당 템플릿을 참조한다. Agent마다 템플릿을 복붙하지 않는다.
- Agent는 자신의 역할별 책임에 맞는 정보만 처리하고, 상위 구조로 메시지와 결과를 반환한다.
- protocols는 문서형 프로토콜 원칙을 기록한다.
- workflow는 실제 실행 경로를 분리한다.
- logs는 추적성과 감사성 확보를 위한 보관 구조다.
- config는 역할 정의와 환경 정의를 보관한다.

---

## 6. 향후 구현 목표

이 문서가 작성된 이후 실제 개발 단계에서는 다음을 수행한다.

1. 최상위 구조를 실제 디렉터리로 생성한다.
2. templates 하위에 필요한 JSON/Markdown 표준 템플릿을 작성한다.
3. 각 Agent 디렉터리에 역할을 기술하는 README를 작성한다.
4. protocols 문서를 설계 구조와 연결한다.
5. workflow와 logs의 기본 흐름을 설계한다.
6. config 파일을 통해 역할 / 환경을 명확히 설정한다.

---

## 7. 현재 상태 메모

현재 워크스페이스에는 ReadMe 디렉터리 안에 문서 두 개만 존재한다.
실제 실행 가능한 Agent 조직 구조는 아직 생성되지 않았다.

따라서 이 pre-PROTOCOL-README.md는 문서 이해 내용과 설계 방향을 기록하는 중간 문서로서, 사용자 승인 후 실제 구조 생성 작업으로 이어간다.
