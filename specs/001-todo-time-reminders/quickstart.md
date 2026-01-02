# Quickstart Guide: In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

## Prerequisites
- Python 3.13+
- uv package manager

## Setup
1. Clone the repository
2. Install dependencies with uv:
   ```bash
   uv sync
   ```
3. Run the application:
   ```bash
   uv run python src/main.py
   ```

## Key Features

### Time-Based Reminders
- Set due dates/times when creating or updating tasks
- Reminders appear in terminal when due time is reached
- Reminder format: "[REMINDER] Task Title - Description (due: YYYY-MM-DD HH:MM)"

### Recurring Tasks
- Set recurrence when creating or updating tasks
- Supported intervals: daily, weekly, monthly
- Tasks automatically reschedule after due time passes

### CLI Commands
- `add "task title" --due "YYYY-MM-DD HH:MM" --recurrence "daily|weekly|monthly"`
- `update <id> --due "YYYY-MM-DD HH:MM" --recurrence "daily|weekly|monthly|none"`
- `list` - shows all tasks including due dates and recurrence
- `complete <id>` - marks task as complete

## Time-Based Behavior
- Application checks for due tasks every 10 seconds during runtime
- Only shows reminders for tasks due during current session
- For monthly recurring tasks, if target day doesn't exist in next month, uses last day of that month
- Accepts multiple common date/time formats (MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD HH:MM, etc.)