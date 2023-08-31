# ***Definicion***

El patrón de diseño "Flyweight" es un patrón estructural que se utiliza para optimizar la memoria al compartir eficientemente objetos similares entre varias instancias. En lugar de crear una instancia separada para cada objeto idéntico o similar, el patrón Flyweight almacena la información compartida en un lugar centralizado y la comparte entre múltiples objetos. Esto permite ahorrar memoria y mejorar el rendimiento al reducir la cantidad de objetos que deben crearse.

Elementos clave del patrón Flyweight:

1. **Flyweight:** Es la interfaz o clase abstracta que define los métodos que deben ser implementados por los objetos concretos y que proporcionan la funcionalidad compartida.

2. **Flyweight Concreto:** Es la clase que implementa la interfaz Flyweight y almacena la información compartida. Los objetos flyweight concretos se comparten entre múltiples objetos.

3. **Cliente:** Son las clases que utilizan los objetos flyweight. Los clientes no almacenan información compartida, sino que la obtienen de los objetos flyweight.

El patrón Flyweight es útil cuando tienes una gran cantidad de objetos similares que comparten datos comunes, lo que puede resultar en un alto consumo de memoria si cada objeto almacena su propia información duplicada. Al usar el patrón Flyweight, puedes reducir drásticamente la cantidad de memoria utilizada al compartir la información común y centralizarla en objetos flyweight.

Un ejemplo común es el uso de caracteres en aplicaciones de procesamiento de texto. En lugar de crear un objeto único para cada carácter en un texto, puedes utilizar el patrón Flyweight para compartir instancias de caracteres similares, ahorrando memoria y mejorando la eficiencia.

En resumen, el patrón Flyweight se utiliza para ahorrar memoria al compartir datos comunes entre objetos similares. Esto se logra almacenando la información compartida en objetos flyweight y compartiendo estas instancias entre múltiples objetos, lo que resulta en una reducción significativa en el uso de memoria.

# ***Ejemplos***

Ejemplo con Python:

```python
import java.util.HashMap;
import java.util.Map;

class Character {
    private char symbol;

    public Character(char symbol) {
        this.symbol = symbol;
    }

    public void render(int fontSize) {
        System.out.println("Symbol: " + symbol + ", Font Size: " + fontSize);
    }
}

class CharacterFactory {
    private static Map<Character, Character> characters = new HashMap<>();

    public static Character getCharacter(char symbol) {
        Character character = characters.get(symbol);
        if (character == null) {
            character = new Character(symbol);
            characters.put(symbol, character);
        }
        return character;
    }
}

public class TextEditor {
    public static void main(String[] args) {
        Character A = CharacterFactory.getCharacter('A');
        Character B = CharacterFactory.getCharacter('B');
        Character A2 = CharacterFactory.getCharacter('A'); // Reusing 'A'

        A.render(12); // Output: Symbol: A, Font Size: 12
        B.render(16); // Output: Symbol: B, Font Size: 16
        A2.render(14); // Output: Symbol: A, Font Size: 14 (Reused)
    }
}
```

Ejemplo 2:

```python
class Character:
    def __init__(self, symbol):
        self.symbol = symbol

    def display(self, font_size):
        print(f"Character '{self.symbol}' with font size {font_size}")

class CharacterFactory:
    _characters = {}

    @classmethod
    def get_character(cls, symbol):
        if symbol not in cls._characters:
            cls._characters[symbol] = Character(symbol)
        return cls._characters[symbol]

text = "Hello, World!"
font_size = 12
for char in text:
    character = CharacterFactory.get_character(char)
    character.display(font_size)
```

Ejemplo con Java:

```java
import java.util.HashMap;
import java.util.Map;

class Character {
    private char symbol;

    public Character(char symbol) {
        this.symbol = symbol;
    }

    public void render(int fontSize) {
        System.out.println("Symbol: " + symbol + ", Font Size: " + fontSize);
    }
}

class CharacterFactory {
    private static Map<Character, Character> characters = new HashMap<>();

    public static Character getCharacter(char symbol) {
        Character character = characters.get(symbol);
        if (character == null) {
            character = new Character(symbol);
            characters.put(symbol, character);
        }
        return character;
    }
}

public class TextEditor {
    public static void main(String[] args) {
        Character A = CharacterFactory.getCharacter('A');
        Character B = CharacterFactory.getCharacter('B');
        Character A2 = CharacterFactory.getCharacter('A'); // Reusing 'A'

        A.render(12); // Output: Symbol: A, Font Size: 12
        B.render(16); // Output: Symbol: B, Font Size: 16
        A2.render(14); // Output: Symbol: A, Font Size: 14 (Reused)
    }
}
```

Ejemplo 2:

```java
import java.util.HashMap;
import java.util.Map;

interface Shape {
    void draw(int x, int y);
}

class Circle implements Shape {
    private String color;

    public Circle(String color) {
        this.color = color;
    }

    public void draw(int x, int y) {
        System.out.println("Drawing a " + color + " circle at (" + x + ", " + y + ")");
    }
}

class ShapeFactory {
    private static final Map<String, Shape> shapes = new HashMap<>();

    public static Shape getCircle(String color) {
        Shape circle = shapes.get(color);
        if (circle == null) {
            circle = new Circle(color);
            shapes.put(color, circle);
        }
        return circle;
    }
}

public class DrawingApp {
    public static void main(String[] args) {
        String[] colors = {"Red", "Green", "Blue"};
        for (int i = 0; i < 5; i++) {
            String color = colors[i % colors.length];
            Circle circle = (Circle) ShapeFactory.getCircle(color);
            circle.draw(i, i);
        }
    }
}
```


# ***Conclusion***
En conclusion, el patron de diseno Flyweight se refiere a una clase con
un metodo estatico que permite almacenar diferentes instancias de objetos
relacionados con un id y esto ayudara a que se evite la instanciacion exesiva
de objetos del mismo tipo.


Los elementos claves son con su definicion en los ejemplos seria:

1. **Flyweight:** Se refiere a la interfaz del objeto que tiene potencial
de ser instanciado muchas veces. En los ejemplos son las clases 
`UserStructure` y `Animal`.

2. **Flyweight Concreto:** Son las clases que implementan las interfaces,
es decir donde se aplica la logica de la aplicacion. En el ejemplo son las
clases `User` y `Pet`.

3. **Cliente:** Es el codigo donde se implementa la logica de validacion
de instancias de objetos que pueden reutilizarse. En los ejemplos podemos
ver las clases `PetFeeder` y `UserCreator` que validan por id de usuario
y nombre de mascota.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/flyweight)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/flyweight/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/flyweight)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/flyweight/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/flyweight-pattern/)
