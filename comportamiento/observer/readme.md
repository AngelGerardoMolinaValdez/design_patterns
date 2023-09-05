# ***Definicion***

El patrón de diseño Observer, también conocido como el patrón de observador o patrón publish-subscribe, es un patrón de comportamiento que se utiliza en el diseño de software para establecer una relación de uno a muchos entre objetos. El propósito principal de este patrón es definir un mecanismo para que un objeto, llamado "sujeto" o "publicador", notifique a múltiples objetos "observadores" cuando su estado cambie. 

A continuación, se describen los componentes clave del patrón Observer:

- **Sujeto (Subject o Publisher)**: Es el objeto que mantiene un registro de sus observadores y notifica a estos observadores cuando ocurre un cambio en su estado. El sujeto también proporciona métodos para que los observadores se registren (suscriban) y cancelen la suscripción.

- **Observador (Observer o Subscriber)**: Son los objetos que desean recibir notificaciones cuando el estado del sujeto cambie. Los observadores implementan una interfaz o heredan de una clase abstracta que define un método de actualización.

- **Actualización (Update)**: Es el método que se llama en cada observador cuando el sujeto notifica un cambio. Este método permite a los observadores realizar acciones basadas en la notificación.

El patrón Observer es útil en situaciones en las que varios objetos deben estar informados sobre los cambios en el estado de un objeto sin que el sujeto conozca los detalles de los observadores. Ejemplos comunes de uso del patrón Observer incluyen sistemas de eventos en interfaces de usuario, notificación de cambios en modelos de datos y la implementación de patrones de diseño como el Modelo-Vista-Controlador (MVC).

En resumen, el patrón Observer permite una comunicación eficiente entre objetos sin que estos objetos estén acoplados de manera rígida. Los observadores pueden registrarse y desregistrarse dinámicamente, y el sujeto notifica automáticamente a todos los observadores cuando se producen cambios en su estado, lo que mejora la flexibilidad y la extensibilidad del sistema.

# ***Ejemplos***


Ejemplo con Python:

```python
# Sujeto (Subject)
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

# Observador (Observer)
class Observer:
    def update(self):
        pass

# Observador Concreto (Concrete Observer)
class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self):
        print(f"{self._name} ha sido notificado de un cambio en el sujeto.")

# Sujeto Concreto (Concrete Subject)
class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        self.notify()

# Uso del patrón Observer
subject = ConcreteSubject("Estado inicial")
observer1 = ConcreteObserver("Observador 1")
observer2 = ConcreteObserver("Observador 2")

subject.attach(observer1)
subject.attach(observer2)

subject.set_state("Nuevo estado")
```

Ejemplo con Java:

```java
import java.util.ArrayList;
import java.util.List;

// Sujeto (Subject)
class Subject {
    private List<Observer> observers = new ArrayList<>();
    private String state;

    public void attach(Observer observer) {
        observers.add(observer);
    }

    public void detach(Observer observer) {
        observers.remove(observer);
    }

    public void setState(String state) {
        this.state = state;
        notifyObservers();
    }

    public String getState() {
        return state;
    }

    private void notifyObservers() {
        for (Observer observer : observers) {
            observer.update();
        }
    }
}

// Observador (Observer)
interface Observer {
    void update();
}

// Observador Concreto (Concrete Observer)
class ConcreteObserver implements Observer {
    private String name;

    public ConcreteObserver(String name) {
        this.name = name;
    }

    @Override
    public void update() {
        System.out.println(name + " ha sido notificado de un cambio en el sujeto.");
    }
}

public class Main {
    public static void main(String[] args) {
        Subject subject = new Subject();
        Observer observer1 = new ConcreteObserver("Observador 1");
        Observer observer2 = new ConcreteObserver("Observador 2");

        subject.attach(observer1);
        subject.attach(observer2);

        subject.setState("Nuevo estado");
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno observer es un patron de comportamiento. Esto se refiere que una clase puede notificar a n clases del cambio/ejecucion de otra clase o de la misma.

Los elementos claves son con su definicion en los ejemplos seria:

- **Sujeto (Subject o Publisher)**: Es la clase que sera observada y que notificara a las clases observadoras. En el ejemplo son: `Child` y `CarFactory`

- **Observador (Observer o Subscriber)**: Es la clase que recibe la notificacion de los cambios hechos. En el ejemplo son: `Familiar` y `FactoryManager`

- **Actualización (Update)**: Este concepto se refiere al metodo que contienen todos los observadores, el cual es invocado al realizar n accion.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/observer)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/observer/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/observer)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/observer/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/observer-pattern/)
