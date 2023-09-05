from abc import ABC, abstractmethod

# observer / suscriber
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# concrete observer / suscriber
class Familiar(Observer):
    _name: str = None
    _relationship: str = None

    def __init__(self, name: str, relationship: str) -> None:
        self._name = name
        self._relationship = relationship

    def update(self):
        print(f"Su {self._relationship.title()} {self._name.title()} ha visto!")

# subject / publisher
class Subject:
    _parents: list[Observer] = []

    def add(self, parent: Observer):
        self._parents.append(parent)

    def notify(self):
        for parent in self._parents:
            parent.update()

# concrete subject / publisher
class Child(Subject):
    _name: str = None

    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name
    
    def speak(self, words: str):
        print(f"Soy {self._name.title()}, he dicho: {words}")
        self.notify()

def main():
    madre = Familiar("Aranza", "Madre")
    padre = Familiar("raul", "padre")
    juan = Child("JUAN")

    juan.add(madre)
    juan.add(padre)

    juan.speak("Hola mundo!")

main()