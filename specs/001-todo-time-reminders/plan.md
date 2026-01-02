# Implementation Plan: In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

**Branch**: `001-todo-time-reminders` | **Date**: 2026-01-02 | **Spec**: specs/001-todo-time-reminders/spec.md
**Input**: Feature specification from `/specs/001-todo-time-reminders/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Extend the existing in-memory Todo Console App with time-based task behavior limited to: 1) recurring task rescheduling with daily, weekly, and monthly intervals, and 2) due date and time-based reminders that trigger terminal notifications. Implementation will extend the existing Task model with due_at and recurrence fields, add time-checking logic that runs every 10 seconds during runtime, and update the CLI to allow users to set due dates/times and recurrence options.

## Technical Context

**Language/Version**: Python 3.13+ with PEP-8 conventions (from Constitution)
**Primary Dependencies**: Python standard library only (from Constitution)
**Storage**: In-memory only, no persistence (from Constitution and Spec)
**Testing**: N/A - no automated testing frameworks allowed (from Constitution)
**Target Platform**: Cross-platform terminal application (from Constitution)
**Project Type**: Single terminal-based Python application (from Constitution)
**Performance Goals**: Sub-second response time for CLI operations, 10-second reminder display (from Spec)
**Constraints**: No external libraries, no persistence, terminal-first operation, controlled time checks every 10 seconds (from Spec)
**Scale/Scope**: Single-user, in-memory task management with time-based reminders (from Spec)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Language Compliance**: Python 3.13+ with PEP-8 conventions (from Constitution)
- **No External Dependencies**: Use only Python standard library unless explicitly allowed (from Constitution)
- **In-Memory Storage**: No file, database, or external persistence allowed (from Constitution)
- **Terminal-First UI**: Application must be fully operable via CLI (from Constitution)
- **Error Handling**: Never terminate unexpectedly, show helpful messages to users (from Constitution)
- **Project Structure**: All Python files must be in /src directory (from Constitution)
- **Tooling**: Must use `uv` for environment and execution (from Constitution)

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models.py          # Task data model with time-based extensions
├── todo.py            # Core todo logic and time-based checks
└── main.py            # CLI and user interaction
```

**Structure Decision**: Single project structure with three required files as specified in the constitution and feature spec. The existing structure is maintained with extensions to support time-based functionality.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
