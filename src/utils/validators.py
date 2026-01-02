from typing import Any, Optional


def validate_task_id(task_id: str) -> Optional[int]:
    """
    Validate that the task ID is a positive integer.

    Args:
        task_id: String representation of task ID

    Returns:
        int: Validated task ID or None if invalid
    """
    try:
        id_num = int(task_id)
        if id_num <= 0:
            return None
        return id_num
    except ValueError:
        return None


def validate_title(title: str) -> bool:
    """
    Validate that the title is not empty.

    Args:
        title: Task title to validate

    Returns:
        bool: True if valid, False otherwise
    """
    return bool(title and title.strip())


def validate_todo_input(title: str, description: str = "") -> tuple[bool, str]:
    """
    Validate todo input parameters.

    Args:
        title: Task title
        description: Task description (optional)

    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not validate_title(title):
        return False, "Title cannot be empty"

    if not isinstance(description, str):
        return False, "Description must be a string"

    return True, ""