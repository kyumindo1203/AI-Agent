# Root Abstract Multi-Agent Structure

This repository holds the abstract structure for a multi-agent environment.

## Flow

User -> Secretary Agent -> Orchestrator Agent -> Specialist Agents -> Orchestrator Agent -> Secretary Agent -> User

## Top-level Areas

- agents/: agent role definitions and responsibility boundaries
- protocol/: message, task, state, and verification protocols
- workflow/: workflow and project task decomposition
- state/: project state and task state
- logs/: message logs and run records
- artifacts/: generated outputs and verified artifacts
