class GameOver(Exception):
    _value: str
    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        return self._value
