# from typing import
from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_: str):
        self._name: str = name
        self._type: str = type_

    @abstractmethod
    def attack(self):
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type} Creature"


class Flameling(Creature):
    def __init__(self):
        self._name = "Flameling"
        self._type = "Fire"

    def attack(self) -> str:
        return f"{self._name} uses Ember!"

    def describe(self) -> str:
        return super().describe()


class Pyrodon(Creature):
    def __init__(self):
        self._name = "Pyrodon"
        self._type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"

    def describe(self) -> str:
        return super().describe()


class Aquabub(Creature):
    def __init__(self):
        self._name = "Aquabub"
        self._type = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"

    def describe(self) -> str:
        return super().describe()


class Torragon(Creature):
    def __init__(self):
        self._name = "Torragon"
        self._type = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"

    def describe(self) -> str:
        return super().describe()
