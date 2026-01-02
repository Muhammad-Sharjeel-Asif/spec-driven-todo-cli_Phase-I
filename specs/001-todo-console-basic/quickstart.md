# Quickstart: Todo Console Basic

## Setup

1. Ensure Python 3.13+ is installed
2. Make sure `uv` is installed and available in your PATH
3. Navigate to the project root directory

## Running the Application

Execute the application using uv:

```bash
uv run src/main.py
```

## Using the Application

1. The application will start with a menu-driven interface
2. Select options by entering the corresponding number
3. Follow the prompts to perform task operations:
   - Add tasks with title and optional description
   - View all tasks with their status
   - Update existing tasks
   - Delete tasks by ID
   - Mark tasks as complete/incomplete

## Key Features

- Menu-driven interface for easy navigation
- All data stored in memory only (resets on exit)
- Sequential ID assignment starting from 1
- Input validation with length limits
- Comprehensive error handling
- Fast response times (<1 second per operation)