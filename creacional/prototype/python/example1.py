from abc import ABC, abstractmethod
from copy import copy


# prototype
class CellPhonePrototype(ABC):
    """la base del protoype que se creara

    Args:
        ABC (absctract class): la base de una clase abstracta
    """
    @abstractmethod
    def clone(self) -> object:
        """genera la copia del objeto instanciado

        Returns:
            object: la copia del objeto
        """

# concrete prototype
class SamsumgCellPhone(CellPhonePrototype):
    """implementa los metodos de la interfaz

    Args:
        CellPhonePrototype (abstract class): la intefaz con los metodos
    """
    def __init__(self, model: str, color: str, androd_version: int) -> None:
        """inicializa los componentes necesarios para la clase

        Args:
            model (str): el modelo el telefono
            color (str): el color del telefono
            androd_version (int): la version de android
        """
        self.model = model
        self.color = color
        self.androd_version = androd_version

    def clone(self) -> object:
        return copy(self)

class AppleCellPhone(CellPhonePrototype):
    """implementa los metodos de la interfaz

    Args:
        CellPhonePrototype (abstract class): la intefaz con los metodos
    """
    def __init__(self, model: str, color: str, ios_version: int) -> None:
        """inicializa los componentes necesarios para la clase

        Args:
            model (str): el modelo el telefono
            color (str): el color del telefono
            android_version (int): la version de android
        """
        self.model = model
        self.color = color
        self.ios_version = ios_version

    def clone(self) -> object:
        return copy(self)

# client code
samsung_s8 = SamsumgCellPhone("Galaxy S8", "white", 14)
samsung_s22 = samsung_s8.clone()
samsung_s22.model = "Galaxy S22"
print(
    f"original: {samsung_s8.model}, clonado: {samsung_s22.model}",
    end="\n\n"
)

iphone_10 = AppleCellPhone("IPhone 10", "black", 10)
iphone_12 = iphone_10.clone()
iphone_12.model = "IPhone 12"
print(
    f"original: {iphone_10.model}, clonado: {iphone_12.model}",
    end="\n\n"
)
