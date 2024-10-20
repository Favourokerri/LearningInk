# LearningInk

## Table of Contents

1. [Project Structure](#1-project-structure)
2. [Setup and Installation](#2-setup-and-installation)
   - [Virtual Environment Setup](#virtual-environment-setup)
   - [Installing Dependencies](#installing-dependencies)
3. [Database Migrations](#3-database-migrations)
4. [Running the Application](#4-running-the-application)
5. [Accessing the API](#5-accessing-the-api)

---

## 1. Project Structure

```
src/
│
├── alembic/                # Directory for Alembic migrations
│   └── versions/           # Contains migration files
│   └── env.py              # Alembic configuration for migrations
│
├── core/                   # Core application functionality
│   ├── config.py           # Configuration settings (DB URL, etc.)
│   └── security.py         # Security-related utilities (authentication, etc.)
│
├── crud/                   # CRUD (Create, Read, Update, Delete) operations
│   └── <various files>     # Contains functions to interact with DB
│
├── db/                     # Database session and base setup
│   ├── base.py             # SQLAlchemy model base class
│   └── session.py          # Database session management
│
├── router/                 # API endpoints
│   └── <various files>     # Contains FastAPI route handlers
│
├── schema/                 # Pydantic models (schemas for request/response validation)
│   └── <various files>     # Contains Pydantic models
│
├── __pycache__/            # Python cache files
│
├── alembic.ini             # Alembic configuration file
├── mvp.db                  # SQLite database (or another DB file)
└── main.py                 # Main FastAPI application entry point
```

---

## 2. Setup and Installation

### Virtual Environment Setup

To ensure that all dependencies are contained within the project, it's recommended to create and use a virtual environment. Here’s how to do it:

#### On Windows:
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

#### On macOS/Linux:
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Installing Dependencies

Once the virtual environment is activated, install the required dependencies using the `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### creating environmental variables
create a file .env, its content should contain
```
SECRET_KEY = "09d25e094faa6hgstertwkam86647hdbdgsf6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

## 3. Database Migrations

Alembic is used for managing database migrations in this project. you can use the following commands:

1. **Create a new migration**:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

2. **Apply migrations to the database**:
   ```bash
   alembic upgrade head
   ```

This will ensure that your database schema is up to date with the latest models defined in the application.

---

## 4. Running the Application

Once the dependencies are installed and migrations are applied, you can start the FastAPI application using **Uvicorn**, which is the ASGI server used to serve FastAPI applications.

Run the application with:
first change directory to the src folder
```bash
cd src
uvicorn main:app --reload
```

- `main`: Refers to the `main.py` file in your project.
- `app`: Refers to the FastAPI instance in `main.py` (e.g., `app = FastAPI()`).
- `--reload`: Enables automatic reloading when code changes are detected, useful for development.

---

## 5. Accessing the API

Once the application is running, you can access the API at the following URL:

- **Base URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive API Documentation**: FastAPI provides interactive API documentation via Swagger UI, accessible at:
  - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  
This allows you to explore and test the API endpoints directly from the browser.
