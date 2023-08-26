# ***Definicion***
El patrón de diseño "Singleton" es un patrón creacional que asegura que una clase tenga una única instancia y proporciona un punto global para acceder a esa instancia desde cualquier parte del programa. Esto se logra restringiendo la creación de instancias de la clase a una sola instancia y controlando el acceso a esta instancia única.

Elementos clave del patrón "Singleton":

1. **Constructor Privado:** La clase Singleton tiene un constructor privado, lo que significa que no se puede crear instancias de la clase directamente desde fuera de la clase.

2. **Instancia Única:** La clase mantiene una instancia privada y estática de sí misma. Esta instancia es la única que existe durante toda la vida del programa.

3. **Método Estático de Acceso:** Se proporciona un método público y estático (como `getInstance()`) que devuelve la única instancia existente. Si la instancia aún no se ha creado, se crea la primera vez que se llama a este método, y las llamadas subsiguientes devuelven la misma instancia creada previamente.

El patrón "Singleton" es útil en situaciones donde se requiere una única instancia compartida de una clase. Puede ser útil para controlar el acceso a recursos compartidos, gestionar configuraciones globales, crear objetos costosos en términos de recursos o implementar registros.

Es importante tener en cuenta que el patrón Singleton puede introducir problemas de concurrencia si se utiliza en un entorno multihilo sin una implementación adecuada. Para abordar este problema, se pueden aplicar técnicas como el uso de bloqueos, el uso de inicialización en línea o el uso de la inicialización perezosa con doble verificación.

En resumen, el patrón "Singleton" asegura que una clase tenga una única instancia y proporciona un acceso global a esa instancia única, lo que puede ser útil para controlar recursos compartidos y manejar configuraciones globales de manera centralizada.


# ***Ejemplos***

Ejemplo con Python:

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Cliente
instance1 = Singleton()
instance2 = Singleton()

print(instance1 == instance2)  # Salida: True (ambas variables apuntan a la misma instancia)
```

Ejemplo con Java:

```java
public class Singleton {
    private static Singleton instance;

    private Singleton() {
        // Constructor privado para evitar instanciación directa
    }

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}

public class Main {
    public static void main(String[] args) {
        Singleton instance1 = Singleton.getInstance();
        Singleton instance2 = Singleton.getInstance();

        System.out.println(instance1 == instance2); // Salida: true (ambas referencias apuntan a la misma instancia)
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno Singleton permite validar si ya se ha
creado una instancia de la clase en concreto, en caso que sea correcta esta
afirmacion se devolvera la instancia creada de lo contrario se creara una
nueva que sera la que se devolvera para las proximas instanciaciones.

# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/singleton)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/singleton/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/singleton)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/singleton/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/singleton-design-pattern/)