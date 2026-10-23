import json
from dataclasses import asdict
from pathlib import Path

from employee import Employee


class JsonEmployeeRepository:
    def __init__(self, file_path: str = "employees.json") -> None:
        self.file_path = Path(file_path)

    def get_all(self) -> list[Employee]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Employee(**item) for item in data]

    def save_all(self, employees: list[Employee]) -> None:
        data = [asdict(employee) for employee in employees]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)