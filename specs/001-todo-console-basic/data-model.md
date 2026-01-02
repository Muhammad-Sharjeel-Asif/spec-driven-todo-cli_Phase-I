# Data Model: Todo Console Basic

## Entity: Task

### Fields
- **id** (int): Unique sequential identifier, starting from 1, never reused after deletion
- **title** (str): Required task title with maximum 100 characters
- **description** (str): Optional task description with maximum 500 characters
- **completed** (bool): Task completion status (True = completed, False = incomplete)

### Validation Rules
- Title must not be empty
- Title must be 1-100 characters if provided
- Description must be 0-500 characters if provided
- ID must be unique within the application session

### State Transitions
- A task can transition from incomplete (completed=False) to complete (completed=True)
- A task can transition from complete (completed=True) back to incomplete (completed=False)

### Relationships
- No relationships with other entities (standalone entity)