# The Evolution of Todo – AI-Native Software Development Constitution

## Core Principles

### Spec-driven development
All implementation must originate from written specifications. Every feature and functionality must be traceable back to a specific requirement in the specification document.

### Agentic workflow integrity
Adhere to the Write spec → generate plan → break into tasks → implement via Claude Code workflow. Maintain strict separation between specification, planning, and implementation phases.

### Clarity and simplicity
Code and specifications must be understandable to intermediate Python developers. Prioritize clear, readable code over clever optimizations when there's a trade-off.

### Incremental complexity
Each phase builds cleanly on the previous phase. Add complexity only when necessary and ensure each addition is well-integrated with existing functionality.

### Determinism and traceability
Every feature must map back to a spec requirement. Maintain clear traceability from user requirements through specifications to implementation code.

### No manual coding
All code must be generated via Claude Code. Manual edits to generated source code are not allowed unless explicitly specified in exceptional circumstances.

## Additional Constraints

### Language and Dependencies
- Language: Python 3.13+
- Dependency management: UV
- Development tools: Claude Code, Spec-Kit Plus

### Phase I Scope Limitations
- In-memory data storage (no database)
- Console-based interface (CLI)
- Single-process application
- No external API dependencies beyond core requirements

### Deliverable Requirements
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

## Development Workflow

### Specification Requirements
- Specifications must be concise, unambiguous, and testable
- All features must be documented in specifications before implementation
- Specifications must include acceptance criteria for each feature

### Implementation Standards
- Clean architecture with clear separation of concerns
- Proper Python project structure following standard conventions
- Consistent naming following Python conventions (PEP 8)
- Reproducibility: another developer should be able to regenerate the project from specs alone

### Quality Assurance
- All 5 basic todo features must work correctly via CLI
- Project must strictly follow spec-driven and agentic workflow
- Codebase must run without errors using documented setup steps
- Specifications must fully describe system behavior with no undocumented logic

## Governance

This constitution governs all development activities for the Todo application project. All implementation work must comply with these principles. Amendments to this constitution require explicit documentation of the change, approval from project stakeholders, and a migration plan for existing code. All pull requests and code reviews must verify compliance with these principles before approval.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
