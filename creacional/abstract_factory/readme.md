# ***Definicion***

El patrón de diseño "Abstract Factory" (Fábrica Abstracta) es un patrón creacional que proporciona una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas. En otras palabras, permite crear objetos que están interconectados o dependen entre sí, pero de una manera que aisla el código cliente de los detalles específicos de implementación.

El patrón "Abstract Factory" se compone de las siguientes partes principales:

- *AbstractFactory*: Esta es la interfaz que declara los métodos para crear los diferentes tipos de objetos. Define un conjunto de métodos abstractos, cada uno para crear un tipo específico de objeto.

- *ConcreteFactory*: Estas son las implementaciones concretas de la interfaz AbstractFactory. Cada ConcreteFactory produce una familia específica de objetos relacionados.

- *AbstractProduct*: Esta es la interfaz que declara los métodos que los productos concretos deben implementar.

- *ConcreteProduct*: Estos son los objetos concretos que se crean a través de las fábricas concretas. Implementan la interfaz AbstractProduct.

- *Client*: Es el código que utiliza las interfaces AbstractFactory y AbstractProduct para crear y trabajar con objetos. El cliente no necesita conocer las clases concretas involucradas.

En términos simples, el patrón de diseño "Abstract Factory" es como una fábrica de fábricas. Proporciona una manera de crear grupos de objetos relacionados sin preocuparse por las clases exactas de esos objetos. Ayuda a organizar la creación de objetos de manera coherente y aislada.


# ***Ejemplos***

Ejemplo con Python:

```python
# AbstractFactory
class GUIFactory:
    def create_button(self):
        pass

# ConcreteFactories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

# AbstractProduct
class Button:
    def paint(self):
        pass

# ConcreteProducts
class WindowsButton(Button):
    def paint(self):
        return "Windows button"

class MacOSButton(Button):
    def paint(self):
        return "MacOS button"

# Client
def create_ui(factory):
    button = factory.create_button()
    return button.paint()

# Usage
windows_ui = create_ui(WindowsFactory())
macos_ui = create_ui(MacOSFactory())

print(windows_ui)  # Output: Windows button
print(macos_ui)    # Output: MacOS button
```

Ejemplo con Java:

```java
// AbstractFactory
interface GUIFactory {
    Button createButton();
}

// ConcreteFactories
class WindowsFactory implements GUIFactory {
    public Button createButton() {
        return new WindowsButton();
    }
}

class MacOSFactory implements GUIFactory {
    public Button createButton() {
        return new MacOSButton();
    }
}

// AbstractProduct
interface Button {
    void paint();
}

// ConcreteProducts
class WindowsButton implements Button {
    public void paint() {
        System.out.println("Windows button");
    }
}

class MacOSButton implements Button {
    public void paint() {
        System.out.println("MacOS button");
    }
}

// Client
public class Client {
    public static void createUI(GUIFactory factory) {
        Button button = factory.createButton();
        button.paint();
    }

    public static void main(String[] args) {
        createUI(new WindowsFactory()); // Output: Windows button
        createUI(new MacOSFactory());   // Output: MacOS button
    }
}
```

# ***Conclusion***

En conclusion el patron de diseno abstract factory es similar al patron de 
diseno factory method con la diferencia que, en factory method solo debemos
especificar un metodo de creacion de objetos, mientras que en abstract factory
podemos especificar multiples metodos de creacion de objetos.

## ***Cual es la diferencia entre "Factory Method" y "Abstract Factory"?***

La diferencia esta en que Abtract Factory permite multiples metodos de creacion
en las clases que crean los objetos, mientras que el Factory Method solo permite
tener un solo metodo de creacion, por ende se dice lo siguiente:

"El patrón "Factory Method" se centra en crear objetos de una familia particular, mientras que el patrón "Abstract Factory" se enfoca en crear familias enteras de objetos relacionados. En el patrón "Factory Method" cada subclase del Creator tiene un único Factory Method para crear un tipo específico de producto. En el patrón "Abstract Factory", cada familia de productos tiene su propio conjunto de Factory Methods en la Abstract Factory."

Ejemplo en python:

***Factory Method***

```python
# Product
class Document:
    def create_page(self):
        pass

# Concrete Products
class Spreadsheet(Document):
    def create_page(self):
        return SpreadsheetPage()

class Presentation(Document):
    def create_page(self):
        return PresentationPage()

# Creator (Factory Method)
class DocumentCreator:
    def create_document(self):
        pass

# Concrete Creators
class SpreadsheetCreator(DocumentCreator):
    def create_document(self):
        return Spreadsheet()

class PresentationCreator(DocumentCreator):
    def create_document(self):
        return Presentation()

# Client
def use_document(creator):
    document = creator.create_document()
    page = document.create_page()
    return page.render()

# Usage
spreadsheet_result = use_document(SpreadsheetCreator())
presentation_result = use_document(PresentationCreator())

print(spreadsheet_result)  # Output: Rendering a spreadsheet page
print(presentation_result)  # Output: Rendering a presentation page
```

***Abstract Factory***

```python
# Abstract Factory
class PageFactory:
    def create_header(self):
        pass

    def create_body(self):
        pass

    def create_footer(self):
        pass

# Concrete Factories
class SpreadsheetPageFactory(PageFactory):
    def create_header(self):
        return SpreadsheetHeader()

    def create_body(self):
        return SpreadsheetBody()

    def create_footer(self):
        return SpreadsheetFooter()

class PresentationPageFactory(PageFactory):
    def create_header(self):
        return PresentationHeader()

    def create_body(self):
        return PresentationBody()

    def create_footer(self):
        return PresentationFooter()

# Abstract Products
class Header:
    def render(self):
        pass

class Body:
    def render(self):
        pass

class Footer:
    def render(self):
        pass

# Concrete Products
class SpreadsheetHeader(Header):
    def render(self):
        return "Rendering a spreadsheet header"

class PresentationHeader(Header):
    def render(self):
        return "Rendering a presentation header"

# ... (similar implementations for Body and Footer)

# Client
def use_page_factory(factory):
    header = factory.create_header()
    body = factory.create_body()
    footer = factory.create_footer()
    return f"{header.render()}, {body.render()}, {footer.render()}"

# Usage
spreadsheet_page_result = use_page_factory(SpreadsheetPageFactory())
presentation_page_result = use_page_factory(PresentationPageFactory())

print(spreadsheet_page_result)  # Output: Rendering a spreadsheet header, Rendering a spreadsheet body, Rendering a spreadsheet footer
print(presentation_page_result)  # Output: Rendering a presentation header, Rendering a presentation body, Rendering a presentation footer
```

***Diferencias Y Similitudes***

1. **Objetivo:** El patrón "Factory Method" se centra en crear objetos de una familia particular, mientras que el patrón "Abstract Factory" se enfoca en crear familias enteras de objetos relacionados.

2. **Factory Method vs. Abstract Factory:** En el patrón "Factory Method", cada subclase del Creator tiene un único Factory Method para crear un tipo específico de producto. En el patrón "Abstract Factory", cada familia de productos tiene su propio conjunto de Factory Methods en la Abstract Factory.

3. **Flexibilidad:** El patrón "Factory Method" permite cambiar el tipo de producto creado por las subclases. El patrón "Abstract Factory" permite cambiar toda la familia de productos reemplazando las fábricas concretas.

4. **Relación:** El patrón "Abstract Factory" a menudo utiliza el patrón "Factory Method" para crear productos individuales dentro de cada familia.

En el ejemplo, puedes ver cómo el patrón "Factory Method" se usa para crear diferentes tipos de documentos, mientras que el patrón "Abstract Factory" se usa para crear diferentes partes (encabezado, cuerpo, pie de página) de los documentos.


# ***Referencias***

- [Refactoring Guru](https://refactoring.guru/es/design-patterns/abstract-factory/python/example)
- [Refactoring Guru(Example)](https://refactoring.guru/es/design-patterns/abstract-factory)
- [SourceMaking](https://sourcemaking.com/design_patterns/abstract_factory)
- [SourceMaking(Example)](https://sourcemaking.com/design_patterns/abstract_factory/python/1)
- [Gang of Four Design Patterns](https://springframework.guru/gang-of-four-design-patterns/abstract-factory-design-pattern/)