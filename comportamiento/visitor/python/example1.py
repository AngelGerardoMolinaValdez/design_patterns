from abc import abstractmethod, ABC

# visitor
class CarConsultant:
    def visit_car(self, car) -> None:
        pass

    def visit_motorcycle(self, motorcycle) -> None:
        pass

# element
class Transport(ABC):
    @abstractmethod
    def accept(self, visitor: CarConsultant) -> None:
        pass

# concrete element
class YahamaR6Raze(Transport):
    _color: str
    _owner: str

    def __init__(self, color: str, owner: str) -> None:
        self._color = color
        self._owner = owner

    def owner(self) -> str:
        return self._owner

    def color(self) -> str:
        return self._color

    def accept(self, visitor: CarConsultant) -> None:
        visitor.visit_car(self)

class NissanVersa(Transport):
    _color: str
    _owner: str
    _number_doors: int

    def __init__(self, color: str, owner: str, number_doors: int) -> None:
        self._color = color
        self._owner = owner
        self._number_doors = number_doors

    def owner(self) -> str:
        return self._owner

    def color(self) -> str:
        return self._color

    def number_doors(self) -> str:
        return self._number_doors

    def accept(self, visitor: CarConsultant) -> None:
        visitor.visit_car(self)

# concrete visitor
class SupervisorTranportDealerShip(CarConsultant):
    def visit_car(self, car: NissanVersa) -> None:
        print(
            f"{car.owner().title()} ha comprado un" +
            f" versa color {car.color()}"
        )

    def visit_motorcycle(self, motorcycle: YahamaR6Raze) -> None:
        print(
            f"{motorcycle.owner().title()} ha comprado una" +
            f" yamaha color {motorcycle.color()}"
        )

# object structure
class TransportDealerShip:
    _transports: list = None

    def __init__(self) -> None:
        self._transports = []

    def add(self, transport: Transport):
        self._transports.append(transport)

    def accept(self, visitor: CarConsultant):
        for transport in self._transports:
            transport.accept(visitor)


def main() -> None:
    my_yahama = YahamaR6Raze("azul", "Angel Molina")
    another_yamaha = YahamaR6Raze("azul", "Raul Perez")
    my_nissan = NissanVersa("naranja", "Angel Molina", 4)
    another_nissan = NissanVersa("naranja", "Ingrid Juarez", 4)

    dealer_ship = TransportDealerShip()

    dealer_ship.add(my_yahama)
    dealer_ship.add(another_yamaha)
    dealer_ship.add(my_nissan)
    dealer_ship.add(another_nissan)

    dealer_ship.accept(SupervisorTranportDealerShip())

main()
