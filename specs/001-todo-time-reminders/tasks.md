---
description: "Task list for In-Memory Todo Console App with Recurring Tasks & Time-Based Reminders"
---

# Tasks: In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

**Input**: Design documents from `/specs/001-todo-time-reminders/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Constitution Compliance**: All tasks must adhere to In-Memory Todo Console Application Constitution requirements:
- Use only Python standard library (no external dependencies)
- Store data in memory only (no file/database persistence)
- All Python files must be in `/src` directory
- Must use `uv` for environment and execution
- Terminal-first CLI interface
- Robust error handling

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create src/ directory structure with models.py, todo.py, and main.py files
- [X] T002 Initialize uv project with pyproject.toml configuration
- [X] T003 [P] Create basic project files if they don't exist

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 [P] Extend Task model with due_at and recurrence fields in src/models.py
- [X] T005 [P] Implement basic TaskManager in src/todo.py with time-checking functionality
- [X] T006 [P] Set up CLI framework in src/main.py with basic commands
- [X] T007 Implement datetime parsing utility function in src/todo.py
- [X] T008 Implement recurrence calculation utility functions in src/todo.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Set Time-Based Reminders for Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to set due dates and times for tasks and receive terminal-based reminders when those tasks are due

**Independent Test**: Can be fully tested by creating a task with a due date/time in the near future and verifying that a reminder message appears in the terminal at the specified time, delivering the core value of time-based notifications.

### Implementation for User Story 1

- [X] T009 [P] [US1] Update Task model to support due_at datetime field in src/models.py
- [X] T010 [P] [US1] Implement time-checking loop in src/todo.py that runs every 10 seconds
- [X] T011 [US1] Implement reminder display function with format "[REMINDER] Task Title - Description (due: YYYY-MM-DD HH:MM)" in src/todo.py "only for 10 seconds"
- [X] T012 [US1] Update CLI to support adding tasks with due date in src/main.py
- [X] T013 [US1] Add due date parsing for multiple formats (MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD HH:MM) in src/main.py
- [X] T014 [US1] Implement reminder display during application runtime in src/todo.py
- [X] T015 [US1] Add reminder display for overdue tasks when application starts in src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Create Recurring Tasks (Priority: P2)

**Goal**: Enable users to mark tasks as recurring so they automatically reschedule themselves after their due date passes

**Independent Test**: Can be fully tested by creating a recurring task, waiting for its due time to pass, and verifying that the task gets rescheduled for the next occurrence while remaining in memory.

### Implementation for User Story 2

- [X] T016 [P] [US2] Update Task model to support recurrence field in src/models.py
- [X] T017 [P] [US2] Implement recurrence calculation logic for daily, weekly, monthly intervals in src/todo.py
- [X] T018 [US2] Implement monthly recurrence handling for invalid dates (e.g., Feb 30 → Feb 28/29) in src/todo.py
- [X] T019 [US2] Update time-checking logic to handle recurring task rescheduling in src/todo.py
- [X] T020 [US2] Update CLI to support adding tasks with recurrence options in src/main.py
- [X] T021 [US2] Update CLI to support updating tasks with recurrence options in src/main.py
- [X] T022 [US2] Add recurrence display in task listing functionality in src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Manage Time-Based Task Properties (Priority: P3)

**Goal**: Enable users to modify the due date/time and recurrence settings of their tasks to adjust their schedule as needed

**Independent Test**: Can be fully tested by creating a task with time-based properties, modifying those properties, and verifying that the changes take effect without errors.

### Implementation for User Story 3

- [X] T023 [US3] Update CLI to support modifying due date for existing tasks in src/main.py
- [X] T024 [US3] Update CLI to support modifying recurrence for existing tasks in src/main.py
- [X] T025 [US3] Update CLI to support disabling recurrence for existing tasks in src/main.py
- [X] T026 [US3] Add validation for updated due dates and recurrence values in src/todo.py
- [ ] T027 [US3] Add error handling for invalid time-based property updates in src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T028 [P] Update task listing to show due dates and recurrence in human-readable format in src/main.py
- [X] T029 [P] Add comprehensive error handling for all time-based operations in src/todo.py
- [X] T030 Add validation for recurrence values (daily, weekly, monthly, None) in src/todo.py
- [X] T031 Add proper error messages for invalid date/time formats in src/main.py
- [X] T032 Ensure application never crashes during time-based operations in src/todo.py
- [X] T033 Run quickstart.md validation to verify all features work together

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on time-checking infrastructure from US1
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Builds on time-checking and recurrence infrastructure from US1/US2

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Update Task model to support due_at datetime field in src/models.py"
Task: "Implement time-checking loop in src/todo.py that runs every 10 seconds"
Task: "Implement reminder display function with format in src/todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence