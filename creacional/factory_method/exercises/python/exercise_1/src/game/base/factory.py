from abc import ABC, abstractmethod
from game.base.character import Character

# factory
class FactoryCreator(ABC):
    @abstractmethod
    def create(self, name: str) -> Character:
        pass
