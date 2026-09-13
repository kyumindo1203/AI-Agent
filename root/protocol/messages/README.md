# Message Protocol

Message is the communication contract between Secretary, Orchestrator, and Specialists.

## Required Message Fields

```json
{
  "message_id": "MSG-YYYYMMDD-NNNN",
  "task_id": "TASK-YYYYMMDD-NNNN",
  "sender": "secretary|orchestrator|planner|researcher|developer|tester|reviewer|security|documenter",
  "receiver": "secretary|orchestrator|planner|researcher|developer|tester|reviewer|security|documenter",
  "message_type": "REQUEST|TASK|RESULT|QUESTION|REPORT|REVIEW_REQUEST|REVIEW_RESULT|ERROR|APPROVAL_REQUEST|APPROVAL_RESULT|STATUS|CANCEL",
  "priority": "low|normal|high|urgent",
  "context": {
    "project_id": "PROJECT-YYYYMMDD-NNNN",
    "project_name": "example-project",
    "timestamp": "2026-09-13T00:00:00Z",
    "trace_id": "TRACE-YYYYMMDD-NNNN"
  },
  "payload": {},
  "protocol_version": "1.0",
  "status": "CREATED|SENT|DELIVERED|PROCESSED|FAILED"
}
```

## Policy

- User communicates only through Secretary.
- Specialist Agent does not communicate directly with User.
- Specialist Agent uses Orchestrator as the routing and validation hub.
