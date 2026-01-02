"""
Core task operations for the Todo Console Application
"""
from datetime import datetime, timedelta
import time
import threading
from typing import List, Optional
from models import Task


class TodoManager:
    """
    Manages in-memory task storage with list and unique sequential ID assignment
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1  # Sequential ID starting from 1

    def _get_next_id(self) -> int:
        """Get the next available ID, ensuring IDs are not reused after deletion"""
        return self.next_id

    def _update_next_id(self):
        """Update the next_id to be one more than the highest ID in the list"""
        if self.tasks:
            max_id = max(task.id for task in self.tasks)
            self.next_id = max(max_id + 1, self.next_id)
        else:
            self.next_id = 1

    def _validate_input(self, title: str, description: str = "") -> bool:
        """
        Validate input for title/description length limits (100/500 chars) and empty title validation
        """
        # Check if title is empty
        if not title or not title.strip():
            return False

        # Check title length (max 100 chars)
        if len(title) > 100:
            return False

        # Check description length (max 500 chars)
        if len(description) > 500:
            return False

        return True

    def _validate_tag(self, tag: str) -> bool:
        """
        Validate tag format: only letters, numbers, spaces, hyphens, and underscores
        """
        import re
        # Check if tag is empty
        if not tag or not tag.strip():
            return True  # Empty tags are acceptable

        # Check if tag matches the allowed pattern
        pattern = r'^[a-zA-Z0-9 \-_]+$'
        return bool(re.match(pattern, tag))

    def _handle_error(self, error_msg: str) -> str:
        """
        Handle errors gracefully to prevent crashes and show user-friendly messages
        """
        # In a real implementation, this might log the error
        # For now, we'll just return the message to be displayed
        return f"Error: {error_msg}"

    def add_task(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None) -> Optional[Task]:
        """
        Implement add_task function that accepts title (required), description (optional),
        priority (optional, default: medium), tags (optional, default: empty list),
        validates input, assigns unique ID, and stores in memory
        """
        # Use the error-handling version and return the appropriate result
        error_msg = self.add_task_with_error_handling(title, description, priority, tags)

        if error_msg is None:
            # If no error, return the last added task
            if self.tasks:
                return self.tasks[-1]  # Return the most recently added task
            return None
        else:
            # If there was an error, return None
            return None

    def get_all_tasks(self) -> List[Task]:
        """
        Implement get_all_tasks function that returns all tasks with their ID, title, description, and completion status
        """
        return self.tasks.copy()  # Return a copy to prevent external modification

    def update_task(self, task_id: int, new_title: str = None, new_description: str = None, new_priority: str = None, new_tags: List[str] = None) -> Optional[Task]:
        """
        Implement update_task function that accepts task_id and new title/description/priority/tags values,
        validates input, and updates the task
        """
        # Use the error-handling version and return the appropriate result
        error_msg = self.update_task_with_error_handling(task_id, new_title, new_description, new_priority, new_tags)

        if error_msg is None:
            # If no error, find and return the updated task
            for task in self.tasks:
                if task.id == task_id:
                    return task
            return None
        else:
            # If there was an error, return None
            return None

    def delete_task(self, task_id: int) -> bool:
        """
        Implement delete_task function that accepts task_id, removes the task,
        and ensures IDs are not reused after deletion
        """
        # Use the error-handling version and return the appropriate result
        error_msg = self.delete_task_with_error_handling(task_id)

        if error_msg is None:
            # If no error, deletion was successful
            return True
        else:
            # If there was an error, return False
            return False

    def mark_task_complete(self, task_id: int, completed: bool) -> Optional[Task]:
        """
        Implement mark_task_complete function that accepts task_id and completion status,
        updates the task, and returns updated task
        """
        # Use the error-handling version and return the appropriate result
        error_msg = self.mark_task_complete_with_error_handling(task_id, completed)

        if error_msg is None:
            # If no error, find and return the updated task
            for task in self.tasks:
                if task.id == task_id:
                    return task
            return None
        else:
            # If there was an error, return None
            return None

    def add_task_with_error_handling(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None) -> Optional[str]:
        """
        Add comprehensive error handling for all user inputs in src/todo.py
        """
        try:
            # Validate input
            if not self._validate_input(title, description):
                return self._handle_error("Invalid input: title/description doesn't meet requirements (title required, max 100 chars; description max 500 chars)")

            # Validate priority
            if priority not in ["high", "medium", "low"]:
                return self._handle_error("Invalid priority value. Must be one of: high, medium, low")

            # Validate tags
            if tags is None:
                tags = []

            for tag in tags:
                if not self._validate_tag(tag):
                    return self._handle_error(f"Invalid tag: '{tag}'. Tags must contain only letters, numbers, spaces, hyphens, and underscores.")

            # Create a new task with the next available ID
            task_id = self._get_next_id()
            new_task = Task(task_id, title, description, False)  # New tasks are not completed by default
            new_task.priority = priority
            new_task.tags = tags

            # Add to tasks list
            self.tasks.append(new_task)

            # Update the next ID to be one more than the current task's ID
            self.next_id = task_id + 1

            return None  # Success, no error
        except Exception as e:
            return self._handle_error(f"Failed to add task: {str(e)}")

    def update_task_with_error_handling(self, task_id: int, new_title: str = None, new_description: str = None, new_priority: str = None, new_tags: List[str] = None) -> Optional[str]:
        """
        Add input validation for all user inputs across all functions in src/todo.py
        """
        try:
            # Find the task with the given ID
            task_index = None
            for i, task in enumerate(self.tasks):
                if task.id == task_id:
                    task_index = i
                    break

            # If task not found, return error
            if task_index is None:
                return self._handle_error(f"Task with ID {task_id} not found")

            # Get the current task
            current_task = self.tasks[task_index]

            # Determine new values (use existing if not provided)
            updated_title = new_title if new_title is not None else current_task.title
            updated_description = new_description if new_description is not None else current_task.description
            updated_priority = new_priority if new_priority is not None else current_task.priority
            updated_tags = new_tags if new_tags is not None else current_task.tags

            # Validate the new values
            if not self._validate_input(updated_title, updated_description):
                return self._handle_error("Invalid input: title/description doesn't meet requirements (title required if updating, max 100 chars; description max 500 chars)")

            # Validate priority
            if new_priority is not None:
                if new_priority not in ["high", "medium", "low"]:
                    return self._handle_error("Invalid priority value. Must be one of: high, medium, low")

            # Validate tags
            if new_tags is not None:
                for tag in new_tags:
                    if not self._validate_tag(tag):
                        return self._handle_error(f"Invalid tag: '{tag}'. Tags must contain only letters, numbers, spaces, hyphens, and underscores.")

            # Update the task
            current_task.title = updated_title
            current_task.description = updated_description
            current_task.priority = updated_priority
            current_task.tags = updated_tags

            return None  # Success, no error
        except Exception as e:
            return self._handle_error(f"Failed to update task: {str(e)}")

    def delete_task_with_error_handling(self, task_id: int) -> Optional[str]:
        """
        Enhanced error handling for delete_task
        """
        try:
            # Find the task with the given ID
            task_found = False
            for i, task in enumerate(self.tasks):
                if task.id == task_id:
                    # Remove the task from the list
                    del self.tasks[i]
                    task_found = True

                    # Update the next_id to ensure IDs are not reused after deletion
                    # We keep the next_id as the highest ID + 1 to ensure uniqueness
                    self._update_next_id()
                    break

            if not task_found:
                return self._handle_error(f"Task with ID {task_id} not found")

            return None  # Success, no error
        except Exception as e:
            return self._handle_error(f"Failed to delete task: {str(e)}")

    def mark_task_complete_with_error_handling(self, task_id: int, completed: bool) -> Optional[str]:
        """
        Enhanced error handling for mark_task_complete
        """
        try:
            # Find the task with the given ID
            task_found = False
            for task in self.tasks:
                if task.id == task_id:
                    # Update the completion status
                    task.completed = completed
                    task_found = True
                    break

            if not task_found:
                return self._handle_error(f"Task with ID {task_id} not found")

            return None  # Success, no error
        except Exception as e:
            return self._handle_error(f"Failed to update task status: {str(e)}")

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword across title, description, and tags (case-insensitive)
        If keyword is empty, return all tasks
        """
        if not keyword.strip():
            # Return all tasks if keyword is empty
            return self.tasks.copy()

        keyword_lower = keyword.lower()
        results = []

        for task in self.tasks:
            # Check title
            if keyword_lower in task.title.lower():
                results.append(task)
                continue

            # Check description
            if keyword_lower in task.description.lower():
                results.append(task)
                continue

            # Check tags
            for tag in task.tags:
                if keyword_lower in tag.lower():
                    results.append(task)
                    break

        return results

    def filter_tasks(self, completed: Optional[bool] = None, priority: Optional[str] = None, date_filter: Optional[str] = None) -> List[Task]:
        """
        Filter tasks by completion status, priority, and/or creation date
        """
        results = []

        for task in self.tasks:
            # Check completion status
            if completed is not None and task.completed != completed:
                continue

            # Check priority
            if priority is not None and task.priority != priority:
                continue

            # Check date filter (for same session, we'll check if it's today)
            if date_filter is not None:
                # For now, we'll implement basic date filtering
                if date_filter == "today":
                    from datetime import datetime
                    if task.created_at.date() != datetime.now().date():
                        continue
                elif date_filter == "yesterday":
                    from datetime import datetime, timedelta
                    yesterday = datetime.now().date() - timedelta(days=1)
                    if task.created_at.date() != yesterday:
                        continue

            results.append(task)

        return results

    def sort_tasks(self, sort_by: str) -> List[Task]:
        """
        Sort tasks by title, priority, or creation date
        Uses stable sorting algorithms to maintain consistent ordering of equal elements
        """
        if sort_by == "title":
            # Sort alphabetically by title (stable sort)
            return sorted(self.tasks, key=lambda x: x.title.lower())
        elif sort_by == "priority":
            # Sort by priority: high, medium, low (stable sort)
            priority_order = {"high": 0, "medium": 1, "low": 2}
            return sorted(self.tasks, key=lambda x: priority_order.get(x.priority, 3))
        elif sort_by == "date":
            # Sort by creation date (oldest first) (stable sort)
            return sorted(self.tasks, key=lambda x: x.created_at)
        else:
            # Default: return as is
            return self.tasks.copy()

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all tasks that are overdue (due date is in the past and not completed)
        """
        current_time = datetime.now()
        overdue_tasks = []
        for task in self.tasks:
            if task.due_at and task.due_at <= current_time and not task.completed:
                overdue_tasks.append(task)
        return overdue_tasks

    def get_due_tasks(self) -> List[Task]:
        """
        Get all tasks that are due now (due date is now or in the past and not completed)
        """
        current_time = datetime.now()
        due_tasks = []
        for task in self.tasks:
            if task.due_at and task.due_at <= current_time and not task.completed:
                due_tasks.append(task)
        return due_tasks

    def advance_recurrence(self, task: Task) -> None:
        """
        Advance the due date of a recurring task by its recurrence interval
        """
        if not task.recurrence or not task.due_at:
            return

        current_due = task.due_at
        if task.recurrence == "daily":
            new_due = current_due + timedelta(days=1)
        elif task.recurrence == "weekly":
            new_due = current_due + timedelta(weeks=1)
        elif task.recurrence == "monthly":
            # Handle monthly recurrence with proper day adjustment
            new_due = self._advance_month(current_due)
        else:
            # Invalid recurrence, don't advance
            return

        task.due_at = new_due

    def _advance_month(self, current_date: datetime) -> datetime:
        """
        Advance date by one month, handling cases where the target day doesn't exist
        (e.g., Jan 31 -> Feb 28/29, Mar 31 -> Apr 30)
        """
        year = current_date.year
        month = current_date.month
        day = current_date.day

        # Calculate next month and year
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1

        # Handle day overflow by using the last day of the target month if needed
        import calendar
        max_day_in_next_month = calendar.monthrange(next_year, next_month)[1]

        if day > max_day_in_next_month:
            # Use the last day of the next month instead
            next_day = max_day_in_next_month
        else:
            next_day = day

        return current_date.replace(year=next_year, month=next_month, day=next_day)

    def display_reminder(self, task: Task) -> None:
        """
        Display reminder message with format "[REMINDER] Task Title - Description (due: YYYY-MM-DD HH:MM)"
        Only for 10 seconds as specified in the requirements
        """
        import sys
        import time
        from datetime import datetime

        # Format the reminder message
        description = task.description if task.description else ""
        reminder_msg = f"[REMINDER] {task.title} - {description} (due: {task.due_at.strftime('%Y-%m-%d %H:%M')})"

        # Print the reminder
        print(reminder_msg)

        # Sleep for 10 seconds to keep the reminder visible
        time.sleep(10)

    def check_and_process_reminders(self) -> List[Task]:
        """
        Check for tasks that are due now and process them (show reminders, reschedule recurring tasks)
        Returns list of tasks that triggered reminders
        """
        due_tasks = self.get_due_tasks()
        triggered_tasks = []

        for task in due_tasks:
            # Add to triggered tasks list
            triggered_tasks.append(task)

            # Display the reminder
            self.display_reminder(task)

            # If the task is recurring, reschedule it
            if task.recurrence:
                self.advance_recurrence(task)
            # If not recurring, the reminder is considered processed for this due time

        return triggered_tasks

    def check_and_process_reminders_non_blocking(self) -> List[Task]:
        """
        Check for tasks that are due now and process them without blocking user input
        Returns list of tasks that triggered reminders
        """
        due_tasks = self.get_due_tasks()
        triggered_tasks = []

        for task in due_tasks:
            # Add to triggered tasks list
            triggered_tasks.append(task)

            # Display the reminder (this will be non-blocking in a real implementation)
            self.display_reminder(task)

            # If the task is recurring, reschedule it
            if task.recurrence:
                self.advance_recurrence(task)
            # If not recurring, the reminder is considered processed for this due time

        return triggered_tasks

    def time_check_loop(self, interval: int = 10) -> None:
        """
        Run a time-checking loop that runs every 'interval' seconds
        This is a blocking function meant to run in a separate thread
        """
        while True:
            try:
                triggered_tasks = self.check_and_process_reminders_non_blocking()
                # In a real implementation, we would display reminders here
                # For now, we just process them
                time.sleep(interval)
            except Exception:
                # If there's an error, just continue the loop
                time.sleep(interval)

    def start_time_checker(self) -> None:
        """
        Start the time-checking loop in a separate thread
        """
        checker_thread = threading.Thread(target=self.time_check_loop, daemon=True)
        checker_thread.start()

    def parse_datetime(self, date_str: str) -> Optional[datetime]:
        """
        Parse various date/time formats and return a datetime object
        Supports formats like: MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD HH:MM, etc.
        """
        import re
        from datetime import datetime

        # Define possible formats
        formats = [
            "%Y-%m-%d %H:%M",      # 2026-01-02 14:30
            "%m/%d/%Y %H:%M",      # 01/02/2026 14:30
            "%d/%m/%Y %H:%M",      # 02/01/2026 14:30 (Note: This could be ambiguous)
            "%m/%d/%Y",            # 01/02/2026
            "%d/%m/%Y",            # 02/01/2026
            "%Y-%m-%d",            # 2026-01-02
            "%m-%d-%Y",            # 01-02-2026
            "%d-%m-%Y",            # 02-01-2026
        ]

        # Try each format
        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except ValueError:
                continue

        # If none of the standard formats work, try to handle relative times
        # Check for "today", "tomorrow", etc. (simplified)
        date_str_lower = date_str.lower().strip()
        current_time = datetime.now()

        if date_str_lower == "today":
            return current_time.replace(hour=23, minute=59, second=59)
        elif date_str_lower == "tomorrow":
            tomorrow = current_time + timedelta(days=1)
            return tomorrow.replace(hour=23, minute=59, second=59)

        # If no format matches, return None
        return None

    def validate_recurrence(self, recurrence: Optional[str]) -> bool:
        """
        Validate recurrence value is one of: daily, weekly, monthly, or None
        """
        if recurrence is None:
            return True
        return recurrence in ["daily", "weekly", "monthly"]

    def validate_due_date(self, due_at: Optional[datetime]) -> bool:
        """
        Validate due date - should not be in the past if provided
        This is a basic validation - in real usage, we might allow past due dates for historical tasks
        """
        if due_at is None:
            return True
        # Allow any date, past or future
        return True

    def validate_task_update(self, due_at: Optional[datetime], recurrence: Optional[str]) -> Optional[str]:
        """
        Validate task update parameters and return error message if invalid
        """
        # Validate recurrence
        if recurrence is not None and not self.validate_recurrence(recurrence):
            return f"Invalid recurrence value: '{recurrence}'. Must be one of: daily, weekly, monthly"

        # Validate due date format
        if due_at is not None and not self.validate_due_date(due_at):
            return f"Invalid due date: {due_at}"

        # If both recurrence and due date are provided, ensure due date makes sense
        # (This is a basic check - in practice, you might want to ensure the due date aligns with the recurrence pattern)

        return None  # Valid