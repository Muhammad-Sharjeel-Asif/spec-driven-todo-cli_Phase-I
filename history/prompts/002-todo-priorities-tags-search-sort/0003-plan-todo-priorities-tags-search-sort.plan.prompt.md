---
id: 0003
title: plan-todo-priorities-tags-search-sort
stage: plan
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: 002-todo-priorities-tags-search-sort
branch: 002-todo-priorities-tags-search-sort
user: unknown
command: /sp.plan
labels: ["plan", "todo", "priorities", "tags", "search", "sort", "architecture"]
links:
  spec: "../specs/002-todo-priorities-tags-search-sort/spec.md"
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-todo-priorities-tags-search-sort/plan.md
 - specs/002-todo-priorities-tags-search-sort/research.md
 - specs/002-todo-priorities-tags-search-sort/data-model.md
 - specs/002-todo-priorities-tags-search-sort/quickstart.md
 - specs/002-todo-priorities-tags-search-sort/contracts/task-api-contract.md
tests:
 - none
---

## Prompt

# Plan — In-Memory Todo Console App (Priorities, Tags, Search, Sort)

## 1. Scope & Constitutional Validation
- Reconfirm alignment with Constitution
- Confirm implementation is limited strictly to features
- Ensure existing features and their behavior remains unchanged and functional
- Verify exclusions:
  - No persistence
  - No background threads or timers
  - No due dates or recurrence
  - No external libraries
  - No GUI or web interface
- Confirm constraints:
  - Python 3.13+
  - Standard library only
  - uv as the only execution tool

---

## 2. Project Structure Enforcement
- Ensure all Python files remain inside `/src`
- Confirm only the following files exist:
  - `main.py`
  - `todo.py`
  - `models.py`
- Do not introduce any new Python modules

---

## 3. Data Model Extension (`models.py`)
- Extend the existing Task model to include Phase-II fields:
  - `priority`
  - `tags`
  - `created_at`
- Enforce constraints:
  - Priority values limited to: high, medium, low
  - Tags stored as a list of strings
  - `created_at` used only for in-session filtering and sorting
- Ensure:
  - No persistence logic
  - No derived or future-oriented fields
  - Model remains a data container only

---

## 4. Business Logic Enhancements (`todo.py`)
- Preserve all existing task operations without modification
- Extend logic to support:
  - Assigning and updating task priority
  - Assigning and updating task tags
- Implement read-only operations for:
  - Keyword-based search (title, description, tags)
  - Filtering by:
    - Completion status
    - Priority level
    - Creation date
  - Sorting by:
    - Alphabetical order of title
    - Priority level
    - Creation date
- Ensure:
  - Search, filter, and sort do not mutate stored task data
  - Invalid inputs are handled gracefully
  - All logic remains in-memory only

---

## 5. CLI Interaction Updates (`main.py`)
- Extend the existing terminal interface to expose these features
- Provide clear, human-readable prompts for:
  - Setting priority and tags during task creation
  - Updating priority and tags
  - Selecting search keywords
  - Choosing filter criteria
  - Selecting sorting options
- Ensure:
  - CLI remains error-tolerant
  - Invalid choices return helpful messages
  - Control always returns to the main CLI loop

---

## 6. Input Validation & Error Handling
- Validate:
  - Priority values against allowed set
  - Tag input formatting
  - Search and filter selections
- Handle:
  - Empty search results
  - Invalid filter or sort options
- Ensure:
  - No crashes
  - No stack traces
  - Consistent, user-friendly error messages

---

## 7. uv-Based Execution
- Verify application execution using uv
- Ensure no additional tooling or dependency configuration is introduced
- Confirm standard library usage only

---

## 8. Acceptance Criteria Verification
- Confirm tasks support priority and tags correctly
- Verify search returns accurate results
- Verify filters work by status, priority, and creation date
- Verify sorting works alphabetically, by priority, and by creation date
- Ensure all behavior remains in-memory only
- Confirm no excluded or future-phase features exist
- Validate every behavior is traceable to the specification

---

## 9. Phase Boundary Enforcement
- Stop implementation immediately after acceptance criteria are met
- Do not refactor or optimize beyond specification
- Require a new specification for any further features or phases

## Response snapshot

Completed implementation planning for Todo Console App with Priorities, Tags, Search, and Sort. Created comprehensive plan with technical context, data model, API contracts, and quickstart guide.

## Outcome

- ✅ Impact: Complete implementation plan created with all required artifacts for development
- 🧪 Tests: none
- 📁 Files: specs/002-todo-priorities-tags-search-sort/plan.md, research.md, data-model.md, quickstart.md, contracts/task-api-contract.md
- 🔁 Next prompts: /sp.tasks to generate development tasks
- 🧠 Reflection: Planning phase complete with constitutional compliance verified and all technical decisions documented

## Evaluation notes (flywheel)

- Failure modes observed: None - all planning artifacts successfully created and constitutional compliance verified
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
