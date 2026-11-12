
from psycopg import sql
from database import get_connection


TABLES = {
    "department": "department_id",
    "employee": "employee_id",
    "position": "position_id",
    "assignment": "assignment_id"
}


def get_all_records(table_name):
    if table_name not in TABLES:
        raise ValueError("Nevidoma tablica")

    query = sql.SQL("SELECT * FROM {} ORDER BY {} LIMIT 100").format(
        sql.Identifier(table_name),
        sql.Identifier(TABLES[table_name])
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            columns = [column.name for column in cur.description]
            records = cur.fetchall()

    return columns, records


def add_department(name, location):
    query = """
        INSERT INTO department (name, location)
        VALUES (%s, %s)
        RETURNING department_id
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, location))
            department_id = cur.fetchone()[0]

    return department_id

def update_department(department_id, name, location):
    query = """
        UPDATE department
        SET name = %s, location = %s
        WHERE department_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, location, department_id))
            return cur.rowcount > 0

def delete_department(department_id):
    query = """
        DELETE FROM department
        WHERE department_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (department_id,))
            return cur.rowcount > 0

def add_employee(full_name, birth_date, phone, email, department_id):
    query = """
        INSERT INTO employee
        (full_name, birth_date, phone, email, department_id)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING employee_id
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                query,
                (full_name, birth_date, phone, email, department_id)
            )
            employee_id = cur.fetchone()[0]

    return employee_id


def add_position(name, salary):
    query = """
        INSERT INTO position (name, salary)
        VALUES (%s, %s)
        RETURNING position_id
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, salary))
            position_id = cur.fetchone()[0]

    return position_id


def add_assignment(employee_id, position_id, assignment_date, rate):
    query = """
        INSERT INTO assignment
        (employee_id, position_id, assignment_date, rate)
        VALUES (%s, %s, %s, %s)
        RETURNING assignment_id
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                query,
                (employee_id, position_id, assignment_date, rate)
            )
            assignment_id = cur.fetchone()[0]

    return assignment_id

def update_employee(employee_id, full_name, birth_date, phone, email, department_id):
    query = """
        UPDATE employee
        SET full_name = %s,
            birth_date = %s,
            phone = %s,
            email = %s,
            department_id = %s
        WHERE employee_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                query,
                (full_name, birth_date, phone, email, department_id, employee_id)
            )
            return cur.rowcount > 0


def update_position(position_id, name, salary):
    query = """
        UPDATE position
        SET name = %s, salary = %s
        WHERE position_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (name, salary, position_id))
            return cur.rowcount > 0


def update_assignment(assignment_id, employee_id, position_id, assignment_date, rate):
    query = """
        UPDATE assignment
        SET employee_id = %s,
            position_id = %s,
            assignment_date = %s,
            rate = %s
        WHERE assignment_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                query,
                (employee_id, position_id, assignment_date, rate, assignment_id)
            )
            return cur.rowcount > 0

def delete_employee(employee_id):
    query = """
        DELETE FROM employee
        WHERE employee_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (employee_id,))
            return cur.rowcount > 0


def delete_position(position_id):
    query = """
        DELETE FROM position
        WHERE position_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (position_id,))
            return cur.rowcount > 0


def delete_assignment(assignment_id):
    query = """
        DELETE FROM assignment
        WHERE assignment_id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (assignment_id,))
            return cur.rowcount > 0

def search_employees_by_salary(min_salary, max_salary):
    query = """
        SELECT test_id, full_name, salary
        FROM employee_test
        WHERE salary BETWEEN %s AND %s
        ORDER BY salary
        LIMIT 100
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (min_salary, max_salary))
            columns = [column.name for column in cur.description]
            records = cur.fetchall()

    return columns, records


def get_department_statistics():
    query = """
        SELECT
            department_id,
            COUNT(*) AS employee_count,
            ROUND(AVG(salary), 2) AS average_salary
        FROM employee_test
        GROUP BY department_id
        ORDER BY department_id
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            columns = [column.name for column in cur.description]
            records = cur.fetchall()

    return columns, records


def get_hiring_statistics():
    query = """
        SELECT
            EXTRACT(YEAR FROM hire_date) AS hire_year,
            COUNT(*) AS employee_count,
            ROUND(AVG(salary), 2) AS average_salary,
            MIN(salary) AS minimum_salary,
            MAX(salary) AS maximum_salary
        FROM employee_test
        GROUP BY EXTRACT(YEAR FROM hire_date)
        ORDER BY hire_year
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            columns = [column.name for column in cur.description]
            records = cur.fetchall()

    return columns, records

def generate_test_data():
    query = """
        INSERT INTO employee_test
            (full_name, department_id, salary, hire_date)
        SELECT
            'Employee ' || i,
            (i % 3) + 1,
            15000 + (i % 50000),
            DATE '2020-01-01' + (i % 2000)
        FROM generate_series(1, 100000) AS s(i)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("LOCK TABLE employee_test IN EXCLUSIVE MODE")
            cur.execute("SELECT COUNT(*) FROM employee_test")
            count = cur.fetchone()[0]

            if count > 0:
                return False, count

            cur.execute(query)
            return True, cur.rowcount


