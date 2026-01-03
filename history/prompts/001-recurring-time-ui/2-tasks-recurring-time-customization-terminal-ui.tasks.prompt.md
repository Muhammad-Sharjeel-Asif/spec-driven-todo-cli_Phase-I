---
id: 2
title: Tasks recurring time customization terminal ui
stage: tasks
date: 2026-01-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-recurring-time-ui
branch: 001-recurring-time-ui
user: claude
command: /sp.tasks
labels: [feature, tasks, recurring-tasks, ui, time-formatting]
links:
  spec: /specs/001-recurring-time-ui/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - /specs/001-recurring-time-ui/tasks.md
tests:
 -
---
## Prompt

```text
$ARGUMENTS
```

## Response snapshot

# Tasks: Recurring Time Customization & Terminal UI Presentation

**Feature**: 001-recurring-time-ui
**Generated**: 2026-01-03
**Spec**: /specs/001-recurring-time-ui/spec.md
**Plan**: /specs/001-recurring-time-ui/plan.md

## Dependencies
- User Story 2 [US2] depends on foundational time utility functions from Setup phase
- User Story 3 [US3] depends on User Story 1 [US1] time setting functionality

## Parallel Execution Examples
- T001-T004 [P] can run in parallel (foundational setup)
- T010-T015 [P] [US1] can run in parallel (CLI and business logic for recurring time)
- T020-T025 [P] [US2] can run in parallel (UI formatting functions)

## Implementation Strategy
- **MVP**: Complete User Story 1 (P1) - custom time for recurring tasks creation
- **Incremental Delivery**: Add UI enhancements (US2), then update functionality (US3)
- **Final**: Polish and integration testing

---

## Phase 1: Setup Tasks

### Goal
Initialize foundational components needed for time handling and UI enhancements.

- [ ] T001 Create time utility functions in src/todo.py for HH:MM format validation
- [ ] T002 [P] Implement validate_time_format function using datetime.strptime with %H:%M format
- [ ] T003 [P] Create ANSI color code constants for UI formatting in src/main.py
- [ ] T004 [P] Add table formatting helper functions in src/main.py for column alignment

---

## Phase 2: Foundational Tasks

### Goal
Implement core functionality that supports all user stories.

- [ ] T005 Update advance_recurrence function in src/todo.py to preserve time component during advancement
- [ ] T006 [P] Modify existing recurring task logic to maintain time component across recurrences
- [ ] T007 [P] Add time parsing functionality for HH:MM format in src/todo.py
- [ ] T008 [P] Create helper function to combine date and time components in src/todo.py

---

## Phase 3: User Story 1 - Set Custom Time for Recurring Tasks (Priority: P1)

### Goal
Allow users to specify a custom time of day when creating recurring tasks.

### Independent Test Criteria
Can be fully tested by creating a recurring task with a custom time (e.g., "14:30") and verifying that the task appears at that time, and that future recurrences also maintain that time.

- [ ] T010 [US1] Update CLI prompt in src/main.py to ask for optional time when creating recurring tasks
- [ ] T011 [P] [US1] Implement time validation in src/main.py with error handling for invalid formats
- [ ] T012 [P] [US1] Modify add_task function in src/todo.py to accept and apply time to due_at field
- [ ] T013 [P] [US1] Set default time to 00:00 when no time is specified for recurring tasks
- [ ] T014 [US1] Test that recurring tasks preserve specified time across multiple recurrences
- [ ] T015 [US1] Add error handling for invalid time input with clear user feedback

---

## Phase 4: User Story 2 - View Enhanced Terminal UI with Table Formatting (Priority: P1)

### Goal
Display tasks in a clean, table-like format with visual indicators for task status.

### Independent Test Criteria
Can be fully tested by viewing the task list and verifying that tasks are displayed in aligned columns with headers and visual indicators for completed vs incomplete tasks.

- [ ] T020 [US2] Create format_task_table function in src/main.py for table-like task display
- [ ] T021 [P] [US2] Implement column alignment using string formatting methods (ljust, center, etc.)
- [ ] T022 [P] [US2] Add ANSI color formatting for completed vs incomplete tasks
- [ ] T023 [P] [US2] Apply color formatting for priority levels (high, medium, low)
- [ ] T024 [US2] Update View All Tasks menu option to use new table format
- [ ] T025 [US2] Ensure table formatting gracefully handles varying content lengths

---

## Phase 5: User Story 3 - Update Recurring Task Time (Priority: P2)

### Goal
Allow users to update the time of day for an existing recurring task.

### Independent Test Criteria
Can be fully tested by updating an existing recurring task with a new time and verifying that future recurrences use the new time.

- [ ] T030 [US3] Modify update_task function in src/todo.py to handle time updates for recurring tasks
- [ ] T031 [P] [US3] Update CLI update flow in src/main.py to allow time modification
- [ ] T032 [P] [US3] Ensure updated time is preserved across future recurrences
- [ ] T033 [US3] Add validation for time updates to recurring tasks
- [ ] T034 [US3] Test that time updates only affect future recurrences, not past ones

---

## Phase 6: Polish & Cross-Cutting Concerns

### Goal
Integrate all features and ensure consistent behavior across the application.

- [ ] T040 Add comprehensive error handling for all new time-related functionality
- [ ] T041 [P] Ensure UI formatting works correctly in terminals without color support
- [ ] T042 [P] Test that all existing functionality remains unchanged when new features are used
- [ ] T043 [P] Verify no infinite loops occur with recurring task time handling
- [ ] T044 [P] Validate all edge cases for time input (invalid formats, out-of-range values)
- [ ] T045 [P] Perform integration testing of all new features together
- [ ] T046 [P] Update help text and user prompts to reflect new time-setting capabilities
- [ ] T047 [P] Ensure graceful fallback when ANSI color codes are not supported

## Outcome

- ✅ Impact: Created comprehensive task breakdown for recurring time customization and terminal UI enhancements
- 🧪 Tests: No automated tests planned per constitution constraints
- 📁 Files: Created tasks.md with 30+ specific, actionable tasks organized by user story
- 🔁 Next prompts: Ready for implementation of individual tasks
- 🧠 Reflection: Tasks are well-organized by user story priority with clear dependencies and parallel execution opportunities

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of Phase 1 setup tasks