from abc import ABC, abstractmethod

# state
class CellPhoneState(ABC):
    @abstractmethod
    def handle_state(self) -> str:
        pass

# concrete state
class CellPhoneOnState(CellPhoneState):
    def handle_state(self) -> str:
        return "Celular encendido..."

class CellPhoneOffState(CellPhoneState):
    def handle_state(self) -> str:
        return "Celular apagado..."

# context
class CellPhone:
    _state: CellPhoneState = None

    def __init__(self, model: str) -> None:
        print(f"Modelo {model} creado...")
        self._state = CellPhoneOffState()
    
    def define_state(self, state: CellPhoneState) -> None:
        self._state = state
    
    def state_value(self) -> str:
        return self._state.handle_state()

def main() -> None:
    galaxy_s8 = CellPhone("Galaxy S8")
    on_state = CellPhoneOnState()

    print(galaxy_s8.state_value())

    galaxy_s8.define_state(on_state)
    print(galaxy_s8.state_value())

main()
