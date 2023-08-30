from abc import ABC, abstractmethod

class TechGagdet(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class LedStrip(TechGagdet):
    def turn_on(self):
        print("Tira led encendida")

    def turn_off(self):
        print("tira led apagada")

class SecurityCamera(TechGagdet):
    def turn_on(self):
        print("Camara de seguridad encendida")

    def turn_off(self):
        print("Camara de seguridad apagada")

class PcGamer(TechGagdet):
    def turn_on(self):
        print("Computadora encendida")

    def turn_off(self):
        print("Computadora apagada")

class Setup:
    def __init__(self) -> None:
        self.led_strip = LedStrip()
        self.security_camera = SecurityCamera()
        self.pc = PcGamer()

    def start_routine_gamer(self):
        self.led_strip.turn_on()
        self.security_camera.turn_on()
        self.pc.turn_on()

    def end_routine_gamer(self):
        self.led_strip.turn_off()
        self.security_camera.turn_off()
        self.pc.turn_off()

def main() -> None:
    my_setup = Setup()
    my_setup.start_routine_gamer()
    my_setup.end_routine_gamer()

main()
