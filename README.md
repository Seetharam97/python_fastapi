# python_fastapi

shortly
Sure, here’s a concise version of the README file:

FastAPI CRUD with PostgreSQL
A simple project demonstrating CRUD operations using Python, FastAPI, and PostgreSQL.

Prerequisites
Python 3.7+

PostgreSQL

pip

Installation
1. Clone the Repo & Setup

git clone https://github.com/Seetharam97/python_fastapi.git
cd fastapi-postgres-crud
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Configure PostgreSQL

CREATE DATABASE fastapi_db;
CREATE USER fastapi_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE fastapi_db TO fastapi_user;
Add .env file:

env
DATABASE_URL=postgresql://postgres:Admin123@127.0.0.1:5432/test_fast_api
Running the Application

3. Run command

uvicorn main:app --reload

4. API Documentation
Visit http://127.0.0.1:8000/docs for interactive API docs.