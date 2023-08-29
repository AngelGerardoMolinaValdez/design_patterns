# ***Definicion***
El patrón de diseño "Decorator" es un patrón estructural que permite agregar funcionalidades adicionales a objetos existentes de manera flexible y sin alterar su estructura. Esto se logra mediante la creación de una serie de clases "decoradoras" que envuelven el objeto original y añaden comportamientos adicionales. Cada decorador implementa la misma interfaz que el objeto original, lo que permite encadenar varios decoradores para construir una serie de capas de funcionalidad.

Elementos clave del patrón Decorator:

1. **Componente:** Es la interfaz o clase abstracta que define las operaciones comunes tanto para el objeto original como para los decoradores.

2. **Objeto Concreto:** Representa el objeto original al que se añadirán funcionalidades.

3. **Decorador:** Es la clase base abstracta para los decoradores concretos. Implementa la misma interfaz que el componente y mantiene una referencia al componente.

4. **Decorador Concreto:** Son las clases que heredan del decorador y añaden funcionalidad adicional. Pueden añadir comportamientos antes o después de llamar al método del componente.

El patrón Decorator es útil cuando deseas extender o personalizar las funcionalidades de objetos de manera modular y flexible, sin necesidad de alterar su estructura original. Esto permite crear combinaciones de comportamientos a medida que se necesiten.

Un ejemplo común es cuando tienes una clase que representa un componente gráfico y deseas añadir bordes, sombras o colores a ese componente sin alterar su código base. En lugar de crear múltiples clases para todas las combinaciones posibles, puedes usar decoradores para agregar estas características de manera dinámica.

En resumen, el patrón Decorator se utiliza para añadir funcionalidades adicionales a objetos existentes de manera flexible y modular, sin modificar su estructura original. Esto se logra a través de la creación de clases decoradoras que envuelven y extienden el comportamiento del objeto original.

# ***Ejemplos***

Ejemplo con Python:

```python
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
sugar_milk_coffee = SugarDecorator(milk_coffee)

print(coffee.cost())           # Salida: 5
print(milk_coffee.cost())      # Salida: 7
print(sugar_milk_coffee.cost()) # Salida: 8
```

Ejemplo con Java:

```java
interface Coffee {
    int cost();
}

class SimpleCoffee implements Coffee {
    public int cost() {
        return 5;
    }
}

class MilkDecorator implements Coffee {
    private Coffee coffee;

    public MilkDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    public int cost() {
        return coffee.cost() + 2;
    }
}

class SugarDecorator implements Coffee {
    private Coffee coffee;

    public SugarDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    public int cost() {
        return coffee.cost() + 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Coffee coffee = new SimpleCoffee();
        Coffee milkCoffee = new MilkDecorator(coffee);
        Coffee sugarMilkCoffee = new SugarDecorator(milkCoffee);

        System.out.println(coffee.cost());           // Salida: 5
        System.out.println(milkCoffee.cost());      // Salida: 7
        System.out.println(sugarMilkCoffee.cost()); // Salida: 8
    }
}
```

# ***Conclusion***
El patron de diseno Decorator se refiere relacion entre una clase y otra
que sin afectar su funcionalidad principal agrega nueva usabilidad.

En los ejemplos mencionados se utiliza la clase principal `CellPhone` y `Liquid`. Por otra parte se utilizan las clases decoradoras `CellPhoneCase` y `Flavor` que agregan una funcionalidad mas a la principal, ejemplo:

`CellPhone` tiene un metodo llamado `turn_on` que retorna una cadena de texto
y la clase `CellPhoneCase` invoca ese metodo `turn_on` y el resultado le agrega
un texto mas para agregarle esa funcionalidad extra.

Los elementos claves son con su definicion en los ejemplos seria:

***Componente:*** Se refiere a la interfaz de donde son tomados los
metodos para las clases del funcionamiento principal. Estas clases son
`CellPhone` y `Liquid`

***Objeto Concreto:*** Son las clases que implementan los metodos de las
interfaces `CellPhone` y `Liquid`, las cuales serian `XiaomiCellPhone`
y `Water`


***Decorador:*** La interfaz para crear las clases que agregaran funcionalidad
a los componentes concretos. En este ejemplo serian `CellPhoneCase`
y `Flavor`


***Decorador Concreto:*** Son la clases que implementan las intefaces de los
decoradores y ahi se agrega la logica. Las clases `XiaomiCase` y `LemonFlavor`
son los decoradores en este ejemplo.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/decorator)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/decorator/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/decorator)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/decorator/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/decorator-pattern/)