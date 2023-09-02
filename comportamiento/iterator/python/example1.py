# iterator
# aggregate (collection)
""" En python no es necesario implementar estas interfaces ya que en
existen dos metodos reservados para esto que son `__iter__` y `__next__`
"""

# concrete iterator
class UsersIDIterator:
    _data: list[str]
    _index_user: int

    def __init__(self, data: list[str]) -> None:
        self._data = data
        self._index_user = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index_user >= len(self._data):
            raise StopIteration()
        actual_data = self._data[self._index_user]
        self._index_user += 1
        new_value: str = "user" + '_' + actual_data + '_' +str(self._index_user)
        return new_value.lower()

# concrete aggregate (collection)
class UsersCollection:

    def __init__(self) -> None:
        self._data: list[str] = []
    
    def add(self, name: str):
        self._data.append(name)
    
    def create_iterator(self) -> UsersIDIterator:
        return UsersIDIterator(self._data)


def main():
    users_collection = UsersCollection()
    users_collection.add("Angel")
    users_collection.add("Ramon")
    users_collection.add("Abigail")

    iterator: UsersIDIterator = users_collection.create_iterator()

    for i in iterator:
        print(i)

main()
