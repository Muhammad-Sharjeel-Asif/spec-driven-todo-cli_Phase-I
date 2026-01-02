"""
Task data model for the Todo Console Application
"""
from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a single todo item with id, title, description, completion status,
    priority level, tags list, and creation timestamp.
    All data exists only in memory during the session.
    """
    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False, due_at: Optional[datetime] = None, recurrence: Optional[str] = None):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = "medium"  # Default priority
        self.tags: List[str] = []  # Default empty tags list
        self.created_at = datetime.now()
        self.due_at = due_at  # Optional due date and time
        self.recurrence = recurrence  # One of: "daily", "weekly", "monthly", or None

    def __str__(self):
        status = "✓" if self.completed else "○"
        due_info = f", Due: {self.due_at.strftime('%Y-%m-%d %H:%M')}" if self.due_at else ""
        recurrence_info = f", Rec: {self.recurrence}" if self.recurrence else ""
        return f"[{status}] {self.id}. {self.title} (Priority: {self.priority}, Tags: {', '.join(self.tags)}{due_info}{recurrence_info})"

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed}, priority='{self.priority}', tags={self.tags}, due_at={self.due_at}, recurrence={self.recurrence})"