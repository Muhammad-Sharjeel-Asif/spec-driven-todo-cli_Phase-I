# Task Management API Contracts

## Core Operations

### Add Task
- **Method**: Internal function call
- **Input**: title (string, required, 1-100 chars), description (string, optional, 0-500 chars)
- **Output**: Task object with assigned ID
- **Errors**: ValidationError if input doesn't meet requirements

### View All Tasks
- **Method**: Internal function call
- **Input**: None
- **Output**: List of Task objects
- **Errors**: None

### Update Task
- **Method**: Internal function call
- **Input**: task_id (int), title (string, optional), description (string, optional)
- **Output**: Updated Task object
- **Errors**: NotFoundError if task_id doesn't exist

### Delete Task
- **Method**: Internal function call
- **Input**: task_id (int)
- **Output**: Boolean indicating success
- **Errors**: NotFoundError if task_id doesn't exist

### Mark Task Complete/Incomplete
- **Method**: Internal function call
- **Input**: task_id (int), completed (bool)
- **Output**: Updated Task object
- **Errors**: NotFoundError if task_id doesn't exist