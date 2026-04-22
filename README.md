# MoviFisio

MoviFisio is a modern backend system designed for physiotherapy clinics. It provides a robust API for managing patients, therapists, appointments, and medical records.

## 🚀 Features

- **Authentication & Authorization**: Secure access using JWT (JSON Web Tokens).
- **User Management**: Support for patients and therapists with detailed profiles.
- **Appointment Scheduling**: Manage sessions, services, and pricing.
- **Medical Records**: Keep track of patient progress and attach relevant files.
- **Database Migrations**: Version-controlled database schema with Alembic.

## 🛠️ Technologies

- **[FastAPI](https://fastapi.tiangolo.com/)**: High-performance web framework for building APIs.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Powerful SQL Toolkit and Object-Relational Mapper.
- **[Alembic](https://alembic.sqlalchemy.org/)**: Lightweight database migration tool.
- **[Poetry](https://python-poetry.org/)**: Dependency management and packaging.
- **[SQLite](https://www.sqlite.org/)**: Self-contained, serverless SQL database engine.

## 📋 Prerequisites

- Python 3.13+
- Poetry

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JoaoPSchiavoni/Movi-Fisio
   cd MoviFisio
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Configure environment variables**:
   Create a `.env` file in the root directory (refer to `.env.example` if available).

## 🗄️ Database Migrations

Before running the application, apply the database migrations:

```bash
poetry run alembic upgrade head
```

To create a new migration after model changes:

```bash
poetry run alembic revision --autogenerate -m "Description of changes"
```

## 🏃 Running the Application

Start the development server:

```bash
poetry run uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
