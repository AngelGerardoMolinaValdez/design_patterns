import os
import sys

path = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.insert(0, os.path.abspath(path))

from unittest import TestCase, expectedFailure
from assertpy import assert_that
from game.characters import Magician, Warrior


class Character(TestCase):
    _magician: Magician
    _warrior: Warrior

    def setUp(self) -> None:
        self._magician = Magician("Foo")
        self._warrior = Warrior("Bar")

    def test_validate_character_name(self):
        assert_that(self._magician.name_character()).is_equal_to("Foo")
        assert_that(self._warrior.name_character()).is_equal_to("Bar")

    def test_validate_the_increase_in_health(self):
        self._magician.increase_health(100)
        self._warrior.increase_health(100)
        assert_that(self._magician.life_level()).is_equal_to(100)
        assert_that(self._warrior.life_level()).is_equal_to(100)

    def test_validate_the_character_attack(self):
        self._magician.attack(self._warrior, "maleficio", 30)
        self._warrior.attack(self._magician, "lanza de fuego", 40)
        assert_that(self._magician.life_level()).is_equal_to(60)
        assert_that(self._warrior.life_level()).is_equal_to(70)

    @expectedFailure
    def test_validate_end_of_game(self):
        self._magician.attack(self._warrior, "maleficio", 100)
        