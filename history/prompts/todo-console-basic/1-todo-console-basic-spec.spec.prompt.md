---
id: 1
title: Todo Console Basic Spec
stage: spec
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-console-basic
branch: 001-todo-console-basic
user: claude
command: /sp.specify
labels: [specification, todo, console, basic]
links:
  spec: specs/001-todo-console-basic/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/001-todo-console-basic/spec.md
- specs/001-todo-console-basic/checklists/requirements.md
tests:
- none
---

## Prompt

```text
# Specification
## In-Memory Todo Console Application (Basic Features Only)

---

## 1. Purpose

This specification defines functionality for the In-Memory Todo Console Application.

It establishes the **core task management foundation** and explicitly excludes all advanced features (priority, time, recurrence, reminders).

---

## 2. Scope

### 2.1 Included Features (Mandatory)

The application **must support** the following operations via CLI:

1. Add a task with:
   - Title (required)
   - Description (optional)
2. View all tasks
3. Update task title and/or description
4. Delete a task by ID
5. Mark a task as complete or incomplete

---

### 2.2 Explicitly Excluded Features (Phase I)

The following **must not exist** in Phase I:

- Due dates or time handling
- Recurring tasks
- Reminders or background checks
- Priorities or tags
- Search, filtering, or sorting
- File or database persistence
- Background threads, timers, or loops

This exclusion is **intentional** to prevent architectural leakage into later phases.

---

## 3. Data Model

Each task must exist **only in memory** and contain:

| Field        | Type    | Description                          |
|-------------|---------|--------------------------------------|
| id          | int     | Unique identifier                    |
| title       | string  | Short task title (required)          |
| description | string  | Optional longer description          |
| completed   | boolean | Completion status                    |

No additional fields are allowed for now.

---

## 4. CLI Behavior

- Application must run entirely in terminal
- Menu-driven or command-driven interaction is allowed
- All prompts must be:
  - Clear
  - Human-readable
  - Error-tolerant
- Invalid input must:
  - Show a helpful message
  - Return the user to a safe state
  - Never crash the application

---

## 5. Error Handling Rules

- No stack traces may be shown to the user
- Invalid IDs must be handled gracefully
- Empty or invalid titles must be rejected with explanation
- Application must never terminate unexpectedly

---

## 6. Project Structure Constraints

- All Python files **must reside inside `/src`**
- Required files:
/src
├── main.py # CLI entry point only
├── todo.py # Core task operations
└── models.py # Task data model


- Business logic must not live in `main.py`
- No additional Python modules are permitted

---

## 7. Tooling Constraint

- The project must be executed using **uv**
- No other environment or dependency managers are allowed
- Only Python standard library may be used

---

## 8. Acceptance Criteria

It is complete when:

- All 5 basic operations work correctly
- Tasks exist only in memory
- The app runs without errors
- No advanced or time-based features are present
- All behavior is traceable to this specification

---
```

## Response snapshot

Created a comprehensive feature specification for the In-Memory Todo Console Application with basic features only. The specification includes 5 user stories covering all required operations (add, view, update, delete, mark complete/incomplete), functional requirements, key entities (Task), and success criteria. The specification complies with the project constitution and includes a quality checklist.

## Outcome

- ✅ Impact: Complete feature specification created
- 🧪 Tests: none
- 📁 Files: 2 files created (spec.md, requirements.md)
- 🔁 Next prompts: Ready for planning phase
- 🧠 Reflection: Specification covers all required functionality without implementation details

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning phase