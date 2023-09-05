from typing import Any

# memento
class BackUp:
    _value: Any

    def __init__(self, value: Any) -> None:
        self._value = value
    
    def get_backup(self):
        return self._value

# originator
class WindowsLicense:
    _version: str = None

    def update_to(self, version: str):
        self._version = version
    
    def backup(self):
        return BackUp(self._version)

    def restore(self, backup: BackUp):
        self._version: str = backup.get_backup()
    
    def get_version(self):
        return self._version

# caretaker
class WindowsManager:
    _licences: list[BackUp] = []

    def add_backup(self, license: BackUp):
        self._licences.append(license)

    def get_backup(self, index: int):
        return self._licences[index]

def main():
    manager = WindowsManager()
    my_license = WindowsLicense()

    my_license.update_to("Windows 10")
    backup = my_license.backup()
    manager.add_backup(backup)
    print(f"Ahora mi version es: {my_license.get_version()}")

    my_license.update_to("Windows 11")
    backup = my_license.backup()
    manager.add_backup(backup)
    print(f"Ahora mi version es: {my_license.get_version()}")

    my_license.restore(manager.get_backup(0))
    print(f"Mi primer licencia fue: {my_license.get_version()}")

main()
