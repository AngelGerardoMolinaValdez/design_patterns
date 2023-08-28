# ***Definicion***
El patrón de diseño "Composite" es un patrón estructural que permite construir estructuras jerárquicas y tratar tanto a objetos individuales como a composiciones de objetos de manera uniforme. Esto se logra mediante la creación de una estructura de árbol donde los nodos hoja representan objetos individuales y los nodos compuestos representan colecciones de objetos. El patrón Composite permite a los clientes tratar a ambos tipos de nodos de la misma manera, lo que simplifica el código y aumenta la flexibilidad en el diseño.

Elementos clave del patrón Composite:

1. **Componente:** Es la interfaz o clase base que define las operaciones comunes tanto para los nodos hoja como para los nodos compuestos.

2. **Nodo Hoja:** Representa objetos individuales. Implementa el componente y contiene la funcionalidad específica de los objetos individuales.

3. **Nodo Compuesto:** Representa la composición de objetos, ya que contiene varios componentes, ya sean nodos hoja o nodos compuestos. Implementa el componente y proporciona la lógica para agregar, eliminar y operar sobre los componentes hijos.

El patrón Composite es útil cuando tienes una estructura jerárquica en la que deseas tratar de manera uniforme tanto a objetos individuales como a grupos de objetos. Esto evita la necesidad de tener lógica especializada para cada tipo de objeto y simplifica la manipulación de la estructura en su conjunto.

Un ejemplo común es un árbol de elementos gráficos, donde cada elemento puede ser un objeto individual o un grupo de elementos. El patrón Composite permite tratar a los elementos y grupos de elementos de manera coherente, lo que es especialmente útil en sistemas de diseño gráfico y editores.

En resumen, el patrón Composite se utiliza para crear estructuras jerárquicas en las que los nodos individuales y compuestos se tratan de manera uniforme. Esto mejora la flexibilidad, la reutilización de código y la organización en el diseño de software.

# ***Ejemplos***

Ejemplo con Python:

```python
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite [{', '.join(results)}]"

leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

print(leaf1.operation())        # Salida: Leaf
print(leaf2.operation())        # Salida: Leaf
print(composite.operation())    # Salida: Composite [Leaf, Leaf]
```

Ejemplo con Java:

```java
import java.util.ArrayList;
import java.util.List;

interface Component {
    String operation();
}

class Leaf implements Component {
    public String operation() {
        return "Leaf";
    }
}

class Composite implements Component {
    private List<Component> children = new ArrayList<>();

    public void add(Component component) {
        children.add(component);
    }

    public String operation() {
        List<String> results = new ArrayList<>();
        for (Component child : children) {
            results.add(child.operation());
        }
        return "Composite [" + String.join(", ", results) + "]";
    }
}

public class Main {
    public static void main(String[] args) {
        Component leaf1 = new Leaf();
        Component leaf2 = new Leaf();
        Composite composite = new Composite();
        composite.add(leaf1);
        composite.add(leaf2);

        System.out.println(leaf1.operation());        // Salida: Leaf
        System.out.println(leaf2.operation());        // Salida: Leaf
        System.out.println(composite.operation());    // Salida: Composite [Leaf, Leaf]
    }
}
```

# ***Conclusion***
En conclusion el patron de diseno composite se refiere a 3 componentes
`Component`, `Leaf` y `Composite`.

Donde `Component` se refiere a la case abstracta o interfaz que compartiran
de base las implementaciones `Leaf` y `Composite`, la diferencia radica en la logica que se implementa para cada una de ellas donde `Leaf` trata a los
metodos como un objeto individual es decir, retorna una cadena, imprime un
texto, etc, mientras que el `Composite` implementa los metodos con logica de
tratamiento de multiples objetos de la clase `Leaf` y este mismo metodo al
final igual retorna una cadena imprime un texto, etc pero de la manipulacion
del mismo metodo que se implemento en la clase `Leaf`.

En el ejemplo aplicado en este patron se utiliza la interfaz `LedStructure` y
`Employee`, de estas clases su implementacion individual son `Led` y
`AmazonEmployee`. Las implementaciones grupales son `StripLed` y
`AmazonEmployees`, todas estas clases tienen el comun los metodos de la
interfaz que heredan, sin embargo las que se definen para tratar el conjunto
de objetos implementan un metodo mas para agregar los objetos individuales 
(`add`) y posteriormente iterar sobre cada uno de los objetos agregados
invocando cada uno de los metodos para al final retorna todo lo obtenido
de dicha operacion.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/composite)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/composite/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/composite)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/composite/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/composite-pattern/)