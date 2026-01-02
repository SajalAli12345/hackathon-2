---
description: "Task list for In-Memory Python Console Todo Application implementation"
---

# Tasks: In-Memory Python Console Todo Application (Phase I)

**Input**: Design documents from `/specs/1-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python 3.13 project with pyproject.toml
- [X] T003 [P] Create directory structure (src/models/, src/services/, src/repositories/, src/cli/, src/utils/, tests/)

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Todo data model in src/models/todo.py
- [X] T005 Create in-memory todo repository in src/repositories/todo_repository.py
- [X] T006 Create validators utility in src/utils/validators.py
- [X] T007 Create basic CLI menu structure in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo Task (Priority: P1) 🎯 MVP

**Goal**: Implement the ability for users to add new tasks to their todo list with title and optional description

**Independent Test**: The application can accept a new todo task with a title and optional description, store it in memory, and display a confirmation message to the user.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T008 [P] [US1] Unit test for Todo model validation in tests/unit/models/test_todo.py
- [ ] T009 [P] [US1] Unit test for repository add functionality in tests/unit/repositories/test_todo_repository.py

### Implementation for User Story 1

- [X] T010 [P] [US1] Implement Todo model with validation in src/models/todo.py
- [X] T011 [US1] Implement repository add method in src/repositories/todo_repository.py
- [X] T012 [US1] Implement input validation for adding tasks in src/utils/validators.py
- [X] T013 [US1] Implement add task functionality in CLI menu in src/cli/main.py
- [X] T014 [US1] Add success/error messages for add task operation

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement the ability for users to view all their tasks with titles, descriptions, and completion status

**Independent Test**: The application can display all currently stored tasks with their titles, descriptions, and completion status in a clear, readable format.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T015 [P] [US2] Unit test for repository get_all functionality in tests/unit/repositories/test_todo_repository.py
- [ ] T016 [P] [US2] Integration test for viewing all tasks in tests/integration/test_view_tasks.py

### Implementation for User Story 2

- [X] T017 [P] [US2] Implement repository get_all method in src/repositories/todo_repository.py
- [X] T018 [US2] Implement view all tasks functionality in CLI menu in src/cli/main.py
- [X] T019 [US2] Add formatting for displaying tasks in src/cli/main.py
- [X] T020 [US2] Handle case for no tasks in the list

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Implement the ability for users to update the completion status of specific tasks by their ID

**Independent Test**: The application can update the completion status of a specific task by its ID and reflect this change in the task list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T021 [P] [US3] Unit test for repository mark complete/incomplete in tests/unit/repositories/test_todo_repository.py

### Implementation for User Story 3

- [X] T022 [P] [US3] Implement repository mark_complete method in src/repositories/todo_repository.py
- [X] T023 [P] [US3] Implement repository mark_incomplete method in src/repositories/todo_repository.py
- [X] T024 [US3] Implement mark task functionality in CLI menu in src/cli/main.py
- [X] T025 [US3] Add input validation for task ID in src/utils/validators.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Implement the ability for users to update the title and/or description of existing tasks by their ID

**Independent Test**: The application can update the title and/or description of a specific task by its ID while preserving other attributes.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T026 [P] [US4] Unit test for repository update functionality in tests/unit/repositories/test_todo_repository.py

### Implementation for User Story 4

- [X] T027 [US4] Implement repository update method in src/repositories/todo_repository.py
- [X] T028 [US4] Implement update task functionality in CLI menu in src/cli/main.py
- [X] T029 [US4] Add input validation for updating tasks in src/utils/validators.py

---
## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: Implement the ability for users to remove specific tasks by their ID

**Independent Test**: The application can remove a specific task by its ID and confirm the deletion to the user.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T030 [P] [US5] Unit test for repository delete functionality in tests/unit/repositories/test_todo_repository.py

### Implementation for User Story 5

- [X] T031 [US5] Implement repository delete method in src/repositories/todo_repository.py
- [X] T032 [US5] Implement delete task functionality in CLI menu in src/cli/main.py
- [X] T033 [US5] Add confirmation prompts for deletion in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T034 [P] Add comprehensive error handling across all operations
- [X] T035 [P] Add input validation for all user inputs
- [X] T036 Improve CLI user experience with better prompts and messages
- [X] T037 [P] Add README.md with setup and usage instructions
- [X] T038 Run quickstart validation to ensure all functionality works

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model validation in tests/unit/models/test_todo.py"
Task: "Unit test for repository add functionality in tests/unit/repositories/test_todo_repository.py"

# Launch all models for User Story 1 together:
Task: "Implement Todo model with validation in src/models/todo.py"
```

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence