# Research: In-Memory Todo Console App (Recurring Tasks & Time-Based Reminders)

## Decision: Time-based reminder implementation approach
**Rationale**: Using a controlled loop that checks every 10 seconds during runtime aligns with constitutional constraints (no external libraries, no background threads) while ensuring timely reminders without excessive resource usage.
**Alternatives considered**:
- Continuous background thread (violates constitutional constraint against persistent background schedulers)
- Check only on user interaction (would miss time-based triggers)
- External scheduler library (violates constitutional constraint of standard library only)

## Decision: Task model extension
**Rationale**: Extending the existing Task model with `due_at` (datetime) and `recurrence` (str | None) fields directly supports the specification requirements while maintaining in-memory constraints.
**Alternatives considered**:
- Separate reminder system (would add unnecessary complexity)
- Storing time data externally (violates in-memory constraint)

## Decision: Date/time input parsing
**Rationale**: Using Python's standard library `datetime.strptime()` with multiple format patterns supports the specification requirement to accept multiple common date/time formats.
**Alternatives considered**:
- External date parsing libraries (violates standard library constraint)
- Natural language parsing (requires external libraries)

## Decision: Recurrence interval calculation
**Rationale**: Using Python's `datetime` and `timedelta` modules for daily/weekly intervals and `calendar.monthrange()` for monthly intervals handles all requirements including edge cases like month-end dates.
**Alternatives considered**:
- External date manipulation libraries (violates standard library constraint)
- Custom date arithmetic (would be error-prone)

## Decision: CLI interaction updates
**Rationale**: Extending existing CLI commands with new options for setting due dates and recurrence maintains consistency with existing UX while adding required functionality.
**Alternatives considered**:
- Separate time-based commands (would fragment user experience)
- New UI paradigm (violates terminal-first constraint)