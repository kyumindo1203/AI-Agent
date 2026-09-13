# Task Protocol

Task is the atomic execution unit managed by Orchestrator.

## Required Task Fields

```json
{
  "task_id": "TASK-YYYYMMDD-NNNN",
  "parent_task_id": null,
  "project_id": "PROJECT-YYYYMMDD-NNNN",
  "title": "Task Title",
  "objective": "What this task must achieve.",
  "background": "Context for the task.",
  "inputs": [],
  "allowed_resources": [],
  "required_protocol_knowledge": [],
  "constraints": [],
  "dependencies": [],
  "assigned_agent": "planner|researcher|developer|tester|reviewer|security|documenter",
  "priority": "low|normal|high|urgent",
  "acceptance_criteria": [],
  "expected_output": {
    "type": "markdown|json|code|artifact",
    "format": "report|review|test|implementation",
    "fields": []
  },
  "protocol_version": "1.0",
  "attempt": 1,
  "max_attempts": 3,
  "status": "PENDING|ASSIGNED|IN_PROGRESS|REVIEW_REQUIRED|APPROVED|COMPLETED|FAILED|BLOCKED|CANCELLED"
}
```

## Policy

- Task is created by Orchestrator from a goal.
- Specialist must not expand the task scope without Orchestrator approval.
- Completion is confirmed only after verification and acceptance criteria review.
