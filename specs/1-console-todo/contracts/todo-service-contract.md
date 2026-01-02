# Todo Service API Contract

## Overview
This contract defines the interface for the TodoService that handles all business logic for todo operations.

## Methods

### `add_todo(title: str, description: str = "") -> dict`
- **Purpose**: Add a new todo item
- **Input**: title (required), description (optional)
- **Output**: Todo object with id, title, description, completed
- **Validation**: Title must not be empty
- **Error cases**: ValueError if title is empty

### `get_all_todos() -> list[dict]`
- **Purpose**: Retrieve all todo items
- **Input**: None
- **Output**: List of all todo objects
- **Error cases**: None

### `get_todo_by_id(id: int) -> dict | None`
- **Purpose**: Retrieve a specific todo by ID
- **Input**: Todo ID
- **Output**: Todo object or None if not found
- **Error cases**: None (returns None if not found)

### `update_todo(id: int, title: str, description: str) -> dict | None`
- **Purpose**: Update todo details
- **Input**: Todo ID, new title, new description
- **Output**: Updated todo object or None if not found
- **Error cases**: None (returns None if not found)

### `delete_todo(id: int) -> bool`
- **Purpose**: Delete a todo by ID
- **Input**: Todo ID
- **Output**: True if deleted, False if not found
- **Error cases**: None

### `mark_todo_complete(id: int) -> dict | None`
- **Purpose**: Mark a todo as complete
- **Input**: Todo ID
- **Output**: Updated todo object or None if not found
- **Error cases**: None (returns None if not found)

### `mark_todo_incomplete(id: int) -> dict | None`
- **Purpose**: Mark a todo as incomplete
- **Input**: Todo ID
- **Output**: Updated todo object or None if not found
- **Error cases**: None (returns None if not found)