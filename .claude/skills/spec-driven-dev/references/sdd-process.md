# Spec-Driven Development Reference Guide

This reference guide provides detailed information about the spec-driven development (SDD) process for terminal-based Python applications.

## SDD Artifacts

### 1. Constitution (constitution.md)
The constitution defines the fundamental principles, constraints, and non-negotiables for the project:

- Technology stack constraints (Python standard library only)
- Architecture principles (in-memory only, no persistence)
- Code quality standards
- Team collaboration guidelines
- Project structure requirements (/src directory)

### 2. Specification (spec.md)
The specification document details what the application should do:

- User stories and use cases
- Functional requirements
- Non-functional requirements
- Acceptance criteria
- Example usage scenarios
- Error handling requirements
- Performance expectations

### 3. Plan (plan.md)
The plan document describes how the application will be built:

- Architectural decisions
- Implementation approach
- Technology choices
- Risk analysis
- Data flow diagrams
- Interface definitions
- Testing strategy

### 4. Tasks (tasks.md)
The tasks document breaks down implementation into executable steps:

- Individual, testable tasks
- Dependencies between tasks
- Acceptance criteria for each task
- Code references and file locations
- Test scenarios

## SDD Commands and Workflow

### Initialization
1. `/sp.specify` - Create or update feature specification
2. `/sp.plan` - Create implementation plan
3. `/sp.tasks` - Generate actionable tasks
4. `/sp.analyze` - Validate consistency across artifacts

### Implementation
1. `/sp.implement` - Execute implementation plan
2. `/sp.adr` - Create architectural decision records
3. `/sp.phr` - Create prompt history records
4. `/sp.git.commit_pr` - Commit and create pull request

## Quality Checks

### Specification Quality
- Clear acceptance criteria
- Complete user stories
- Defined error cases
- Performance requirements
- Security considerations

### Plan Quality
- Architectural decisions justified
- Risk mitigation strategies
- Technology choices explained
- Implementation approach clear
- Resource requirements defined

### Task Quality
- Each task is testable
- Tasks are atomic and independent
- Dependencies clearly defined
- Code references precise
- Acceptance criteria measurable

## Common Anti-Patterns to Avoid

### 1. Implementation Before Specification
- Never write code without an approved specification
- Always validate requirements before implementation
- Get sign-off on spec and plan before coding

### 2. Feature Creep
- Stick strictly to the specification
- Don't add features not in the original spec
- Create new specs for additional features

### 3. Technology Constraint Violations
- No external dependencies beyond standard library
- No persistence mechanisms (files, databases)
- No network calls unless specified
- Follow /src directory structure

### 4. Inadequate Testing
- Each task should include test scenarios
- Test edge cases and error conditions
- Validate output formats
- Ensure cross-platform compatibility

## Validation Checklist

Before proceeding with implementation, ensure:

### Specification Validation
- [ ] All user stories have acceptance criteria
- [ ] Error cases are defined
- [ ] Performance requirements are measurable
- [ ] Security requirements are specified
- [ ] The spec aligns with constitution

### Plan Validation
- [ ] Architecture decisions are justified
- [ ] Risk analysis is complete
- [ ] Technology choices align with constraints
- [ ] Implementation approach is feasible
- [ ] Plan follows specification exactly

### Task Validation
- [ ] All tasks are testable
- [ ] Dependencies are properly ordered
- [ ] Tasks reference specific code locations
- [ ] Acceptance criteria are measurable
- [ ] Tasks are atomic and focused

## Architectural Decision Record (ADR) Guidelines

Create ADRs when decisions meet these criteria:
- Long-term consequences (framework, data model, API, security)
- Multiple viable alternatives considered
- Cross-cutting impact on system design

Common ADR topics:
- Data storage approach (in-memory structures)
- CLI framework choice (argparse vs alternatives)
- Error handling strategy
- Testing framework selection
- Configuration management
- Logging approach