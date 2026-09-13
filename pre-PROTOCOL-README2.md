# pre-PROTOCOL-README2

## 1. Message 프로퍼티 정의와 구체화

Agent 간 구조화된 통신은 Message 객체로 관리한다. Message는 단순한 문자열이 아니라, 모든 메시지의 발신자/수신자/의도/작업/예상 결과/상태를 하나의 표준으로 구조화해야 한다.

기본 메시지 구조는 다음과 같다.

```json
{
  "message_id": "MSG-20260913-0001",
  "task_id": "TASK-20260913-0001",
  "sender": "secretary",
  "receiver": "orchestrator",
  "message_type": "TASK",
  "priority": "normal",
  "context": {
    "project_id": "PROJECT-20260913-0001",
    "project_name": "example-project",
    "timestamp": "2026-09-13T10:00:00Z",
    "trace_id": "TRACE-20260913-0001"
  },
  "task": {
    "task_id": "TASK-20260913-0001",
    "title": "요구사항 수집",
    "objective": "사용자 요구사항을 정리한다.",
    "background": "현재 사용자의 목표를 이해해야 한다.",
    "inputs": [],
    "allowed_resources": [],
    "constraints": [],
    "dependencies": [],
    "assigned_agent": "planner",
    "priority": "normal",
    "acceptance_criteria": [],
    "expected_output": {},
    "status": "PENDING"
  },
  "constraints": [
    "사용자 요청 범위를 넘지 않는다",
    "비밀정보를 그대로 포함하지 않는다"
  ],
  "expected_output": {
    "type": "requirements-summary",
    "format": "markdown",
    "required_fields": [
      "objective",
      "inputs",
      "constraints",
      "dependencies"
    ]
  },
  "status": "pending"
}
```

### 1.1 Message 프로퍼티 상세

#### message_id
- 메시지의 고유 식별자.
- 값 형식은 `MSG-YYYYMMDD-NNNN`과 같은 규칙을 권장한다.
- 예: `MSG-20260913-0001`.
- 메시지 추적, 로그, 감사 기록, 재전송 감지에서 사용된다.

#### task_id
- 이 메시지가 연결되는 Task의 식별자.
- 값 형식은 `TASK-YYYYMMDD-NNNN`으로 관리한다.
- 예: `TASK-20260913-0001`.

#### sender
- 메시지를 보낸 Agent의 식별 이름.
- 값은 Agent 역할 이름을 사용한다.
- 예: `secretary`, `orchestrator`, `planner`, `researcher`, `developer`, `tester`, `reviewer`, `security`.

#### receiver
- 메시지를 받는 Agent의 식별 이름.
- 값도 Agent 역할 이름이어야 한다.
- 예: `orchestrator`, `planner`, `developer`.

#### message_type
- 메시지의 종류.
- 허용 값은 다음과 같다.

```text
REQUEST
TASK
RESULT
QUESTION
REPORT
REVIEW_REQUEST
REVIEW_RESULT
ERROR
APPROVAL_REQUEST
APPROVAL_RESULT
STATUS
CANCEL
```

각 값의 의미는 아래와 같다.

- REQUEST: 상위 Agent가 하위 Agent로 작업을 요청하는 메시지.
- TASK: 실제 작업 지시 메시지.
- RESULT: 작업 결과 보고 메시지.
- QUESTION: 추가 정보가 필요할 때의 질문 메시지.
- REPORT: 현재 상황 보고 메시지.
- REVIEW_REQUEST: 검증 요청 메시지.
- REVIEW_RESULT: 검토 결과 메시지.
- ERROR: 실패 원인 또는 오류 상태 보고 메시지.
- APPROVAL_REQUEST: 사용자 또는 상위 Agent의 승인이 필요한 메시지.
- APPROVAL_RESULT: 승인/거절 결과 메시지.
- STATUS: 상태 보고 메시지.
- CANCEL: 작업 취소 메시지.

#### priority
- 우선순위 수준.
- 허용 값은 `low`, `normal`, `high`, `urgent` 중 하나여야 한다.
- 예: `normal`.

#### context
- 메시지가 전달되는 전체 맥락.
- 필수 하위 값은 다음과 같다.

```json
{
  "project_id": "PROJECT-20260913-0001",
  "project_name": "example-project",
  "timestamp": "2026-09-13T10:00:00Z",
  "trace_id": "TRACE-20260913-0001"
}
```

설명:

- project_id: 작업이 속한 프로젝트 식별자.
- project_name: 프로젝트 이름.
- timestamp: 메시지 생성 시각.
- trace_id: 전체 대화/실행 추적 ID.

#### task
- 실제 수행되는 Task 객체.
- 이것은 Task의 필수 요소를 포함하는 서브 객체다.
- 일반적으로 Task가 Missing되면 `task_id`, `title`, `objective`, `assigned_agent`만 들어 있어도 된다.

#### constraints
- Agent에게 지켜야 할 제한 조건.
- 예: "비밀정보를 포함하지 않는다", "외부 API를 직접 호출하지 않는다", "사용자 승인 없이 배포하지 않는다".
- 항상 목록으로 표현한다.

#### expected_output
- Agent가 최종적으로 반환해야 하는 형태.
- 구조를 특정 형식으로 지정할 수 있다.
- 예:

```json
{
  "type": "requirements-summary",
  "format": "markdown",
  "required_fields": [
    "objective",
    "inputs",
    "constraints",
    "dependencies"
  ]
}
```

#### status
- 메시지의 상태.
- 허용 값은 `pending`, `assigned`, `in_progress`, `sent`, `review_required`, `approved`, `completed`, `failed`, `blocked`, `cancelled` 중 하나다.
- Example: `pending`.

---

## 2. Task 프로퍼티 정의와 구체화

Task는 실제 담당 에이전트가 수행해야 할 최소 단위의 작업 단위다. Task는 반드시 독립적인 ID를 갖고, 입력·제한·의존성·수용 기준을 명확히 해야 한다.

예시 구조:

```json
{
  "task_id": "TASK-20260913-0001",
  "parent_task_id": null,
  "title": "요구사항 수집",
  "objective": "사용자 요구사항을 정리하고 설계에서 사용할 수 있도록 보관한다.",
  "background": "신규 프로젝트의 시작 단계이며, 요구사항의 불명확성을 줄여야 한다.",
  "inputs": [
    "사용자 요청 텍스트",
    "기존 프로젝트 문서",
    "관련 비즈니스 정보"
  ],
  "allowed_resources": [
    "workspace/config"
  ],
  "required_protocol_knowledge": [
    "ReadMe/AGENT_CONSTITUTION.md",
    "ReadMe/TASK_PROTOCOL.md"
  ],
  "constraints": [
    "비밀정보를 일반 텍스트로 저장하지 않는다",
    "기존 기능을 무단으로 변경하지 않는다"
  ],
  "dependencies": [],
  "assigned_agent": "planner",
  "priority": "normal",
  "acceptance_criteria": [
    "요구사항이 명확한 문장으로 정리되어야 한다.",
    "불명확한 부분이 질문 목록으로 남아 있어야 한다."
  ],
  "expected_output": {
    "type": "requirements-summary",
    "format": "markdown",
    "fields": [
      "objective",
      "constraints",
      "dependencies",
      "acceptance_criteria"
    ]
  },
  "status": "PENDING"
}
```

### 2.1 Task 프로퍼티 상세

#### task_id
- Task의 고유 식별자.
- 값 형식: `TASK-YYYYMMDD-NNNN`.
- 예: `TASK-20260913-0001`.
- `task_id`는 동일 프로젝트 내에서 유일해야 한다.

#### parent_task_id
- 상위 Task가 존재할 경우 연결되는 부모 Task ID.
- 상위 Task가 없으면 `null`.
- 예: `TASK-20260913-0000`.
- 의미: 큰 Task를 분해한 하위 Task일 경우, 원인/상위 문맥을 연결한다.

#### title
- 작업의 짧은 제목.
- 하나 줄, 실행 가능한 문장 또는 명사형 표현을 사용한다.
- 예: `요구사항 수집`, `DB 설계`, `API 설계`, `코드 구현`.

#### objective
- 작업을 수행하는 목적.
- 왜 이 작업을 해야 하는지 서술한다.
- 예: "사용자의 요구사항을 정리하여 개발 계획의 입력으로 제공한다."

#### background
- 작업 수행에 필요한 현재 상황 설명.
- 예: "현재 기능 구현 전 단계이며, 기능 범위를 명확히 해야 한다."

#### inputs
- 작업에 필요한 데이터, 문서, 자료, 파일, 템플릿 경로, 사용자 요청 정보.
- 값은 문자열 목록 또는 객체 목록으로 정의한다.
- 예:

```json
[
  "ReadMe/TASK_PROTOCOL.md",
  "ReadMe/AGENT_CONSTITUTION.md",
  "사용자 요청 문서"
]
```

#### allowed_resources
- Agent가 작업 중 사용할 수 있는 자원.
- 파일 목록, 디렉터리 목록, 도구 목록, API 목록 등을 명시한다.
- 이 값은 Agent가 작업에 실제로 접근할 수 있는 자원을 허가하는 목록이다.
- 예:

```json
[
  "workspace/config",
  "templates/task/task_template.json",
  "agents/developer/README.md",
  "workflow/projects"
]
```

#### required_protocol_knowledge
- `required_protocol_knowledge`는 `List<String>` 타입으로 관리한다.
- 이 항목은 Agent가 작업 수행 전에 인지해야 하는 Markdown 프로토콜 문서 경로 목록이다.
- 목록에 저장된 문서 파일은 단순히 읽는 수준을 넘어서, 그 문서의 전체 의미와 규칙을 이해하고 작업에 반영할 수 있어야 한다.
- 예:

```json
[
  "ReadMe/AGENT_CONSTITUTION.md",
  "ReadMe/TASK_PROTOCOL.md"
]
```

- 이 목록에 포함된 Markdown 문서는 Agent의 전체 이해 대상이며, Agent는 그 문서의 계층 구조, 역할 관계, 통신 규칙, Task 규칙, 검증 원칙, 승인 원칙, 보고 원칙을 전반적으로 파악해야 한다.
- 따라서 `required_protocol_knowledge`는 문서 경로 목록의 저장소 역할을 하며, Agent는 이 목록에 포함된 Markdown 파일에 대한 전반적인 이해를 갖고 있어야 한다.

#### constraints
- 작업 수행 중 지켜야 하는 제한사항.
- 예: "배포를 실행하지 않는다", "비밀번호를 로그에 남기지 않는다", "외부 서비스 데이터를 저장하지 않는다".

#### dependencies
- 선행으로 완료되어야 하는 Task ID 리스트.
- 예:

```json
[
  "TASK-20260913-0001",
  "TASK-20260913-0002"
]
```

#### assigned_agent
- 작업을 담당할 Agent.
- 값은 Agent 역할 이름을 사용한다.
- 예: `planner`, `researcher`, `developer`, `tester`, `reviewer`, `security`, `secretary`, `orchestrator`.

#### priority
- 작업의 중요도.
- 허용 값은 `low`, `normal`, `high`, `urgent`.

#### acceptance_criteria
- 작업 완료를 판단하는 기준.
- 반드시 체크 가능하고 검증 가능한 문장 목록이다.
- 본 항목은 결과가 완성되었는지 여부를 확인하는 기준으로 유지한다.
- 예:

```json
[
  "요구사항이 문서화되었다.",
  "인수 기준이 명확하게 정의되었다.",
  "필요한 검증 항목이 존재한다."
]
```

#### expected_output
- 작업 결과물의 형식.
- 예:

```json
{
  "type": "markdown",
  "format": "report",
  "fields": [
    "objective",
    "summary",
    "accepted_criteria",
    "remaining_risks"
  ]
}
```

#### status
- Task의 상태.
- Task Lifecycle는 다음과 같다.

```text
PENDING
ASSIGNED
IN_PROGRESS
REVIEW_REQUIRED
APPROVED
COMPLETED
```

실패 시 상태는 다음과 같이 전이된다.

```text
IN_PROGRESS → FAILED → RETRY → IN_PROGRESS
```

재시도를 해도 해결되지 않으면:

```text
FAILED → BLOCKED → ORCHESTRATOR
```

Orchestrator가 해결할 수 없으면 Secretary를 통해 사용자에게 질문한다.

### 2.2 Task 설명을 단순한 JSON이 아니라 실제 문서화하는 이유

Task는 체계적인 작업단위로서 단순 상태 값이 아니라, 다음을 포함해야 한다.

- 작업의 목적
- 작업을 수행하는 맥락
- 필요한 입력 데이터
- 사용할 수 있는 자원
- 수행에 필요한 제약
- 선행 의존성
- 담당 Agent
- 완료 기준
- 결과물 형식

이 요소들은 Task를 만들 때 반드시 정의되고, 상태 전이는 이 정보를 기반으로 관리된다.

---

## 3. Workflow 구조 개편

기존 설계에서는 workflow 디렉터리 하위 구조가 `planning`, `execution`, `review`, `reporting`으로 고정되어 있었다. 하지만 여러 프로젝트를 관리할 예정이므로, workflow는 프로젝트 단위로 저장 가능한 구조로 변경한다.

### 3.1 변경된 workflow 구조

```text
/workspaces/AI-Agent/
├─ workflow/
│  └─ projects/
│     ├─ PROJECT-20260913-0001/
│     │  ├─ project.yaml
│     │  ├─ planning/
│     │  │  ├─ requirements/
│     │  │  ├─ design/
│     │  │  └─ tasks/
│     │  ├─ execution/
│     │  │  ├─ code/
│     │  │  ├─ tests/
│     │  │  └─ artifacts/
│     │  ├─ review/
│     │  │  ├─ review_requests/
│     │  │  ├─ review_results/
│     │  │  └─ quality_checks/
│     │  └─ reporting/
│     │     ├─ reports/
│     │     ├─ summaries/
│     │     └─ user_reports/
│     └─ PROJECT-20260913-0002/
│        ├─ project.yaml
│        ├─ planning/
│        ├─ execution/
│        ├─ review/
│        └─ reporting/
└─ ...
```

### 3.2 프로젝트 중심 구조의 의미

workflow는 단순한 실행 단계의 디렉터리 모음이 아니라, 여러 프로젝트를 저장하고 추적할 수 있는 프로젝트 컨테이너로 정의한다.

즉:

- `workflow/`는 전역 저장소
- `workflow/projects/`는 프로젝트 저장소
- 각 프로젝트 폴더는 별도의 고유 `project_id` 또는 `project_name`로 구분
- 각 프로젝트의 내부 단계는 `planning`, `execution`, `review`, `reporting`으로 분리

### 3.3 프로젝트별 구조 상세

#### planning
- 요구사항 수집, 목표 분석, 작업 분해, 일정/우선순위 정의, 입력/의존성 정리.
- 권장 하위 디렉터리:

```text
planning/
├─ requirements/
├─ design/
└─ tasks/
```

- `requirements/`: 사용자 요구사항과 목표 문서
- `design/`: 설계 아키텍처/데이터 모델 문서
- `tasks/`: Task 파일, Task 분해 파일, Task 리스트

#### execution
- 코딩, 테스트, 구현 결과, 실행 파일, 산출물 보관.
- 권장 하위 디렉터리:

```text
execution/
├─ code/
├─ tests/
└─ artifacts/
```

- `code/`: 구현 코드
- `tests/`: 테스트 코드
- `artifacts/`: 로그, 빌드 산출물, 실행 결과

#### review
- 코드 검토, 품질 검토, 보안 검토, 검토 요청과 결과 저장.
- 권장 하위 디렉터리:

```text
review/
├─ review_requests/
├─ review_results/
└─ quality_checks/
```

- `review_requests/`: 검토를 요청하는 메시지/문서
- `review_results/`: 리뷰어 결과 문서
- `quality_checks/`: 정적 분석, 보안 점검, 품질 점검 결과

#### reporting
- 사용자에게 최종보고하거나 요약을 정리.
- 권장 하위 디렉터리:

```text
reporting/
├─ reports/
├─ summaries/
└─ user_reports/
```

- `reports/`: 실행 결과 문서
- `summaries/`: 전체 상태 요약
- `user_reports/`: 비서 Agent가 사용자에게 전달할 최종 보고 문서

### 3.4 프로젝트 식별 규칙

프로젝트 저장 시 다음 규칙을 준수한다.

- 프로젝트 이름은 `project_name` 형식의 디렉터리로 저장한다.
- 프로젝트 식별자는 `PROJECT-YYYYMMDD-NNNN` 형식을 사용한다.
- 프로젝트 메타데이터는 `project.yaml`로 저장한다.

예:

```yaml
project_id: PROJECT-20260913-0001
project_name: example-project
owner: user
created_at: 2026-09-13T10:00:00Z
status: active
workflow:
  planning: true
  execution: true
  review: true
  reporting: true
```

---

## 4. 신규 파일 생성 계획

이전 문서에서 설계한 원칙과 지금 정리한 구체화 내용을 반영해 새로운 파일 `pre-PROTOCOL-README2.md`를 생성한다.

이 파일은 기존 설계 문서 위에 다음을 추가한다.

1. Message 프로퍼티를 구체화한 설명.
2. Task의 모든 요소를 설명하고 값 형식을 정리.
3. workflow를 여러 프로젝트를 저장할 수 있는 구조로 발전.
4. 프로젝트 내부의 `planning`, `execution`, `review`, `reporting` 디렉터리 구조를 설명.

새 문서는 사용자가 피드백 수용 후 실제 여건에 맞는 구현 구조로 이어질 수 있도록, 구현 전의 설계 문법을 기준으로 작성한다.

---

## 5. 최종 설계 원칙

모든 작업은 다음 순서로 관리한다.

```text
사용자 요구
  ↓
Secretary Agent 요구 수집
  ↓
Orchestrator Agent 분해
  ↓
Specialist Agent 담당작업
  ↓
Reviewer / Tester / Security 검증
  ↓
Secretary Agent 최종 보고
```

이 구조는 여러 프로젝트를 저장하고 관리할 수 있도록 `workflow/projects`로 확장하며, 본 문서의 구체화 작업은 이를 위한 표준 문서 역할을 한다.
