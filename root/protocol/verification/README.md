# Verification Protocol

Verification confirms that Task results satisfy acceptance criteria.

## Verification Flow

```text
Developer / Researcher / Planner result
  ↓
Reviewer / Tester / Security review
  ↓
Orchestrator validation
  ↓
Secretary final report
```

## Review Output Template

```json
{
  "task_id": "TASK-YYYYMMDD-NNNN",
  "verdict": "PASS|FAIL|PASS_WITH_RISK|NEEDS_REVISION",
  "criteria": [
    {
      "criterion": "Acceptance criterion text",
      "result": "PASS|FAIL",
      "evidence": "Evidence summary"
    }
  ],
  "issues": [],
  "remaining_risks": []
}
```
