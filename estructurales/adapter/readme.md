# ***Definicion***
El patrón de diseño Adapter, también conocido como el patrón Wrapper, es un patrón estructural que permite que dos interfaces incompatibles trabajen juntas. Actúa como un intermediario que traduce una interfaz en términos que el cliente espera. En resumen, el Adapter adapta una clase existente a una interfaz que el cliente necesita.

Características clave del patrón Adapter:

1. **Objetivo**: Facilitar la colaboración entre clases o sistemas con interfaces diferentes.
2. **Funcionamiento**: Se crea una clase adaptadora que "envuelve" o "adapta" un objeto existente, proporcionando una interfaz que es compatible con la que el cliente espera.
3. **Tipos de Adapter**:
   - **Adapter de objetos**: Utiliza composición para incluir el objeto adaptado como un miembro de la clase adaptadora.
   - **Adapter de clases**: Utiliza herencia para adaptar la clase existente al cliente.
4. **Ventajas**:
   - Reutiliza clases existentes con interfaces incompatibles.
   - Permite la interoperabilidad entre componentes con diferentes interfaces.
   - Introduce menos cambios en el código existente que si se modificara directamente.
5. **Desventajas**:
   - Puede aumentar la complejidad al agregar una capa adicional de indirección.
   - En casos complejos, puede llevar a una mayor cantidad de clases en el diseño.

En resumen, el patrón de diseño Adapter es una solución que permite que dos interfaces incompatibles colaboren. Actúa como un intermediario que adapta una interfaz existente a una nueva interfaz que el cliente espera. Esto facilita la reutilización de clases y la interoperabilidad entre componentes con interfaces diferentes sin modificar el código existente de manera significativa. En esencia, el Adapter ayuda a que clases o sistemas con diferencias de interfaz trabajen juntos sin problemas.


# ***Ejemplos***

Ejemplo con Python:

```python
class MusicPlayer:
    def play_music(self, song):
        pass  # Lógica para reproducir música

class NewMusicLibrary:
    def play_song(self, track):
        pass  # Lógica para reproducir canción

class MusicLibraryAdapter(MusicPlayer):
    def __init__(self, new_library):
        self.new_library = new_library

    def play_music(self, song):
        self.new_library.play_song(song)

# Uso del Adapter
old_player = MusicPlayer()
new_library = NewMusicLibrary()
adapter = MusicLibraryAdapter(new_library)

old_player.play_music("Old Song")
adapter.play_music("New Song")
```

Ejemplo con Java:

```java
interface ImageProcessor {
    void process_image(String image);
}

class ActualImageProcessor implements ImageProcessor {
    public void process_image(String image) {
        // Lógica para procesar la imagen
    }
}

class NewImageLibrary {
    public void process_new_image(String image) {
        // Lógica para procesar la imagen con la biblioteca nueva
    }
}

class ImageLibraryAdapter implements ImageProcessor {
    private NewImageLibrary newLibrary;

    public ImageLibraryAdapter(NewImageLibrary newLibrary) {
        this.newLibrary = newLibrary;
    }

    public void process_image(String image) {
        newLibrary.process_new_image(image);
    }
}

// Uso del Adapter
ImageProcessor processor = new ActualImageProcessor();
NewImageLibrary newLibrary = new NewImageLibrary();
ImageProcessor adapter = new ImageLibraryAdapter(newLibrary);

processor.process_image("Image1.jpg");
adapter.process_image("Image2.jpg");
```

# ***Conclusion***
En conclusion el patron de diseno Adapter, es una clase que permite adaptar
los nuevos metodos de otra clase nueva, con la de una ya existente.

Por ejemplo si hay una clase de una api con un metodo llamado `get` y se crea
una nueva clase con un metodo llamado `post`, el adapter permite a traves de
la interfaz de creacion de la primer clase recibir los parametros habituales y
enviarlos al nuevo metodo de la nueva clase que debe ser pasada por parametro
al instanciar el adapter

# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/adapter)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/adapter/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/adapter)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/adapter/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/adapter-pattern/)