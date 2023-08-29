# ***Definicion***

Los patrones de diseño creacionales son un conjunto de soluciones comunes para problemas relacionados con la creación de objetos en la programación orientada a objetos. Estos patrones proporcionan enfoques estandarizados para crear instancias de clases de manera flexible y reutilizable. Los patrones creacionales se utilizan para controlar cómo se crean y se instancian los objetos, lo que puede ser útil para manejar la complejidad de la creación de objetos y garantizar la flexibilidad y eficiencia en el diseño de software.

En términos simples, los patrones de diseño creacionales son como recetas o plantillas que te ayudan a crear objetos de manera organizada y estructurada, abordando situaciones comunes en la creación de objetos.

Hay varios patrones de diseño creacionales, incluyendo:

1. **Singleton:**
   El patrón Singleton asegura que una clase tenga solo una única instancia y proporciona un punto global para acceder a esa instancia. Es útil cuando se necesita una única instancia compartida en todo el programa, como configuraciones globales o recursos compartidos.

2. **Factory Method:**
   El patrón Factory Method define una interfaz para crear objetos en una superclase, pero permite a las subclases decidir qué clase concreta instanciar. Esto proporciona flexibilidad al crear objetos y permite que las subclases ajusten la lógica de creación.

3. **Abstract Factory:**
   El patrón Abstract Factory proporciona una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas. Permite crear objetos que sigan una cierta temática o estilo y garantiza que los objetos creados sean coherentes entre sí.

4. **Builder:**
   El patrón Builder permite la construcción paso a paso de objetos complejos. Se utiliza cuando un objeto tiene muchos componentes y configuraciones, permitiendo crear diferentes tipos de objetos utilizando los mismos pasos de construcción.

5. **Prototype:**
   El patrón Prototype implica la clonación de objetos para crear nuevos objetos sin tener que crear una clase desde cero. Se utiliza para crear copias de objetos existentes con algunas diferencias mínimas, lo que es útil cuando se requieren múltiples objetos similares.

En resumen, los patrones de diseño creacionales ofrecen enfoques estructurados y estandarizados para resolver problemas relacionados con la creación de objetos. Cada patrón aborda diferentes aspectos de la creación de objetos, como la reutilización, la flexibilidad, la encapsulación y la consistencia, lo que contribuye a un diseño de software más organizado y eficiente.
