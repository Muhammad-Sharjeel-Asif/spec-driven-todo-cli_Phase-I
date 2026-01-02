---
name: terminal-todo-ui
description: Provide consistently styled, attractive terminal user interface layouts and patterns for a to-do list app, focusing on clarity, spacing, colors, and components.
---

# Terminal To-Do UI Skill

This Skill teaches Claude how to produce polished, clear, and visually appealing **terminal UI layouts** for a to-do list application when asked to generate UI designs, ASCII art layouts, or terminal display formats.

## When to Use

Use this skill whenever:
- The user prompts for a terminal-based UI (CLI app layout)
- The user requests attractive formatting/display for terminal output
- The task is about designing screens, menus, headers, footers, boxes, tables, or interactive elements for a terminal to-do app

## Goals

Claude should:
1. Produce terminal screens with clear separation of UI elements.
2. Use consistent ASCII box components, spacing, and symbols.
3. Add simple color annotations (if supported) or conventions like `[INFO]`, `[DONE]`, `>` selection pointers.
4. Avoid verbose prose — UI screens only.

## Instructions

1. Generate layouts primarily using **ASCII boxes**, lines, and sections (e.g., `┌─ ─┐`, `│   │`, `└─ ─┘`).
2. Minimize clutter — show only essential UI elements.
3. Use consistent symbols for to-do items (e.g., `[ ]`, `[x]`, `>` for selection).
4. Use headings like **TODAY'S TASKS**, **PENDING**, **COMPLETED**, etc.
5. Provide **responsive spacing** (e.g., center lists, pad content).
6. If color codes are mentioned (e.g., ANSI codes), keep them consistent and minimal.

## Component Patterns

### Header
```
┌──────────────────────────────────┐
│ 📋 TO-DO LIST APP               │
└──────────────────────────────────┘
```

### Task List
```
[ ] 1. Buy groceries
[x] 2. Write report
[ ] 3. Call team
```

### Input / Prompt
```
Add new task: __________________
```

### Footer
```
────────────────────────────────────
q: exit ↑/↓: move enter: select
────────────────────────────────────
```

## Examples

### Example 1 — Simple To-Do Screen

```
┌──────────────────────┐
│ 📋 MY TODO APP       │
├──────────────────────┤
│ [ ] 1. Learn skills  │
│ [x] 2. Save project  │
│ [ ] 3. Commit code   │
└──────────────────────┘

Enter new task:
```

### Example 2 — Detailed View with Sections

```
┌───────────────────────────────┐
│ 📌 TODAY'S TASKS              │
├───────────────────────────────┤
│ → [ ] Design CLI UI           │
│ [x] Write documentation       │
│ [ ] Test interactive input    │
└───────────────────────────────┘
────────────────────────────────
esc: quit ↑/↓: navigate enter: action
────────────────────────────────
```

## Guidelines

- Always format using ASCII art components.
- May add colors
- Use consistent spacing and alignment.
- Keep the UI concise and easy to parse at a glance.
- If prompted for interactivity hints (keys, navigation), include a footer legend.