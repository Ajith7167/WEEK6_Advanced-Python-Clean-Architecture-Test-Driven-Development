import json
from pathlib import Path

from employee import Employee


class EmployeeRepository:
    def __init__(self, file_path: str = "employees.json") -> None:
        self.file_path = Path(file_path)

    def load_all(self) -> list[Employee]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Employee(**item) for item in data]

    def save_all(self, employees: list[Employee]) -> None:
        data = [
            {
                "employee_id": employee.employee_id,
                "name": employee.name,
                "department": employee.department,
                "salary": employee.salary,
            }
            for employee in employees
        ]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)