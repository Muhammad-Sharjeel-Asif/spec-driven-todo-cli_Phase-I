---
id: 1
title: Constitution Update
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: claude
command: /sp.constitution
labels: [constitution, governance, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
- .specify/templates/plan-template.md
- .specify/templates/spec-template.md
- .specify/templates/tasks-template.md
tests:
- none
---

## Prompt

```text
# In-Memory Todo Console Application Constitution

## Core Principles

### Clean Code and Minimalism
Functions must do one clear task. Avoid deeply nested logic. Prefer readability over cleverness. No unused variables or dead code. Avoid unnecessary abstraction (e.g., service layers) unless explicitly required by the specification.

### Python Standards Compliance
- Python version: **3.13+**
- Follow PEP-8 conventions
- Use clear, descriptive names
- Use only Python standard library unless explicitly allowed by specification

### In-Memory Data Management
All task data must be stored **in memory only**.
No file, database, or external persistence is allowed.
All data resets when the program exits.

Each task must have, at minimum:
- Unique ID
- Title
- Description
- Completion status

Additional attributes (priority, tags, due dates, recurrence) are allowed **only if specified**.

### Terminal-First User Interface
- Application must be fully operable via terminal (CLI)
- Prompts must be clear, human-readable, and error-tolerant
- Invalid input must be handled gracefully
- Background behaviors (e.g., reminders) **must not block user input**
- reminders **must not** goes into infinite loop.

### Robust Error Handling
- The application must never terminate unexpectedly
- User-facing errors must show helpful messages
- Stack traces must never be shown to the user

---

## Scope Definition

### Phase I — Core Todo Features (Mandatory)
- Add a task (title + description)
- View all tasks with status indicators
- Update task title and description
- Delete task by ID
- Mark task as complete or incomplete

### Phase II — Task Organization Features (Optional via Spec)
Allowed only when specified:
- Task priorities (e.g., high / medium / low)
- Tags or categories
- Search and filtering
- Sorting (alphabetical, priority, date)

### Phase III — Time-Based Features (Optional via Spec)
Allowed only when specified:
- Due dates with date **and time**
- Recurring tasks (only when time exist)
- Non-blocking CLI reminders
- Automatic rescheduling of recurring tasks

---

## Explicit Exclusions (All Phases)

The following must **never** be implemented:
- File or database persistence
- Authentication or multi-user support
- Networking or APIs
- GUI or web interface
- Automated testing frameworks
- External Python libraries

---

## Project Structure Requirements

All Python-related files **must reside inside the `/src` directory**.

Minimum required structure:
/src
├── main.py        # Application entry point (CLI only)
├── todo.py        # Core todo logic
└── models.py      # Task data models

Rules:
- Business logic must not live in `main.py`
- Models must be separated from control flow
- Additional Python modules may be added **inside `/src`** if required by later-phase specifications

---

## Tooling Constraint

- The project **must use `uv`** for environment and execution
- `uv` commands must be runnable from within the project context
- No alternative environment or dependency managers are allowed

---

## Governance

This constitution governs **all phases** of the In-Memory Todo Console Application.

- All Claude-generated outputs must comply with this constitution
- If a conflict arises:
  **Specification correctness and project progress take priority**, but the constitution must not be amended
```

## Response snapshot

Updated the project constitution file with the provided In-Memory Todo Console Application Constitution, including all core principles, scope definitions, exclusions, and governance rules. Updated dependent templates to ensure consistency with the new constitution requirements.

## Outcome

- ✅ Impact: Updated constitution and dependent templates
- 🧪 Tests: none
- 📁 Files: 4 files updated
- 🔁 Next prompts: Feature development can now proceed according to constitution
- 🧠 Reflection: Constitution provides clear governance framework for project

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification