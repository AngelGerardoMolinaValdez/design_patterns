# ***Definicion***

El patrón de diseño "Template Method" (Método Plantilla) es un patrón de diseño de comportamiento que define la estructura general de un algoritmo en una clase base, pero permite que las subclases implementen ciertos pasos específicos de ese algoritmo sin cambiar su estructura básica. En otras palabras, proporciona un esqueleto de algoritmo en una clase base, pero delega la implementación de partes específicas del algoritmo a las subclases. Esto promueve la reutilización del código y permite que las subclases personalicen ciertos aspectos del algoritmo según sea necesario.

Características clave del patrón Template Method:

1. **Clase Base Abstracta**: La clase base (a menudo abstracta) define el esqueleto del algoritmo general, incluyendo la secuencia de pasos y métodos abstractos (llamados "métodos primitivos") que las subclases deben implementar.

2. **Métodos Primitivos**: Los métodos abstractos dentro de la clase base representan las partes del algoritmo que deben ser implementadas por las subclases. Estos métodos son específicos para cada subclase y permiten la personalización del comportamiento.

3. **Método Template**: El método principal (llamado "método plantilla") en la clase base coordina la secuencia de llamadas a los métodos primitivos. Este método generalmente no se puede sobrescribir en las subclases y garantiza que el algoritmo general siga siendo consistente.

El patrón Template Method es útil en situaciones en las que se necesita compartir un flujo de trabajo común, pero se permiten variaciones en ciertas partes de ese flujo de trabajo. Al utilizar este patrón, se promueve la coherencia y se evita la duplicación de código, ya que el esqueleto del algoritmo está definido una vez en la clase base.

Un ejemplo común de este patrón se encuentra en la programación orientada a objetos, donde las subclases pueden proporcionar implementaciones específicas para métodos como `toString()` en Java o `__str__()` en Python, mientras que el código que utiliza estos métodos permanece invariable.

# ***Ejemplos***

Ejemplo con Python:

```python
class CakeRecipe:
    def prepare(self):
        self.mix_ingredients()
        self.bake()
        self.decorate()

    def mix_ingredients(self):
        print("Mezclar los ingredientes comunes")

    def bake(self):
        print("Hornear a una temperatura común")

    def decorate(self):
        pass  # Dejar la decoración específica para las subclases

class ChocolateCake(CakeRecipe):
    def decorate(self):
        print("Decorar con chocolate")

class StrawberryCake(CakeRecipe):
    def decorate(self):
        print("Decorar con fresas")

# Uso del patrón Template Method
chocolate_cake = ChocolateCake()
chocolate_cake.prepare()

strawberry_cake = StrawberryCake()
strawberry_cake.prepare()
```

Ejemplo con Java:

```java
abstract class AbstractClass {
    public final void templateMethod() {
        stepOne();
        stepTwo();
    }

    protected void stepOne() {
        System.out.println("Paso 1 (común a todas las subclases)");
    }

    protected abstract void stepTwo();
}

class ConcreteClassA extends AbstractClass {
    protected void stepTwo() {
        System.out.println("Paso 2 (específico para ConcreteClassA)");
    }
}

class ConcreteClassB extends AbstractClass {
    protected void stepTwo() {
        System.out.println("Paso 2 (específico para ConcreteClassB)");
    }
}

public class Main {
    public static void main(String[] args) {
        AbstractClass obj1 = new ConcreteClassA();
        obj1.templateMethod();

        AbstractClass obj2 = new ConcreteClassB();
        obj2.templateMethod();
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno *Template Method* es la implementacion de una clase abstracta con un algoritmo definido y un metodo abstracto (*metodo primitivo*) que permitira reutilizar codigo y aplicar logica propia dentro del mismo algoritmo pero con una referencia de la estructura creada.

Los elementos claves son con su definicion en los ejemplos seria:

1. **Clase Base Abstracta**: La clase abstracta que contiene la estructura del algoritmo. En los ejemplos son las clases `Coffee` y `CompanySystem`

2. **Métodos Primitivos**: Son los metodos abstractos que deben ser implementados dentro de las clases hijas para aplicar logica propia. En los ejemplos son los metodos `execute()` y `applyChanges()`

3. **Método Template**: Es el metodo principal de la clase abstracta (este metodo no es abstracto) que coordina y ejecuta todos los pasos del algoritmo, incluyendo la propia implementacion de las clases hijas.

# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/template-method)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/template-method/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/template_method)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/template_method/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/template-method-pattern/)
