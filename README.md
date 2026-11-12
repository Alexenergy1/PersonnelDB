
# PersonnelDB

## Project Description

PersonnelDB is a Python console application for managing personnel data using PostgreSQL.

The application follows the MVC architecture and uses parameterized SQL queries for secure database operations.

## Technologies

- Python 3
- PostgreSQL 18
- psycopg 3
- python-dotenv
- MVC architecture

## Database Structure

The database `personnel_db` contains four main tables:

- department
- employee
- position
- assignment

An additional table `employee_test` is used for performance testing.

## Features

1. View database records
2. Add new records
3. Edit existing records
4. Delete records
5. Generate test data
6. Search and analytics
7. Error handling and input validation

## Project Files

- main.py - Application entry point
- database.py - PostgreSQL connection
- model.py - Database queries
- view.py - User interface
- controller.py - Application logic
- .env - Local database configuration
- requirements.txt - Python dependencies

## Installation

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file with your PostgreSQL connection settings:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=personnel_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Create the database tables using the SQL schema.

## Running the Application

```bash
python main.py
```

## Performance Testing

The application supports generating 100000 test records.

SQL query performance was analyzed using EXPLAIN ANALYZE.

Measured execution times:

- Department statistics: 22.071 ms
- Salary search without index: 14.442 ms
- Salary search with index: 7.102 ms (average of three warm runs)
- Hiring statistics: 92.349 ms

The salary index improved execution time in the measured warm runs. Results may vary depending on caching and system load.

## Error Handling

The application handles:

- Invalid menu options
- Invalid salary ranges
- Foreign key violations
- Database operation errors
- Invalid user input
```
