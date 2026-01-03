---
id: 1
title: Plan recurring time customization terminal ui
stage: plan
date: 2026-01-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-recurring-time-ui
branch: 001-recurring-time-ui
user: claude
command: /sp.plan
labels: [feature, planning, recurring-tasks, ui]
links:
  spec: /specs/001-recurring-time-ui/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - /specs/001-recurring-time-ui/plan.md
 - /specs/001-recurring-time-ui/research.md
 - /specs/001-recurring-time-ui/data-model.md
 - /specs/001-recurring-time-ui/quickstart.md
 - /specs/001-recurring-time-ui/contracts/api-contracts.md
tests:
 - /specs/001-recurring-time-ui/tasks.md
---
## Prompt

```text
# Plan — Recurring Time Customization & Terminal UI Presentation

## 1. Scope & Constitutional Validation
- Reconfirm alignment with Constitution
- Confirm implementation is limited strictly to this enhancement specification
- Ensure existing behavior remains unchanged
- Enforce exclusions:
  - No persistence
  - No external libraries
  - No GUI or browser notifications
  - No new task fields
- Confirm constraints:
  - Python 3.13+
  - Standard library only
  - uv as the sole execution tool
  - In-memory data only

---

## 2. Project Structure Enforcement
- Ensure all Python files remain inside `/src`
- Confirm only the following files exist:
  - `main.py`
  - `todo.py`
  - `models.py`

---

## 3. Recurring Time Customization

### 3.1 CLI Input Handling (`main.py`)
- Extend recurring task creation and update flows to:
  - Prompt the user for an optional time value
  - Accept a valid time format (e.g., `HH:MM`)
- If no time is provided:
  - Apply the default value `00:00`
- Validate user input:
  - Reject invalid time formats with a clear message
  - Re-prompt or safely fall back to default

---

### 3.2 Time Application Logic (`todo.py`)
- When setting or updating a recurring task:
  - Apply the user-specified time to the task's existing `due_at` date
- During recurrence rescheduling:
  - Preserve the original time component
  - Advance only the date portion by the recurrence interval
- Ensure:
  - Each recurrence advances exactly once per trigger
  - No recursive or immediate re-triggering occurs
  - No infinite loops are introduced

---

## 4. Terminal UI Presentation Enhancements

### 4.1 Table Layout Formatting
- Implement table-like display for task listings using:
  - Fixed-width columns
  - Header separators
  - Aligned text output
- Ensure:
  - Layout adapts safely to varying content lengths
  - Display logic does not mutate task data

---

### 4.2 Color Output
- Apply ANSI escape codes to:
  - Highlight table headers
  - Differentiate completed vs incomplete tasks
  - Visually distinguish priority levels (if present)
- Ensure:
  - Color usage is optional and non-blocking
  - Output remains readable in terminals without color support

---

## 5. Error Handling & Safety
- Handle all invalid inputs gracefully
- Ensure:
  - No stack traces are displayed
  - Application flow always returns to the CLI
  - UI-related errors do not affect task logic or reminders

---

## 6. uv-Based Execution
- Verify application runs correctly using uv
- Ensure no additional tooling or dependency configuration is introduced
- Confirm standard library usage only

---

## 7. Acceptance Criteria Verification
- Confirm users can set a custom time for recurring tasks
- Verify default recurring time remains `00:00`
- Confirm recurring tasks preserve the specified time across reschedules
- Ensure no infinite reminder loops occur
- Verify task listings display in a table-like, optionally colored format
- Confirm existing functionality remains unchanged

---

## 8. Boundary Enforcement
- Stop implementation once enhancement acceptance criteria are met
- Do not refactor or extend beyond this specification
```

## Response snapshot

# Plan — Recurring Time Customization & Terminal UI Presentation

## 1. Scope & Constitutional Validation
- Reconfirm alignment with Constitution
- Confirm implementation is limited strictly to this enhancement specification
- Ensure existing behavior remains unchanged
- Enforce exclusions:
  - No persistence
  - No external libraries
  - No GUI or browser notifications
  - No new task fields
- Confirm constraints:
  - Python 3.13+
  - Standard library only
  - uv as the sole execution tool
  - In-memory data only

---

## 2. Project Structure Enforcement
- Ensure all Python files remain inside `/src`
- Confirm only the following files exist:
  - `main.py`
  - `todo.py`
  - `models.py`

---

## 3. Recurring Time Customization

### 3.1 CLI Input Handling (`main.py`)
- Extend recurring task creation and update flows to:
  - Prompt the user for an optional time value
  - Accept a valid time format (e.g., `HH:MM`)
- If no time is provided:
  - Apply the default value `00:00`
- Validate user input:
  - Reject invalid time formats with a clear message
  - Re-prompt or safely fall back to default

---

### 3.2 Time Application Logic (`todo.py`)
- When setting or updating a recurring task:
  - Apply the user-specified time to the task's existing `due_at` date
- During recurrence rescheduling:
  - Preserve the original time component
  - Advance only the date portion by the recurrence interval
- Ensure:
  - Each recurrence advances exactly once per trigger
  - No recursive or immediate re-triggering occurs
  - No infinite loops are introduced

---

## 4. Terminal UI Presentation Enhancements

### 4.1 Table Layout Formatting
- Implement table-like display for task listings using:
  - Fixed-width columns
  - Header separators
  - Aligned text output
- Ensure:
  - Layout adapts safely to varying content lengths
  - Display logic does not mutate task data

---

### 4.2 Color Output
- Apply ANSI escape codes to:
  - Highlight table headers
  - Differentiate completed vs incomplete tasks
  - Visually distinguish priority levels (if present)
- Ensure:
  - Color usage is optional and non-blocking
  - Output remains readable in terminals without color support

---

## 5. Error Handling & Safety
- Handle all invalid inputs gracefully
- Ensure:
  - No stack traces are displayed
  - Application flow always returns to the CLI
  - UI-related errors do not affect task logic or reminders

---

## 6. uv-Based Execution
- Verify application runs correctly using uv
- Ensure no additional tooling or dependency configuration is introduced
- Confirm standard library usage only

---

## 7. Acceptance Criteria Verification
- Confirm users can set a custom time for recurring tasks
- Verify default recurring time remains `00:00`
- Confirm recurring tasks preserve the specified time across reschedules
- Ensure no infinite reminder loops occur
- Verify task listings display in a table-like, optionally colored format
- Confirm existing functionality remains unchanged

---

## 8. Boundary Enforcement
- Stop implementation once enhancement acceptance criteria are met
- Do not refactor or extend beyond this specification

## Outcome

- ✅ Impact: Created comprehensive implementation plan for recurring time customization and terminal UI enhancements
- 🧪 Tests: No automated tests created, manual testing will be used
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and API contracts
- 🔁 Next prompts: Will proceed to task generation and implementation
- 🧠 Reflection: Planning phase successfully completed with all required artifacts generated

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Implementation of the planned features