# Capability and Permission Matrix

## Purpose

This document separates technical ability from authorized behavior.

## Capability

Capability is what an agent can technically perform.

Example:

```text
Developer
- read files
- modify files
- run tests
- run build commands
```

## Permission

Permission is the scope where the agent is allowed to act inside the project.

Example:

```text
Developer
Permission:
- /root/** read allowed
- /root/agents/** write allowed
- /root/protocol/** read allowed
- /root/state/** write allowed
- production deployment forbidden
- external API key access forbidden
```

## Matrix

```text
Role           Capability                       Permission
Secretary      receive/report                 user interface only
Orchestrator   plan/decompose/assign/verify   workflow orchestration only
Planner        requirements decomposition      project planning scope
Researcher    information gathering          internal docs and public facts only
Developer      code implementation            repository files inside allowed scope
Tester         verification execution          allowed test scope only
Reviewer       review and acceptance check    review evidence only
Security       review risks                   restricted access to security evidence
Documenter     documentation generation       doc and artifact write scope
```

## Rule

Capability does not automatically grant permission.
Every action must be verified against project permission boundaries.
