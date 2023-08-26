# ***Definicion***

Los patrones de diseño estructurales son como recetas reutilizables para resolver problemas comunes en la organización de clases y objetos en un programa de computadora. Son formas probadas y eficaces de diseñar y conectar partes de código para que funcionen juntas de manera más flexible y eficiente. Estos patrones te ayudan a construir software más ordenado y fácil de mantener al proporcionarte soluciones predefinidas para desafíos típicos en la estructura del código.

Algunos patrones son:

1. **Adaptador (Adapter)**: El patrón Adapter se utiliza para permitir que dos interfaces incompatibles trabajen juntas. Actúa como un intermediario que convierte la interfaz de una clase en otra interfaz que el cliente espera. Esto permite que objetos con interfaces diferentes colaboren sin necesidad de modificar sus códigos fuente.

2. **Puente (Bridge)**: El patrón Bridge separa la abstracción de su implementación, permitiendo que ambas evolucionen de manera independiente. En lugar de tener una única clase que combine ambas, se crean dos jerarquías de clases: una para la abstracción y otra para la implementación. Esto permite que se puedan combinar diferentes abstracciones con diferentes implementaciones de manera flexible.

3. **Composite**: El patrón Composite permite construir estructuras jerárquicas en forma de árbol, donde los objetos individuales y las composiciones se tratan de manera uniforme. La clave es que todos los elementos del árbol implementan la misma interfaz, lo que permite tratar a objetos individuales y sus agrupaciones de la misma manera.

4. **Decorador (Decorator)**: El patrón Decorator se utiliza para agregar funcionalidad adicional a objetos de manera dinámica, sin modificar su estructura básica. Se logra creando una serie de "capas" alrededor del objeto original, cada una de las cuales agrega características específicas.

5. **Fachada (Facade)**: El patrón Facade proporciona una interfaz simplificada para un conjunto de subsistemas más complejos. Actúa como un punto de entrada único para realizar operaciones en esos subsistemas, ocultando la complejidad subyacente y proporcionando una forma más fácil de interactuar con el sistema en su conjunto.

6. **Peso Ligero (Flyweight)**: El patrón Flyweight se utiliza para reducir la cantidad de objetos creados, especialmente cuando hay muchos objetos similares. Consiste en compartir objetos para minimizar el uso de memoria, almacenando datos compartidos por varios objetos en lugar de replicarlos en cada objeto.

7. **Proxy**: El patrón Proxy se utiliza para controlar el acceso a un objeto. Actúa como un intermediario que controla las llamadas al objeto real. Puede tener diferentes variantes, como el Proxy Virtual, que pospone la creación del objeto real hasta que sea necesario, o el Proxy de Protección, que verifica los permisos de acceso antes de permitir una operación en el objeto real.

En resumen, los patrones de diseño estructurales son soluciones reutilizables para organizar y componer clases y objetos en un sistema de software de manera más eficiente y flexible. Estos patrones se centran en cómo las clases y objetos interactúan y se agrupan para formar estructuras más grandes. Ayudan a simplificar la relación entre componentes y a reducir la complejidad del diseño general, mejorando la modularidad y reutilización del código.