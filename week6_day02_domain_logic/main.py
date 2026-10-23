from employee import Employee
from employee_repository import JsonEmployeeRepository
from employee_service import EmployeeService


def main() -> None:
    repository = JsonEmployeeRepository("employees.json")
    service = EmployeeService(repository)

    employee = Employee(
        employee_id=105,
        name="qw",
        department="CSE",
        salary=-23000.0,
    )

    try:
        service.add_employee(employee)
        print("Employee added successfully")

    except ValueError as error:
        print(f"Validation error: {error}")

    print("\nEmployee records:")

    for record in service.get_employees():
        print(record)


if __name__ == "__main__":
    main()