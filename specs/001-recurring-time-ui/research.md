# Research for Recurring Time Customization & Terminal UI Presentation

## Decision: Time Input Format
**Rationale:** The system will accept time in HH:MM format (24-hour format) to maintain consistency with existing datetime display format in the application. This aligns with the existing `due_at` field format which displays as `YYYY-MM-DD HH:MM`.

**Alternatives considered:**
- 12-hour format with AM/PM: Would require additional parsing and conversion logic
- Natural language parsing (e.g., "3pm", "15:30"): Would require complex parsing libraries that violate the standard library constraint

## Decision: Time Validation Method
**Rationale:** Use Python's `datetime.strptime()` with format `%H:%M` to validate time input. This uses only standard library and provides accurate validation for HH:MM format with hours 00-23 and minutes 00-59.

**Alternatives considered:**
- Regular expression validation: Would require more complex patterns to ensure valid time ranges
- Manual parsing with int conversion: Would be more error-prone and verbose

## Decision: Default Time for Recurring Tasks
**Rationale:** Default to `00:00` (midnight) when no time is specified, maintaining the existing behavior. This ensures backward compatibility and provides a consistent default.

## Decision: UI Formatting Approach
**Rationale:** Use ANSI escape codes directly for color formatting and string formatting methods for table-like layout. This adheres to the constraint of using only standard library functionality.

**Alternatives considered:**
- External libraries (rich, tabulate, colorama): Prohibited by constitution
- HTML or rich text formatting: Prohibited by constitution

## Decision: Task Display Structure
**Rationale:** Implement fixed-width column formatting using Python's string formatting capabilities (e.g., `str.ljust()`, `str.center()`, f-strings with width specifiers) to create a table-like appearance without external dependencies.

## Decision: Recurrence Time Preservation Logic
**Rationale:** When advancing a recurring task, preserve the original time component from the due_at field while only advancing the date portion according to the recurrence interval. This ensures that the user-specified time is maintained across all recurrences.

**Alternatives considered:**
- Resetting to default time: Would violate the requirement to preserve user-specified time
- Random time assignment: Would be unpredictable and not user-friendly