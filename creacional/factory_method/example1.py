from abc import ABC, abstractmethod

class AbstractEmployeeFactory(ABC):
    """ Esta clase sera la encargada de definir los metodos para las
    fabricas concretas que crearan los objetos denominados "Productos"
    """
    @abstractmethod
    def create_employee(self):
        """los metodos abstractos se definen vacios
        ya que la funcionalidad debe ser otorgada al implementarlos
        en las clases hijas
        """
        pass


class ConcreteEmployeeFactoryFoo(AbstractEmployeeFactory):
    """En esta clase se implementan los metodos abstractos de 
    AbstractEmployeeFactory y estos mismos son los que retornaran
    las instancias de los objetos ConcreteEmployee

    Args:
        AbstractEmployeeFactory (object): Clase abstracta
    """
    def create_employee(self):
        """Este es el metodo definido como abstracto
        en la clase AbstractEmployeeFactory, aqui se retornaran
        los objetos de cada empleado
        """
        return ConcreteEmployeeFoo()


class ConcreteEmployeeFactoryBar(AbstractEmployeeFactory):
    """En esta clase se implementan los metodos abstractos de 
    AbstractEmployeeFactory y estos mismos son los que retornaran
    las instancias de los objetos ConcreteEmployee

    Args:
        AbstractEmployeeFactory (object): Clase abstracta
    """
    def create_employee(self):
        """Este es el metodo definido como abstracto
        en la clase AbstractEmployeeFactory, aqui se retornaran
        los objetos de cada empleado
        """
        return ConcreteEmployeeBar()
    

class AbstractEmployee(ABC):
    """ Esta clase sera la encargada de crear la instancia de un ConcreteEmployee
    con el metodo abstracto create_employee
    """
    @abstractmethod
    def work(self):
        """los metodos abstractos se definen vacios
        ya que la funcionalidad debe ser otorgada al implementarlos
        en las clases hijas
        """
        pass

class ConcreteEmployeeFoo(AbstractEmployee):
    """En esta clase se implementan los metodos abstractos de 
    AbstractEmployee y estos mismos son los que cuentan con la funcionalidad
    Args:
        AbstractEmployee (object): Clase abstracta
    """
    def work(self):
        """Este es el metodo definido como abstracto
        en la clase AbstractEmployee, aqui se encuentra la funcionalidad
        """
        print("I work in Foo Star Up!!")


class ConcreteEmployeeBar(AbstractEmployee):
    """En esta clase se implementan los metodos abstractos de 
    AbstractEmployee y estos mismos son los que cuentan con la funcionalidad
    Args:
        AbstractEmployee (object): Clase abstracta
    """
    def work(self):
        """Este es el metodo definido como abstracto
        en la clase AbstractEmployee, aqui se encuentra la funcionalidad
        """
        print("I work in Bar Star Up!!")


def client_code(factories: object) -> None:
    """codigo cliente, aqui se define toda la logica sin incluir informacion
    sensible

    Args:
        factories (object): fabrica de objetos employee
    """
    for factory in factories:
        new_client = factory.create_employee()
        new_client.work()


client_code([ConcreteEmployeeFactoryBar(), ConcreteEmployeeFactoryFoo()])
