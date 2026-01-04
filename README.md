# spec-driven-todo-cli_Phase-I

A powerful and feature-rich command-line interface (CLI) todo application built with Python. This application provides comprehensive task management capabilities with a focus on usability and functionality.

## Features

### Task Management
- **Add Tasks**: Create new tasks with titles, descriptions, priorities, tags, due dates, and recurrence patterns
- **View Tasks**: Display all tasks in a formatted table with color-coded status indicators
- **Update Tasks**: Modify existing tasks with new titles, descriptions, priorities, tags, due dates, or recurrence settings
- **Delete Tasks**: Remove tasks by ID with validation
- **Mark Complete/Incomplete**: Update task completion status with intuitive prompts

### Advanced Task Features
- **Priorities**: Assign high, medium, or low priority levels to tasks with color-coded visual indicators
- **Tags**: Organize tasks with custom tags for better categorization and filtering
- **Due Dates**: Set flexible due dates with support for various date formats (MM/DD/YYYY, YYYY-MM-DD, etc.)
- **Recurring Tasks**: Create daily, weekly, or monthly recurring tasks that automatically reschedule themselves
- **Time-based Reminders**: Automatic reminder system that alerts users when tasks are due

### Search and Filter
- **Search**: Find tasks by keyword across titles, descriptions, and tags (case-insensitive)
- **Filter**: Apply multiple filters simultaneously:
  - By completion status (completed/incomplete)
  - By priority level (high/medium/low)
  - By date (today/yesterday)
- **Sort**: Organize tasks by:
  - Title (alphabetical)
  - Priority (high to low)
  - Creation date (oldest first)

### User Experience
- **Color-coded Interface**: Visual indicators for task status, priority levels, and completion states
- **Table Format**: Clean, organized display of tasks with ID, title, status, priority, tags, and due dates
- **Error Handling**: Comprehensive error validation and user-friendly error messages
- **Input Validation**: Robust validation for all user inputs including titles, descriptions, tags, dates, and priorities
- **Keyboard Interrupt Handling**: Graceful exit with Ctrl+C

### Technical Features
- **In-Memory Storage**: Fast, lightweight task management without external dependencies
- **Sequential ID Assignment**: Unique, non-repeating task IDs that persist across deletions
- **Thread-Safe Operations**: Background time checking for reminders without blocking user input
- **Python Standard Library Only**: No external dependencies required

## Installation

1. Ensure you have Python 3.13+ installed on your system
2. Clone or download this repository
3. Navigate to the project directory
4. Run the application with:
   ```uv run src/main.py
   ```

## Usage

The application provides an interactive menu system:

1. **Add Task**: Create a new task with title, description, priority, tags, due date, and recurrence
2. **View All Tasks**: Display all tasks in a formatted table
3. **Update Task**: Modify an existing task by ID
4. **Delete Task**: Remove a task by ID
5. **Mark Task Complete/Incomplete**: Toggle task completion status
6. **Search Tasks**: Find tasks by keyword
7. **Filter Tasks**: Apply multiple filters to narrow down task lists
8. **Sort Tasks**: Organize tasks by various criteria
9. **Exit**: Close the application

## Task Properties

Each task contains the following properties:
- **ID**: Unique sequential identifier
- **Title**: Task name (required, max 100 characters)
- **Description**: Detailed task information (optional, max 500 characters)
- **Status**: Completed (✓) or Pending (○)
- **Priority**: High, Medium, or Low with color coding
- **Tags**: List of user-defined tags for organization
- **Due Date**: Optional date and time for task completion
- **Recurrence**: Optional recurrence pattern (daily/weekly/monthly)
- **Creation Date**: Timestamp of when the task was created

## Date and Time Formats

The application supports multiple date formats:
- YYYY-MM-DD HH:MM (e.g., 2026-01-02 14:30)
- MM/DD/YYYY HH:MM (e.g., 01/02/2026 14:30)
- MM/DD/YYYY (e.g., 01/02/2026)
- YYYY-MM-DD (e.g., 2026-01-02)
- Relative terms: "today", "tomorrow"

## Tag Format

Tags support letters, numbers, spaces, hyphens, and underscores only.

## Recurring Tasks

Recurring tasks automatically reschedule themselves when their due date passes:
- **Daily**: Every 24 hours
- **Weekly**: Every 7 days
- **Monthly**: Same day of the following month (with proper handling for months with fewer days)