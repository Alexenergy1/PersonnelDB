
def show_main_menu():
    print("\n========== PERSONNEL MANAGEMENT ==========")
    print("1. View records")
    print("2. Add record")
    print("3. Edit record")
    print("4. Delete record")
    print("5. Generate test data")
    print("6. Search and analytics")
    print("0. Exit")
    print("=" * 42)

    return input("Choose an option: ").strip()


def show_table_menu():
    print("\n========== SELECT TABLE ==========")
    print("1. Departments")
    print("2. Employees")
    print("3. Positions")
    print("4. Assignments")
    print("0. Back")

    return input("Choose a table: ").strip()


def show_records(columns, records):
    if not records:
        print("\nNo records found.")
        return

    print("\n" + " | ".join(columns))
    print("-" * 80)

    for record in records:
        print(" | ".join(str(value) for value in record))

    print(f"\nTotal records displayed: {len(records)}")


def show_message(message):
    print(f"\n{message}")


def show_error(message):
    print(f"\nError: {message}")

