from abc import ABC, abstractmethod

# colleagues
class Email(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

    @abstractmethod
    def receive(self, message: str) -> None:
        pass

# mediator
class Mediator(ABC):
    @abstractmethod
    def send_email(self, email: Email, message: str) -> None:
        pass

# concrete colleague
class FooBarStarUpEmail(Email):
    _name: str
    _mediator: Mediator
    def __init__(self, name: str, mediator: Mediator) -> None:
        self._name = name
        self._mediator = mediator
    
    def name_user(self) -> str:
        return self._name

    def send(self, message: str) -> None:
        print(f"{self._name} envia el siguiente correo: {message}")
        self._mediator.send_email(self, message)
    
    def receive(self, message: str) -> None:
        print(f"{self._name} recibe el siguiente correo: {message}")

# concrete mediator
class FooBarStarUpEmailBase(Mediator):
    _emails: list[Email] = []

    def add_email(self, email: Email) -> None:
        self._emails.append(email)

    def send_email(self, email_sender: Email, message: str) -> None:
        for email in self._emails:
            if email != email_sender:
                email.receive(message)

def main():
    base = FooBarStarUpEmailBase()
    angel = FooBarStarUpEmail("Angel M", base)
    regina = FooBarStarUpEmail("Regina B", base)
    javier = FooBarStarUpEmail("Javier A", base)

    base.add_email(angel)
    base.add_email(regina)
    base.add_email(javier)

    angel.send(
        "Hola, mi nombre es " + angel.name_user() + " soy nuevo por aqui.")
    regina.send(
        "Hola, mi nombre es " + regina.name_user() + " soy nuevo por aqui.")
    javier.send(
        "Hola, mi nombre es " + javier.name_user() + " soy nuevo por aqui.")

main()
