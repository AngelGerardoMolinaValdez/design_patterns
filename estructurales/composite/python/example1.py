from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def greetings(self):
        pass

class AmazonEmployee(Employee):
    def __init__(self, name: str) -> None:
        self.name = name
    
    def greetings(self):
        return f"Hi, Im {self.name}"

class AmazonEmployees(Employee):
    def __init__(self) -> None:
        self.employees: list = []

    def add(self, employee: Employee):
        self.employees.append(employee)

    def greetings(self):
        employees_greetings: list = list(map(
            lambda employee: employee.greetings(),
            self.employees
        ))
        return f"""All greetings: {"| ".join(employees_greetings)}"""

def main():
    angel = AmazonEmployee("Angel Molina")
    foobar = AmazonEmployee("Foo Bar")
    
    group = AmazonEmployees()
    group.add(angel)
    group.add(foobar)

    print(angel.greetings())
    print(foobar.greetings())
    print(group.greetings())

main()
