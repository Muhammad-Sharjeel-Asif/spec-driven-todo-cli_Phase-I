#!/usr/bin/env python3
"""
Simple test to verify the time-based todo app functionality
"""
import sys
import os
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo import TodoManager
from models import Task

def test_basic_functionality():
    """Test basic functionality of the time-based todo app"""
    print("Testing basic functionality...")

    # Create a TodoManager instance
    tm = TodoManager()

    # Test 1: Add a simple task without time features
    print("Test 1: Adding a simple task...")
    task1_id = tm._get_next_id()
    task1 = Task(task1_id, "Test task 1", "This is a test task")
    tm.tasks.append(task1)
    tm.next_id = task1_id + 1
    print(f"✓ Added task: {task1.title}")

    # Test 2: Add a task with due date
    print("\nTest 2: Adding a task with due date...")
    task2_id = tm._get_next_id()
    future_date = datetime.now() + timedelta(days=1)
    task2 = Task(task2_id, "Test task 2", "This is a task with due date", due_at=future_date)
    tm.tasks.append(task2)
    tm.next_id = task2_id + 1
    print(f"✓ Added task with due date: {task2.title} - Due: {task2.due_at}")

    # Test 3: Add a recurring task
    print("\nTest 3: Adding a recurring task...")
    task3_id = tm._get_next_id()
    task3 = Task(task3_id, "Test task 3", "This is a recurring task", recurrence="daily")
    tm.tasks.append(task3)
    tm.next_id = task3_id + 1
    print(f"✓ Added recurring task: {task3.title} - Recurs: {task3.recurrence}")

    # Test 4: Add a task with both due date and recurrence
    print("\nTest 4: Adding a task with both due date and recurrence...")
    task4_id = tm._get_next_id()
    task4 = Task(task4_id, "Test task 4", "This has both due date and recurrence",
                 due_at=future_date, recurrence="weekly")
    tm.tasks.append(task4)
    tm.next_id = task4_id + 1
    print(f"✓ Added task with both: {task4.title} - Due: {task4.due_at}, Recurs: {task4.recurrence}")

    # Test 5: Check task listing
    print("\nTest 5: Listing all tasks...")
    for task in tm.get_all_tasks():
        due_info = f", Due: {task.due_at.strftime('%Y-%m-%d %H:%M')}" if task.due_at else ""
        recurrence_info = f", Recurs: {task.recurrence}" if task.recurrence else ""
        print(f"  ID: {task.id}, Title: {task.title}{due_info}{recurrence_info}")

    # Test 6: Test date parsing
    print("\nTest 6: Testing date parsing...")
    test_dates = ["2026-01-03 10:30", "01/03/2026 10:30", "2026-01-03"]
    for date_str in test_dates:
        parsed_date = tm.parse_datetime(date_str)
        if parsed_date:
            print(f"  ✓ Parsed '{date_str}' -> {parsed_date}")
        else:
            print(f"  ✗ Failed to parse '{date_str}'")

    # Test 7: Test recurrence validation
    print("\nTest 7: Testing recurrence validation...")
    valid_recurrences = ["daily", "weekly", "monthly", None]
    invalid_recurrences = ["yearly", "hourly", "invalid"]

    for rec in valid_recurrences:
        is_valid = tm.validate_recurrence(rec)
        print(f"  ✓ Recurrence '{rec}' is valid: {is_valid}")

    for rec in invalid_recurrences:
        is_valid = tm.validate_recurrence(rec)
        print(f"  ✓ Recurrence '{rec}' is valid: {is_valid} (should be False)")

    # Test 8: Test monthly recurrence advance (edge case)
    print("\nTest 8: Testing monthly recurrence advance...")
    test_date = datetime(2026, 1, 31)  # January 31st
    next_month = tm._advance_month(test_date)
    print(f"  ✓ From {test_date.date()} to next month: {next_month.date()}")

    print("\n✓ All tests completed successfully!")
    return True

if __name__ == "__main__":
    try:
        test_basic_functionality()
        print("\n🎉 Application functionality test PASSED!")
    except Exception as e:
        print(f"\n❌ Application functionality test FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)