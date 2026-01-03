# Quickstart Guide for Recurring Time Customization & Terminal UI Presentation

## Overview
This guide explains how to implement the recurring time customization and terminal UI presentation enhancements to the in-memory Todo Console Application.

## Prerequisites
- Python 3.13+ installed
- `uv` package manager installed
- Understanding of the existing application structure in `/src`

## Implementation Steps

### 1. Update CLI Input Handling (main.py)
- Extend recurring task creation flow to prompt for optional time input
- Add time validation using HH:MM format
- Apply default time (00:00) when no time is provided
- Handle invalid time formats gracefully

### 2. Update Time Application Logic (todo.py)
- Modify recurrence advancement logic to preserve the time component
- When creating/updating recurring tasks, apply the specified time to due_at field
- Ensure each recurrence advances only the date, not the time

### 3. Implement Terminal UI Enhancements
- Create table-like display using string formatting
- Apply ANSI escape codes for color formatting
- Ensure UI changes don't affect underlying task data

### 4. Testing
- Test recurring task creation with custom times
- Verify time preservation across recurrences
- Test table-like display formatting
- Validate error handling for invalid inputs

## Key Files to Modify
- `/src/main.py` - CLI input handling
- `/src/todo.py` - Recurrence logic updates
- UI display functions in both files

## Constraints to Remember
- Use only Python standard library
- Maintain backward compatibility
- Preserve existing functionality
- No external dependencies