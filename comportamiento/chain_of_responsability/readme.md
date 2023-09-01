# ***Definicion***

El patrón de diseño "Chain of Responsibility" (Cadena de Responsabilidad) es un patrón de comportamiento que se utiliza para pasar solicitudes a través de una cadena de manejadores. Cada manejador decide si puede manejar la solicitud o debe pasarla al siguiente manejador en la cadena. Este patrón desacopla el remitente de la solicitud del receptor, permitiendo que varios objetos tengan la oportunidad de manejar la solicitud.

Elementos clave del patrón "Chain of Responsibility":

1. **Manejadores (Handlers):** Son objetos que implementan una interfaz común y contienen lógica para manejar solicitudes. Cada manejador tiene una referencia opcional al siguiente manejador en la cadena.

2. **Interfaz o Clase Abstracta:** Define una interfaz común que todos los manejadores deben implementar. Esto permite que los manejadores sean intercambiables y se ajusten a una estructura común.

3. **Cliente:** Es quien inicia la solicitud y la envía al primer manejador en la cadena. El cliente no necesita conocer los detalles de la cadena ni de los manejadores concretos.

4. **Cadena:** Es la secuencia de manejadores conectados en serie. Cuando un manejador recibe una solicitud, decide si la maneja o la pasa al siguiente manejador en la cadena.

Ventajas del patrón "Chain of Responsibility":

- Desacopla el remitente de la solicitud del receptor, lo que permite una mayor flexibilidad en la asignación de responsabilidades.
- Facilita la adición o eliminación de nuevos manejadores sin afectar al cliente existente.
- Permite que los manejadores se reutilicen en diferentes combinaciones.

El patrón "Chain of Responsibility" es especialmente útil en situaciones en las que se debe determinar dinámicamente quién debe procesar una solicitud entre un grupo de objetos, o cuando se necesita evitar que una solicitud específica sea manejada por un único objeto fijo.

En resumen, el patrón "Chain of Responsibility" se utiliza para diseñar una cadena de objetos manejadores que pueden procesar solicitudes en secuencia, pasándolas al siguiente manejador si no pueden manejarlas. Esto promueve la flexibilidad y el desacoplamiento en la lógica de manejo de solicitudes.

# ***Ejemplos***

Ejemplo con Python:

```python
class Approver:
    def set_next(self, approver):
        pass

    def process_request(self, amount):
        pass

class Employee(Approver):
    def set_next(self, approver):
        self.next_approver = approver

    def process_request(self, amount):
        if amount <= 1000:
            print("Employee approved the expense")
        elif self.next_approver:
            self.next_approver.process_request(amount)

class Supervisor(Approver):
    def set_next(self, approver):
        self.next_approver = approver

    def process_request(self, amount):
        if amount <= 5000:
            print("Supervisor approved the expense")
        elif self.next_approver:
            self.next_approver.process_request(amount)

class Manager(Approver):
    def set_next(self, approver):
        self.next_approver = approver

    def process_request(self, amount):
        if amount <= 10000:
            print("Manager approved the expense")
        else:
            print("Expense cannot be approved")

def main():
    employee = Employee()
    supervisor = Supervisor()
    manager = Manager()

    employee.set_next(supervisor)
    supervisor.set_next(manager)

    employee.process_request(800)
    employee.process_request(4500)
    employee.process_request(12000)

main()
```

Ejemplo con Java:

```java
abstract class SupportHandler {
    protected SupportHandler nextHandler;

    public void setNextHandler(SupportHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    public abstract void handleRequest(String request);
}

class Level1Support extends SupportHandler {
    public void handleRequest(String request) {
        if (request.equals("Nivel 1")) {
            System.out.println("Operador de Nivel 1 maneja la solicitud.");
        } else if (nextHandler != null) {
            nextHandler.handleRequest(request);
        } else {
            System.out.println("Ningún operador puede manejar la solicitud.");
        }
    }
}

class Level2Support extends SupportHandler {
    public void handleRequest(String request) {
        if (request.equals("Nivel 2")) {
            System.out.println("Operador de Nivel 2 maneja la solicitud.");
        } else if (nextHandler != null) {
            nextHandler.handleRequest(request);
        } else {
            System.out.println("Ningún operador puede manejar la solicitud.");
        }
    }
}

class SupervisorSupport extends SupportHandler {
    public void handleRequest(String request) {
        if (request.equals("Supervisor")) {
            System.out.println("Supervisor maneja la solicitud.");
        } else if (nextHandler != null) {
            nextHandler.handleRequest(request);
        } else {
            System.out.println("Ningún operador puede manejar la solicitud.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Level1Support operator1 = new Level1Support();
        Level2Support operator2 = new Level2Support();
        SupervisorSupport supervisor = new SupervisorSupport();

        operator1.setNextHandler(operator2);
        operator2.setNextHandler(supervisor);

        operator1.handleRequest("Nivel 1");
        operator1.handleRequest("Nivel 2");
        operator1.handleRequest("Supervisor");
        operator1.handleRequest("Ninguna");
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno Chain of resposability es una relacion
entre objetos con la misma interfaz que permitira ejecutar siguiendo una
jerarquia en cada objeto, esta jerquia permite validar la complejidad de una
tarea y en caso de imposilitarze se continuara con el siguiente objeto
responsable de ejecutar la tarea.


Los elementos claves son con su definicion en los ejemplos seria:

1. **Manejadores (Handlers):** Son las clases que se relacionan y que cuentan
con una jerarquia. En el ejemplo de Python las clases `JrDeveloper`,
`SemiDeveloper` y `SrDeveloper` son los handlers, mientras que en ejemplo de
Java las clases `PrimarySchoolGroup`, `HighSchoolGroup`,
`UniversitySchoolGroup` son los handlers


2. **Interfaz o Clase Abstracta:** Es la clase que comparte los handlers.
En el ejemplo de python es la clase `Developer` y en Java es `AlumnsGroupHandler`

3. **Cliente:** Es quien manda la primer solicitud para procesar, es decir
el primer objeto. En python el cliente seria la clase `JrDeveloper` porque
este mismo inicia la cadena y en caso que no pueda procesarla invoca al
siguiente objeto y asi sucesivamente, por otra parte en Java el cliente seria
`PrimarySchoolGroup`.

4. **Cadena:** Este es el contenido del metodo que define si se ejecuta o se
continua con el siguiente objeto, en Python seria el metodo `develop` y en
Java seria `study` que validan ciertos parametros y en caso de ser verdaderos
realizan la operacion caso contrario invocan al mismo metodo que se esta ejecutando pero desde el siguiente objeto. Dicho objeto debe especificarse
en otro metodo. En Python seria `set_superior` y en Java `setNextGroup`.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/chain-of-responsibility)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/chain-of-responsibility/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/chain_of_responsibility)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/chain_of_responsibility/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/chain-of-responsibility-pattern/)
