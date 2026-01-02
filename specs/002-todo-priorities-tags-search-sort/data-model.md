# Data Model: Todo Console App with Priorities, Tags, Search and Sort

## Task Entity

### Fields
- **id**: int - Unique identifier (runtime only)
- **title**: str - Task title
- **description**: str - Optional description
- **completed**: bool - Completion status
- **priority**: str - Priority level (high, medium, low) - validated
- **tags**: list[str] - List of text labels - validated (letters, numbers, spaces, hyphens, underscores)
- **created_at**: datetime - In-memory creation timestamp (session only)

### Validation Rules
- priority: Must be one of "high", "medium", "low" (case-sensitive)
- tags: Each tag must match basic validation (letters, numbers, spaces, hyphens, underscores only)
- created_at: Automatically set at task creation, read-only

### State Transitions
- New Task: id, title, description, completed=False, priority="medium", tags=[], created_at=datetime.now()
- Update Priority: priority can change to any valid value
- Update Tags: tags list can be modified to any valid list of tags
- Complete Task: completed changes from False to True
- Uncomplete Task: completed changes from True to False

### Relationships
- No relationships to other entities (standalone task model)