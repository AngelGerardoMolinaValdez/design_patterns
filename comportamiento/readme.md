# ***Definicion***
Los patrones de diseño de comportamiento son un conjunto de soluciones probadas y estandarizadas para problemas comunes relacionados con la interacción y la comunicación entre objetos en un sistema de software. Estos patrones se centran en cómo los objetos colaboran y cómo se manejan las relaciones y responsabilidades entre ellos para lograr un comportamiento deseado.

En esencia, los patrones de diseño de comportamiento proporcionan pautas y estructuras para:

1. Definir interacciones efectivas entre objetos.
2. Controlar el flujo de ejecución y la coordinación entre objetos.
3. Separar las responsabilidades entre los componentes del sistema.
4. Hacer que el sistema sea más flexible y adaptable a cambios futuros.

Los patrones de diseño de comportamiento abordan problemas relacionados con eventos, comunicación, manejo de estados, ejecución secuencial y otros aspectos de cómo los objetos trabajan juntos en un sistema.

Aquí hay una descripción de algunos patrones de diseño de comportamiento comunes:

1. **Patrón Strategy (Estrategia):** Permite definir una familia de algoritmos intercambiables y encapsular cada uno como una clase separada. Esto permite cambiar el algoritmo utilizado en tiempo de ejecución sin alterar el cliente que lo utiliza.

2. **Patrón Observer (Observador):** Define una relación uno a muchos entre objetos, de manera que cuando un objeto cambia de estado, todos sus observadores son notificados y actualizados automáticamente.

3. **Patrón Command (Comando):** Encapsula una solicitud como un objeto, lo que permite parametrizar a los clientes con diferentes solicitudes y controlar el registro de comandos, la inversión de comandos y la ejecución diferida.

4. **Patrón Template Method (Método de Plantilla):** Define el esqueleto de un algoritmo en una clase base, pero permite que las subclases proporcionen implementaciones concretas para ciertas etapas del algoritmo.

5. **Patrón Iterator (Iterador):** Proporciona una forma de acceder secuencialmente a los elementos de una colección sin exponer su estructura interna.

6. **Patrón Chain of Responsibility (Cadena de Responsabilidad):** Permite construir una cadena de objetos que pueden manejar solicitudes secuencialmente. La solicitud se pasa a lo largo de la cadena hasta que un objeto la maneja o se alcanza el final de la cadena.

7. **Patrón Interpreter (Intérprete):** Define una gramática y proporciona una forma de evaluar sentencias en el lenguaje definido. Se utiliza para crear un intérprete para una lengua o expresión.

8. **Patrón Mediator (Mediador):** Define un objeto que coordina las interacciones entre objetos separados, evitando que los objetos se comuniquen directamente entre sí.

9. **Patrón Memento (Memento):** Permite capturar y restaurar el estado interno de un objeto sin revelar los detalles de su implementación.

10. **Patrón Visitor (Visitante):** Permite agregar funcionalidad a clases individuales sin modificar su estructura. Se logra definiendo operaciones externas (visitantes) que actúan sobre las clases sin afectarlas directamente.

En resumen, los patrones de diseño de comportamiento son herramientas poderosas que proporcionan soluciones estandarizadas para desafíos comunes en la colaboración y comunicación de objetos en sistemas de software. Estos patrones ayudan a mejorar la estructura, la flexibilidad y la mantenibilidad del código.
