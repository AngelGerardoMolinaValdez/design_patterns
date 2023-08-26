# ***Definicion***

El patrón de diseño "Prototype" es un patrón creacional que se utiliza para crear objetos duplicados o clonados a partir de un objeto existente, conocido como el "prototipo". En lugar de crear objetos desde cero, el patrón "Prototype" permite la creación de copias exactas o modificadas de un objeto prototipo, lo que es especialmente útil cuando se necesitan objetos similares con diferencias mínimas.

Elementos clave del patrón "Prototype":

1. **Prototype:** Es la clase base que define la interfaz para la clonación. Puede ser una clase abstracta o una interfaz. El prototipo generalmente contiene un método `clone` que las subclases deben implementar para realizar la clonación.

2. **Concrete Prototype:** Son las subclases concretas que implementan el método `clone`. Cada subclase define cómo se clona el objeto y puede modificar los valores según sea necesario.

3. **Client:** Utiliza el prototipo para clonar objetos y crear nuevas instancias. El cliente puede modificar las propiedades de las copias clonadas según sus necesidades.

El patrón "Prototype" es útil cuando:

- Se necesitan múltiples objetos con estructuras similares y algunas diferencias.
- Se desea evitar la creación de objetos desde cero y se prefiere clonar un objeto existente.
- La creación de objetos es costosa en términos de rendimiento y recursos.

En resumen, el patrón "Prototype" permite la creación eficiente de objetos clonados a partir de un prototipo existente. Esto proporciona una forma flexible de crear objetos similares y puede mejorar el rendimiento al evitar la creación repetida de objetos desde cero.


# ***Ejemplos***

Ejemplo con Python:

```python
import copy

# Prototype
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def clone(self):
        return copy.copy(self)

# Client
original_car = Car("Toyota", "Corolla")
cloned_car = original_car.clone()
cloned_car.make = "Honda"

print(original_car.make, original_car.model)  # Output: Toyota Corolla
print(cloned_car.make, cloned_car.model)      # Output: Honda Corolla
```

Ejemplo con Java:

```java
// Prototype
class Car implements Cloneable {
    private String make;
    private String model;

    public Car(String make, String model) {
        this.make = make;
        this.model = model;
    }

    @Override
    protected Car clone() {
        try {
            return (Car) super.clone();
        } catch (CloneNotSupportedException e) {
            return null;
        }
    }

    public void setMake(String make) {
        this.make = make;
    }

    public String getInfo() {
        return make + " " + model;
    }
}

// Client
public class Client {
    public static void main(String[] args) {
        Car originalCar = new Car("Toyota", "Corolla");
        Car clonedCar = originalCar.clone();
        clonedCar.setMake("Honda");

        System.out.println(originalCar.getInfo()); // Output: Toyota Corolla
        System.out.println(clonedCar.getInfo());   // Output: Honda Corolla
    }
}
```


# ***Conclusion***

En conclusion, el patron de diseno Prototype permite clonar la instancia
de un objeto y modificarlo sin afectar la instancia original y sin la
necesidad de crear una nueva instancia de la clase, evitando asi el uso
mayor de recursos


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/prototype)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/prototype/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/prototype)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/prototype/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/prototype-pattern/)