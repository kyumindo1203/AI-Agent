# Message Protocol

This file is an abstract message protocol description for the workspace.

## Message fields

message_id, task_id, sender, receiver, message_type, priority, context, task,
constraints, expected_output, status.

## Message types

REQUEST, TASK, RESULT, QUESTION, REPORT, REVIEW_REQUEST, REVIEW_RESULT,
ERROR, APPROVAL_REQUEST, APPROVAL_RESULT, STATUS, CANCEL.
