---
description: "Task list for Todo Console App with Priorities, Tags, Search, and Sort feature"
---

# Tasks: Todo Console App with Priorities, Tags, Search and Sort

**Input**: Design documents from `/specs/002-todo-priorities-tags-search-sort/`
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

- [X] T001 Create src directory structure if not already present

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T002 [P] Extend Task model with priority, tags, and created_at fields in src/models.py
- [X] T003 [P] Update business logic in src/todo.py to support new Task fields
- [X] T004 Update CLI argument parsing to support new options in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create tasks with priorities and tags (Priority: P1) 🎯 MVP

**Goal**: Enable users to create tasks with priority levels and tags so that they can better organize and categorize their work.

**Independent Test**: Can be fully tested by creating tasks with different priority levels (high, medium, low) and various tags, and verifying they are properly stored in memory.

### Implementation for User Story 1

- [X] T005 [P] [US1] Add priority validation function to src/todo.py
- [X] T006 [P] [US1] Add tag validation function to src/todo.py
- [X] T007 [US1] Update add_task method in src/todo.py to accept priority and tags
- [X] T008 [US1] Update CLI to accept --priority and --tags options for add command in src/main.py
- [X] T009 [US1] Add error handling for invalid priority values in src/todo.py
- [X] T010 [US1] Add error handling for invalid tag values in src/todo.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Search tasks by content and tags (Priority: P1)

**Goal**: Allow users to search through their tasks by title, description, and tags so that they can quickly find specific tasks among many.

**Independent Test**: Can be fully tested by creating multiple tasks with different content and tags, then searching for specific keywords and verifying the correct tasks are returned.

### Implementation for User Story 2

- [X] T011 [P] [US2] Add search functionality to src/todo.py
- [X] T012 [P] [US2] Add case-insensitive search algorithm in src/todo.py
- [X] T013 [US2] Add CLI search command to main.py
- [X] T014 [US2] Handle empty string search to return all tasks in src/todo.py
- [X] T015 [US2] Add search results display formatting in src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Filter tasks by status, priority, and date (Priority: P2)

**Goal**: Allow users to filter their tasks by completion status, priority level, and creation date so that they can focus on specific subsets of tasks.

**Independent Test**: Can be fully tested by creating tasks with different statuses, priorities, and creation times, then applying various filters and verifying the correct tasks are displayed.

### Implementation for User Story 3

- [X] T016 [P] [US3] Add filter functionality to src/todo.py
- [X] T017 [P] [US3] Add completion status filter in src/todo.py
- [X] T018 [P] [US3] Add priority filter in src/todo.py
- [X] T019 [P] [US3] Add creation date filter (day-level granularity) in src/todo.py
- [X] T020 [US3] Update CLI list command to accept filter options in src/main.py
- [X] T021 [US3] Add filter validation and error handling in src/todo.py

**Checkpoint**: User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Sort tasks by various criteria (Priority: P2)

**Goal**: Allow users to sort their tasks by title, priority, and creation date so that they can view them in a meaningful order.

**Independent Test**: Can be fully tested by creating tasks with different titles, priorities, and creation times, then applying various sorting options and verifying the tasks are displayed in the correct order.

### Implementation for User Story 4

- [X] T022 [P] [US4] Add sort functionality to src/todo.py
- [X] T023 [P] [US4] Add alphabetical sort by title in src/todo.py
- [X] T024 [P] [US4] Add priority sort (high to low) in src/todo.py
- [X] T025 [P] [US4] Add creation date sort in src/todo.py
- [X] T026 [US4] Ensure stable sorting algorithm in src/todo.py
- [X] T027 [US4] Update CLI list command to accept sort options in src/main.py

**Checkpoint**: User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Update task priorities and tags (Priority: P3)

**Goal**: Allow users to update the priority and tags of existing tasks so that they can reorganize their tasks as their needs change.

**Independent Test**: Can be fully tested by creating tasks with specific priorities and tags, updating them, and verifying the changes are properly applied.

### Implementation for User Story 5

- [X] T028 [P] [US5] Add update priority functionality to src/todo.py
- [X] T029 [P] [US5] Add update tags functionality to src/todo.py
- [X] T030 [US5] Update CLI update command to accept priority and tags options in src/main.py
- [X] T031 [US5] Add validation for updated priority values in src/todo.py
- [X] T032 [US5] Add validation for updated tag values in src/todo.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T033 [P] Update documentation in src/main.py for all new features
- [X] T034 [P] Consolidate error handling across all modules
- [X] T035 Add comprehensive validation for all user inputs
- [X] T036 [P] Add help text for all new CLI options
- [X] T037 Run quickstart.md validation to ensure all features work as expected

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

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all parallel tasks for User Story 1 together:
Task: "Add priority validation function to src/todo.py"
Task: "Add tag validation function to src/todo.py"
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
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

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
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence