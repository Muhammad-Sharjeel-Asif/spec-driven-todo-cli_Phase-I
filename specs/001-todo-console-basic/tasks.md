---
description: "Task list for Todo Console Basic feature implementation"
---

# Tasks: Todo Console Basic

**Input**: Design documents from `/specs/001-todo-console-basic/`
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

- [x] T001 Create project structure with src directory in repository root
- [x] T002 [P] Create empty models.py file in src/models.py
- [x] T003 [P] Create empty todo.py file in src/todo.py
- [x] T004 [P] Create empty main.py file in src/main.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Task model class in src/models.py with id (int), title (str), description (str), completed (bool) fields
- [x] T006 Implement in-memory task storage with list in src/todo.py
- [x] T007 Implement unique sequential ID assignment starting from 1 in src/todo.py, ensuring IDs are not reused after deletion
- [x] T008 Implement input validation functions in src/todo.py for title/description length limits (100/500 chars) and empty title validation
- [x] T009 Implement error handling infrastructure in src/todo.py to prevent crashes and show user-friendly messages
- [x] T010 Create basic CLI menu structure in src/main.py that imports from todo.py and models.py
- [x] T011 Implement performance validation to ensure each task operation completes in under 1 second

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: User can create a new task in their todo list with a title and optional description using a menu-driven interface

**Independent Test**: User can add a new task with title and description, then view it in the list

### Implementation for User Story 1

- [x] T012 [P] [US1] Implement add_task function in src/todo.py that accepts title (required) and description (optional), validates input, assigns unique ID, and stores in memory
- [x] T013 [US1] Implement CLI menu option for adding tasks in src/main.py that prompts user for title and description, validates input, and calls todo.add_task
- [x] T014 [US1] Test that adding a task with valid title creates a new task with unique ID and displays in task list

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: User can see all their tasks with their completion status using a menu-driven interface

**Independent Test**: User can see a list of all tasks with their IDs, titles, descriptions, and completion status

### Implementation for User Story 2

- [x] T015 [P] [US2] Implement get_all_tasks function in src/todo.py that returns all tasks with their ID, title, description, and completion status
- [x] T016 [US2] Implement CLI menu option for viewing all tasks in src/main.py that displays tasks in a readable format with ID, title, description, and completion status
- [x] T017 [US2] Test that viewing tasks shows all tasks with proper status indicators and handles empty list case

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: User can modify the title or description of an existing task using a menu-driven interface

**Independent Test**: User can update an existing task's title or description by providing the task ID

### Implementation for User Story 3

- [x] T018 [P] [US3] Implement update_task function in src/todo.py that accepts task_id and new title/description values, validates input, and updates the task
- [x] T019 [US3] Implement CLI menu option for updating tasks in src/main.py that prompts for task ID and new title/description values, validates input, and calls todo.update_task
- [x] T020 [US3] Test that updating a task with valid ID and data updates the task properly and handles invalid ID case

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: User can remove a task from their todo list using a menu-driven interface

**Independent Test**: User can delete a task by providing its ID

### Implementation for User Story 4

- [x] T021 [P] [US4] Implement delete_task function in src/todo.py that accepts task_id, removes the task, and ensures IDs are not reused after deletion
- [x] T022 [US4] Implement CLI menu option for deleting tasks in src/main.py that prompts for task ID, validates existence, and calls todo.delete_task
- [x] T023 [US4] Test that deleting a task with valid ID removes it and handles invalid ID case, ensuring ID is not reused

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: User can mark a task as completed or mark it as incomplete if it was previously completed using a menu-driven interface

**Independent Test**: User can change the completion status of a task by providing its ID

### Implementation for User Story 5

- [x] T024 [P] [US5] Implement mark_task_complete function in src/todo.py that accepts task_id and completion status, updates the task, and returns updated task
- [x] T025 [US5] Implement CLI menu option for marking tasks complete/incomplete in src/main.py that prompts for task ID and completion status, validates input, and calls todo.mark_task_complete
- [x] T026 [US5] Test that marking tasks complete/incomplete updates the status properly and handles invalid ID case

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T027 [P] Add comprehensive error handling for all user inputs in src/main.py
- [x] T028 [P] Add input validation for all user inputs across all functions in src/todo.py
- [x] T029 [P] Add user-friendly error messages for all error cases in src/main.py
- [x] T030 [P] Ensure no stack traces are shown to users in any error condition
- [x] T031 [P] Final performance validation to ensure each task operation completes in under 1 second
- [x] T032 Run quickstart.md validation to verify application works as expected

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Stories 1 and 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test User Stories 1 and 2 independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 + 2 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 3 → Test independently → Deploy/Demo
4. Add User Story 4 → Test independently → Deploy/Demo
5. Add User Story 5 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence