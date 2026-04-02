# Task Management System

A RESTful Task Management API with a CLI interface built with Python (FastAPI and Typer).

## Features

- **Back-end API**: Built with FastAPI, SQLite, and SQLAlchemy.
- **RESTful Endpoints**: Perform CRUD operations on tasks.
- **Data Persistence**: Uses SQLite database.
- **CLI Interface**: Command-line tool to interact with the API using Typer and Requests.
- **Rich Output**: Pretty tables and status messages in the terminal.

## Project Structure

- `app/`: Contains the FastAPI application.
  - `main.py`: Entry point and API endpoints.
  - `models.py`: SQLAlchemy database models.
  - `schemas.py`: Pydantic data validation schemas.
  - `database.py`: Database configuration.
- `cli/`: Contains the command-line interface.
  - `main.py`: Typer CLI implementation.
- `requirements.txt`: Python dependencies.

## Installation & Setup

1. **Clone the project**:
   ```bash
   git clone https://github.com/lakumbhavdip/task-manager-api-cli.git
   cd task-manager-api-cli
   ```

2. **Setup Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the API server**:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`. You can also access the interactive documentation at `http://127.0.0.1:8000/docs`.

## API Documentation

- `GET /tasks`: List all tasks with optional status and priority filtering.
- `POST /tasks`: Create a new task.
- `GET /tasks/{task_id}`: Retrieve a specific task by ID.
- `PATCH /tasks/{task_id}`: Update specific fields of a task.
- `DELETE /tasks/{task_id}`: Delete a task.

## CLI Usage Examples

Make sure the API server is running in a separate terminal before using the CLI.

**Add a new task:**
```bash
python -m cli.main add "Finish Project" --description "Complete the assessment" --priority high --due-date 2026-05-10
```

**List all tasks (with filtering):**
```bash
python -m cli.main list
python -m cli.main list --status pending --priority high
```

**View task details (Read):**
```bash
python -m cli.main get 1
```

**Update a task or change status (Incomplete/Pending):**
```bash
python -m cli.main update 1 --title "New Title" --status pending
```

**Quickly complete a task:**
```bash
python -m cli.main complete 1
```

**Delete a task:**
```bash
python -m cli.main delete 1
```

## Assumptions & Design Choices

1. **Database**: SQLite was chosen for ease of setup and persistence within a single file (`tasks.db`).
2. **Frameworks**: FastAPI was used for its modern features, automatic documentation, and high performance. Typer was used for the CLI for its ease of development and beautiful terminal output.
3. **Data format**: Created/updated timestamps are handled automatically. For simplicity, dates are accepted in `YYYY-MM-DD` format via the CLI.
4. **Validation**: Pydantic ensures titles are required and restricted in length, while enums ensure valid statuses and priority levels.
