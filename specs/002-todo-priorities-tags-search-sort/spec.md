# Feature Specification: Todo Console App with Priorities, Tags, Search and Sort

**Feature Branch**: `002-todo-priorities-tags-search-sort`
**Created**: 2026-01-01
**Status**: Draft
**Constitution Compliance**: All features must comply with In-Memory Todo Console Application Constitution
**Input**: User description: "# Specification — In-Memory Todo Console App (Priorities, Tags, Search, Sort)

## 1. Purpose
Extend the in-memory Todo Console App with **organizational and discovery features** while fully preserving:
- In-memory–only behavior
- Terminal-first CLI operation
- Clean, minimal, and readable Python code

No further features are included or anticipated.

---

## 2. Constitutional Alignment
This specification strictly complies with **Constitution**:
- All features are explicitly specified before implementation
- No persistence, networking, GUI, authentication, or external libraries
- Python 3.13+, PEP-8, standard library only
- All tasks remain **in memory only**
- Robust error handling with no crashes or stack traces
- Terminal-first, human-readable CLI
- Execution and environment management via **uv** only

---

## 3. Scope Definition

### Included Features
1. **Priorities**
   - Assign exactly one priority level per task
   - Allowed values:
     - `high`
     - `medium`
     - `low`

2. **Tags / Categories**
   - Assign zero or more textual labels to a task
   - Examples: `work`, `home`, `study`
   - Tags are simple strings without hierarchy

3. **Search**
   - Keyword-based search over:
     - Task title
     - Task description
     - Tags

4. **Filtering**
   - Filter tasks by:
     - Completion status (completed / incomplete)
     - Priority level
     - Creation date (same-session only)

5. **Sorting**
   - Reorder task display by:
     - Alphabetical order of title
     - Priority level
     - Creation date

---

## 4. Explicit Exclusions
The following are **not allowed**:
- Due dates or times
- Recurring tasks
- Background threads, timers, or reminders
- Persistence (file system or database)
- Networking or APIs
- GUI or web interfaces
- Automated testing frameworks
- External libraries
- Advance features of any kind

---

## 5. Data Model Extension

### Task Fields
The task model is extended with the following **Phase-II–only fields**:

| Field        | Type        | Description                                  |
|-------------|-------------|----------------------------------------------|
| id          | int         | Unique identifier (runtime only)             |
| title       | str         | Task title                                   |
| description | str         | Optional description                         |
| completed   | bool        | Completion status                            |
| priority    | str         | One of: high / medium / low                  |
| tags        | list[str]   | Zero or more category labels                 |
| created_at  | datetime    | In-memory creation timestamp (session only) |

### Constraints
- No additional fields are allowed
- No persistence of timestamps beyond runtime
- No derived or computed fields stored on the model

---

## 6. CLI Behavior & User Interaction

### Priority & Tags
- User may set priority and tags at task creation
- User may update priority and tags during task update
- Invalid priority values are rejected with a clear message

### Search
- User can search tasks using a keyword
- Search is case-insensitive
- Search results are displayed without modifying stored data

### Filtering
- Filters are applied at display-time only
- Multiple filters may be applied sequentially
- Filters do not mutate the task list

### Sorting
- Sorting affects display order only
- Original in-memory task order is preserved unless explicitly re-sorted again
- Sorting options are user-selectable via CLI

---

## 7. Error Handling & Validation
- All invalid inputs are handled gracefully
- Examples:
  - Invalid priority value
  - Invalid filter or sort option
  - Empty search results
- The application must:
  - Never crash
  - Never display stack traces
  - Always return control to the CLI loop

---

## 8. Project Structure
All files must reside in `/src` only.

Required files:
- `main.py` — CLI interaction and input handling
- `todo.py` — core business logic
- `models.py` — task data model

No additional Python files are permitted unless introduced by a future specification.

---

## 9. Tooling & Execution
- The application must be executed using **uv**
- No alternative environment or dependency tools are allowed
- Only Python standard library modules may be used

---

## 10. Acceptance Criteria
- Tasks support priority and tags
- Search returns correct matching tasks
- Filters work by status, priority, and creation date
- Sorting works alphabetically, by priority, and by creation date
- All behavior remains in memory only
- No excluded or future features are present
- Every behavior is directly traceable to this specification

---

## 11. Phase Boundary Enforcement
- Implementation must stop once acceptance criteria are met
- No refactoring or optimization beyond specification
- Any additional functionality requires a new specification"

## Clarifications

### Session 2026-01-01

- Q: What happens when a user searches for an empty string? → A: Return all tasks
- Q: For creation date filtering, what granularity should be supported? → A: By day
- Q: Should there be validation or restrictions on tag names? → A: Basic validation
- Q: Should sorting be stable when multiple tasks have the same sort value? → A: Yes, stable sort
- Q: When sorting by priority, what should be the order? → A: High to Low

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create tasks with priorities and tags (Priority: P1)

As a user, I want to create tasks with priority levels and tags so that I can better organize and categorize my work.

**Why this priority**: This is the foundational functionality that enables all other organizational features. Without the ability to assign priorities and tags during task creation, the other features (search, filter, sort) would have no data to work with.

**Independent Test**: Can be fully tested by creating tasks with different priority levels (high, medium, low) and various tags, and verifying they are properly stored in memory.

**Acceptance Scenarios**:

1. **Given** I am in the todo app, **When** I create a new task with priority "high" and tags "work, urgent", **Then** the task is created with the specified priority and tags
2. **Given** I am creating a task, **When** I provide an invalid priority value, **Then** I receive a clear error message and the task is not created
3. **Given** I am creating a task, **When** I provide no tags, **Then** the task is created with an empty tags list

---

### User Story 2 - Search tasks by content and tags (Priority: P1)

As a user, I want to search through my tasks by title, description, and tags so that I can quickly find specific tasks among many.

**Why this priority**: This provides the core discovery functionality that makes large task lists manageable. It's essential for users who have many tasks and need to find specific ones quickly.

**Independent Test**: Can be fully tested by creating multiple tasks with different content and tags, then searching for specific keywords and verifying the correct tasks are returned.

**Acceptance Scenarios**:

1. **Given** I have tasks with various titles, descriptions, and tags, **When** I search for a keyword that appears in a task title, **Then** all matching tasks are displayed
2. **Given** I have tasks with various titles, descriptions, and tags, **When** I search for a tag name, **Then** all tasks with that tag are displayed
3. **Given** I search for a keyword that doesn't exist in any task, **When** I execute the search, **Then** I see a message indicating no matches were found

---

### User Story 3 - Filter tasks by status, priority, and date (Priority: P2)

As a user, I want to filter my tasks by completion status, priority level, and creation date so that I can focus on specific subsets of tasks.

**Why this priority**: This allows users to narrow down their task list to focus on what's most relevant to their current needs, improving productivity and focus.

**Independent Test**: Can be fully tested by creating tasks with different statuses, priorities, and creation times, then applying various filters and verifying the correct tasks are displayed.

**Acceptance Scenarios**:

1. **Given** I have tasks with different completion statuses, **When** I apply a "completed" filter, **Then** only completed tasks are displayed
2. **Given** I have tasks with different priority levels, **When** I apply a "high" priority filter, **Then** only high priority tasks are displayed
3. **Given** I have tasks created at different times, **When** I apply a date filter, **Then** only tasks created within the specified date range are displayed

---

### User Story 4 - Sort tasks by various criteria (Priority: P2)

As a user, I want to sort my tasks by title, priority, and creation date so that I can view them in a meaningful order.

**Why this priority**: This enhances the user experience by allowing users to organize their task list in ways that make sense for their workflow and preferences.

**Independent Test**: Can be fully tested by creating tasks with different titles, priorities, and creation times, then applying various sorting options and verifying the tasks are displayed in the correct order.

**Acceptance Scenarios**:

1. **Given** I have tasks with different titles, **When** I sort by title, **Then** tasks are displayed alphabetically by title
2. **Given** I have tasks with different priorities, **When** I sort by priority, **Then** tasks are displayed in priority order (high, medium, low)
3. **Given** I have tasks created at different times, **When** I sort by creation date, **Then** tasks are displayed in chronological order

---

### User Story 5 - Update task priorities and tags (Priority: P3)

As a user, I want to update the priority and tags of existing tasks so that I can reorganize my tasks as my needs change.

**Why this priority**: This provides flexibility to adjust task organization over time as priorities shift and new information becomes available.

**Independent Test**: Can be fully tested by creating tasks with specific priorities and tags, updating them, and verifying the changes are properly applied.

**Acceptance Scenarios**:

1. **Given** I have a task with a specific priority, **When** I update its priority, **Then** the task's priority is changed to the new value
2. **Given** I have a task with specific tags, **When** I update its tags, **Then** the task's tags are changed to the new values
3. **Given** I attempt to update a task with invalid priority, **When** I submit the update, **Then** I receive an error message and the task remains unchanged

---

### Edge Cases

- What happens when a user searches for an empty string? The system should return all tasks to allow resetting the search view.
- How does the system handle invalid priority values during creation or update? The system should reject them with a clear error message.
- What happens when a user tries to filter by a non-existent priority level? The system should handle gracefully and return no results.
- How does the system handle case-insensitive search? Search should work regardless of case differences.
- What happens when a task has no tags and the user searches for tags? The system should handle this scenario appropriately.
- How does the system handle date filtering? Date filtering should be by day granularity (e.g., today, yesterday, specific date).
- How does the system validate tags? Tags should have basic validation allowing letters, numbers, spaces, hyphens, and underscores only.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to assign exactly one priority level (high, medium, low) to each task during creation
- **FR-002**: System MUST allow users to assign zero or more textual tags to each task during creation
- **FR-003**: System MUST validate priority values and reject invalid ones with a clear error message
- **FR-004**: System MUST support case-insensitive keyword search across task titles, descriptions, and tags
- **FR-005**: System MUST allow users to filter tasks by completion status (completed/incomplete)
- **FR-006**: System MUST allow users to filter tasks by priority level (high, medium, low)
- **FR-007**: System MUST allow users to filter tasks by creation date (within the current session) with day-level granularity
- **FR-008**: System MUST allow users to sort tasks alphabetically by title
- **FR-009**: System MUST allow users to sort tasks by priority level in high-to-low order (high first)
- **FR-010**: System MUST allow users to sort tasks by creation date (oldest to newest or newest to oldest)
- **FR-011**: System MUST allow users to update priority and tags of existing tasks
- **FR-012**: System MUST display search results without modifying the original task list in memory
- **FR-013**: System MUST preserve the original task order unless explicitly re-sorted
- **FR-014**: System MUST handle all invalid inputs gracefully without crashing
- **FR-015**: System MUST never display stack traces to users
- **FR-016**: System MUST return all tasks when searching with an empty string
- **FR-017**: System MUST validate tags using basic validation (letters, numbers, spaces, hyphens, underscores only)
- **FR-018**: System MUST use stable sorting algorithms to maintain consistent ordering of equal elements

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single todo item with id, title, description, completion status, priority level, tags list, and creation timestamp. All data exists only in memory during the session.
- **Priority**: An attribute of a task that can have one of three values: high, medium, or low, used for organization and sorting.
- **Tag**: A textual label that can be associated with zero or more tasks for categorization and searching purposes. Tags must pass basic validation (letters, numbers, spaces, hyphens, underscores only).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create tasks with priority levels and tags in under 30 seconds
- **SC-002**: Search functionality returns results within 1 second for up to 1000 tasks
- **SC-003**: 95% of users can successfully filter tasks by priority without assistance
- **SC-004**: Users can sort tasks by any available criterion in under 5 seconds
- **SC-005**: System handles all invalid inputs gracefully without crashes (100% of test cases)
- **SC-006**: Users can update task priorities and tags successfully in 95% of attempts
- **SC-007**: All functionality remains in-memory only with no persistence to disk
- **SC-008**: Users can find specific tasks using search functionality in 90% of attempts
