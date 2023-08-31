from abc import ABC, abstractmethod

# flyweight
class UserStructure(ABC):
    @abstractmethod
    def information(self):
        pass

# concrete flyweight
class User(UserStructure):
    def __init__(self, id_: str, name: str) -> None:
        self.id = id_
        self.name = name

    def information(self):
        print(f"Usuario {self.name} con id: {self.id}")

# client
class UserCreator:
    _users: dict = {}

    @classmethod
    def create(cls, id_: str, name: str):
        if not (user := cls._users.get(id_)):
            user = User(id_, name)
            cls._users[id_] = user
        return user

def main():
    users_data = [
        ("Angel123", "Angel"),
        ("Eduardo123", "Eduardo"),
        ("Jose123", "Jose"),
        ("Angel123", "Daniel")
    ]
    for user_data in users_data:
        user: UserStructure = UserCreator.create(*user_data)
        user.information()

main()
