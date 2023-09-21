import sys
import os
# Agregar el directorio raíz del proyecto a sys.path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

import random
from game.factory import MagicianFactory, WarriorFactory
from game.characters import Magician, Warrior

def play_move() -> tuple:
    magician_move: list[tuple[str, int]] = [
        ("hechizo mortal", 10),
        ("maldición", 20),
        ("rayo infernal", 15)]
    warrior_move: list[tuple[str, int]] = [
        ("hachazo de fuego", 10),
        ("espada de la muerte", 20),
        ("embestida", 15)]
    return magician_move, warrior_move

def game(round_):
    magician_move, warrior_move = play_move()

    magician: Magician = MagicianFactory().create("Mago " + str(round_))
    warrior: Warrior = WarriorFactory().create("Guerrero " + str(round_))

    while magician.life_level() >= 0 and warrior.life_level() >= 0:
        random_number: int = random.randint(1, 6)
        random_health_level: int = random.randint(1, 100)

        match random_number:
            case 0:
                magician_movement: tuple = random.choice(magician_move)
                magician.attack(warrior, *magician_movement)

            case 1:
                warrior_movement: tuple = random.choice(warrior_move)
                warrior.attack(magician, *warrior_movement)

            case 2:
                warrior.special_attack(magician)

            case 3:
                magician.special_attack(warrior)

            case 4:
                warrior.increase_health(random_health_level)

            case 5:
                magician.increase_health(random_health_level)

def main() -> None:
    rounds: int = 3
    for round_ in range(rounds):
        print("{:=^50}".format(f"INICIO BATALLA {round_}"))
        try:
            game(round_)
        except Exception as e:
            print(e)
        finally:
            print("{:=^50}".format(f"FIN BATALLA {round_}"), end='\n' * 3)

main()
