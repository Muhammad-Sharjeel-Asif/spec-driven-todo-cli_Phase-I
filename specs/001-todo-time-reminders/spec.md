# Feature Specification: In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

**Feature Branch**: `001-todo-time-reminders`
**Created**: 2026-01-02
**Status**: Draft
**Constitution Compliance**: All features must comply with In-Memory Todo Console Application Constitution
**Input**: User description: "# Specification — In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

## 1. Purpose
Extend the existing in-memory Todo Console App with **time-based task behavior** limited strictly to:
- Recurring task rescheduling
- Due date and time-based reminders

No functionality outside this scope is permitted.

---

## 2. Constitutional Alignment
This specification fully complies with **Constitution**:
- Python 3.13+, PEP-8, standard library only
- In-memory task management only
- Terminal-first CLI operation
- No GUI or web interface
- No networking or external services
- Robust error handling with no crashes or stack traces
- Execution via **uv** only

> Note: Due to constitutional constraints, reminders are delivered via **terminal-based time notifications**, not via web or browser-based interfaces.

---

## 3. Scope Definition

### Included Features

1. **Recurring Tasks**
   - Tasks may be marked as recurring
   - Supported recurrence intervals:
     - Daily
     - Weekly
     - Monthly
   - When a recurring task reaches its due time:
     - The task is automatically rescheduled to its next occurrence
     - The task remains in memory only
   - Recurrence behavior is strictly time-based

2. **Due Dates & Time-Based Reminders**
   - Tasks may have an optional due date and time
   - At the specified time:
     - A reminder message is displayed in the terminal
   - Reminders are triggered only once per scheduled time for 10 seconds only

---

## 4. Explicit Constraints & Safety Rules

- Recurring task reminders **must not** cause infinite loops
- Each reminder is triggered only at its scheduled time
- No busy-waiting or uncontrolled looping is allowed
- Time checks must be controlled and non-blocking
- No background threads or asynchronous schedulers that persist beyond program runtime
- No browser-based or GUI notifications are permitted

---

## 5. Explicit Exclusions
The following are **not allowed**:
- File or database persistence
- Web or browser interfaces
- System tray or OS-level notifications
- External libraries or schedulers
- Networking or APIs
- Automated testing frameworks
- Any Phase IV or speculative features

---

## 6. Data Model Extension

### Task Fields
The task model is extended with the following **given fields only**:

| Field          | Type        | Description                                      |
|----------------|-------------|--------------------------------------------------|
| id             | int         | Unique runtime identifier                        |
| title          | str         | Task title                                       |
| description    | str         | Optional description                             |
| completed      | bool        | Completion status                                |
| priority       | str         | existing field                                   |
| tags           | list[str]   | existing field                                   |
| created_at     | datetime    | In-memory creation timestamp                     |
| due_at         | datetime    | Optional due date and time                       |
| recurrence     | str \| None | One of: daily / weekly / monthly / None          |

### Constraints
- No additional fields are allowed
- No persistence of dates or schedules beyond runtime
- No derived or cached scheduling state stored on the model

---

## 7. Reminder & Recurrence Behavior

### Reminder Rules
- Reminders are checked against the current system time
- A reminder is shown only when the current time reaches or exceeds `due_at`
- Once triggered, the reminder is not repeated for the same due time
- Reminder messages follow the format: "[REMINDER] Task Title - Description (due: YYYY-MM-DD HH:MM)"
- The application checks for due tasks every 10 seconds during runtime
- Only show reminders for tasks due during the current session

### Recurrence Rules
- After a recurring task reminder triggers:
  - The task's `due_at` is advanced exactly one interval forward
  - The task is not duplicated
- Recurrence advancement occurs only once per trigger
- No recursive or immediate re-triggering is allowed
- When rescheduling monthly recurring tasks, if the target day doesn't exist in the next month, use the last day of that month

---

## 8. CLI Behavior
- Users may:
  - Set or update due date and time via terminal input
  - Enable or disable recurrence for a task
- All inputs are validated with clear error messages
- All reminder messages are displayed in the terminal in a human-readable format
- The system accepts multiple common date/time formats (MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD HH:MM, etc.)

---

## 9. Error Handling & Validation
- Handle invalid date/time input gracefully
- Handle unsupported recurrence values with clear feedback
- Ensure:
  - Application never crashes
  - No stack traces are displayed
  - Control always returns to the CLI loop

---

## 10. Project Structure
All Python files must remain in `/src` only.

Required files:
- `main.py` — CLI and user interaction
- `todo.py` — business logic and time-based checks
- `models.py` — task data model

No additional Python modules are permitted.

---

## 11. Tooling & Execution
- Application must run using **uv**
- Only Python standard library modules may be used
- No alternative environment or dependency tools are allowed

---

## 12. Acceptance Criteria
- Tasks can have optional due dates and times
- Terminal-based reminders trigger at the correct time
- Recurring tasks reschedule correctly without duplication
- No infinite loops occur
- All behavior is time-based and in-memory only
- No excluded or future features are present
- Every behavior is traceable directly to this specification

---

## 13. Phase Boundary Enforcement
- Implementation must stop once acceptance criteria are met
- No refactoring or extensions beyond this specification
- Any future functionality requires a new specification"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Set Time-Based Reminders for Tasks (Priority: P1)

As a user of the todo console app, I want to be able to set due dates and times for my tasks so that I can receive timely reminders in the terminal when those tasks are due. This will help me stay on track with my responsibilities and not miss important deadlines.

**Why this priority**: This is the core functionality of the feature - without the ability to set and receive time-based reminders, the feature doesn't deliver its primary value proposition.

**Independent Test**: Can be fully tested by creating a task with a due date/time in the near future and verifying that a reminder message appears in the terminal at the specified time, delivering the core value of time-based notifications.

**Acceptance Scenarios**:

1. **Given** I have created a task with a due date/time in the future, **When** the current time reaches the due time, **Then** a reminder message appears in the terminal for 10 seconds
2. **Given** I have a task with a due date/time that has passed, **When** I start the application, **Then** I see a reminder message for that overdue task
3. **Given** I have multiple tasks with different due times, **When** their due times arrive, **Then** I receive reminders for each task at the appropriate time

---

### User Story 2 - Create Recurring Tasks (Priority: P2)

As a user of the todo console app, I want to be able to mark tasks as recurring so that they automatically reschedule themselves after their due date passes. This will help me manage regular tasks like daily routines, weekly reviews, or monthly reports without having to manually recreate them.

**Why this priority**: This provides significant value for users who have regular, repeating tasks, but builds upon the core reminder functionality.

**Independent Test**: Can be fully tested by creating a recurring task, waiting for its due time to pass, and verifying that the task gets rescheduled for the next occurrence while remaining in memory.

**Acceptance Scenarios**:

1. **Given** I have created a daily recurring task with a due time, **When** the due time passes and the reminder triggers, **Then** the task's due date is advanced by one day
2. **Given** I have created a weekly recurring task, **When** the due time passes, **Then** the task reschedules itself for the same day of the following week
3. **Given** I have created a monthly recurring task, **When** the due time passes, **Then** the task reschedules itself for the same day of the following month

---

### User Story 3 - Manage Time-Based Task Properties (Priority: P3)

As a user of the todo console app, I want to be able to modify the due date/time and recurrence settings of my tasks so that I can adjust my schedule as needed without losing the time-based functionality.

**Why this priority**: This provides flexibility and control over time-based tasks, but is secondary to the core functionality of setting and receiving reminders.

**Independent Test**: Can be fully tested by creating a task with time-based properties, modifying those properties, and verifying that the changes take effect without errors.

**Acceptance Scenarios**:

1. **Given** I have a task with a due date/time, **When** I update the due date/time, **Then** the new due time is used for future reminders
2. **Given** I have a non-recurring task, **When** I enable recurrence, **Then** the task will reschedule after its due time passes
3. **Given** I have a recurring task, **When** I disable recurrence, **Then** the task will not reschedule after its due time passes

---

### Edge Cases

- What happens when multiple tasks are due at the same time? (All reminders should be displayed)
- How does the system handle invalid date/time formats during input? (Should show clear error messages and not crash)
- What happens when the system clock is changed backward past a due time? (Should handle appropriately without infinite loops)
- How does the system handle recurrence for monthly tasks on days that don't exist in all months? (Should advance to the last day of the month if the target day doesn't exist)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to set optional due date and time for tasks
- **FR-002**: System MUST display reminder messages in the terminal when a task's due time is reached or exceeded
- **FR-003**: System MUST limit reminder display to 10 seconds per due time
- **FR-004**: System MUST support three recurrence intervals: daily, weekly, and monthly
- **FR-005**: System MUST automatically reschedule recurring tasks to their next occurrence after the due time passes
- **FR-006**: System MUST validate date/time input and provide clear error messages for invalid formats
- **FR-007**: System MUST validate recurrence values and provide clear feedback for unsupported values
- **FR-008**: System MUST ensure application never crashes or displays stack traces during time-based operations
- **FR-009**: System MUST return control to the CLI loop after handling time-based operations
- **FR-010**: System MUST prevent infinite loops in recurring task reminders

### Key Entities

- **Task**: Represents a user's todo item with optional time-based properties including due_at (datetime) and recurrence (str | None)
- **Reminder**: A time-based notification that appears in the terminal when a task's due time is reached or exceeded
- **Recurrence**: A time interval (daily, weekly, monthly) that determines how recurring tasks are rescheduled after their due time passes

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully set due dates and times for tasks with 95% success rate (no crashes or errors)
- **SC-002**: Reminder messages appear in the terminal within 1 second of the due time being reached
- **SC-003**: Recurring tasks reschedule correctly 100% of the time without duplication or infinite loops
- **SC-004**: The application handles invalid date/time input gracefully without crashing 100% of the time
- **SC-005**: Users can modify time-based properties of tasks without losing functionality 95% of the time

## Clarifications

### Session 2026-01-02

- Q: What format should reminder messages follow? → A: Define exact format for reminder messages (e.g., "[REMINDER] Task Title - Description (due: YYYY-MM-DD HH:MM)")
- Q: How should the application check for due tasks during runtime? → A: Check for due tasks every 10 seconds during application runtime
- Q: How should the system handle recurrence for monthly tasks on days that don't exist in all months? → A: When rescheduling monthly recurring tasks, if the target day doesn't exist in the next month, use the last day of that month
- Q: What date/time format should the system accept for input? → A: Accept multiple common formats (MM/DD/YYYY, DD/MM/YYYY, etc.)
- Q: What should happen with overdue tasks when the application starts? → A: Only show reminders for tasks due during current session
