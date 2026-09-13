# Task Protocol

This file is an abstract task protocol description for the workspace.

## Structure

Task contains task_id, parent_task_id, title, objective, background, inputs,
allowed_resources, required_protocol_knowledge, constraints, dependencies,
assigned_agent, priority, acceptance_criteria, expected_output, and status.

## Lifecycle

PENDING -> ASSIGNED -> IN_PROGRESS -> REVIEW_REQUIRED -> APPROVED -> COMPLETED

Failure paths:

IN_PROGRESS -> FAILED -> RETRY -> IN_PROGRESS
FAILED -> BLOCKED -> ORCHESTRATOR
