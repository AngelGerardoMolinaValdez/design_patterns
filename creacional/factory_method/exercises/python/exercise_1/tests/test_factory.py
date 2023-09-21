import os
import sys

path = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.insert(0, os.path.abspath(path))

from unittest import TestCase
from assertpy import assert_that
from game.factory import MagicianFactory, WarriorFactory
from game.characters import Magician, Warrior

class CharacterFactory(TestCase):
    def test_validate_character_magician_creator(self):
        magician = MagicianFactory().create("FooBar")
        assert_that(magician).is_instance_of(Magician)

    def test_validate_character_warrior_creator(self):
        warrior = WarriorFactory().create("FooBar")
        assert_that(warrior).is_instance_of(Warrior)
