# Task API Contract: Time-Based Todo Features

## Overview
This contract defines the API for time-based task features including due dates and recurring tasks.

## Task Model Extension
```python
class Task:
    id: int                 # Unique runtime identifier
    title: str              # Task title
    description: str        # Optional description
    completed: bool         # Completion status
    created_at: datetime    # Creation timestamp
    due_at: Optional[datetime]  # Optional due date/time
    recurrence: Optional[str]   # One of: "daily", "weekly", "monthly", None
```

## CLI Command Contracts

### Add Task with Time Features
- **Command**: `add "title" --due "YYYY-MM-DD HH:MM" --recurrence "daily|weekly|monthly"`
- **Input**: Title (required), due date/time (optional), recurrence (optional)
- **Output**: Success message with task ID
- **Error cases**: Invalid date format, invalid recurrence value

### Update Task Time Features
- **Command**: `update <id> --due "YYYY-MM-DD HH:MM" --recurrence "daily|weekly|monthly|none"`
- **Input**: Task ID, due date/time (optional), recurrence (optional)
- **Output**: Success message
- **Error cases**: Task not found, invalid date format, invalid recurrence value

### List Tasks with Time Features
- **Command**: `list`
- **Output**: All tasks with due dates and recurrence indicators
- **Format**: "[ID] Title [completed/uncompleted] (due: YYYY-MM-DD HH:MM, rec: daily/weekly/monthly)"

## Time-Based Behavior Contracts

### Reminder Display
- **Trigger**: Current time >= task.due_at
- **Format**: "[REMINDER] Task Title - Description (due: YYYY-MM-DD HH:MM)"
- **Duration**: 10 seconds per due time
- **Frequency**: Every 10 seconds during runtime

### Recurrence Rescheduling
- **Trigger**: Reminder triggers for recurring task
- **Action**: task.due_at advanced by recurrence interval
- **Constraints**: No duplication, no infinite loops