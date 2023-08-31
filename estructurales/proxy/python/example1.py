from abc import ABC, abstractmethod

# subject
class Food(ABC):
    def status(self) -> dict:
        pass

# concrete subject
class AnyFood(Food):
    def status(self) -> dict:
        return {
            "status": "ok"
        }

class RottenFood(Food):
    def status(self) -> dict:
        return {
            "status": "rotten"
        }

# proxy
class ProxyFood:
    def validate(self, food: Food, food_name: str):
        food_status = food.status()
        if food_status.get("status") == "ok":
            print(f"La comida {food_name} se puede comer")
            return
        print(f"La comida {food_name} no se puede comer")

def main():
    ok_food = AnyFood()
    rotten_food = RottenFood()
    proxy = ProxyFood()
    proxy.validate(ok_food, "spaguetti")
    proxy.validate(rotten_food, "rotten spaguetti")

main()
