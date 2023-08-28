# ***Definicion***
El patrón de diseño "Bridge" es un patrón estructural que se utiliza para separar la abstracción de su implementación, permitiendo que ambas puedan variar independientemente sin afectarse mutuamente. Este patrón ayuda a evitar una explosión de clases derivadas al dividir las clases en dos jerarquías: una para la abstracción y otra para la implementación.

En términos más simples, imagina que tienes dos dimensiones de variación en tu diseño, y no quieres crear una clase para cada combinación posible. En lugar de eso, creas dos jerarquías de clases separadas, una para la abstracción y otra para la implementación. Luego, conectas estas jerarquías utilizando un puente, lo que te permite combinar diferentes abstracciones con diferentes implementaciones de manera flexible.

Elementos clave del patrón Bridge:

1. **Abstracción:** Representa la interfaz de alto nivel que el cliente utiliza. Contiene una referencia a un objeto de la implementación.

2. **Implementación:** Define la interfaz de bajo nivel que proporciona la funcionalidad concreta. Puede ser una clase o una interfaz.

3. **Refinamiento Abstracción:** Es una subclase de Abstracción que refina o extiende la interfaz de la abstracción básica.

4. **Refinamiento Implementación:** Es una subclase de Implementación que refina o extiende la implementación básica.

El patrón Bridge es útil cuando deseas evitar una conexión fija entre la abstracción y la implementación, lo que permite una mayor flexibilidad y extensibilidad en tu diseño. También es beneficioso cuando tienes múltiples dimensiones de variación y quieres evitar la creación de una gran cantidad de clases derivadas.

En resumen, el patrón Bridge se utiliza para separar la abstracción de su implementación, permitiendo que ambas varíen independientemente y se combinen de manera flexible. Esto facilita la creación de diseños más mantenibles y adaptables en situaciones donde existen múltiples dimensiones de variación.


# ***Ejemplos***

Ejemplo con Python:

```python
class Color:
    def fill(self):
        pass

class RedColor(Color):
    def fill(self):
        return "Filled with red color"

class BlueColor(Color):
    def fill(self):
        return "Filled with blue color"

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Drawn a circle. {self.color.fill()}"

class Square(Shape):
    def draw(self):
        return f"Drawn a square. {self.color.fill()}"

red_circle = Circle(RedColor())
blue_square = Square(BlueColor())

print(red_circle.draw())   # Output: Drawn a circle. Filled with red color
print(blue_square.draw())  # Output: Drawn a square. Filled with blue color
```

Ejemplo con Java:

```java
interface Color {
    String fill();
}

class RedColor implements Color {
    public String fill() {
        return "Filled with red color";
    }
}

class BlueColor implements Color {
    public String fill() {
        return "Filled with blue color";
    }
}

abstract class Shape {
    protected Color color;

    public Shape(Color color) {
        this.color = color;
    }

    public abstract String draw();
}

class Circle extends Shape {
    public Circle(Color color) {
        super(color);
    }

    public String draw() {
        return "Drawn a circle. " + color.fill();
    }
}

class Square extends Shape {
    public Square(Color color) {
        super(color);
    }

    public String draw() {
        return "Drawn a square. " + color.fill();
    }
}

public class Main {
    public static void main(String[] args) {
        Shape redCircle = new Circle(new RedColor());
        Shape blueSquare = new Square(new BlueColor());

        System.out.println(redCircle.draw());   // Output: Drawn a circle. Filled with red color
        System.out.println(blueSquare.draw());  // Output: Drawn a square. Filled with blue color
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno Bridge es una clase abstracta que recibe 
un objeto al ser instanciada, dicha clase debio haber implementado una los
metodos de una interfaz, dentro de la clase instanciada se invocara el metodo
de la clase pasada por argumento.

En el ejemplo de los archivos tenemos la interfaz `Car` o `Computer` que
cuentan con los metodos a cumplir con las implementaciones. Posteriormente
contamos con las clases abstractas `Employee` que reciben en el metodo
constructor la instancia de la clase que implementa la primer interfaz, en
esta clase abstracta se cuenta con un metodo que a su vez invocara el metodo
de la instancia recibida por parametro.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/bridge)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/bridge/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/bridge)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/bridge/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/bridge-pattern/)
