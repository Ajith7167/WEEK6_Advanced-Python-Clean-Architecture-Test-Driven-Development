
from employee import Employee
from employee_repository import EmployeeRepository
from employee_service import EmployeeService


def main() -> None:
    repository = EmployeeRepository()
    service = EmployeeService(repository)

    while True:
        print("\nEmployee Management")
        print("1. Add employee")
        print("2. Update employee")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "3":
            break

        if choice not in {"1", "2"}:
            print("Invalid option. Please choose 1, 2, or 3.")
            continue

        try:
            employee_id = int(input("Employee ID: "))
            name = input("Name: ")
            department = input("Department: ")
            salary = float(input("Salary: "))
            employee = Employee(employee_id, name, department, salary)

            if choice == "1":
                service.add_employee(employee)
                print("Employee added successfully")
            else:
                service.update_employee(employee)
                print("Employee updated successfully")
        except ValueError as error:
            print(f"Error: {error}")

    print("\nEmployee Records:")
    for record in service.get_employees():
        print(record)


if __name__ == "__main__":
    main()
