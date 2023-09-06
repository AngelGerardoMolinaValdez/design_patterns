# ***Definicion***

El patrón de diseño State (Estado) es un patrón de diseño de comportamiento que permite que un objeto cambie su comportamiento cuando su estado interno cambia. En otras palabras, este patrón permite que un objeto altere su comportamiento sin cambiar su clase. El cambio de estado se maneja mediante la delegación a objetos llamados "estados", cada uno de los cuales representa un comportamiento específico asociado a un estado particular del objeto.

Elementos clave del patrón de diseño State:

1. **Contexto (Context)**: Es el objeto que tiene un estado interno y cuyo comportamiento cambia según su estado. El contexto mantiene una referencia a un objeto de estado concreto y delega las solicitudes de cambio de estado a este objeto.

2. **Estado (State)**: Es una interfaz o clase abstracta que define un conjunto de métodos que representan los comportamientos asociados a los diferentes estados del contexto. Cada estado concreto implementa esta interfaz o hereda de la clase abstracta y proporciona una implementación específica de esos métodos.

3. **Estados Concretos (Concrete States)**: Son las clases que implementan la interfaz o heredan de la clase abstracta de estado. Cada estado concreto proporciona una implementación concreta de los métodos definidos en la interfaz de estado y representa un estado particular en el cual el contexto puede encontrarse.

El patrón de diseño State es útil cuando un objeto necesita cambiar su comportamiento en función de su estado interno, y se prefiere evitar la proliferación de múltiples condicionales en el código para manejar diferentes estados. En su lugar, cada estado se modela como un objeto separado, lo que facilita la extensión y mantenimiento del código.

Este patrón se utiliza en situaciones en las que un objeto puede tener un comportamiento que varía según su estado actual, como en máquinas de estados, sistemas de control, interfaces de usuario y más.

En resumen, el patrón de diseño State permite que un objeto cambie su comportamiento dinámicamente en función de su estado interno, promoviendo la encapsulación y la flexibilidad en el diseño del software.

# ***Ejemplos***

Ejemplo con Python:

```python
# State
class State:
    def handle_state(self):
        pass

# Concrete States
class OnState(State):
    def handle_state(self):
        return "The device is on."

class OffState(State):
    def handle_state(self):
        return "The device is off."

# Context
class Device:
    def __init__(self):
        self.state = OffState()

    def change_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state.handle_state()

# Using the State Pattern
device = Device()
print(device.get_state())  # Output: The device is off.

device.change_state(OnState())
print(device.get_state())  # Output: The device is on.
```

Ejemplo con Java:

```java
// State
interface State {
    String handleState();
}

// Concrete States
class OnState implements State {
    public String handleState() {
        return "The device is on.";
    }
}

class OffState implements State {
    public String handleState() {
        return "The device is off.";
    }
}

// Context
class Device {
    private State state = new OffState();

    public void changeState(State newState) {
        state = newState;
    }

    public String getState() {
        return state.handleState();
    }
}

public class Main {
    public static void main(String[] args) {
        Device device = new Device();
        System.out.println(device.getState()); // Output: The device is off.

        device.changeState(new OnState());
        System.out.println(device.getState()); // Output: The device is on.
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno *State* se refiere al cambio de comportamiento de un objeto a traves de la instancia de otro mismo, con el fin de reducir la cantidad de condicionales. El objeto que altera el comportamiento se conoce como *state*, el objeto que busca cambiar el comportamiento se conoce como *context*.

Este *state* se define en el metodo constructor del objeto *context* y es posible modificarlo durante la ejecucion.

Los elementos claves son con su definicion en los ejemplos seria:

1. **Contexto (Context)**: La clase que contiene en su estructura el soporte a los difentes objetos *state*.

2. **Estado (State)**: Es la interfaz o clase abstracta que se utilizara como punto de inicio para los diferentes estados de comportamiento.

3. **Estados Concretos (Concrete States)**: La clase que contiene la logica que se ejecutara cuando en el *context* sea invocado el metodo definido.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/state)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/state/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/state)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/state/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/state-pattern/)
