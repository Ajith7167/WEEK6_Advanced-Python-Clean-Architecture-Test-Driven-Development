from typing import Protocol
from employee import Employee

class EmployeeRepositoryProtocol(Protocol):

    def get_all(self) -> list[Employee]:
        ...

    def save_all(self, employees: list[Employee]) -> None:
        ...