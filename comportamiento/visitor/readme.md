# ***Definicion***

El patrón de diseño Visitor es un patrón de comportamiento que se utiliza para separar el algoritmo de procesamiento de objetos de su estructura. Permite definir una nueva operación o comportamiento que se puede aplicar a una colección de objetos sin cambiar las clases de esos objetos. El patrón Visitor se basa en la idea de que se puede representar la operación como un objeto separado llamado "visitor" que visita los elementos de la estructura y realiza la operación deseada.

**Componentes clave del patrón Visitor:**

1. **Visitor (Visitante)**: Define una interfaz que declara un método de visita para cada tipo de elemento que puede ser visitado. Cada método de visita toma como argumento un objeto del tipo concreto que está siendo visitado.

2. **Element (Elemento)**: Define una interfaz o clase abstracta que declara un método `accept` que toma un objeto visitor como argumento. Cada clase concreta que implementa esta interfaz debe proporcionar una implementación para el método `accept`.

3. **ConcreteElement (Elemento Concreto)**: Son las clases concretas que implementan la interfaz o clase abstracta `Element`. Cada una de estas clases define su propia implementación del método `accept`.

4. **ObjectStructure (Estructura de Objetos)**: Representa una colección o estructura de objetos que pueden ser visitados por el visitor. Proporciona un método para agregar elementos a la estructura y un método para iterar a través de los elementos y llamar al método `accept` en cada uno.

5. **ConcreteVisitor (Visitante Concreto)**: Son las clases concretas que implementan la interfaz `Visitor`. Cada una de estas clases define la operación específica que realizará en los elementos visitados.

**Beneficios del patrón Visitor:**

- Permite agregar nuevas operaciones a una estructura de objetos sin modificar las clases de esos objetos (Open/Closed Principle).
- Facilita la separación de preocupaciones al mantener las operaciones en clases visitor separadas de las clases de elementos.
- Puede mejorar la legibilidad del código al agrupar todas las operaciones relacionadas en clases visitor con nombres descriptivos.

Un ejemplo común de uso del patrón Visitor es en el procesamiento de árboles sintácticos en compiladores o análisis de lenguaje natural, donde diferentes tipos de nodos del árbol pueden ser visitados por diferentes visitors para realizar análisis específicos.

La implementación del patrón Visitor puede ser un poco más compleja que otros patrones, pero ofrece una gran flexibilidad y extensibilidad cuando se trabaja con estructuras de objetos complejas que deben ser procesadas de múltiples maneras.

# ***Ejemplos***

Ejemplo con Python:

```python
# Visitor
class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_rectangle(self, rectangle):
        pass

# Element
class Shape:
    def accept(self, visitor):
        pass

# Concrete Element
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectangle(self)

# Object Structure
class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def accept(self, visitor):
        for shape in self.shapes:
            shape.accept(visitor)

# Concrete Visitor
class AreaCalculator(Visitor):
    def __init__(self):
        self.total_area = 0

    def visit_circle(self, circle):
        area = 3.14 * circle.radius * circle.radius
        print(f"Calculating area of Circle with radius {circle.radius}: {area}")
        self.total_area += area

    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Calculating area of Rectangle with width {rectangle.width} and height {rectangle.height}: {area}")
        self.total_area += area

# Uso del patrón Visitor
circle1 = Circle(5)
circle2 = Circle(3)
rectangle1 = Rectangle(4, 6)
rectangle2 = Rectangle(2, 8)

collection = ShapeCollection()
collection.add_shape(circle1)
collection.add_shape(circle2)
collection.add_shape(rectangle1)
collection.add_shape(rectangle2)

calculator = AreaCalculator()
collection.accept(calculator)

print(f"Total area: {calculator.total_area}")
```

Ejemplo con Java:

```java
interface SoftwareElement {
    void accept(Visitor visitor);
}

class Application implements SoftwareElement {
    public void accept(Visitor visitor) {
        visitor.visitApplication(this);
    }
}

class Library implements SoftwareElement {
    public void accept(Visitor visitor) {
        visitor.visitLibrary(this);
    }
}

class Visitor {
    void visitApplication(Application application) {
        System.out.println("Analizando la aplicación.");
    }

    void visitLibrary(Library library) {
        System.out.println("Analizando la biblioteca.");
    }
}

public class Main {
    public static void main(String[] args) {
        SoftwareElement application = new Application();
        SoftwareElement library = new Library();
        Visitor analyzer = new Visitor();

        application.accept(analyzer);
        library.accept(analyzer);
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno **Visitor** es una implementacion de una clase que permite recibir la informacion de una instancia para actuar sobre esa misma informacion, sin una relacion directa

Los elementos claves son con su definicion en los ejemplos seria:

1. **Visitor (Visitante)**: Interfaz que define los metodos de visita para los objetos que permitan esta implementacion. En los ejemplos son las clases: `ProcessesValidator` y `CarConsultant`

2. **Element (Elemento)**: Interfaz que define los metodos para crear las clases relacionadas con los **visitor**, estas clases deberan tener un metodo `accept()` que recibira como parametro el visitante para invocar el metodo `visit_x()` del objeto en cuestion

3. **ConcreteElement (Elemento Concreto)**: Son las clases que implementan el metodo `accept()` antes mencionado pero agregando la logica adicional de su proceso

4. **ObjectStructure (Estructura de Objetos)**: Es una clase que permite almacenar diferentes objetos **concrete element** y posteriormente con el mismo metodo `accept()` de la interfaz **element** iterar sobre los mismos elementos e invocar su metodo `accept()`.

5. **ConcreteVisitor (Visitante Concreto)**: Es la implementacion de la interfaz **visitor**, aqui se aplica la logica del comportamiento adicional de una clase no relacionada a su estructura.

# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/visitor)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/visitor/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/visitor)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/visitor/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/visitor-pattern/)
