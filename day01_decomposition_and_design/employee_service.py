from employee import Employee
from employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self, repository: EmployeeRepository) -> None:
        self.repository = repository

    def add_employee(self, employee: Employee) -> None:
        employees = self.repository.load_all()

        if any(
            existing.employee_id == employee.employee_id
            for existing in employees
        ):
            raise ValueError("Employee ID already exists")

        self._validate_employee(employee)
        self.repository.save_all(employees + [employee])

    def update_employee(self, employee: Employee) -> None:
        employees = self.repository.load_all()
        for index, existing in enumerate(employees):
            if existing.employee_id == employee.employee_id:
                self._validate_employee(employee)
                employees[index] = employee
                self.repository.save_all(employees)
                return

        raise ValueError("Employee not found")

    def _validate_employee(self, employee: Employee) -> None:
        if employee.employee_id <= 0:
            raise ValueError("Employee ID must be positive")

        if not employee.name.strip():
            raise ValueError("Employee name cannot be empty")

        if employee.salary < 0:
            raise ValueError("Salary cannot be negative")

    def get_employees(self) -> list[Employee]:
        return self.repository.load_all()