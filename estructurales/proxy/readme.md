# ***Definicion***
El patrón de diseño "Proxy" es un patrón estructural que actúa como un intermediario que controla el acceso a un objeto real. Proporciona una capa adicional entre el cliente y el objeto real para controlar cómo y cuándo se accede al objeto real, además de permitir agregar funcionalidades adicionales.

Elementos clave del patrón Proxy:

1. **Sujeto:** Es la interfaz o clase abstracta que define los métodos que el proxy y el objeto real deben implementar. Define las operaciones que el cliente puede utilizar.

2. **Proxy:** Es la clase que actúa como un intermediario entre el cliente y el objeto real. Implementa la misma interfaz que el sujeto y contiene una referencia al objeto real. El proxy puede controlar el acceso, realizar verificaciones o agregar funcionalidades adicionales antes o después de acceder al objeto real.

3. **Sujeto Real:** Es la clase que representa el objeto real que el proxy protege o controla. Implementa la interfaz del sujeto y realiza las operaciones reales.

El patrón Proxy es útil en situaciones donde se necesita controlar el acceso a un objeto o agregar funcionalidades adicionales sin afectar directamente al objeto real. Esto puede ser útil para implementar cachés, autenticación, control de acceso, contabilidad, entre otros.

En resumen, el patrón Proxy permite agregar una capa de control y funcionalidad adicional entre el cliente y el objeto real. Esto puede mejorar la seguridad, la eficiencia y la flexibilidad de la interacción con el objeto real.

# ***Ejemplos***

Ejemplo con Python:

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        print(f"Reading file: {self.filename}")

class FileManagerProxy:
    def __init__(self, filename):
        self._file_manager = None
        self.filename = filename

    def read(self):
        if self._file_manager is None:
            self._file_manager = FileManager(self.filename)
        print("Proxy is preparing to read the file")
        self._file_manager.read()

proxy = FileManagerProxy("my_document.txt")
proxy.read()
```

Ejemplo con Java:

```java
interface Video {
    void play();
}

class RealVideo implements Video {
    private String filename;

    public RealVideo(String filename) {
        this.filename = filename;
        loadFromDisk();
    }

    private void loadFromDisk() {
        System.out.println("Loading video: " + filename);
    }

    public void play() {
        System.out.println("Playing video: " + filename);
    }
}

class VideoProxy implements Video {
    private RealVideo realVideo;
    private String filename;

    public VideoProxy(String filename) {
        this.filename = filename;
    }

    public void play() {
        if (realVideo == null) {
            realVideo = new RealVideo(filename);
        }
        System.out.println("Proxy is preparing to play the video");
        realVideo.play();
    }
}

public class Main {
    public static void main(String[] args) {
        VideoProxy videoProxy = new VideoProxy("my_video.mp4");
        videoProxy.play();
    }
}
```

# ***Conclusion***
En conclusion, el patron de diseno 



Los elementos claves son con su definicion en los ejemplos seria:



# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/proxy)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/proxy/python/example)
- [SourceMaking](https://sourcemaking.com/design_patterns/proxy)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/proxy/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/proxy-pattern/)