---
id: 1
title: spec-todo-time-reminders
stage: spec
date_iso: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-time-reminders
branch: 001-todo-time-reminders
user: user
command: /sp.specify
labels:
  - specification
  - todo-app
  - time-based-reminders
  - recurring-tasks
links:
  SPEC: "null"
  TICKET: "null"
  ADR: "null"
  PR: "null"
files_yaml: |
  - specs/001-todo-time-reminders/spec.md
  - specs/001-todo-time-reminders/checklists/requirements.md
tests_yaml: |
  - "spec validation"
prompt_text: "# Specification — In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)\n\n## 1. Purpose\nExtend the existing in-memory Todo Console App with **time-based task behavior** limited strictly to:\n- Recurring task rescheduling\n- Due date and time-based reminders\n\nNo functionality outside this scope is permitted.\n\n---\n\n## 2. Constitutional Alignment\nThis specification fully complies with **Constitution**:\n- Python 3.13+, PEP-8, standard library only\n- In-memory task management only\n- Terminal-first CLI operation\n- No GUI or web interface\n- No networking or external services\n- Robust error handling with no crashes or stack traces\n- Execution via **uv** only\n\n> Note: Due to constitutional constraints, reminders are delivered via **terminal-based time notifications**, not via web or browser-based interfaces.\n\n---\n\n## 3. Scope Definition\n\n### Included Features\n\n1. **Recurring Tasks**\n   - Tasks may be marked as recurring\n   - Supported recurrence intervals:\n     - Daily\n     - Weekly\n     - Monthly\n   - When a recurring task reaches its due time:\n     - The task is automatically rescheduled to its next occurrence\n     - The task remains in memory only\n   - Recurrence behavior is strictly time-based\n\n2. **Due Dates & Time-Based Reminders**\n   - Tasks may have an optional due date and time\n   - At the specified time:\n     - A reminder message is displayed in the terminal\n   - Reminders are triggered only once per scheduled time for 10 seconds only\n\n---\n\n## 4. Explicit Constraints & Safety Rules\n\n- Recurring task reminders **must not** cause infinite loops\n- Each reminder is triggered only at its scheduled time\n- No busy-waiting or uncontrolled looping is allowed\n- Time checks must be controlled and non-blocking\n- No background threads or asynchronous schedulers that persist beyond program runtime\n- No browser-based or GUI notifications are permitted\n\n---\n\n## 5. Explicit Exclusions\nThe following are **not allowed**:\n- File or database persistence\n- Web or browser interfaces\n- System tray or OS-level notifications\n- External libraries or schedulers\n- Networking or APIs\n- Automated testing frameworks\n- Any Phase IV or speculative features\n\n---\n\n## 6. Data Model Extension\n\n### Task Fields\nThe task model is extended with the following **given fields only**:\n\n| Field          | Type        | Description                                      |\n|----------------|-------------|--------------------------------------------------|\n| id             | int         | Unique runtime identifier                        |\n| title          | str         | Task title                                       |\n| description    | str         | Optional description                             |\n| completed      | bool        | Completion status                                |\n| priority       | str         | existing field                                   |\n| tags           | list[str]   | existing field                                   |\n| created_at     | datetime    | In-memory creation timestamp                     |\n| due_at         | datetime    | Optional due date and time                       |\n| recurrence     | str \\| None | One of: daily / weekly / monthly / None          |\n\n### Constraints\n- No additional fields are allowed\n- No persistence of dates or schedules beyond runtime\n- No derived or cached scheduling state stored on the model\n\n---\n\n## 7. Reminder & Recurrence Behavior\n\n### Reminder Rules\n- Reminders are checked against the current system time\n- A reminder is shown only when the current time reaches or exceeds `due_at`\n- Once triggered, the reminder is not repeated for the same due time\n\n### Recurrence Rules\n- After a recurring task reminder triggers:\n  - The task's `due_at` is advanced exactly one interval forward\n  - The task is not duplicated\n- Recurrence advancement occurs only once per trigger\n- No recursive or immediate re-triggering is allowed\n\n---\n\n## 8. CLI Behavior\n- Users may:\n  - Set or update due date and time via terminal input\n  - Enable or disable recurrence for a task\n- All inputs are validated with clear error messages\n- All reminder messages are displayed in the terminal in a human-readable format\n\n---\n\n## 9. Error Handling & Validation\n- Handle invalid date/time input gracefully\n- Handle unsupported recurrence values with clear feedback\n- Ensure:\n  - Application never crashes\n  - No stack traces are displayed\n  - Control always returns to the CLI loop\n\n---\n\n## 10. Project Structure\nAll Python files must remain in `/src` only.\n\nRequired files:\n- `main.py` — CLI and user interaction\n- `todo.py` — business logic and time-based checks\n- `models.py` — task data model\n\nNo additional Python modules are permitted.\n\n---\n\n## 11. Tooling & Execution\n- Application must run using **uv**\n- Only Python standard library modules may be used\n- No alternative environment or dependency tools are allowed\n\n---\n\n## 12. Acceptance Criteria\n- Tasks can have optional due dates and times\n- Terminal-based reminders trigger at the correct time\n- Recurring tasks reschedule correctly without duplication\n- No infinite loops occur\n- All behavior is time-based and in-memory only\n- No excluded or future features are present\n- Every behavior is traceable directly to this specification\n\n---\n\n## 13. Phase Boundary Enforcement\n- Implementation must stop once acceptance criteria are met\n- No refactoring or extensions beyond this specification\n- Any future functionality requires a new specification"
response_text: "Created comprehensive specification for In-Memory Todo Console App with Recurring Tasks & Time-Based Reminders. The specification includes user scenarios, functional requirements, success criteria, and follows all constitutional constraints. Created user stories with priorities (P1-P3), defined edge cases, and established measurable outcomes. The specification is ready for planning phase."
outcome: "Specification successfully created and validated with quality checklist"
evaluation: "The specification meets all requirements and is ready for the planning phase"
---

# Specification — In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

## 1. Purpose
Extend the existing in-memory Todo Console App with **time-based task behavior** limited strictly to:
- Recurring task rescheduling
- Due date and time-based reminders

No functionality outside this scope is permitted.

---

## 2. Constitutional Alignment
This specification fully complies with **Constitution**:
- Python 3.13+, PEP-8, standard library only
- In-memory task management only
- Terminal-first CLI operation
- No GUI or web interface
- No networking or external services
- Robust error handling with no crashes or stack traces
- Execution via **uv** only

> Note: Due to constitutional constraints, reminders are delivered via **terminal-based time notifications**, not via web or browser-based interfaces.

---

## 3. Scope Definition

### Included Features

1. **Recurring Tasks**
   - Tasks may be marked as recurring
   - Supported recurrence intervals:
     - Daily
     - Weekly
     - Monthly
   - When a recurring task reaches its due time:
     - The task is automatically rescheduled to its next occurrence
     - The task remains in memory only
   - Recurrence behavior is strictly time-based

2. **Due Dates & Time-Based Reminders**
   - Tasks may have an optional due date and time
   - At the specified time:
     - A reminder message is displayed in the terminal
   - Reminders are triggered only once per scheduled time for 10 seconds only

---

## 4. Explicit Constraints & Safety Rules

- Recurring task reminders **must not** cause infinite loops
- Each reminder is triggered only at its scheduled time
- No busy-waiting or uncontrolled looping is allowed
- Time checks must be controlled and non-blocking
- No background threads or asynchronous schedulers that persist beyond program runtime
- No browser-based or GUI notifications are permitted

---

## 5. Explicit Exclusions
The following are **not allowed**:
- File or database persistence
- Web or browser interfaces
- System tray or OS-level notifications
- External libraries or schedulers
- Networking or APIs
- Automated testing frameworks
- Any Phase IV or speculative features

---

## 6. Data Model Extension

### Task Fields
The task model is extended with the following **given fields only**:

| Field          | Type        | Description                                      |
|----------------|-------------|--------------------------------------------------|
| id             | int         | Unique runtime identifier                        |
| title          | str         | Task title                                       |
| description    | str         | Optional description                             |
| completed      | bool        | Completion status                                |
| priority       | str         | existing field                                   |
| tags           | list[str]   | existing field                                   |
| created_at     | datetime    | In-memory creation timestamp                     |
| due_at         | datetime    | Optional due date and time                       |
| recurrence     | str \| None | One of: daily / weekly / monthly / None          |

### Constraints
- No additional fields are allowed
- No persistence of dates or schedules beyond runtime
- No derived or cached scheduling state stored on the model

---

## 7. Reminder & Recurrence Behavior

### Reminder Rules
- Reminders are checked against the current system time
- A reminder is shown only when the current time reaches or exceeds `due_at`
- Once triggered, the reminder is not repeated for the same due time

### Recurrence Rules
- After a recurring task reminder triggers:
  - The task's `due_at` is advanced exactly one interval forward
  - The task is not duplicated
- Recurrence advancement occurs only once per trigger
- No recursive or immediate re-triggering is allowed

---

## 8. CLI Behavior
- Users may:
  - Set or update due date and time via terminal input
  - Enable or disable recurrence for a task
- All inputs are validated with clear error messages
- All reminder messages are displayed in the terminal in a human-readable format

---

## 9. Error Handling & Validation
- Handle invalid date/time input gracefully
- Handle unsupported recurrence values with clear feedback
- Ensure:
  - Application never crashes
  - No stack traces are displayed
  - Control always returns to the CLI loop

---

## 10. Project Structure
All Python files must remain in `/src` only.

Required files:
- `main.py` — CLI and user interaction
- `todo.py` — business logic and time-based checks
- `models.py` — task data model

No additional Python modules are permitted.

---

## 11. Tooling & Execution
- Application must run using **uv**
- Only Python standard library modules may be used
- No alternative environment or dependency tools are allowed

---

## 12. Acceptance Criteria
- Tasks can have optional due dates and times
- Terminal-based reminders trigger at the correct time
- Recurring tasks reschedule correctly without duplication
- No infinite loops occur
- All behavior is time-based and in-memory only
- No excluded or future features are present
- Every behavior is traceable directly to this specification

---

## 13. Phase Boundary Enforcement
- Implementation must stop once acceptance criteria are met
- No refactoring or extensions beyond this specification
- Any future functionality requires a new specification