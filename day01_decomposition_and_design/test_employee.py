import pytest

from employee import Employee
from employee_repository import EmployeeRepository
from employee_service import EmployeeService


def test_add_employee(tmp_path):
    repository = EmployeeRepository(str(tmp_path / "employees.json"))
    service = EmployeeService(repository)

    employee = Employee(101, "Ajith", "IT", 30000.0)
    service.add_employee(employee)

    assert service.get_employees() == [employee]


def test_duplicate_employee_id(tmp_path):
    repository = EmployeeRepository(str(tmp_path / "employees.json"))
    service = EmployeeService(repository)

    employee = Employee(101, "Ajith", "IT", 30000.0)
    service.add_employee(employee)

    with pytest.raises(ValueError, match="already exists"):
        service.add_employee(employee)


def test_negative_salary(tmp_path):
    repository = EmployeeRepository(str(tmp_path / "employees.json"))
    service = EmployeeService(repository)

    employee = Employee(102, "Ravi", "IT", -1000.0)

    with pytest.raises(ValueError, match="Salary cannot be negative"):
        service.add_employee(employee)


def test_update_employee(tmp_path):
    repository = EmployeeRepository(str(tmp_path / "employees.json"))
    service = EmployeeService(repository)
    service.add_employee(Employee(101, "Ajith", "IT", 30000.0))

    updated_employee = Employee(101, "Ajith Kumar", "Engineering", 35000.0)
    service.update_employee(updated_employee)

    assert service.get_employees() == [updated_employee]


def test_update_missing_employee(tmp_path):
    repository = EmployeeRepository(str(tmp_path / "employees.json"))
    service = EmployeeService(repository)

    with pytest.raises(ValueError, match="Employee not found"):
        service.update_employee(Employee(101, "Ajith", "IT", 30000.0))