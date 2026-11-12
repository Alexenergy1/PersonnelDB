
import psycopg
from datetime import date
from decimal import Decimal, InvalidOperation


from model import (
    get_all_records,
    add_department,
    add_employee,
    add_position,
    add_assignment,
    update_department,
    update_employee,
    update_position,
    update_assignment,
    delete_department,
    delete_employee,
    delete_position,
    delete_assignment,
        search_employees_by_salary,
    get_department_statistics,
    get_hiring_statistics,
    generate_test_data,
)


from view import (
    show_main_menu,
    show_table_menu,
    show_records,
    show_message,
    show_error
)


TABLE_OPTIONS = {
    "1": "department",
    "2": "employee",
    "3": "position",
    "4": "assignment"
}


def read_positive_id(prompt):
    value = int(input(prompt).strip())

    if value <= 0:
        raise ValueError("ID must be positive.")

    return value


def read_date(prompt):
    value = date.fromisoformat(input(prompt).strip())

    if value > date.today():
        raise ValueError("Future dates are not allowed.")

    return value


def read_decimal(prompt):
    value = Decimal(input(prompt).strip())

    if not value.is_finite():
        raise ValueError("Invalid number.")

    return value


def read_employee_data():
    full_name = input("Full name: ").strip()
    birth_date = read_date("Birth date (YYYY-MM-DD): ")
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    department_id = read_positive_id("Department ID: ")

    if not full_name or not phone or not email:
        raise ValueError("All fields are required.")

    return full_name, birth_date, phone, email, department_id


def read_position_data():
    name = input("Position name: ").strip()
    salary = read_decimal("Salary: ")

    if not name or salary <= 0:
        raise ValueError("Invalid position data.")

    return name, salary


def read_assignment_data():
    employee_id = read_positive_id("Employee ID: ")
    position_id = read_positive_id("Position ID: ")
    assignment_date = read_date("Assignment date (YYYY-MM-DD): ")
    rate = read_decimal("Rate (0-1): ")

    if rate <= 0 or rate > 1:
        raise ValueError("Rate must be between 0 and 1.")

    return employee_id, position_id, assignment_date, rate


def handle_database_error(error):
    if isinstance(error, psycopg.errors.UniqueViolation):
        show_error("A record with these values already exists.")

    elif isinstance(error, psycopg.errors.ForeignKeyViolation):
        show_error("Invalid reference or related records exist.")

    elif isinstance(error, psycopg.errors.CheckViolation):
        show_error("Data violates database constraints.")

    elif isinstance(error, psycopg.errors.NotNullViolation):
        show_error("A required field is missing.")

    else:
        show_error(f"Database error: {error}")


def view_records():
    while True:
        choice = show_table_menu()

        if choice == "0":
            return

        table_name = TABLE_OPTIONS.get(choice)

        if table_name is None:
            show_error("Invalid table selection.")
            continue

        try:
            columns, records = get_all_records(table_name)
            show_message(f"Table: {table_name}")
            show_records(columns, records)

        except psycopg.Error as error:
            handle_database_error(error)


def add_record():
    choice = show_table_menu()

    if choice == "0":
        return

    try:
        if choice == "1":
            name = input("Department name: ").strip()
            location = input("Location: ").strip()

            if not name or not location:
                raise ValueError("All fields are required.")

            record_id = add_department(name, location)

        elif choice == "2":
            record_id = add_employee(*read_employee_data())

        elif choice == "3":
            record_id = add_position(*read_position_data())

        elif choice == "4":
            record_id = add_assignment(*read_assignment_data())

        else:
            show_error("Invalid table selection.")
            return

        show_message(f"Record added successfully. ID: {record_id}")

    except (ValueError, InvalidOperation) as error:
        show_error(str(error))

    except psycopg.Error as error:
        handle_database_error(error)


def edit_record():
    choice = show_table_menu()

    if choice == "0":
        return

    try:
        if choice == "1":
            record_id = read_positive_id("Department ID: ")
            name = input("New department name: ").strip()
            location = input("New location: ").strip()

            if not name or not location:
                raise ValueError("All fields are required.")

            updated = update_department(record_id, name, location)

        elif choice == "2":
            record_id = read_positive_id("Employee ID: ")
            updated = update_employee(
                record_id, *read_employee_data()
            )

        elif choice == "3":
            record_id = read_positive_id("Position ID: ")
            updated = update_position(
                record_id, *read_position_data()
            )

        elif choice == "4":
            record_id = read_positive_id("Assignment ID: ")
            updated = update_assignment(
                record_id, *read_assignment_data()
            )

        else:
            show_error("Invalid table selection.")
            return

        if updated:
            show_message("Record updated successfully.")
        else:
            show_error("Record not found.")

    except (ValueError, InvalidOperation) as error:
        show_error(str(error))

    except psycopg.Error as error:
        handle_database_error(error)



def delete_record():
    choice = show_table_menu()

    if choice == "0":
        return

    if choice not in TABLE_OPTIONS:
        show_error("Invalid table selection.")
        return

    table_name = TABLE_OPTIONS[choice]

    try:
        record_id = read_positive_id(
            f"Enter {table_name} ID: "
        )

        confirmation = input(
            "Confirm deletion (yes/no): "
        ).strip().lower()

        if confirmation != "yes":
            show_message("Deletion cancelled.")
            return

        if choice == "1":
            deleted = delete_department(record_id)

        elif choice == "2":
            deleted = delete_employee(record_id)

        elif choice == "3":
            deleted = delete_position(record_id)

        elif choice == "4":
            deleted = delete_assignment(record_id)

        if deleted:
            show_message("Record deleted successfully.")
        else:
            show_error("Record not found.")

    except ValueError as error:
        show_error(str(error))

    except psycopg.errors.ForeignKeyViolation:
        show_error(
            "Cannot delete record. Related records exist."
        )

    except psycopg.Error as error:
        handle_database_error(error)


def search_and_analytics():
    while True:
        print("\n========== SEARCH AND ANALYTICS ==========")
        print("1. Search employees by salary")
        print("2. Department statistics")
        print("3. Hiring statistics")
        print("0. Back")
        print("==========================================")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            return

        try:
            if choice == "1":
                min_salary = read_decimal("Minimum salary: ")
                max_salary = read_decimal("Maximum salary: ")

                if min_salary < 0 or max_salary < min_salary:
                    raise ValueError("Invalid salary range.")

                columns, records = search_employees_by_salary(
                    min_salary, max_salary
                )

            elif choice == "2":
                columns, records = get_department_statistics()

            elif choice == "3":
                columns, records = get_hiring_statistics()

            else:
                show_error("Invalid menu option.")
                continue

            show_records(columns, records)

        except (ValueError, InvalidOperation) as error:
            show_error(str(error))

        except psycopg.Error as error:
            handle_database_error(error)

def generate_data():
    try:
        created, count = generate_test_data()

        if created:
            show_message(
                f"Test data generated successfully. Records: {count}"
            )
        else:
            show_message(
                f"Test data already exists. Records: {count}"
            )

    except psycopg.Error as error:
        handle_database_error(error)


def run_application():
    while True:
        choice = show_main_menu()

        if choice == "1":
            view_records()

        elif choice == "2":
            add_record()

        elif choice == "3":
            edit_record()

        elif choice == "4":
            delete_record()

        elif choice == "0":
            show_message("Application closed.")
            break



        elif choice == "5":
            generate_data()

        elif choice == "6":
            search_and_analytics()


        else:
            show_error("Invalid menu option.")
