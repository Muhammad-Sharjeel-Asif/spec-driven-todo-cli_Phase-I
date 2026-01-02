# Data Model: In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

## Task Entity

### Fields
| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| id | int | Unique runtime identifier | Auto-incrementing integer |
| title | str | Task title | Required, non-empty |
| description | str | Optional description | Optional, can be empty |
| completed | bool | Completion status | Boolean (True/False) |
| priority | str | Task priority | Optional, if implemented in base app |
| tags | list[str] | Task tags | Optional, list of strings |
| created_at | datetime | In-memory creation timestamp | Auto-set on creation |
| due_at | datetime | Optional due date and time | Optional, datetime object |
| recurrence | str \| None | Recurrence interval | One of: "daily", "weekly", "monthly", or None |

### Constraints
- All data remains in-memory only (no persistence)
- No additional fields beyond those specified
- No derived or cached scheduling state stored on the model
- `due_at` is optional and time-based
- `recurrence` is limited to: daily, weekly, monthly, or None

### State Transitions
- Task created: `completed=False`, `created_at` set to current time
- Task completed: `completed=True`, other fields unchanged
- Task reminder triggered: If recurring, `due_at` advanced by recurrence interval; otherwise, reminder marked as completed
- Task deleted: Object removed from in-memory storage

## Relationships
- No relationships needed - all tasks are independent
- Time-based behavior is determined by `due_at` and `recurrence` fields