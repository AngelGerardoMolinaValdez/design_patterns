# ***Definicion***
El patrón de diseño "Facade" es un patrón estructural que proporciona una interfaz simplificada y unificada para interactuar con un sistema más complejo. Actúa como una "fachada" que oculta la complejidad interna de los subsistemas y presenta una interfaz más fácil de usar para los clientes. El objetivo principal es simplificar la interacción con sistemas complejos al reducir la exposición a su funcionamiento interno.

Elementos clave del patrón Facade:

1. **Fachada:** Es una clase que proporciona una interfaz simple y coherente para interactuar con uno o varios subsistemas complejos. Los clientes se comunican con la fachada en lugar de interactuar directamente con los subsistemas.

2. **Subsistema:** Consiste en un conjunto de clases y componentes relacionados que realizan tareas específicas. La fachada encapsula la interacción con estos subsistemas y presenta una interfaz más simple.

El patrón Facade es útil cuando tienes un sistema complejo con muchos componentes y deseas proporcionar una manera más fácil y unificada de utilizarlo. Esto ayuda a reducir la complejidad y el acoplamiento en tu código, al tiempo que mejora la modularidad y la mantenibilidad.

Un ejemplo cotidiano es el uso de la interfaz gráfica de usuario (GUI) en aplicaciones. En lugar de tratar con múltiples componentes y eventos de GUI directamente, puedes utilizar una fachada que maneje la interacción con la GUI, ocultando detalles de implementación y haciéndolo más fácil de usar.

En resumen, el patrón Facade se utiliza para simplificar la interacción con sistemas complejos al proporcionar una interfaz unificada y fácil de usar. Ayuda a ocultar la complejidad interna y mejora la modularidad y la mantenibilidad de tu código.

# ***Ejemplos***

Ejemplo con Python:

```python
class Amplifier:
    def on(self):
        print("Amplifier is ON")

    def off(self):
        print("Amplifier is OFF")

class Player:
    def play(self):
        print("Player is playing")

    def stop(self):
        print("Player stopped")

class Speaker:
    def loud(self):
        print("Speaker volume set to loud")

class HomeTheaterFacade:
    def __init__(self):
        self.amplifier = Amplifier()
        self.player = Player()
        self.speaker = Speaker()

    def watch_movie(self):
        self.amplifier.on()
        self.player.play()
        self.speaker.loud()

    def end_movie(self):
        self.player.stop()
        self.amplifier.off()

theater = HomeTheaterFacade()
theater.watch_movie()  # Encender amplificador, reproducir y ajustar altavoz
theater.end_movie()    # Detener reproducción y apagar amplificador
```

Ejemplo con Java:

```java
class LightSystem {
    void turnOn() {
        System.out.println("Lights turned on");
    }

    void turnOff() {
        System.out.println("Lights turned off");
    }
}

class LightControlFacade {
    private LightSystem lights;

    LightControlFacade() {
        lights = new LightSystem();
    }

    void turnOnLights() {
        lights.turnOn();
    }

    void turnOffLights() {
        lights.turnOff();
    }
}

public class Main {
    public static void main(String[] args) {
        LightControlFacade lightControl = new LightControlFacade();
        lightControl.turnOnLights();  // Enciende las luces
        lightControl.turnOffLights(); // Apaga las luces
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno Facade se refiere a dos componentes, en
este contexto a una clase principal que se le conoce como punto clave
`Fachada` la cual entre sus metodos tendra la interaccion de una o mas clases
instanciadas para reducir la complejidad de los mismo, dichas clases se les
conoce como `Subsistemas`.

En los ejemplos realizados las clases `LedStript`, `SecurityCamera` y `PcGamer` son los subsistemas con los que se interactuaran dentro la fachada
`Setup`. En el segundo ejemplo las clases `Process`, `Logger` y `Report` son
los subsistemas de la fachada `SystemFoo`.

Los elementos claves son con su definicion en los ejemplos seria:

1. **Fachada:** Se refiere a la clase que manipulara todas las clases
dentro de un proceso para reducir la complejidad. En este ejemplo son las
clases `Setup` y `SystemFoo`.

2. **Subsistema:** Son las clases que seran manipuladas dentro de la fachada
en este ejemplo son: `LedStript`, `SecurityCamera` y `PcGamer`, por otra 
parte estan: `Process`, `Logger` y `Report`.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/facade)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/facade/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/facade)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/facade/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/facade-pattern/)