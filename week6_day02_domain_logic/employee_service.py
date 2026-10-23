from employee import Employee
from protocols import EmployeeRepositoryProtocol


class EmployeeService:
    def __init__(self,repository: EmployeeRepositoryProtocol
) -> None:
        self.repository = repository

    def add_employee(self, employee: Employee) -> None:
        # Validate employee ID
        if employee.employee_id <= 0:
            raise ValueError("Employee ID must be positive")

        # Validate employee name
        if not employee.name.strip():
            raise ValueError("Employee name cannot be empty")

        # Validate salary
        if employee.salary < 0:
            raise ValueError("Salary cannot be negative")

        # Check duplicate employee ID
        employees = self.repository.get_all()

        if any(
            existing.employee_id == employee.employee_id
            for existing in employees
        ):
            raise ValueError("Employee ID already exists")

        # Save through the injected repository
        self.repository.save_all(employees + [employee])

    def get_employees(self) -> list[Employee]:
        return self.repository.get_all()