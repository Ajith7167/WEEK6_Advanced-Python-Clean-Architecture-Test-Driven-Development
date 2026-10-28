class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        """Return the employee's salary."""
        return self.__salary

    def set_salary(self, salary):
        """Update salary only if it is valid."""
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

    def display_details(self):
        print(
            f"ID: {self.employee_id}, "
            f"Name: {self.name}, "
            f"Salary: {self.__salary}"
        )


print("\n========== 1. ENCAPSULATION ==========")

employee = Employee(101, "Ajith", 30000)
employee.display_details()

employee.set_salary(35000)
print("Updated Salary:", employee.get_salary())

employee.set_salary(-5000)  # Invalid salary


class Developer(Employee):
    def __init__(self, employee_id, name, salary, programming_language):
        super().__init__(employee_id, name, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(
            f"{self.name} develops applications using "
            f"{self.programming_language}."
        )


print("\n========== 2. INHERITANCE ==========")

developer = Developer(102, "Rahul", 45000, "Python")
developer.display_details()
developer.write_code()



class Trainer:
    def conduct_training(self):
        print("Conducting technical training.")


class TechnicalManager(Trainer, Developer):
    def manage_team(self):
        print(f"{self.name} manages the development team.")


print("\n========== 3. MULTIPLE INHERITANCE ==========")

technical_manager = TechnicalManager(
    103, "Kiran", 70000, "Python"
)

technical_manager.display_details()
technical_manager.write_code()       # Inherited from Developer
technical_manager.conduct_training()  # Inherited from Trainer
technical_manager.manage_team()



class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} manages a team.")


class SeniorManager(Manager):
    def conduct_review(self):
        print(f"{self.name} reviews team performance.")


print("\n========== 4. MULTILEVEL INHERITANCE ==========")

senior_manager = SeniorManager(104, "Priya", 90000)
senior_manager.display_details()  # From Employee
senior_manager.manage_team()      # From Manager
senior_manager.conduct_review()   # From SeniorManager




class HR(Employee):
    def recruit_employee(self):
        print(f"{self.name} recruits new employees.")


print("\n========== 5. HIERARCHICAL INHERITANCE ==========")

developer2 = Developer(105, "Arun", 40000, "Java")
hr_employee = HR(106, "Sneha", 42000)

developer2.display_details()
developer2.write_code()

hr_employee.display_details()
hr_employee.recruit_employee()


class EmployeeRole:
    def work(self):
        print("Employee performs general work.")


class DeveloperRole(EmployeeRole):
    def work(self):
        print("Developer writes and tests code.")


class ManagerRole(EmployeeRole):
    def work(self):
        print("Manager plans and manages projects.")


print("\n========== 6. POLYMORPHISM ==========")

employees = [
    EmployeeRole(),
    DeveloperRole(),
    ManagerRole()
]

for person in employees:
    person.work()




def calculate_salary(basic_salary, bonus=0, allowance=0):
    """Calculate salary with optional bonus and allowance."""
    return basic_salary + bonus + allowance


print("\n========== 7. DEFAULT ARGUMENTS ==========")

print("Basic Salary:", calculate_salary(30000))
print("Salary with Bonus:", calculate_salary(30000, 5000))
print("Salary with Bonus and Allowance:",
      calculate_salary(30000, 5000, 2000))



class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()  # Created inside the Car

    def start_car(self):
        print(f"Starting {self.model}...")
        self.engine.start()


print("\n========== 8. COMPOSITION ==========")

car = Car("Toyota")
car.start_car()



class Department:
    def __init__(self, department_name, employees):
        self.department_name = department_name
        self.employees = employees  # Existing objects are provided

    def display_employees(self):
        print(f"Department: {self.department_name}")

        for employee in self.employees:
            print(
                f"Employee: {employee.name}, "
                f"Salary: {employee.get_salary()}"
            )


print("\n========== 9. AGGREGATION ==========")

employee1 = Employee(201, "Ravi", 35000)
employee2 = Employee(202, "Anita", 40000)

# These employee objects exist before the department is created.
it_department = Department(
    "IT",
    [employee1, employee2]
)

it_department.display_employees()



print("\n========== ALL OOP EXAMPLES COMPLETED ==========")
