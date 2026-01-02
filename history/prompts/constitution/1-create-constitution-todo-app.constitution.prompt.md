---
id: 2
title: create-constitution-todo-app
stage: constitution
date: 2026-01-01
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, governance, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - constitution.md validated
 - no placeholder tokens remaining
---

## Prompt

/sp.constitution

Project: The Evolution of Todo – AI-Native Software Development

Focus:
Progressive evolution of a Todo application from an in-memory CLI program to a cloud-native, distributed, AI-powered system using agentic, spec-driven development.

Goal:
Enable students to act as Product Architects by using AI agents to design, plan, and implement software systems without writing boilerplate code manually. Emphasis is on process quality, specifications, and architectural thinking rather than raw coding.

Core Principles:
- Spec-driven development: All implementation must originate from written specifications
- Agentic workflow integrity: Write spec → generate plan → break into tasks → implement via Claude Code
- Clarity and simplicity: Code and specs must be understandable to intermediate Python developers
- Incremental complexity: Each phase builds cleanly on the previous phase
- Determinism and traceability: Every feature must map back to a spec requirement

Key Standards:
- No manual coding: All code must be generated via Claude Code
- Clean architecture: Clear separation of concerns and proper Python project structure
- Readable specifications: Specs should be concise, unambiguous, and testable
- Consistent naming: Files, folders, functions, and variables must follow Python conventions
- Reproducibility: Another developer should be able to regenerate the project from specs alone

Constraints:
- Language: Python 3.13+
- Dependency management: UV
- Development tools: Claude Code, Spec-Kit Plus
- Scope (Phase I only):
  - In-memory data storage (no database)
  - Console-based interface (CLI)
  - Single-process application
- Manual edits to generated source code are not allowed

Deliverable Requirements:
- GitHub repository containing:
  - sp.constitution file
  - specs_history/ folder with all spec versions
  - src/ folder with Python source code
  - README.md with setup and run instructions
  - CLAUDE.md with Claude Code usage guidelines
- Working console application demonstrating:
  - Add todo (title, description)
  - View all todos with status
  - Update todo details
  - Delete todo by ID
  - Mark todo as complete/incomplete

Success Criteria:
- All 5 basic todo features work correctly via CLI
- Project strictly follows spec-driven and agentic workflow
- Codebase runs without errors using documented setup steps
- Specs fully describe system behavior with no undocumented logic
- Repository structure matches defined standards

## Response snapshot

I have successfully created the project constitution for "The Evolution of Todo – AI-Native Software Development" according to your specifications. Here's what was accomplished:

### Changes Made:
1. Updated the constitution file at `.specify/memory/constitution.md` with project-specific details
2. Replaced all placeholder tokens with actual project requirements
3. Created 6 core principles aligned with your project goals:
   - Spec-driven development
   - Agentic workflow integrity
   - Clarity and simplicity
   - Incremental complexity
   - Determinism and traceability
   - No manual coding
4. Added sections for Additional Constraints and Development Workflow
5. Included governance rules and version information

### Validation:
- Confirmed no placeholder tokens remain in the file
- Verified all project requirements from your input have been incorporated
- Ensured the constitution follows the required structure and format

### Version Information:
- **Version**: 1.0.0
- **Ratified**: 2026-01-01
- **Last Amended**: 2026-01-01

### Suggested Commit Message:
`docs: create constitution for Todo app project with core principles and governance`

The constitution now properly reflects your project's focus on spec-driven development, agentic workflows, and AI-native software development practices while maintaining all the constraints and requirements you specified.

## Outcome

- ✅ Impact: Created complete constitution with 6 core principles and governance structure
- 🧪 Tests: Validated no placeholder tokens remain in constitution file
- 📁 Files: Updated .specify/memory/constitution.md with project-specific content
- 🔁 Next prompts: Ready for spec creation with /sp.specify
- 🧠 Reflection: Constitution establishes clear governance for agentic development workflow

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All validation checks passed
- Prompt variant (if applicable): Standard /sp.constitution workflow
- Next experiment (smallest change to try): Proceed to specification phase with /sp.specify