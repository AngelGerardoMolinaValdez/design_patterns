"""

"""
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def turnOn(self):
        pass

class AngelComputer(Computer):
    def turnOn(self):
        return "Busy..."

class Employee(ABC):
    def __init__(self, computer: Computer) -> None:
        self.computer = computer

    @abstractmethod
    def work(self):
        pass

class EmployeeAngel(Employee):
    def work(self):
        return self.computer.turnOn()

def main():
    angel = EmployeeAngel(AngelComputer())
    print(angel.work())

main()
