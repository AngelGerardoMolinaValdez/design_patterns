# ***Definicion***

El patrón de diseño "Iterator" es un patrón de comportamiento que se utiliza para proporcionar una forma de acceder secuencialmente a los elementos de una colección sin exponer los detalles internos de la estructura de esa colección. Este patrón permite que un objeto (llamado "iterador") recorra los elementos de una colección uno por uno, sin que el cliente que utiliza el iterador tenga que conocer la estructura o la implementación subyacente de la colección.

Los componentes clave del patrón "Iterator" son:

1. **Iterador (Iterator):** Es una interfaz o clase abstracta que define métodos como `next()` para obtener el siguiente elemento y `hasNext()` para verificar si hay más elementos en la colección. Los iteradores mantienen un seguimiento del estado actual de la iteración.

2. **Colección (Aggregate):** Es la estructura de datos que contiene los elementos que se van a recorrer. La colección generalmente proporciona un método para crear un iterador que se ajusta a su estructura.

3. **Iterador Concreto (Concrete Iterator):** Es una implementación específica del iterador que se adapta a una colección particular. Conoce la estructura de la colección y sabe cómo recorrerla.

4. **Colección Concreta (Concrete Aggregate):** Es una implementación específica de una colección que crea un iterador concreto asociado a su estructura.

El patrón "Iterator" es útil cuando deseas proporcionar una forma estandarizada de recorrer elementos en una colección sin preocuparte por los detalles de esa colección. Esto promueve el desacoplamiento entre el cliente y la colección, lo que facilita la extensibilidad y la reutilización del código.

Un ejemplo común de uso del patrón "Iterator" es en lenguajes de programación que ofrecen estructuras de datos como listas o conjuntos. Los iteradores permiten recorrer estos contenedores de manera uniforme, independientemente de su implementación subyacente.

En resumen, el patrón "Iterator" es una herramienta poderosa para recorrer elementos de una colección de manera secuencial y abstracta, lo que facilita la manipulación de datos en colecciones sin exponer su estructura interna al cliente.

# ***Ejemplos***

Ejemplo con Python:

```python
class NameIterator:
    def __init__(self, names):
        self.names = names
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.names):
            result = self.names[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

class NamesCollection:
    def __init__(self):
        self.names = []

    def add_name(self, name):
        self.names.append(name)

    def create_iterator(self):
        return NameIterator(self.names)

# Uso del iterador
names_collection = NamesCollection()
names_collection.add_name("Alice")
names_collection.add_name("Bob")
names_collection.add_name("Charlie")

iterator = names_collection.create_iterator()

for name in iterator:
    print(name)
```

Ejemplo con Java:

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class MyIterator<T> implements Iterator<T> {
    private List<T> data;
    private int index = 0;

    public MyIterator(List<T> data) {
        this.data = data;
    }

    @Override
    public boolean hasNext() {
        return index < data.size();
    }

    @Override
    public T next() {
        if (hasNext()) {
            T result = data.get(index);
            index++;
            return result;
        } else {
            throw new IndexOutOfBoundsException("No hay más elementos.");
        }
    }
}

class MyCollection<T> implements Iterable<T> {
    private List<T> data = new ArrayList<>();

    public void addItem(T item) {
        data.add(item);
    }

    @Override
    public Iterator<T> iterator() {
        return new MyIterator<>(data);
    }
}

public class Main {
    public static void main(String[] args) {
        MyCollection<String> myCollection = new MyCollection<>();
        myCollection.addItem("Item 1");
        myCollection.addItem("Item 2");
        myCollection.addItem("Item 3");

        for (String item : myCollection) {
            System.out.println(item);
        }
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno 



Los elementos claves son con su definicion en los ejemplos seria:



# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/iterator)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/iterator/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/iterator)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/iterator/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/iterator-pattern/)
