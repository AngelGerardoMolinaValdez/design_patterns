# ***Definicion***

El patrón de diseño Mediator (Mediador) es un patrón de comportamiento que se utiliza en la programación orientada a objetos para facilitar la comunicación y la interacción entre múltiples objetos de manera organizada y desacoplada. El objetivo principal del patrón Mediator es reducir las dependencias directas entre objetos al proporcionar un punto centralizado de control y coordinación.

**Conceptos clave del patrón Mediator:**

1. **Mediador (Mediator):** Es una interfaz o una clase abstracta que actúa como un punto central de coordinación entre objetos. El mediador define métodos que permiten a los objetos comunicarse entre sí a través del mediador, en lugar de comunicarse directamente entre ellos.

2. **Colegas (Colleagues):** Son objetos que interactúan entre sí en el sistema, pero en lugar de comunicarse directamente, utilizan el mediador como intermediario. Los colegas pueden ser cualquier objeto que necesite comunicarse con otros objetos en el sistema.

**Ventajas del patrón Mediator:**

- **Reducción del acoplamiento:** El patrón Mediator ayuda a reducir las dependencias entre objetos, ya que los objetos no necesitan conocerse directamente. Esto hace que el sistema sea más flexible y fácil de mantener.

- **Centralización de la lógica de coordinación:** Toda la lógica de coordinación y comunicación se centraliza en el mediador, lo que facilita la comprensión y el mantenimiento del sistema.

- **Facilita la extensibilidad:** Agregar nuevos objetos o cambiar la forma en que se comunican los objetos existentes generalmente implica realizar modificaciones en el mediador, sin afectar a los objetos individuales.

En resumen, el patrón Mediator permite que varios objetos se comuniquen entre sí de manera indirecta a través de un mediador, lo que simplifica la gestión de las interacciones y promueve la reutilización y la mantenibilidad del código.

# ***Ejemplos***

Ejemplo con Python:

```python
from abc import ABC, abstractmethod

# Colega (Colleague)
class Colleague(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def book_flight(self, flight_name):
        pass

# Mediador (Mediator)
class Mediator(ABC):
    @abstractmethod
    def book_flight(self, colleague, flight_name):
        pass

# Implementación concreta del mediador (Concrete Mediator)
class FlightBookingSystem(Mediator):
    def __init__(self):
        self.flights = {}
        self.passengers = {}

    def add_flight(self, flight_name):
        self.flights[flight_name] = []

    def book_flight(self, colleague, flight_name):
        if flight_name in self.flights:
            self.flights[flight_name].append(colleague)
            self.passengers[colleague] = flight_name
            print(f"{colleague.__class__.__name__} ha reservado el vuelo {flight_name}")
        else:
            print(f"El vuelo {flight_name} no existe")

# Implementación concreta del colega (Concrete Colleague)
class Passenger(Colleague):
    def book_flight(self, flight_name):
        self.mediator.book_flight(self, flight_name)

class TravelAgency(Colleague):
    def book_flight(self, flight_name):
        self.mediator.book_flight(self, flight_name)

def main():
    booking_system = FlightBookingSystem()

    booking_system.add_flight("Vuelo 101")
    booking_system.add_flight("Vuelo 202")

    passenger1 = Passenger(booking_system)
    passenger2 = Passenger(booking_system)
    travel_agency = TravelAgency(booking_system)

    passenger1.book_flight("Vuelo 101")
    passenger2.book_flight("Vuelo 202")
    travel_agency.book_flight("Vuelo 303")

if __name__ == "__main__":
    main()
```

Ejemplo con Java:

```java
import java.util.ArrayList;
import java.util.List;

interface Mediator {
    void send_message(String message, Colleague colleague);
}

class Colleague {
    private Mediator mediator;
    private String name;

    public Colleague(String name, Mediator mediator) {
        this.name = name;
        this.mediator = mediator;
    }

    public void send(String message) {
        System.out.println(name + " envía: " + message);
        mediator.send_message(message, this);
    }

    public void receive(String message) {
        System.out.println(name + " recibe: " + message);
    }
}

class FlightControlMediator implements Mediator {
    private List<Colleague> colleagues = new ArrayList<>();

    public void add_colleague(Colleague colleague) {
        colleagues.add(colleague);
    }

    @Override
    public void send_message(String message, Colleague colleague) {
        for (Colleague c : colleagues) {
            if (c != colleague) {
                c.receive(message);
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        FlightControlMediator mediator = new FlightControlMediator();

        Colleague flight1 = new Colleague("Flight 1", mediator);
        Colleague flight2 = new Colleague("Flight 2", mediator);
        Colleague tower = new Colleague("Tower", mediator);

        mediator.add_colleague(flight1);
        mediator.add_colleague(flight2);
        mediator.add_colleague(tower);

        flight1.send("Solicitud de aterrizaje.");
        flight2.send("Confirmación de altitud.");
        tower.send("Autorización de aterrizaje.");
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno se refiere a una relacion entre clases que tienen que se comunican a traves de una clase, esta misma es denominada **mediator**. Cada clase que se comunica a traves del mediator se le conoce como **colleague**. Cada colleague en el metodo constructor debe asigar el mediator para su posterior invocacion del metodo que comunica a todos los colleagues. Cada metodo que tenga el colleague debe tener uno similar el mediator, el metodo del mediator sera llamado a traves de cada colleague, y el metodo de cada colleague debera llamarse desde el codigo del cliente.

Los elementos claves son con su definicion en los ejemplos seria:

1. **Mediador (Mediator):** Es la clase que comunica los diferentes colleagues mediante uno o mas metodos. En los ejemplos son la clase `Home` y `FooBarStarUpEmailBase`

2. **Colegas (Colleagues):** Son las clases que invocan los metodos del mediator e inician la comunicacion. En los ejemplos son la clase `FooBarStarUpEmail`, `SmartLamp`, `SmartTv` y `SmartHomeTeather`. 

# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/mediator)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/mediator/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/mediator)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/mediator/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/mediator-pattern/)