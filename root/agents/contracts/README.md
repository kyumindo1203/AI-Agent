# Agent Contracts

## Purpose

This document defines the common abstract contract every agent must satisfy.

## Shared Contract Fields

Every agent should expose the following abstract fields:

```text
agent_id
role
capability
permission
input_schema
output_schema
allowed_channels
blocked_channels
state_reference
trace_id
```

## Contract Flow

```text
User -> Secretary Agent
Secretary Agent -> Orchestrator Agent
Orchestrator Agent -> Specialist Agent
Specialist Agent -> Orchestrator Agent
Orchestrator Agent -> Secretary Agent
Secretary Agent -> User
```

## Input Contract

An agent receives:

- user request or normalized objective
- project state summary
- relevant task context
- relevant protocol context
- applicable permission scope

## Output Contract

An agent returns:

- task_id
- agent_id
- summary
- changes
- verification evidence
- remaining risks
- issues
- artifacts

## Constraints

- No agent may report a completion without verification evidence.
- No agent may speak outside its communication channel.
- No agent may bypass the Orchestrator in specialist-to-specialist workflows.
