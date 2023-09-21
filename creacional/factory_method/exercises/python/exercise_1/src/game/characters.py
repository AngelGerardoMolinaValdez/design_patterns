from game.base.character import Character

# concrete products
class Magician(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def special_attack(self, character: Character):
        print("{:*^30}".format("ATAQUE ESPECIAL"))
        self.attack(character, "Hechizo mortal", 50)


class Warrior(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def special_attack(self, character: Character):
        print("{:*^30}".format("ATAQUE ESPECIAL"))
        self.attack(character, "Espada maldecida", 50)
