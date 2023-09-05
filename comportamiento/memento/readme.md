# ***Definicion***

El patrón de diseño Memento se utiliza para capturar y externalizar el estado interno de un objeto sin romper su encapsulación, de modo que el objeto pueda ser restaurado a ese estado en el futuro. Este patrón permite guardar y restaurar instantáneas del estado de un objeto.

A continuación, se describe el patrón de diseño Memento en detalle:

- **Originator (Creador)**: Es la clase u objeto cuyo estado se desea guardar. El Originator tiene dos responsabilidades: guardar su estado en un objeto Memento y restaurar su estado a partir de un objeto Memento.

- **Memento**: Es una clase que almacena el estado del Originator. El Memento es inmutable, lo que significa que una vez que se crea, no se puede modificar. Puede haber varios Mementos guardados en diferentes puntos en el tiempo.

- **Caretaker (Cuidador)**: Es responsable de mantener y gestionar los Mementos. El Cuidador no modifica ni conoce el contenido del Memento, simplemente almacena y recupera Mementos.

El flujo típico de uso del patrón Memento es el siguiente:

1. El Originator crea un Memento que contiene una instantánea de su estado actual.

2. El Originator pasa el Memento al Cuidador y puede guardarlo en una lista de Mementos.

3. En el futuro, si el Originator necesita volver a un estado anterior, puede solicitar al Cuidador el Memento deseado.

4. El Cuidador devuelve el Memento al Originator.

5. El Originator restaura su estado utilizando el Memento.

El patrón Memento es útil en situaciones donde se necesita mantener un historial de cambios en el estado de un objeto o cuando se requiere la capacidad de deshacer o revertir acciones. Un ejemplo común es un editor de texto que permite deshacer y rehacer operaciones.

En resumen, el patrón Memento permite guardar y restaurar el estado de un objeto en diferentes puntos en el tiempo, lo que facilita la reversión de cambios o la recuperación de estados anteriores.

# ***Ejemplos***

Ejemplo con Python:

```python
class Memento:
    def __init__(self, state):
        self.state = state

class Originator:
    def __init__(self):
        self.state = ""

    def set_state(self, state):
        self.state = state

    def save_to_memento(self):
        return Memento(self.state)

    def restore_from_memento(self, memento):
        self.state = memento.state

class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]

# Uso del patrón Memento
originator = Originator()
caretaker = Caretaker()

originator.set_state("Estado 1")
caretaker.add_memento(originator.save_to_memento())

originator.set_state("Estado 2")
caretaker.add_memento(originator.save_to_memento())

originator.restore_from_memento(caretaker.get_memento(0))
print("Estado restaurado:", originator.state)
```

Ejemplo con Java:

```java
import java.util.ArrayList;
import java.util.List;

class Memento {
    private final String state;

    public Memento(String state) {
        this.state = state;
    }

    public String getState() {
        return state;
    }
}

class Originator {
    private String state;

    public void setState(String state) {
        this.state = state;
    }

    public Memento saveToMemento() {
        return new Memento(state);
    }

    public void restoreFromMemento(Memento memento) {
        state = memento.getState();
    }
}

class Caretaker {
    private final List<Memento> mementos = new ArrayList<>();

    public void addMemento(Memento memento) {
        mementos.add(memento);
    }

    public Memento getMemento(int index) {
        return mementos.get(index);
    }
}

public class Main {
    public static void main(String[] args) {
        Originator originator = new Originator();
        Caretaker caretaker = new Caretaker();

        originator.setState("Estado 1");
        caretaker.addMemento(originator.saveToMemento());

        originator.setState("Estado 2");
        caretaker.addMemento(originator.saveToMemento());

        originator.restoreFromMemento(caretaker.getMemento(0));
        System.out.println("Estado restaurado: " + originator.getState());
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno Memento se refiere a guardar un valor que llamaremos **estado** de una clase que podremos definir como **originator**, este estado se guardara a traves de otra clase para no romper el encapsulamiento, la clase que almacena el valor permitira obtener el mismo valor ingresado, a esta misma la llamaremos **memento**.

Por ultimo tendremos una clase mas que permitira guardar y obtener los diferentes **mementos** para obtener el valor guardado al instanciarlas y asi poder restaurar ese valor en la clase **originator**. La clase que gestiona todo esto la podremos llamar **caretaker**


Los elementos claves son con su definicion en los ejemplos seria:

- **Originator (Creador)**: Es la clase que desea guardar el estado de un atributo. En los ejemplos serian las clases `FileObject` y `WindowsLicence`

- **Memento**: Es la clase que almacenara el valor del originator, tendra un metodo para obtener dicho valor y una vez instanciada no podra cambiar el valor guardado. En los ejemplos son las clases `BackUp` y `FileContentBackUp`

- **Caretaker (Cuidador)**: Es la clase que gestionara las diferentes clases **mementos**.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/memento)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/memento/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/memento)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/memento/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/memento-pattern/)
