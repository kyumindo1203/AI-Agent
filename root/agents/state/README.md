# Agent State Model

## Purpose

This abstraction records the shared state an agent should reference while acting.

## Common State

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

## State Trace

```text
conversation history
project state
relevant task state
protocol version
verification evidence
```

## Constraints

- Do not load the entire conversation history into a single agent request.
- Keep project state separate from conversation history.
- Store only the information required to continue the task safely.
