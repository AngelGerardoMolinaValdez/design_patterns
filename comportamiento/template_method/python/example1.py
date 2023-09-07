from abc import ABC, abstractmethod

# base
class Coffee:
    def prepare(self) -> None:
        self._add_water()
        self._boil_water()
        self._choose_flavor()

    def _add_water(self) -> None:
        print("Se agrega agua")

    def _boil_water(self) -> None:
        print("Se hierve el agua")

    @abstractmethod
    def _choose_flavor(self) -> None:
        pass

class CappuccinoCoffee(Coffee):
    def _choose_flavor(self) -> None:
        print("Se agrega el sabor cafe capuchino al agua hirviendo")

class MochaCoffee(Coffee):
    def _choose_flavor(self) -> None:
        print("Se agrega el sabor cafe moka al agua hirviendo")


def main() -> None:
    CappuccinoCoffee().prepare()
    MochaCoffee().prepare()

main()
