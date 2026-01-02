# Quickstart Guide: In-Memory Python Console Todo Application

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone the repository
2. Navigate to project directory
3. Install dependencies: `uv sync`
4. Run the application: `uv run python src/cli/main.py`

## Basic Usage
1. Launch the application
2. Use the menu options to:
   - Add a new task (Option 1)
   - View all tasks (Option 2)
   - Update a task (Option 3)
   - Delete a task (Option 4)
   - Mark task as complete/incomplete (Option 5)
   - Exit (Option 6)

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