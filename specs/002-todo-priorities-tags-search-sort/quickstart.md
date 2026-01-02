# Quickstart Guide: Todo Console App with Priorities, Tags, Search and Sort

## Setup

1. Ensure you have Python 3.13+ installed
2. Install uv if not already installed: `pip install uv`
3. Clone the repository and navigate to the project directory
4. Run the application: `uv run src/main.py`

## Basic Commands

- `add "task title" "description"` - Add a new task
- `list` - List all tasks
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete
- `delete <id>` - Delete a task

## New Features Commands

### Priorities
- `add "task" "desc" --priority high` - Add task with priority
- `update <id> --priority medium` - Update task priority
- `list --priority high` - Filter tasks by priority

### Tags
- `add "task" "desc" --tags work,urgent` - Add task with tags
- `update <id> --tags personal,home` - Update task tags
- `list --tag work` - Filter tasks by tag

### Search
- `search "keyword"` - Search tasks by keyword in title, description, or tags
- `search ""` - Return all tasks (empty search)

### Filtering
- `list --completed` - Show only completed tasks
- `list --incomplete` - Show only incomplete tasks
- `list --priority high` - Show only high priority tasks
- `list --date today` - Show tasks created today

### Sorting
- `list --sort title` - Sort by title alphabetically
- `list --sort priority` - Sort by priority (high to low)
- `list --sort date` - Sort by creation date