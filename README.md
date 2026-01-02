# In-Memory Python Console Todo Application

A simple command-line based todo application that stores all tasks in memory. Supports basic task management operations including adding, viewing, updating, deleting, and marking tasks as complete/incomplete.

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. Clone the repository
2. Navigate to project directory
3. Install dependencies: `uv sync`
4. Run the application: `uv run python src/cli/main.py`

## Usage

The application provides a menu-driven interface:

1. **Add a new task** - Create a new todo with title and optional description
2. **View all tasks** - Display all current tasks with their status
3. **Update a task** - Modify existing task title or description
4. **Delete a task** - Remove a task by its ID
5. **Mark task as complete** - Update task status to completed
6. **Mark task as incomplete** - Update task status to pending
7. **Exit** - Quit the application

## Example Workflow

1. Start the app: `uv run python src/cli/main.py`
2. Select "Add Task" and enter title/description
3. Select "View All Tasks" to see your list
4. Select "Mark Task Complete" to update status
5. Continue managing tasks as needed
6. Exit when finished

## Common Commands

- `uv run python src/cli/main.py` - Run the application
- `uv run pytest` - Run tests
- `uv run python -m pytest tests/` - Run tests with more verbose output

## Architecture

The application follows a clean architecture pattern:

- **Models**: `src/models/` - Data models (Todo class)
- **Repositories**: `src/repositories/` - Data access layer (TodoRepository)
- **Utils**: `src/utils/` - Utility functions (validators)
- **CLI**: `src/cli/` - User interface layer (main application)

## Features

- In-memory storage (no persistence)
- Console-based menu interface
- Task validation (non-empty titles)
- Error handling and user feedback
- Confirmation prompts for destructive operations
- Clean, readable output formatting