from game.base.factory import FactoryCreator
from game.characters import Magician, Warrior

class MagicianFactory(FactoryCreator):
    def create(self, name: str) -> Magician:
        return Magician(name)

class WarriorFactory(FactoryCreator):
    def create(self, name: str) -> Warrior:
        return Warrior(name)
