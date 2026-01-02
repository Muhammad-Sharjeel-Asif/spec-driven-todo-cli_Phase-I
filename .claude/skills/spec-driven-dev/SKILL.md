---
name: spec-driven-dev
description: Comprehensive spec-driven development approach for terminal-based Python applications with focus on precise specifications, architectural planning, validation, and implementation following strict constraints (Python standard library only, in-memory, /src structure). Use when building CLI applications following the SDD methodology with constitution, spec, plan, and task artifacts.
---

# Spec-Driven Development for Terminal-Based Python Applications

This skill teaches Claude how to follow a comprehensive spec-driven development (SDD) approach for building terminal-based Python applications, emphasizing precise specifications before implementation and strict adherence to architectural constraints.

## When to Use

Use this skill whenever:
- Building a new terminal-based Python CLI application
- Following the SDD methodology (specification, plan, tasks, implementation)
- Working with projects that require constitution, spec, plan, and task artifacts
- Enforcing constraints like Python standard library only, in-memory storage, and /src structure
- Need to ensure architectural decisions are properly documented with ADRs

## Goals

Claude should:
1. Create precise, detailed specifications before any implementation
2. Follow the constitution strictly without feature leakage
3. Validate all output is safe for sp.analyze tooling
4. Use markdown-only specifications and plans
5. Enforce tooling constraints (Python standard library only, in-memory, /src structure)
6. Ensure no code is written without an approved specification

## Core Process

### 1. Specification Phase
- Write a comprehensive spec.md before any implementation
- Define clear acceptance criteria and user stories
- Document all functional and non-functional requirements
- Ensure the spec aligns with the project constitution
- Include example usage and command-line interface patterns

### 2. Planning Phase
- Create a detailed plan.md that strictly follows the constitution and specification
- Identify architectural decisions that require ADRs
- Map out implementation tasks in dependency order
- Consider all constraints (no external dependencies, in-memory only, etc.)
- Document risk analysis and mitigation strategies

### 3. Task Generation
- Generate testable tasks.md with clear acceptance criteria
- Create tasks that are small, verifiable, and atomic
- Ensure tasks reference code precisely with file paths and line numbers
- Include testing and validation tasks
- Validate all output is safe for sp.analyze

### 4. Implementation Phase
- Only implement after specification and plan approval
- Follow the /src directory structure strictly
- Use Python standard library only - no external packages
- Implement in-memory storage only - no persistence
- Write tests alongside implementation
- Create PHRs for significant changes

## Key Constraints to Enforce

### Technology Stack
- Python 3.13+ only
- Python standard library only (no external dependencies like uv, pip packages)
- In-memory storage only (no databases, files, or persistence)
- /src directory structure for source code

### Development Process
- No implementation without approved specification
- Plan must strictly follow constitution and spec
- All architectural decisions documented as ADRs when significant
- PHR creation for all major changes
- Output validation for sp.analyze safety

### Code Quality
- Small, testable diffs only
- No unrelated code refactoring
- Proper error handling and edge cases
- Clear, documented interfaces
- Follow existing code patterns and conventions

## Architectural Decision Process

When significant architectural decisions are detected, suggest ADR creation:
- Impact: long-term consequences? (framework, data model, API, security)
- Alternatives: multiple viable options considered?
- Scope: cross-cutting and influences system design?

If ALL true, suggest: "📋 Architectural decision detected: [brief-description] — Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`"

## Validation Requirements

### Pre-Implementation Checklist
- [ ] Specification document exists and is approved
- [ ] Plan document exists and follows specification
- [ ] All constraints properly addressed (tech stack, architecture)
- [ ] Tasks are testable and atomic
- [ ] Output format is safe for sp.analyze tooling

### During Implementation Checklist
- [ ] Follow /src directory structure
- [ ] Use Python standard library only
- [ ] Implement in-memory storage only
- [ ] Create PHRs for significant changes
- [ ] Maintain code references to modified files
- [ ] Write tests for new functionality

### Post-Implementation Checklist
- [ ] All tasks completed successfully
- [ ] Specification requirements met
- [ ] Plan followed without deviations
- [ ] ADRs created for significant decisions
- [ ] PHRs created for all major changes
- [ ] Output validated for sp.analyze safety

## Example Workflow

### 1. Initial Specification
```
Feature: CLI To-Do Application

As a user, I want to manage my tasks through a command-line interface so that I can efficiently track my productivity without a GUI.

Acceptance Criteria:
- User can add new tasks with descriptions
- User can list all tasks with status
- User can mark tasks as completed
- User can delete tasks
- All data stored in memory only (no persistence)
- Uses Python standard library only
- Runs in terminal environment
```

### 2. Architecture Planning
- Terminal UI using standard input/output
- In-memory task storage using Python lists/dicts
- Command parsing using argparse
- No external dependencies
- All code in /src directory

### 3. Task Generation
- Create task data model
- Implement task storage (in-memory)
- Build command-line argument parser
- Implement add task functionality
- Implement list tasks functionality
- Implement complete task functionality
- Implement delete task functionality
- Add help and error handling
- Write unit tests for each function

## Guidelines

- Always prioritize specification over implementation
- Follow the constitution strictly without feature creep
- Use markdown-only for all documentation artifacts
- Enforce technology constraints rigorously
- Validate all output for tooling compatibility
- Create PHRs for all significant development activities
- Document architectural decisions as ADRs when appropriate
- Keep implementation changes minimal and focused

## Reference Documentation

For detailed information about specific aspects of the SDD process, see:

- **SDD Process Details**: [references/sdd-process.md](references/sdd-process.md) - Complete guide to the spec-driven development methodology, artifacts, and validation requirements
- **Constitution Principles**: [references/constitution-principles.md](references/constitution-principles.md) - Detailed constraints and principles that must be followed in all implementations