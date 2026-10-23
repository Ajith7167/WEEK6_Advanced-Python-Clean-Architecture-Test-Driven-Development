import pytest

from employee import Employee
from employee_service import EmployeeService


class FakeEmployeeRepository:
    """Stores employee records in memory for testing."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def get_all(self) -> list[Employee]:
        return list(self.employees)

    def save_all(self, employees: list[Employee]) -> None:
        self.employees = list(employees)


def create_service() -> EmployeeService:
    repository = FakeEmployeeRepository()
    return EmployeeService(repository)


def test_add_employee():
    service = create_service()
    employee = Employee(101, "Ajith", "IT", 30000.0)

    service.add_employee(employee)

    assert service.get_employees() == [employee]


def test_duplicate_employee_id():
    service = create_service()
    employee = Employee(101, "Ajith", "IT", 30000.0)
    service.add_employee(employee)

    with pytest.raises(ValueError, match="Employee ID already exists"):
        service.add_employee(employee)


def test_invalid_employee_id():
    service = create_service()
    employee = Employee(0, "Ajith", "IT", 30000.0)

    with pytest.raises(ValueError, match="Employee ID must be positive"):
        service.add_employee(employee)


def test_negative_salary():
    service = create_service()
    employee = Employee(102, "Ravi", "IT", -1000.0)

    with pytest.raises(ValueError, match="Salary cannot be negative"):
        service.add_employee(employee)


def test_empty_employee_name():
    service = create_service()
    employee = Employee(103, "   ", "IT", 30000.0)

    with pytest.raises(ValueError, match="Employee name cannot be empty"):
        service.add_employee(employee)