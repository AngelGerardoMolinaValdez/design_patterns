from abc import ABC, abstractmethod

# Strategy
class TextStrategy(ABC):
    @abstractmethod
    def operation(self, text: str) -> str:
        pass

# concrete strategies
class UpperTextStrategy(TextStrategy):
    def operation(self, text: str) -> str:
        return text.upper()

class LowerTextStrategy(TextStrategy):
    def operation(self, text: str) -> str:
        return text.lower()

# context 
class TextTransformer:
    _strategy: TextStrategy = None

    def __init__(self, strategy: TextStrategy) -> None:
        self._strategy = strategy
    
    def strategy(self, text: str) -> str:
        return self._strategy.operation(text)

def main() -> None:
    lower_strategy = LowerTextStrategy()
    upper_strategy = UpperTextStrategy()

    text_transformer = TextTransformer(lower_strategy)
    print(text_transformer.strategy("UPPER TEXT"))

    text_transformer2 = TextTransformer(upper_strategy)
    print(text_transformer2.strategy("lower text"))

main()
