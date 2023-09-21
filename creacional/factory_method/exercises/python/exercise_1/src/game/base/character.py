from abc import ABC, abstractmethod
from typing import Self
from game.errors import GameOver

# product
class Character(ABC):
    _name: str
    _life: int = 100

    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def special_attack(self, character: Self):
        pass

    def attack(self, character: Self, name: str, damage: int):
        print(f"'{self._name}' ({self._life}) ^{name}:{damage}^ =>" + 
              f"' {character.name_character()}' ({character.life_level()})")
        character.damage(damage)

    def damage(self, damage: int):
        last_life = self._life
        self._decrease_health(damage)
        print(f"'{self._name}' ({last_life}) => ({self._life})")

    def increase_health(self, quantity: int):
        if (quantity + self._life) > 100:
            self._life = 100
        else:
            self._life += quantity

    def _decrease_health(self, quantity: int):
        if (self._life - quantity) <= 0:
            raise GameOver(f"{self._name} ha sido derrotado")
        self._life -= quantity

    def life_level(self):
        return self._life

    def name_character(self):
        return self._name
