# ***Definicion***
El patrón de diseño "Factory Method" es un patrón creacional que proporciona una forma de crear objetos en una jerarquía de clases sin especificar explícitamente las clases concretas. En lugar de crear objetos directamente utilizando un constructor, el patrón "Factory Method" define un método abstracto en una clase base (también conocida como "Creator") que las subclases (también conocidas como "Concrete Creators") deben implementar. Cada subclase concreta puede decidir qué clase concreta de objeto crear, permitiendo una mayor flexibilidad en la creación de objetos sin afectar el código cliente.

Elementos clave del patrón "Factory Method":

1. **Product:** Define la interfaz del objeto que se va a crear.

2. **Concrete Products:** Son las clases concretas que implementan la interfaz del producto.

3. **Creator:** Define un método abstracto (el "Factory Method") que las subclases deben implementar para crear objetos. También puede contener lógica común para la creación de productos.

4. **Concrete Creators:** Son las subclases que implementan el "Factory Method" para crear instancias específicas de productos.

En resumen, el patrón "Factory Method" permite a una clase delegar la creación de objetos a sus subclases. Esto facilita la expansión y modificación de la jerarquía de clases sin cambiar el código cliente existente.


# ***Ejemplos***

Ejemplo con Python:

```python
# Product
class Vehicle:
    def drive(self):
        pass

# Concrete Products
class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

# Creator (Factory Method)
class VehicleFactory:
    def create_vehicle(self):
        pass

# Concrete Creators
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

# Client
def use_vehicle(factory):
    vehicle = factory.create_vehicle()
    return vehicle.drive()

# Usage
car_result = use_vehicle(CarFactory())
bike_result = use_vehicle(BikeFactory())

print(car_result)  # Output: Driving a car
print(bike_result)  # Output: Riding a bike
```

Ejemplo con Java:

```java
// Product
interface Vehicle {
    void drive();
}

// Concrete Products
class Car implements Vehicle {
    public void drive() {
        System.out.println("Driving a car");
    }
}

class Bike implements Vehicle {
    public void drive() {
        System.out.println("Riding a bike");
    }
}

// Creator (Factory Method)
abstract class VehicleFactory {
    abstract Vehicle createVehicle();
}

// Concrete Creators
class CarFactory extends VehicleFactory {
    public Vehicle createVehicle() {
        return new Car();
    }
}

class BikeFactory extends VehicleFactory {
    public Vehicle createVehicle() {
        return new Bike();
    }
}

// Client
public class Client {
    public static void useVehicle(VehicleFactory factory) {
        Vehicle vehicle = factory.createVehicle();
        vehicle.drive();
    }

    public static void main(String[] args) {
        useVehicle(new CarFactory());  // Output: Driving a car
        useVehicle(new BikeFactory()); // Output: Riding a bike
    }
}
```

# ***Conclusion***

En conclusion el patron de diseno Factory Method se refiere a una interfaz 
donde el metodo definido funcionara para crear el objeto del producto 
especificado, dicho producto tambien tiene una base implementada en otra interfaz, que permitira definir multiples productos y esto a su vez permitira
multiples fabricas de diferentes objetos, teniendo la base de su intefaz que
esto permitira interconectar a todas las clases hijas y clases nietas.

# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/factory-method/python/example)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/factory-method)
- [SourceMaking](https://sourcemaking.com/design_patterns/factory_method)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/factory_method/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/factory-method-design-pattern/)