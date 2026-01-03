# API Contracts for Recurring Time Customization & Terminal UI Presentation

## Time Input Validation

### Function: validate_time_format
- **Input**: time_str (string in HH:MM format)
- **Output**: boolean (True if valid, False otherwise)
- **Errors**: None (silent validation)
- **Contract**: Validates that input string matches HH:MM format where HH is 00-23 and MM is 00-59

### Function: parse_time_input
- **Input**: time_input (string from user)
- **Output**: datetime.time object or None if invalid
- **Errors**: Returns None for invalid formats
- **Contract**: Parses user input and returns time component or None

## Recurring Task Time Handling

### Function: set_recurring_task_time
- **Input**: task (Task object), time_str (string in HH:MM format)
- **Output**: Task object with updated due_at field
- **Errors**: Raises ValueError for invalid time format
- **Contract**: Updates the time component of task.due_at while preserving date

### Function: advance_recurring_task_preserve_time
- **Input**: task (Task object with recurrence)
- **Output**: Task object with updated due_at (next recurrence date, same time)
- **Errors**: None (no-op for non-recurring tasks)
- **Contract**: Advances date according to recurrence pattern while preserving original time component

## UI Display Functions

### Function: format_task_table
- **Input**: tasks (list of Task objects)
- **Output**: formatted string with table-like layout
- **Errors**: None (fails gracefully to basic format)
- **Contract**: Returns string representation of tasks in table format with headers

### Function: apply_color_formatting
- **Input**: text (string), style (color/style identifier)
- **Output**: string with ANSI escape codes applied
- **Errors**: None (returns original text if color not supported)
- **Contract**: Applies ANSI color codes to text without changing content meaning