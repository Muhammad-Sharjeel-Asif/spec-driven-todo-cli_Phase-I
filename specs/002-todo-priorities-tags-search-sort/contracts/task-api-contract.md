# Task API Contract: Todo Console App with Priorities, Tags, Search and Sort

## Core Task Operations

### Add Task
- **Command**: `add "title" "description" [options]`
- **Options**:
  - `--priority`: high|medium|low (default: medium)
  - `--tags`: comma-separated tags (e.g., "work,urgent")
- **Validation**:
  - Priority must be valid (high/medium/low)
  - Tags must pass basic validation (letters, numbers, spaces, hyphens, underscores)
- **Success**: Task created with unique ID, returns confirmation
- **Error**: Invalid priority/tags return error message, no task created

### Update Task
- **Command**: `update <id> [options]`
- **Options**:
  - `--title`: New title
  - `--description`: New description
  - `--priority`: high|medium|low
  - `--tags`: comma-separated tags
- **Validation**: Same as Add Task
- **Success**: Task updated, returns confirmation
- **Error**: Invalid input returns error message, task unchanged

### List Tasks
- **Command**: `list [options]`
- **Options**:
  - `--completed`: Show only completed tasks
  - `--incomplete`: Show only incomplete tasks
  - `--priority`: Filter by priority level
  - `--tag`: Filter by tag
  - `--date`: Filter by creation date (today, yesterday, specific date)
  - `--sort`: Sort by title|priority|date
- **Success**: Returns filtered/sorted list of tasks
- **Error**: Invalid filter/sort options return error message

### Search Tasks
- **Command**: `search "keyword"`
- **Behavior**: Case-insensitive search across title, description, and tags
- **Success**: Returns matching tasks or empty list if no matches
- **Error**: None (empty string returns all tasks)

### Complete/Incomplete Tasks
- **Command**: `complete <id>` or `incomplete <id>`
- **Success**: Task status updated, returns confirmation
- **Error**: Invalid ID returns error message

### Delete Task
- **Command**: `delete <id>`
- **Success**: Task deleted, returns confirmation
- **Error**: Invalid ID returns error message