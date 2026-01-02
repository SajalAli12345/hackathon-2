# Data Model: In-Memory Python Console Todo Application

## Todo Entity

### Attributes
- **id**: `int` - Unique identifier for the task (auto-generated)
- **title**: `str` - Task title/description (required)
- **description**: `str` - Optional detailed description of the task
- **completed**: `bool` - Completion status (default: False)

### Relationships
- No relationships needed for this simple model

### Validation Rules
- `id` must be unique within the session
- `title` must be non-empty (1+ characters)
- `completed` must be boolean type
- `description` can be empty string

### State Transitions
- `completed = False` → `completed = True` (when marking as complete)
- `completed = True` → `completed = False` (when marking as incomplete)

## Todo Repository Interface

### Methods
- `add(todo: Todo) -> Todo` - Add a new todo to the repository
- `get_all() -> List[Todo]` - Retrieve all todos
- `get_by_id(id: int) -> Optional[Todo]` - Retrieve a specific todo by ID
- `update(id: int, title: str, description: str) -> Optional[Todo]` - Update todo details
- `delete(id: int) -> bool` - Delete a todo by ID
- `mark_complete(id: int) -> Optional[Todo]` - Mark a todo as complete
- `mark_incomplete(id: int) -> Optional[Todo]` - Mark a todo as incomplete

### Constraints
- Repository maintains in-memory storage using Python list/dict
- IDs are auto-incremented starting from 1
- Operations must be thread-safe (not required for single-user console app)