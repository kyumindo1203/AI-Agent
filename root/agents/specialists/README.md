# Specialist Agents

## Purpose

Specialist Agents are focused workers with clearly bounded responsibilities.
They perform work inside their capability and permission scope, then return structured results to the Orchestrator.

## Specialist Types

- Planner
- Researcher
- Developer
- Tester
- Reviewer
- Security
- Documenter

## Communication Pattern

```text
Specialist -> Orchestrator
Orchestrator -> Specialist
```

## Constraints

- Specialists must not communicate directly with the user.
- Specialists must not communicate directly with each other by default.
- Specialists must not exceed task permission boundaries.
- Specialists must submit evidence and results for verification.
