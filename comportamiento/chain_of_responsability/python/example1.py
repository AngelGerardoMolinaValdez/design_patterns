from typing import Self, Optional
from abc import ABC, abstractmethod

# abstract handler
class Developer(ABC):
    @abstractmethod
    def set_superior(self, developer: Self) -> None:
        pass

    @abstractmethod
    def develop(self, task: str, complexity: str) -> None:
        pass

# handlers
class JrDeveloper(Developer):
    _superior: Developer = None

    def set_superior(self, developer: Self) -> None:
        self._superior = developer
    
    def develop(self, task: str, complexity: str) -> None:
        if complexity.lower().strip() == "easy":
            print(f"Jr Dev desarrollando tarea {task}")
            return
        # chain
        self._superior.develop(task, complexity)

class SemiDeveloper(Developer):
    _superior: Developer = None

    def set_superior(self, developer: Self) -> None:
        self._superior = developer
    
    def develop(self, task: str, complexity: str) -> None:
        if complexity.lower().strip() == "medium":
            print(f"Semi Dev desarrollando tarea {task}")
            return
        # chain
        self._superior.develop(task, complexity)

class SrDeveloper(Developer):
    _superior: Developer = None

    def set_superior(self, developer: Self) -> None:
        self._superior = developer
    
    def develop(self, task: str, complexity: str) -> None:
        if complexity.lower().strip() == "hard":
            print(f"Sr Dev desarrollando tarea {task}")
            return
        if not self._superior:
            print("Se ha llegado al limite de la cadena!")
            return
        # chain
        self._superior.develop(task, complexity)

# client
def main():
    jr_dev = JrDeveloper()
    semi_dev = SemiDeveloper()
    sr_dev = SrDeveloper()

    jr_dev.set_superior(semi_dev)
    semi_dev.set_superior(sr_dev)

    jr_dev.develop(
        "realizar mantenimiento al codigo", "easy")
    jr_dev.develop(
        "construir crud", "medium")
    jr_dev.develop(
        "construir api", "hard")
    jr_dev.develop(
        "actualizar infraestructura", "impossible")

main()
