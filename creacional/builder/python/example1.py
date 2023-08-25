from abc import ABC, abstractmethod

# product
class Quesadilla:
    def __init__(self) -> None:
        self.base = ""
        self.relleno = ""
        self.condimento = ""

    def describe(self):
        descripcion = f"""Se agrega la base {self.base}, posteriormente
        el relleno que sera {self.relleno} y por ultimo se anade el
        condimiento que es {self.condimento}"""
        return descripcion

# builder
class AbstractQuesadillaBuilder(ABC):
    @abstractmethod
    def add_base(self):
        pass
    
    @abstractmethod
    def add_relleno(self):
        pass

    @abstractmethod
    def add_condimento(self):
        pass

# concrete builder
class QuesadillaBuilder(AbstractQuesadillaBuilder):
    def __init__(self) -> None:
        self.quesadilla = Quesadilla()

    def add_base(self, base: str) -> None:
        self.quesadilla.base = base
    
    def add_relleno(self, relleno: str) -> None:
        self.quesadilla.relleno = relleno

    def add_condimento(self, condimento: str) -> None:
        self.quesadilla.condimento = condimento

    def build(self) -> Quesadilla:
        return self.quesadilla

# director
class QuesadillaMaker:
    def create_quesadilla(self, quesadilla_builder):
        quesadilla_builder.add_base("tortilla de harina")
        quesadilla_builder.add_relleno("quesillo")
        quesadilla_builder.add_condimento("salsa picante")
        return quesadilla_builder.build()

# client code
def cocina():
    quesadilla_builder = QuesadillaBuilder()
    director = QuesadillaMaker()
    quesadilla = director.create_quesadilla(quesadilla_builder)
    print(quesadilla.describe())

cocina()