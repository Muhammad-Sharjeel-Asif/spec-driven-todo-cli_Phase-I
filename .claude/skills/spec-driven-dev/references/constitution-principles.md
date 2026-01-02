# Constitution Reference for Python CLI Applications

This reference provides detailed information about the constitutional principles that must be followed in spec-driven development for terminal-based Python applications.

## Core Technology Constraints

### Python Standard Library Only
- No external dependencies (no pip/uv installations)
- Use only modules available in Python 3.13+ standard library
- Forbidden: requests, numpy, pandas, flask, django, etc.
- Allowed: argparse, os, sys, json, collections, pathlib, etc.

### In-Memory Architecture
- No file persistence
- No database connections
- No external storage mechanisms
- All data exists only during program execution
- State is lost when program terminates

### Project Structure
- All source code in `/src` directory
- Tests in `/tests` directory (if applicable)
- Specifications in `/specs` directory
- No mixing of concerns across directories
- Follow Python package structure conventions

## Development Process Constraints

### Spec-First Development
- Specification must exist before any code
- Plan must align with specification
- Tasks must derive from plan
- No implementation without approved artifacts

### Quality Standards
- Small, focused changes only
- No unrelated refactoring
- Clear, testable acceptance criteria
- Proper error handling
- Documentation for public interfaces

## Architectural Principles

### Minimalism
- Choose the simplest solution that meets requirements
- Avoid over-engineering
- Prefer standard library solutions
- Keep dependencies minimal (none)

### Safety
- Validate all user inputs
- Handle errors gracefully
- No unsafe operations
- Follow security best practices

### Maintainability
- Clear, readable code
- Consistent naming conventions
- Proper separation of concerns
- Testable components

## Code Structure Requirements

### File Organization
```
project/
├── src/
│   ├── __init__.py
│   ├── main.py (entry point)
│   └── modules/
├── specs/
│   ├── feature-name/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   └── tasks.md
├── .specify/
│   └── constitution.md
└── history/
    ├── prompts/
    └── adr/
```

### Module Structure
- Each module should have a single responsibility
- Use clear, descriptive names
- Follow Python naming conventions
- Include docstrings for public functions
- Separate business logic from UI/presentation

## CLI Application Patterns

### Command-Line Interface
- Use argparse for command parsing
- Provide clear help messages
- Handle command-line errors gracefully
- Support standard options (help, version)
- Follow Unix philosophy of single-purpose tools

### Input/Output
- Use standard input/output streams
- Support both interactive and batch modes
- Provide clear, consistent formatting
- Use appropriate exit codes
- Handle terminal size and capabilities appropriately

## Validation Requirements

### Specification Compliance
- Verify all code aligns with spec
- Check that no features are added beyond spec
- Ensure constraints are followed
- Validate architecture decisions

### Tooling Compatibility
- Ensure output is safe for sp.analyze
- Follow markdown formatting standards
- Use consistent artifact structures
- Maintain cross-platform compatibility

## Common Violations to Avoid

### Dependency Violations
- Importing external libraries
- Using non-standard library modules
- Adding package manager files (requirements.txt, pyproject.toml for dependencies)

### Persistence Violations
- Writing to files
- Connecting to databases
- Using any form of persistent storage
- Storing data across program runs

### Architecture Violations
- Implementing before specification
- Deviating from plan without approval
- Adding features not in specification
- Ignoring error cases

## Quality Gates

Before proceeding to the next phase, ensure:

### Specification Phase
- [ ] All requirements are clearly stated
- [ ] Acceptance criteria are measurable
- [ ] User stories are complete
- [ ] Constraints are properly documented

### Planning Phase
- [ ] Architecture aligns with constraints
- [ ] Implementation approach is viable
- [ ] Risk analysis is complete
- [ ] Technology choices are justified

### Implementation Phase
- [ ] Code follows architecture plan
- [ ] All constraints are respected
- [ ] Error handling is comprehensive
- [ ] Code is testable and maintainable