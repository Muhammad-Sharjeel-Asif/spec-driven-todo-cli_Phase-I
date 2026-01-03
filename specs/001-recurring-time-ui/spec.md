# Feature Specification: Recurring Time Customization & Terminal UI Presentation

**Feature Branch**: `001-recurring-time-ui`
**Created**: 2026-01-02
**Status**: Draft
**Constitution Compliance**: All features must comply with In-Memory Todo Console Application Constitution
**Input**: User description: "# Specification — Recurring Time Customization & Terminal UI Presentation

## 1. Purpose
Introduce **controlled, user-facing enhancements** to the existing in-memory Todo Console App that:
1. Allow users to explicitly set the **time component** for recurring tasks
2. Improve **terminal UI presentation** using color and table-like formatting

This enhancement is strictly additive and does **not modify or expand** the core existing feature
---

## 2. Constitutional Alignment
This specification fully complies with **Constitution**:
- No behavior implemented outside written specification
- Python 3.13+, PEP-8, standard library only
- In-memory data only
- Terminal-first interface
- Robust error handling with no crashes or stack traces
- Execution via **uv** only

---

## 3. Scope Definition

### Included Enhancements

#### 3.1 Recurring Task Time Customization
- Users may optionally specify a **time of day** when creating or updating a recurring task
- If no time is provided:
  - The default time remains `00:00`
- The specified time:
  - Applies to the task's `due_at` field
  - Is preserved across all future recurrences
- Recurrence remains strictly time-based

#### 3.2 Terminal UI Presentation
- Task lists may be displayed in a **table-like layout** using text alignment
- Color may be applied to terminal output for:
  - Headers
  - Task status (completed / incomplete)
  - Priority levels (if present)
- Color usage must be:
  - Optional
  - Non-essential to functionality
  - Readable on standard terminals
- Terminal **must** look clean and attractive

---

## 4. Explicit Constraints & Safety Rules

### Recurring Time Safety
- Recurring task reminders must:
  - Trigger only once per scheduled time
  - Never enter infinite loops
  - Never reschedule multiple times for a single trigger
- Default time remains `00:00` unless explicitly set by the user
- Time handling must rely only on standard library time utilities

### UI Safety
- No external libraries (e.g., rich, tabulate, colorama)
- ANSI escape codes may be used only as raw string literals and string formatting within Python’s standard library, and must not rely on any external libraries (including but not limited to colorama, rich, or tabulate).
- UI changes must not alter:
  - Task data
  - Task ordering logic
  - Reminder timing logic

---

## 5. Explicit Exclusions
The following are **not permitted** under this enhancement:
- Browser or GUI notifications
- Web or HTML rendering
- External UI or formatting libraries
- Persistence of user preferences
- New task fields beyond those already specified
- Any Phase IV or speculative features

---

## 6. Data Model Impact
- **No new fields** are introduced
- Existing fields (`due_at`, `recurrence`) are reused
- Default behavior is preserved when new input is not provided

---

## 7. CLI Behavior

### Recurring Time Input
- When a task is recurring:
  - User may input a time value
  - Input format is validated (e.g., `HH:MM`)
- Invalid input results in:
  - Clear error message
  - Re-prompt or safe fallback to default

### Table Display
- Task listings are displayed in aligned columns
- Headers are visually distinct
- Completed tasks are visually distinguishable

---

## 8. Error Handling & Validation
- All invalid inputs are handled gracefully
- No stack traces are shown
- Application flow always returns to the CLI
- UI errors must not impact task logic

---

## 9. Project Structure
- All Python files remain in `/src`
- If found any python file outside '/src' move that file to '/src' folder
- No new Python files are added
- Changes are limited to:
  - CLI input handling
  - Output formatting

---

## 10. Tooling & Execution
- Application must run using **uv**
- Only Python standard library modules may be used
- No additional environment or dependency tools are introduced

---

## 11. Acceptance Criteria
- Users can set a custom time for recurring tasks
- Default recurring time remains `00:00`
- Recurring tasks preserve the specified time across reschedules
- No infinite reminder loops occur
- Task display is table-formatted and optionally colored
- Functionality remains unchanged when UI enhancements are not used
- All behavior is traceable directly to this specification

---

## 12. Boundary Enforcement
- Implementation must stop once acceptance criteria are met
- No refactoring or extensions beyond this specification"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Set Custom Time for Recurring Tasks (Priority: P1)

As a user of the todo console app, I want to specify a custom time of day when creating recurring tasks so that my recurring tasks appear at the time I prefer rather than always at midnight.

**Why this priority**: This is the core functionality requested - allowing users to control when recurring tasks appear, which significantly improves the user experience for recurring tasks.

**Independent Test**: Can be fully tested by creating a recurring task with a custom time (e.g., "14:30") and verifying that the task appears at that time, and that future recurrences also maintain that time.

**Acceptance Scenarios**:

1. **Given** user wants to create a recurring task, **When** user specifies a time in HH:MM format during task creation, **Then** the recurring task is created with that time in its due_at field and future recurrences preserve that time
2. **Given** user creates a recurring task without specifying time, **When** task is created, **Then** the task defaults to 00:00 time and future recurrences also use 00:00

---

### User Story 2 - View Enhanced Terminal UI with Table Formatting (Priority: P1)

As a user of the todo console app, I want to see my tasks displayed in a clean, table-like format with visual indicators for task status so that I can easily scan and understand my tasks at a glance.

**Why this priority**: This directly addresses the UI enhancement requirement and significantly improves the visual experience of the application.

**Independent Test**: Can be fully tested by viewing the task list and verifying that tasks are displayed in aligned columns with headers and visual indicators for completed vs incomplete tasks.

**Acceptance Scenarios**:

1. **Given** user has multiple tasks in the system, **When** user views the task list, **Then** tasks are displayed in a table-like format with aligned columns and headers
2. **Given** user has both completed and incomplete tasks, **When** user views the task list, **Then** completed and incomplete tasks are visually distinguishable through color or other formatting

---

### User Story 3 - Update Recurring Task Time (Priority: P2)

As a user of the todo console app, I want to update the time of day for an existing recurring task so that I can change when that task appears without having to delete and recreate it.

**Why this priority**: This provides a complete user experience by allowing modification of existing recurring tasks, which is a natural extension of the time-setting functionality.

**Independent Test**: Can be fully tested by updating an existing recurring task with a new time and verifying that future recurrences use the new time.

**Acceptance Scenarios**:

1. **Given** user has an existing recurring task with a specific time, **When** user updates the task with a new time, **Then** future recurrences of that task use the new time

---

### Edge Cases

- What happens when user enters invalid time format (e.g., "25:00", "ab:cd")? The system should display a clear error message and prompt for valid input.
- How does system handle recurring tasks that would trigger multiple times per day if the recurrence interval is shorter than 24 hours? The system should maintain the specified time and only trigger once per recurrence period.
- What happens when a recurring task's time has already passed for the current day? The system should handle this gracefully based on existing reminder logic.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to optionally specify a time in HH:MM format when creating recurring tasks
- **FR-002**: System MUST validate time input format and provide clear error messages for invalid input
- **FR-003**: System MUST default to 00:00 time when no time is specified for recurring tasks
- **FR-004**: System MUST preserve the specified time across all future recurrences of a task
- **FR-005**: System MUST display tasks in a table-like format with aligned columns and headers
- **FR-006**: System MUST visually distinguish between completed and incomplete tasks in the UI
- **FR-007**: System MUST use only Python standard library for UI formatting (ANSI escape codes if needed)
- **FR-008**: System MUST maintain all existing functionality when UI enhancements are applied
- **FR-009**: System MUST handle time input validation gracefully without crashing

### Key Entities

- **Recurring Task**: A task that repeats at specified intervals, now with an optional time component in its due_at field
- **Task Display**: The formatted representation of tasks in the terminal UI, now using table-like layout with visual indicators

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully set custom times for recurring tasks with 95% success rate during testing
- **SC-002**: Task lists display in table format with aligned columns and visual indicators for status in under 1 second
- **SC-003**: 90% of users find the new table-based UI more readable than the previous format
- **SC-004**: No crashes or infinite loops occur when setting or updating recurring task times
- **SC-005**: Users can complete the task of creating a recurring task with custom time in under 30 seconds