# AI-Agent Demo

This demo directory mirrors the current abstract multi-agent design in the workspace.

## Top-level structure

```text
AI-Agent/demo/
├── agents/
├── templates/
├── protocols/
├── workflow/
├── logs/
└── config/
```

## Layers

- Agent layer: user, secretary, orchestrator, planner, researcher, developer, tester, reviewer, security.
- Template layer: task, message, report, error templates stored centrally.
- Protocol layer: task, message, review, approval rules.
- Workflow layer: projects organized by planning, execution, review, reporting.
- Logs and config remain separate from the implementation layer.
