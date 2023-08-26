from typing import Self

class OriginalDog:
    # instancia privada y estatica
    _instance = None
    name = str

    def __new__(cls, name) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.name = name
        return cls._instance

    def get_name(self):
        return self.name

dog = OriginalDog("Taz")
another_dog = OriginalDog("Oddie")
another_more_dog = OriginalDog("Max")

print(dog == another_dog == another_more_dog, end='\n'*2)

print(f"el nombre del primer perrito: {dog.get_name()}")
print(f"el nombre del segundo perrito: {another_dog.get_name()}")
print(f"el nombre del tercer perrito: {another_more_dog.get_name()}")
