# Agent Logs

## Purpose

This document defines the abstract log structure for agent records.

## Required Log Records

```text
message_id
task_id
trace_id
sender
receiver
message_type
status
timestamp
payload_summary
verification_note
```

## Log Flow

```text
Secretary request
Orchestrator assignment
Specialist result
Orchestrator verification
Secretary report
```

## Constraints

- Every message should be traceable.
- Every task should keep a lifecycle record.
- Every verification result should be recorded.
- Every approval or rejection should be recorded.
