# AI Agent Workspace

This workspace implements a lightweight multi-agent organization model inspired by the protocol documents in ReadMe/.

## Top-level structure

```text
/workspaces/AI-Agent/
├─ agents/
│  ├─ secretary/
│  ├─ orchestrator/
│  ├─ planner/
│  ├─ researcher/
│  ├─ developer/
│  ├─ tester/
│  ├─ reviewer/
│  └─ security/
├─ templates/
│  ├─ task/
│  ├─ message/
│  ├─ report/
│  └─ error/
├─ protocols/
├─ workflow/
│  └─ projects/
├─ logs/
│  ├─ audit/
│  └─ execution/
├─ config/
└─ README.md
```

## Agent layer

- secretary: user-facing interface and final reporting
- orchestrator: top-level workflow coordination and message routing
- orchestrator/children/: specialist agents managed below the orchestrator
  - planner
  - researcher
  - developer
  - tester
  - reviewer
  - security

계층 메타데이터는 각 에이전트 디렉터리의 metadata.yaml 파일로 표현한다.

## Protocol layer

The workspace stores structured protocol metadata and reference artifacts under protocols/ and templates/.

## Workflow layer

Projects are stored under workflow/projects/ and organized by lifecycle area:

- planning
  - requirements
  - design
  - tasks
- execution
  - code
  - tests
  - artifacts
- review
  - validation
  - quality
- reporting
  - summary
  - deliverables

An example project has been added at workflow/projects/PROJECT-20260913-0001/ with a project manifest and lifecycle folders.

## Audit and execution logs

Important operations and execution traces are recorded under logs/audit and logs/execution.
