# ***Definicion***

El patrón de diseño "Command" (Comando) es un patrón de comportamiento que se utiliza para encapsular una solicitud como un objeto independiente. Esto permite que los clientes emitan solicitudes sin conocer los detalles específicos de la operación que se realizará o el receptor que la llevará a cabo. En otras palabras, el patrón "Command" convierte una solicitud en un objeto que contiene toda la información necesaria para ejecutar esa solicitud en el momento adecuado.

Elementos clave del patrón "Command":

1. **Comando (Command):** Es una interfaz o una clase abstracta que define un método llamado `execute()`. Este método encapsula la acción que debe llevarse a cabo cuando se invoca el comando.

2. **Comandos Concretos (Concrete Commands):** Son clases que implementan la interfaz o heredan de la clase abstracta del comando. Cada comando concreto representa una solicitud específica y contiene la lógica para llevar a cabo esa solicitud.

3. **Receptor (Receiver):** Es el objeto que realiza la acción real asociada con un comando concreto. El receptor es quien sabe cómo llevar a cabo la solicitud.

4. **Invocador (Invoker):** Es el objeto que emite los comandos y los ejecuta. El invocador no necesita conocer los detalles específicos del comando ni del receptor; simplemente ejecuta el comando cuando sea necesario.

5. **Cliente (Client):** Es quien crea los comandos y configura el invocador con los comandos adecuados. El cliente emite solicitudes a través de los comandos sin preocuparse por los detalles de su implementación.

Ventajas del patrón "Command":

- Desacopla al emisor de las solicitudes (cliente) de los objetos que las ejecutan (receptores).
- Permite la creación de comandos personalizados y su composición para implementar funcionalidades complejas.
- Facilita la reversión de operaciones (deshacer) al almacenar el estado antes de ejecutar un comando.

El patrón "Command" se utiliza en situaciones donde se necesita abstraer y parametrizar operaciones, realizar operaciones en un momento específico o gestionar la reversión de operaciones. Es comúnmente utilizado en aplicaciones de interfaz de usuario, sistemas de registro de cambios, y para implementar sistemas de manejo de transacciones, entre otros.

En resumen, el patrón "Command" encapsula solicitudes como objetos, permitiendo que los clientes emitan solicitudes sin conocer los detalles de su ejecución. Esto promueve la flexibilidad y el desacoplamiento en el diseño de software.

# ***Ejemplos***

Ejemplo con Python:

```python
from abc import ABC, abstractmethod

# Comando abstracto
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Comandos concretos
class TurnOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class TurnOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

# Receptor
class Television:
    def turn_on(self):
        print("TV encendida")

    def turn_off(self):
        print("TV apagada")

# Invocador
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

def main():
    tv = Television()
    turn_on_command = TurnOnCommand(tv)
    turn_off_command = TurnOffCommand(tv)

    remote = RemoteControl()

    remote.set_command(turn_on_command)
    remote.press_button()  # Enciende la TV

    remote.set_command(turn_off_command)
    remote.press_button()  # Apaga la TV

if __name__ == "__main__":
    main()
```

Ejemplo con Java:

```java
// Comando abstracto
interface Command {
    void execute();
}

// Comandos concretos
class LightOnCommand implements Command {
    private Light light;

    public LightOnCommand(Light light) {
        this.light = light;
    }

    public void execute() {
        light.turnOn();
    }
}

class LightOffCommand implements Command {
    private Light light;

    public LightOffCommand(Light light) {
        this.light = light;
    }

    public void execute() {
        light.turnOff();
    }
}

// Receptor
class Light {
    public void turnOn() {
        System.out.println("Luz encendida");
    }

    public void turnOff() {
        System.out.println("Luz apagada");
    }
}

// Invocador
class RemoteControl {
    private Command command;

    public void setCommand(Command command) {
        this.command = command;
    }

    public void pressButton() {
        command.execute();
    }
}

public class Main {
    public static void main(String[] args) {
        Light livingRoomLight = new Light();
        LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);

        RemoteControl remote = new RemoteControl();

        remote.setCommand(livingRoomLightOn);
        remote.pressButton();  // Enciende la luz

        remote.setCommand(livingRoomLightOff);
        remote.pressButton();  // Apaga la luz
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno Command se refiere a una clase con un
metodo llamado `execute` que este a su vez ejecutara un metodo del objeto
que debera pasarse como argumento al instanciar los comandos concretos,
este objeto pasado por parametro se le llamara solicitud dentro de la misma. La
la clase pasada como parametro la podemos definir como **receptor** fuera del
contexto del comando. Este comando a su vez debe ser invocado por otra clase
denominada **invoker**.


Los elementos claves son con su definicion en los ejemplos seria:

1. **Comando (Command):** Son las interfaz que definen los metodos para los comandos. En ambos ejemplos la clase es `Command`

2. **Comandos Concretos (Concrete Commands):** Son las clases que implementan
la estructura de `Command` y que ejecutaran el metodo deseado de la solicitud (**receiver**). En el ejemplo de python son las clases `ApprovePaymentCommand` y `RejectPaymentCommand`. En Java son las clases `OpenDoorCommand` y `CloseDoorCommand`.

3. **Receptor (Receiver):** El objeto que sera manipulado a traves de los comandos. En Python es la clase `PaymentProcess` y en Java `Door`

4. **Invocador (Invoker):** El objeto que invoca los comandos, estos mismos deben tener un metodo `set_command` para especificar el comando que ejecutaran y uno mas para ejecutar el comando como tal.

5. **Cliente (Client):** Es quien instancia el codigo e invoca los metodos del invoker. En Python es la funcion main y en Java la clase main.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/command)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/command/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/command)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/command/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/command-pattern/)
