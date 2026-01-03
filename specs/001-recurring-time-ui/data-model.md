# Data Model for Recurring Time Customization & Terminal UI Presentation

## Entities

### Task
The Task entity remains unchanged from the existing model. The time component for recurring tasks is handled through the existing `due_at` datetime field.

**Fields:**
- `id`: int - Unique identifier for the task
- `title`: str - Task title (required)
- `description`: str - Task description (optional)
- `completed`: bool - Completion status
- `priority`: str - Priority level ("high", "medium", "low")
- `tags`: List[str] - List of tags associated with the task
- `created_at`: datetime - Timestamp when the task was created
- `due_at`: datetime - Optional due date and time (includes time component)
- `recurrence`: str - Recurrence pattern ("daily", "weekly", "monthly" or None)

**Validation Rules:**
- The time component of `due_at` will be set based on user input for recurring tasks
- If no time is specified for recurring tasks, default to 00:00 (midnight)
- The time component of `due_at` is preserved during recurrence advancement

**State Transitions:**
- When a recurring task is completed/processed, if it has a recurrence pattern, its `due_at` is updated to the next occurrence while preserving the time component

## UI Display Model
No new data model is required for UI enhancements. The existing Task model will be formatted differently for display purposes.

**Display Properties:**
- Column widths for table-like formatting
- Color codes for different visual elements
- Status indicators for completed/incomplete tasks