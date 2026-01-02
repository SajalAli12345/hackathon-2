from typing import Dict, List, Optional
from src.models.todo import Todo


class TodoRepository:
    """
    In-memory repository for managing Todo items.
    Uses Python dictionary for storage as specified in requirements.
    """

    def __init__(self):
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1

    def add(self, todo: Todo) -> Todo:
        """
        Add a new todo to the repository.
        The ID will be auto-generated if the todo has ID 0 or negative.
        """
        if todo.id <= 0:
            todo.id = self._next_id
            self._next_id += 1
        elif todo.id in self._todos:
            raise ValueError(f"Todo with ID {todo.id} already exists")

        # If the ID is higher than our current next_id, update it
        if todo.id >= self._next_id:
            self._next_id = todo.id + 1

        self._todos[todo.id] = todo
        return todo

    def get_all(self) -> List[Todo]:
        """Retrieve all todos."""
        return list(self._todos.values())

    def get_by_id(self, id: int) -> Optional[Todo]:
        """Retrieve a specific todo by ID."""
        return self._todos.get(id)

    def update(self, id: int, title: str = None, description: str = None) -> Optional[Todo]:
        """Update todo details."""
        todo = self.get_by_id(id)
        if todo is None:
            return None

        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description

        return todo

    def delete(self, id: int) -> bool:
        """Delete a todo by ID."""
        if id in self._todos:
            del self._todos[id]
            return True
        return False

    def mark_complete(self, id: int) -> Optional[Todo]:
        """Mark a todo as complete."""
        todo = self.get_by_id(id)
        if todo is not None:
            todo.mark_complete()
            return todo
        return None

    def mark_incomplete(self, id: int) -> Optional[Todo]:
        """Mark a todo as incomplete."""
        todo = self.get_by_id(id)
        if todo is not None:
            todo.mark_incomplete()
            return todo
        return None