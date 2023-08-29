from abc import ABC, abstractmethod

class CellPhone(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class XiaomiCellPhone(CellPhone):
    def __init__(self, model) -> None:
        self.model = model

    def turn_on(self):
        return "Xiaomi" + self.model


class CellPhoneCase(ABC):
    @abstractmethod
    def protect_cellphone(self):
        pass

class XiaomiCase(CellPhoneCase):
    def __init__(self, cellphone: CellPhone) -> None:
        self.cellphone = cellphone

    def protect_cellphone(self):
        return self.cellphone.turn_on() + " protected with Xiaomi Case"

def main():
    xiaomi_redmi_note_10 = XiaomiCellPhone("Redmi Note 10")
    xiaomi_case_redmi_note_10 = XiaomiCase(xiaomi_redmi_note_10)
    print(xiaomi_case_redmi_note_10.protect_cellphone())

main()
