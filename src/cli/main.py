#!/usr/bin/env python3
"""
Main CLI entry point for the Todo application.
Provides a console-based menu interface for users to interact with the application.
"""
from typing import Optional
import sys

from src.models.todo import Todo
from src.repositories.todo_repository import TodoRepository
from src.utils.validators import validate_task_id, validate_title


class TodoCLI:
    """Main CLI application class."""

    def __init__(self):
        self.repository = TodoRepository()
        self.running = True

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("           TODO APPLICATION")
        print("="*50)
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete")
        print("6. Mark task as incomplete")
        print("7. Exit")
        print("="*50)

    def get_user_choice(self) -> str:
        """Get user choice from the menu."""
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            sys.exit(0)

    def handle_choice(self, choice: str):
        """Handle the user's menu choice."""
        if choice == "1":
            self.add_task()
        elif choice == "2":
            self.view_tasks()
        elif choice == "3":
            self.update_task()
        elif choice == "4":
            self.delete_task()
        elif choice == "5":
            self.mark_complete()
        elif choice == "6":
            self.mark_incomplete()
        elif choice == "7":
            self.exit_app()
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    def add_task(self):
        """Add a new task to the todo list."""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not validate_title(title):
            print("Error: Title cannot be empty.") 
            return

        description = input("Enter task description (optional): ").strip()

        try:
            # Create todo with ID 0 to indicate auto-assignment by repository
            todo = Todo(id=0, title=title, description=description, completed=False)
            self.repository.add(todo)
            print(f"Task '{title}' added successfully with ID {todo.id}")
        except ValueError as e:
            print(f"Error adding task: {e}")

    def view_tasks(self):
        """Display all tasks."""
        print("\n--- All Tasks ---")
        todos = self.repository.get_all()

        if not todos:
            print("No tasks found.")
            return

        print(f"{'ID':<4} {'Status':<10} {'Title':<20} {'Description'}")
        print("-" * 60)

        for todo in todos:
            status = "✓ Done" if todo.completed else "○ Pending"
            print(f"{todo.id:<4} {status:<10} {todo.title[:19]:<20} {todo.description}")

    def update_task(self):
        """Update an existing task."""
        print("\n--- Update Task ---")
        task_id_str = input("Enter task ID to update: ").strip()
        task_id = validate_task_id(task_id_str)

        if task_id is None:
            print("Error: Invalid task ID. Please enter a positive integer.")
            return

        todo = self.repository.get_by_id(task_id)
        if todo is None:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Current task: {todo.title}")
        new_title = input(f"Enter new title (or press Enter to keep '{todo.title}'): ").strip()
        if not new_title:
            new_title = todo.title
        elif not validate_title(new_title):
            print("Error: Title cannot be empty.")
            return

        new_description = input(f"Enter new description (or press Enter to keep current): ").strip()
        if not new_description:
            new_description = todo.description

        try:
            updated_todo = self.repository.update(task_id, new_title, new_description)
            print(f"Task {task_id} updated successfully.")
        except Exception as e:
            print(f"Error updating task: {e}")

    def delete_task(self):
        """Delete a task."""
        print("\n--- Delete Task ---")
        task_id_str = input("Enter task ID to delete: ").strip()
        task_id = validate_task_id(task_id_str)

        if task_id is None:
            print("Error: Invalid task ID. Please enter a positive integer.")
            return

        todo = self.repository.get_by_id(task_id)
        if todo is None:
            print(f"Error: Task with ID {task_id} not found.")
            return

        confirm = input(f"Are you sure you want to delete task '{todo.title}'? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            success = self.repository.delete(task_id)
            if success:
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Error deleting task {task_id}.")
        else:
            print("Deletion cancelled.")

    def mark_complete(self):
        """Mark a task as complete."""
        print("\n--- Mark Task Complete ---")
        task_id_str = input("Enter task ID to mark complete: ").strip()
        task_id = validate_task_id(task_id_str)

        if task_id is None:
            print("Error: Invalid task ID. Please enter a positive integer.")
            return

        todo = self.repository.get_by_id(task_id)
        if todo is None:
            print(f"Error: Task with ID {task_id} not found.")
            return

        updated_todo = self.repository.mark_complete(task_id)
        if updated_todo:
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"Error marking task {task_id} as complete.")

    def mark_incomplete(self):
        """Mark a task as incomplete."""
        print("\n--- Mark Task Incomplete ---")
        task_id_str = input("Enter task ID to mark incomplete: ").strip()
        task_id = validate_task_id(task_id_str)

        if task_id is None:
            print("Error: Invalid task ID. Please enter a positive integer.")
            return

        todo = self.repository.get_by_id(task_id)
        if todo is None:
            print(f"Error: Task with ID {task_id} not found.")
            return

        updated_todo = self.repository.mark_incomplete(task_id)
        if updated_todo:
            print(f"Task {task_id} marked as incomplete.")
        else:
            print(f"Error marking task {task_id} as incomplete.")

    def exit_app(self):
        """Exit the application."""
        print("Thank you for using the Todo application!")
        self.running = False

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Application!")
        while self.running:
            self.display_menu()
            choice = self.get_user_choice()
            self.handle_choice(choice)


def main():
    """Main entry point."""
    try:
        app = TodoCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try again or contact support if the problem persists.")
        sys.exit(1)


if __name__ == "__main__":
    main()