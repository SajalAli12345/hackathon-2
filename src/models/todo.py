from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo task with attributes including unique ID, title, description, and completion status.
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title must be non-empty")
        if not isinstance(self.completed, bool):
            raise ValueError("Completed must be a boolean value")
        # For new todos, ID can be <= 0 (will be assigned by repository)
        # For existing todos, ID must be positive
        # We'll validate the ID properly in the repository

    def mark_complete(self):
        """Mark the todo as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the todo as incomplete."""
        self.completed = False

    def update(self, title: Optional[str] = None, description: Optional[str] = None):
        """Update the todo with new title and/or description."""
        if title is not None:
            if not title.strip():
                raise ValueError("Title must be non-empty")
            self.title = title.strip()

        if description is not None:
            self.description = description