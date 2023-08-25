from abc import ABC, abstractmethod

# Abstract Factory
class HeadPhonesFactory(ABC):
    """Interfaz para crear fabrica de audifonos

    Args:
        ABC (abstract class): clase abstracta que permite definir los
        metodos abstractos para su posterior implementacion en las
        clases hijas
    """
    @abstractmethod
    def create_wireless_headphones(self):
        pass
    
    @abstractmethod
    def create_wired_headphones(self):
        pass

# Concrete Factory
class NothingFactory(HeadPhonesFactory):
    def create_wired_headphones(self):
        return WiredHeadPhonesTransparent()
    
    def create_wireless_headphones(self):
        return WirelessHeadPhonesTransparent()


class HHOGeneFactory(HeadPhonesFactory):    
    def create_wired_headphones(self):
        return WiredHeadPhonesIluminated()

    def create_wireless_headphones(self):
        return WirelessHeadPhonesIluminated()

# Abstract Product
class HeadPhones(ABC):
    @abstractmethod
    def sound(self):
        pass

# Concret Product
class WirelessHeadPhonesTransparent(HeadPhones):
    def sound(self):
        return "Case y audifonos transparentes!!"

class WiredHeadPhonesTransparent(HeadPhones):
    def sound(self):
        return "cable normal, solo los audifonos son transparentes..."

class WirelessHeadPhonesIluminated(HeadPhones):
    def sound(self):
        return "Case color mate y audifonos iluminados!!"

class WiredHeadPhonesIluminated(HeadPhones):
    def sound(self):
        return "sin iluminacion!"

def tech_market(factories: list):
    for factory in factories:
        wireless_headphones = factory.create_wireless_headphones()
        wired_headphones = factory.create_wired_headphones()
        print(wireless_headphones.sound())
        print(wired_headphones.sound())
        print(end="\n\n")

tech_market([
    NothingFactory(), HHOGeneFactory()
])
