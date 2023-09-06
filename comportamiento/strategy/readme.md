# ***Definicion***

El patrón de diseño Strategy (Estrategia) es un patrón de diseño de comportamiento que se centra en definir una familia de algoritmos, encapsular cada uno de ellos y hacer que sean intercambiables. Esto permite que un cliente pueda elegir dinámicamente uno de esos algoritmos en tiempo de ejecución sin alterar el código que lo utiliza. El patrón Strategy promueve la flexibilidad y la reutilización del código al separar los algoritmos de su contexto.

Los elementos clave del patrón de diseño Strategy son los siguientes:

1. **Contexto (Context)**: Es el objeto que necesita realizar una tarea específica y que tiene una referencia a un objeto de estrategia. El contexto utiliza el objeto de estrategia para ejecutar la tarea.

2. **Estrategia (Strategy)**: Es una interfaz o clase abstracta que define un conjunto de métodos que representan los algoritmos o estrategias concretas. Cada estrategia concreta implementa esta interfaz o hereda de la clase abstracta y proporciona una implementación específica de los métodos definidos.

3. **Estrategias Concretas (Concrete Strategies)**: Son las clases que implementan la interfaz de estrategia. Cada estrategia concreta proporciona una implementación específica de los algoritmos que se pueden utilizar en el contexto.

En resumen, el patrón de diseño Strategy permite que un objeto pueda cambiar su comportamiento en tiempo de ejecución al seleccionar una estrategia concreta de un conjunto de estrategias intercambiables. Esto es útil cuando se tienen múltiples algoritmos que pueden ser aplicados a una tarea y se desea permitir que el cliente elija el algoritmo apropiado sin tener que modificar el código existente. El patrón Strategy promueve la modularidad, la flexibilidad y la facilidad de mantenimiento del código.

# ***Ejemplos***

Ejemplo con Python:

```python
# Interfaz de estrategia
class Filter:
    def apply(self, image):
        pass

# Filtros concretos
class GrayscaleFilter(Filter):
    def apply(self, image):
        # Aplicar filtro de escala de grises
        pass

class SepiaFilter(Filter):
    def apply(self, image):
        # Aplicar filtro sepia
        pass

# Contexto
class ImageProcessor:
    def __init__(self, filter_strategy):
        self.filter_strategy = filter_strategy

    def process_image(self, image):
        self.filter_strategy.apply(image)

# Uso del patrón Strategy
image = load_image("image.jpg")
processor = ImageProcessor(GrayscaleFilter())
processor.process_image(image)
```

Ejemplo con Java:

```java
// Interfaz de estrategia
interface PaymentStrategy {
    void pay(int amount);
}

// Estrategias de pago concretas
class CreditCardPayment implements PaymentStrategy {
    public void pay(int amount) {
        // Procesar el pago con tarjeta de crédito
    }
}

class PayPalPayment implements PaymentStrategy {
    public void pay(int amount) {
        // Procesar el pago con PayPal
    }
}

// Contexto
class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public void setPaymentStrategy(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void checkout(int totalAmount) {
        paymentStrategy.pay(totalAmount);
    }
}

// Uso del patrón Strategy
ShoppingCart cart = new ShoppingCart();
cart.setPaymentStrategy(new CreditCardPayment());
cart.checkout(100);
```

# ***Conclusion***
En conclusion, el patron de diseno *Strategy* es la relacion de una clase con la funcion de realizar una operacion (*context*) y multiples clases (*strategy*) con una funcion diferente, creando asi una familia de algoritmos que permiten ser intercambiales durante la ejecucion.

Los elementos claves son con su definicion en los ejemplos seria:

1. **Contexto (Context)**: Es la clase que necesita realizar una operacion

2. **Estrategia (Strategy)**: Es la interfaz que define los metodos para las diferentes estrategias que seran creadas para el programa

3. **Estrategias Concretas (Concrete Strategies)**: Clases que contiene la logica de cada una de las estrategias que seran implementadas en la clase *context*


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/strategy)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/strategy/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/strategy)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/strategy/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/strategy-pattern/)
