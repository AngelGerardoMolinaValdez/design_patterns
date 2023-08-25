# ***Definicion***
El patrón de diseño "Builder" es un patrón creacional que se utiliza cuando se necesita construir objetos complejos paso a paso, permitiendo la creación de diferentes representaciones de un objeto utilizando los mismos pasos de construcción. Este patrón separa la construcción del objeto de su representación final, lo que hace que el proceso de creación sea más flexible y modular.

Elementos clave del patrón "Builder":

1. **Product:** Define el objeto complejo que se va a construir. Puede ser una clase con numerosos atributos y configuraciones.

2. **Builder:** Define una interfaz para construir las diferentes partes del objeto. Contiene métodos para establecer los atributos y configuraciones del producto.

3. **Concrete Builder:** Implementa la interfaz del Builder y proporciona la implementación concreta para construir cada parte del producto. También tiene un método `build` para obtener el producto final.

4. **Director:** Controla el proceso de construcción utilizando un objeto de Concrete Builder. Puede contener métodos específicos para construir distintas variantes del producto.

5. **Client:** Utiliza el Director para construir objetos utilizando un Builder específico. Este paso permite a los clientes tener un control más alto sobre el proceso de construcción.

El patrón "Builder" es útil cuando:

- La creación de objetos implica varios pasos o configuraciones complejas.
- Se necesita construir diferentes representaciones del mismo objeto.
- Quieres aislar el código cliente de los detalles de construcción.

En resumen, el patrón "Builder" ayuda a crear objetos complejos de manera modular y estructurada, permitiendo diferentes configuraciones de objetos sin complicar el código cliente.


# ***Ejemplos***

Ejemplo con Python:

```python
# Product
class Burger:
    def __init__(self):
        self.bread = None
        self.patty = None
        self.veggies = []
        self.condiments = []

    def describe(self):
        description = "Burger with:\n"
        description += f"Bread: {self.bread}\n"
        description += f"Patty: {self.patty}\n"
        description += f"Veggies: {', '.join(self.veggies)}\n"
        description += f"Condiments: {', '.join(self.condiments)}"
        return description

# Builder
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bread(self, bread_type):
        self.burger.bread = bread_type

    def add_patty(self, patty_type):
        self.burger.patty = patty_type

    def add_veggie(self, veggie):
        self.burger.veggies.append(veggie)

    def add_condiment(self, condiment):
        self.burger.condiments.append(condiment)

    def build(self):
        return self.burger

# Director
class Waiter:
    def construct_burger(self, builder):
        builder.add_bread("Wheat")
        builder.add_patty("Beef")
        builder.add_veggie("Lettuce")
        builder.add_veggie("Tomato")
        builder.add_condiment("Ketchup")
        return builder.build()

# Usage
burger_builder = BurgerBuilder()
waiter = Waiter()
burger = waiter.construct_burger(burger_builder)

print(burger.describe())
```

Ejemplo con Java:

```java
// Product
class Burger {
    private String bread;
    private String patty;
    private List<String> veggies = new ArrayList<>();
    private List<String> condiments = new ArrayList<>();

    public void describe() {
        System.out.println("Burger with:");
        System.out.println("Bread: " + bread);
        System.out.println("Patty: " + patty);
        System.out.println("Veggies: " + String.join(", ", veggies));
        System.out.println("Condiments: " + String.join(", ", condiments));
    }
}

// Builder
interface BurgerBuilder {
    void addBread(String breadType);
    void addPatty(String pattyType);
    void addVeggie(String veggie);
    void addCondiment(String condiment);
    Burger build();
}

class ConcreteBurgerBuilder implements BurgerBuilder {
    private Burger burger = new Burger();

    public void addBread(String breadType) {
        burger.bread = breadType;
    }

    public void addPatty(String pattyType) {
        burger.patty = pattyType;
    }

    public void addVeggie(String veggie) {
        burger.veggies.add(veggie);
    }

    public void addCondiment(String condiment) {
        burger.condiments.add(condiment);
    }

    public Burger build() {
        return burger;
    }
}

// Director
class Waiter {
    public Burger constructBurger(BurgerBuilder builder) {
        builder.addBread("Wheat");
        builder.addPatty("Beef");
        builder.addVeggie("Lettuce");
        builder.addVeggie("Tomato");
        builder.addCondiment("Ketchup");
        return builder.build();
    }
}

// Client
public class Client {
    public static void main(String[] args) {
        BurgerBuilder burgerBuilder = new ConcreteBurgerBuilder();
        Waiter waiter = new Waiter();
        Burger burger = waiter.constructBurger(burgerBuilder);
        burger.describe();
    }
}
```

# ***Conclusion***

En conclusion el patron de diseno builder se encarga de configurar los
atributos de un objeto a traves de otra clase la cual genera la
instancia de dicha clase a configurar y crea los metodos para
configurar todos esos atributos de la clase que instancio, a su vez,
la clase que configure es utilizada en otra clase superior que se encarga de
invocar esos metodos y agregar las configuraciones finales para despues
constuir el objeto final.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/builder)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/builder/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/builder)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/builder-pattern/)