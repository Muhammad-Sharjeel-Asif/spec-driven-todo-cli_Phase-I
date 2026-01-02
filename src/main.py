"""
CLI entry point for the Todo Console Application
"""
import re
from todo import TodoManager


def main():
    """Create basic CLI menu structure that imports from todo.py and models.py"""
    print("Welcome to the Todo Console Application!")
    print("Initializing application...")

    # Initialize the todo manager
    todo_manager = TodoManager()

    print("Application initialized successfully!")
    print("Use the menu options to manage your tasks.")

    # Check for overdue tasks when application starts
    try:
        overdue_tasks = todo_manager.get_overdue_tasks()
        if overdue_tasks:
            print(f"\n⚠️  You have {len(overdue_tasks)} overdue task(s):")
            for task in overdue_tasks:
                if task.due_at:  # Ensure due_at is not None
                    description = task.description if task.description else ""
                    print(f"[REMINDER] {task.title} - {description} (due: {task.due_at.strftime('%Y-%m-%d %H:%M')})")
        else:
            print("\nNo overdue tasks found.")
    except Exception:
        print("\nNo overdue tasks found.")

    # Add comprehensive error handling for all user inputs in src/main.py and ensure no stack traces are shown to users
    while True:
        try:
            print("\nMenu Options:")
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Mark Task Complete/Incomplete")
            print("6. Search Tasks")
            print("7. Filter Tasks")
            print("8. Sort Tasks")
            print("9. Exit")

            choice = input("Select an option (1-9): ").strip()

            if choice == "1":
                title = input("Enter task title: ").strip()

                # Check if title is provided
                if not title:
                    print("Error: Task title is required!")
                    continue

                description = input("Enter task description (optional): ").strip()

                # Get priority
                priority = input("Enter priority (high/medium/low, default: medium): ").strip().lower()
                if priority not in ["high", "medium", "low"]:
                    priority = "medium"

                # Get tags
                tags_input = input("Enter tags (comma-separated, optional): ").strip()
                tags = []
                if tags_input:
                    # Split by comma and clean up each tag
                    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                    # Validate each tag
                    for tag in tags:
                        if not re.match(r'^[a-zA-Z0-9 \-_]+$', tag):
                            print(f"Error: Invalid tag format: '{tag}'. Tags must contain only letters, numbers, spaces, hyphens, and underscores.")
                            continue

                # Get due date
                due_date_input = input("Enter due date (optional, format: YYYY-MM-DD HH:MM, MM/DD/YYYY, etc.): ").strip()
                due_at = None
                if due_date_input:
                    due_at = todo_manager.parse_datetime(due_date_input)
                    if due_at is None:
                        print(f"Warning: Invalid date format '{due_date_input}'. Task will be created without due date.")
                    else:
                        print(f"Due date set to: {due_at.strftime('%Y-%m-%d %H:%M')}")

                # Get recurrence
                recurrence_input = input("Enter recurrence (optional, daily/weekly/monthly, or press Enter for none): ").strip().lower()
                recurrence = None
                if recurrence_input:
                    if todo_manager.validate_recurrence(recurrence_input):
                        recurrence = recurrence_input
                        print(f"Recurrence set to: {recurrence}")
                    else:
                        print(f"Warning: Invalid recurrence value '{recurrence_input}'. Task will be created without recurrence.")

                # Call enhanced add_task with error handling - need to update to handle new parameters
                # For now, we'll create the task directly using the Task class
                from models import Task
                task_id = todo_manager._get_next_id()
                new_task = Task(task_id, title, description, False, due_at, recurrence)
                new_task.priority = priority
                new_task.tags = tags
                todo_manager.tasks.append(new_task)
                todo_manager.next_id = task_id + 1

                print(f"Task added successfully! ID: {new_task.id}, Title: {new_task.title}, Priority: {new_task.priority}, Tags: {', '.join(new_task.tags)}")
                if new_task.due_at:
                    print(f"Due: {new_task.due_at.strftime('%Y-%m-%d %H:%M')}")
                if new_task.recurrence:
                    print(f"Recurs: {new_task.recurrence}")

            elif choice == "2":
                # Implement CLI menu option for viewing all tasks that displays tasks in a readable format with ID, title, description, and completion status
                all_tasks = todo_manager.get_all_tasks()

                if not all_tasks:
                    print("No tasks found.")
                else:
                    print("\nAll Tasks:")
                    for task in all_tasks:
                        status = "Completed" if task.completed else "Pending"
                        due_info = f", Due: {task.due_at.strftime('%Y-%m-%d %H:%M')}" if task.due_at else ""
                        recurrence_info = f", Recurs: {task.recurrence}" if task.recurrence else ""
                        print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {status}, Priority: {task.priority}, Tags: {', '.join(task.tags)}, Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}{due_info}{recurrence_info}")

            elif choice == "3":
                # Implement CLI menu option for updating tasks that prompts for task ID and new title/description values, validates input, and calls todo.update_task
                try:
                    task_id = int(input("Enter task ID to update: ").strip())
                except ValueError:
                    print("Error: Invalid task ID. Please enter a number.")
                    continue

                # Check if the task exists
                tasks = todo_manager.get_all_tasks()
                task_exists = any(task.id == task_id for task in tasks)

                if not task_exists:
                    print(f"Error: Task with ID {task_id} not found.")
                    continue

                # Get current task to show existing values
                current_task = None
                for task in tasks:
                    if task.id == task_id:
                        current_task = task
                        break

                if current_task:
                    print(f"Current task: ID {current_task.id}, Title: {current_task.title}")
                    if current_task.description:
                        print(f"Current description: {current_task.description}")
                    print(f"Current priority: {current_task.priority}")
                    if current_task.tags:
                        print(f"Current tags: {', '.join(current_task.tags)}")
                    if current_task.due_at:
                        print(f"Current due date: {current_task.due_at.strftime('%Y-%m-%d %H:%M')}")
                    if current_task.recurrence:
                        print(f"Current recurrence: {current_task.recurrence}")

                new_title = input("Enter new title (or press Enter to keep current): ").strip()
                new_description = input("Enter new description (or press Enter to keep current): ").strip()

                # Get new priority
                new_priority = input("Enter new priority (high/medium/low, or press Enter to keep current): ").strip().lower()
                if new_priority == "":
                    new_priority = None
                elif new_priority not in ["high", "medium", "low"]:
                    print("Error: Invalid priority. Keeping current priority.")
                    new_priority = None

                # Get new tags
                tags_input = input("Enter new tags (comma-separated, or press Enter to keep current): ").strip()
                new_tags = None
                if tags_input:
                    # Split by comma and clean up each tag
                    new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                    # Validate each tag
                    for tag in new_tags:
                        if not re.match(r'^[a-zA-Z0-9 \-_]+$', tag):
                            print(f"Error: Invalid tag format: '{tag}'. Tags must contain only letters, numbers, spaces, hyphens, and underscores.")
                            new_tags = None
                            break

                # Get new due date
                due_date_input = input("Enter new due date (or press Enter to keep current, format: YYYY-MM-DD HH:MM, MM/DD/YYYY, etc.): ").strip()
                new_due_at = None
                if due_date_input:
                    if due_date_input.lower() == "none":
                        new_due_at = None  # Remove due date
                    else:
                        new_due_at = todo_manager.parse_datetime(due_date_input)
                        if new_due_at is None:
                            print(f"Warning: Invalid date format '{due_date_input}'. Keeping current due date.")
                            new_due_at = None
                        else:
                            print(f"New due date set to: {new_due_at.strftime('%Y-%m-%d %H:%M')}")

                # Get new recurrence
                recurrence_input = input("Enter new recurrence (daily/weekly/monthly, 'none' to remove, or press Enter to keep current): ").strip().lower()
                new_recurrence = None
                if recurrence_input:
                    if recurrence_input == "none":
                        new_recurrence = None  # Remove recurrence
                        print("Recurrence removed.")
                    elif todo_manager.validate_recurrence(recurrence_input):
                        new_recurrence = recurrence_input
                        print(f"New recurrence set to: {new_recurrence}")
                    else:
                        print(f"Warning: Invalid recurrence value '{recurrence_input}'. Keeping current recurrence.")
                        new_recurrence = None

                # Use None for values that should remain unchanged
                new_title = new_title if new_title else None
                new_description = new_description if new_description else None

                # Update the task directly since we need to handle new fields
                updated = False
                for task in todo_manager.tasks:
                    if task.id == task_id:
                        if new_title is not None:
                            task.title = new_title
                            updated = True
                        if new_description is not None:
                            task.description = new_description
                            updated = True
                        if new_priority is not None:
                            task.priority = new_priority
                            updated = True
                        if new_tags is not None:
                            task.tags = new_tags
                            updated = True
                        if new_due_at is not None:
                            task.due_at = new_due_at
                            updated = True
                        if new_recurrence is not None:
                            task.recurrence = new_recurrence
                            updated = True

                        break

                if updated:
                    print(f"Task with ID {task_id} updated successfully!")
                else:
                    print("No changes were made to the task.")

            elif choice == "4":
                # Implement CLI menu option for deleting tasks that prompts for task ID, validates existence, and calls todo.delete_task
                try:
                    task_id = int(input("Enter task ID to delete: ").strip())
                except ValueError:
                    print("Error: Invalid task ID. Please enter a number.")
                    continue

                # Call enhanced delete_task with error handling
                error_msg = todo_manager.delete_task_with_error_handling(task_id)

                if error_msg is None:
                    print(f"Task with ID {task_id} deleted successfully!")
                else:
                    print(error_msg)

            elif choice == "5":
                # Implement CLI menu option for marking tasks complete/incomplete that prompts for task ID and completion status, validates input, and calls todo.mark_task_complete
                try:
                    task_id = int(input("Enter task ID to update status: ").strip())
                except ValueError:
                    print("Error: Invalid task ID. Please enter a number.")
                    continue

                # Check if the task exists
                tasks = todo_manager.get_all_tasks()
                task_exists = any(task.id == task_id for task in tasks)

                if not task_exists:
                    print(f"Error: Task with ID {task_id} not found.")
                    continue

                status_choice = input("Mark as (1) Complete or (2) Incomplete? (Enter 1 or 2): ").strip()

                if status_choice == "1":
                    completed = True
                elif status_choice == "2":
                    completed = False
                else:
                    print("Error: Invalid status choice. Please enter 1 for Complete or 2 for Incomplete.")
                    continue

                # Call enhanced mark_task_complete with error handling
                error_msg = todo_manager.mark_task_complete_with_error_handling(task_id, completed)

                if error_msg is None:
                    status = "Complete" if completed else "Incomplete"
                    print(f"Task with ID {task_id} marked as {status} successfully!")
                else:
                    print(error_msg)

            elif choice == "6":
                # Search tasks functionality
                keyword = input("Enter search keyword: ").strip()
                if not keyword:
                    print("Error: Search keyword is required!")
                    continue

                results = todo_manager.search_tasks(keyword)
                if not results:
                    print("No matching tasks found.")
                else:
                    print(f"\nSearch Results for '{keyword}':")
                    for task in results:
                        status = "Completed" if task.completed else "Pending"
                        print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {status}, Priority: {task.priority}, Tags: {', '.join(task.tags)}")

            elif choice == "7":
                # Filter tasks functionality
                print("\nFilter Options:")
                print("1. By completion status")
                print("2. By priority")
                print("3. By date")
                print("4. By completion status and priority")
                print("5. By completion status and date")
                print("6. By priority and date")
                print("7. By completion status, priority, and date")

                filter_choice = input("Select a filter option (1-7): ").strip()

                completed = None
                priority = None
                date_filter = None

                if filter_choice in ["1", "4", "5", "7"]:
                    status_choice = input("Filter by completion status (1) Completed, (2) Incomplete, (3) Both: ").strip()
                    if status_choice == "1":
                        completed = True
                    elif status_choice == "2":
                        completed = False
                    elif status_choice == "3":
                        completed = None  # Don't filter by completion status
                    else:
                        print("Invalid completion status choice.")
                        continue

                if filter_choice in ["2", "4", "6", "7"]:
                    priority_input = input("Filter by priority (high/medium/low, or press Enter for all): ").strip().lower()
                    if priority_input in ["high", "medium", "low"]:
                        priority = priority_input
                    elif priority_input == "":
                        priority = None  # Don't filter by priority
                    else:
                        print("Invalid priority value.")
                        continue

                if filter_choice in ["3", "5", "6", "7"]:
                    date_choice = input("Filter by date (today/yesterday, or press Enter for all): ").strip().lower()
                    if date_choice in ["today", "yesterday"]:
                        date_filter = date_choice
                    elif date_choice == "":
                        date_filter = None  # Don't filter by date
                    else:
                        print("Invalid date filter value. Use 'today' or 'yesterday'.")
                        continue

                results = todo_manager.filter_tasks(completed, priority, date_filter)
                if not results:
                    print("No tasks match the filter criteria.")
                else:
                    print(f"\nFiltered Tasks:")
                    for task in results:
                        status = "Completed" if task.completed else "Pending"
                        print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {status}, Priority: {task.priority}, Tags: {', '.join(task.tags)}")

            elif choice == "8":
                # Sort tasks functionality
                print("\nSort Options:")
                print("1. By title (alphabetical)")
                print("2. By priority (high to low)")
                print("3. By creation date (oldest first)")

                sort_choice = input("Select a sort option (1-3): ").strip()

                if sort_choice == "1":
                    sorted_tasks = todo_manager.sort_tasks("title")
                    sort_method = "Alphabetical by title"
                elif sort_choice == "2":
                    sorted_tasks = todo_manager.sort_tasks("priority")
                    sort_method = "By priority (high to low)"
                elif sort_choice == "3":
                    sorted_tasks = todo_manager.sort_tasks("date")
                    sort_method = "By creation date (oldest first)"
                else:
                    print("Invalid sort option.")
                    continue

                print(f"\nTasks sorted by {sort_method}:")
                for task in sorted_tasks:
                    status = "Completed" if task.completed else "Pending"
                    print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {status}, Priority: {task.priority}, Tags: {', '.join(task.tags)}")

            elif choice == "9":
                print("Exiting application...")
                break
            else:
                print("Invalid option. Please select 1, 2, 3, 4, 5, 6, 7, 8, or 9.")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted by user. Exiting...")
            break
        except Exception as e:
            # Ensure no stack traces are shown to users in any error condition
            print("An unexpected error occurred. Please try again.")
            # In a real application, we would log this error for debugging
            # print(f"Debug info: {str(e)}")  # This would be commented out in production


if __name__ == "__main__":
    main()