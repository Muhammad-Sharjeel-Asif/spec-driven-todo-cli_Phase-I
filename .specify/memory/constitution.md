<!--
Sync Impact Report:
Version change: N/A -> 1.0.0
Modified principles: N/A (new constitution)
Added sections: All sections (new constitution)
Removed sections: N/A
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ no files found
Follow-up TODOs: None
-->
# In-Memory Todo Console Application Constitution

## Core Principles

### Clean Code and Minimalism
Functions must do one clear task. Avoid deeply nested logic. Prefer readability over cleverness. No unused variables or dead code. Avoid unnecessary abstraction (e.g., service layers) unless explicitly required by the specification.

### Python Standards Compliance
Python version: 3.13+. Follow PEP-8 conventions. Use clear, descriptive names. Use only Python standard library unless explicitly allowed by specification.

### In-Memory Data Management
All task data must be stored in memory only. No file, database, or external persistence is allowed. All data resets when the program exits. Each task must have, at minimum: Unique ID, Title, Description, Completion status. Additional attributes (priority, tags, due dates, recurrence) are allowed only if specified.

### Terminal-First User Interface
Application must be fully operable via terminal (CLI). Prompts must be clear, human-readable, and error-tolerant. Invalid input must be handled gracefully. Background behaviors (e.g., reminders) must not block user input. Reminders must not go into infinite loop.

### Robust Error Handling
The application must never terminate unexpectedly. User-facing errors must show helpful messages. Stack traces must never be shown to the user.

### Project Structure Requirements
All Python-related files must reside inside the `/src` directory. Minimum required structure: /src with main.py (Application entry point), todo.py (Core todo logic), models.py (Task data models). Business logic must not live in main.py. Models must be separated from control flow. Additional Python modules may be added inside `/src` if required by later-phase specifications.

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
- Due dates with date and time
- Recurring tasks (only when time exist)
- Non-blocking CLI reminders
- Automatic rescheduling of recurring tasks

## Explicit Exclusions (All Phases)
The following must never be implemented:
- File or database persistence
- Authentication or multi-user support
- Networking or APIs
- GUI or web interface
- Automated testing frameworks
- External Python libraries

## Tooling Constraint
The project must use `uv` for environment and execution. `uv` commands must be runnable from within the project context. No alternative environment or dependency managers are allowed.

## Governance
This constitution governs all phases of the In-Memory Todo Console Application. All Claude-generated outputs must comply with this constitution. If a conflict arises, specification correctness and project progress take priority, but the constitution must not be amended.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
