# from typing import
from abc import ABC, abstractmethod
import creature as cre


class CreatureFactory(ABC):
    @abstractmethod
    def create_base():
        pass

    @abstractmethod
    def create_evolved():
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> cre.Flameling:
        return cre.Flameling()

    def create_evolved(self) -> cre.Pyrodon:
        return cre.Pyrodon()


class AquaFactory(CreatureFactory):

    def create_base(self) -> cre.Aquabub:
        return cre.Aquabub()

    def create_evolved(self) -> cre.Torragon:
        return cre.Torragon()
