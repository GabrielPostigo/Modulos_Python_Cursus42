from ex0 import Creature
from .capabilities import HealCapability, TransformCapability


# == Healing Creature ==
class Sproutling(HealCapability, Creature):
    def __init__(self,
                 name="Sproutling",
                 type_="Grass"):
        self._name = name
        self._type = type_

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def describe(self) -> str:
        return super().describe()

    def heal(self, target: str = "itself") -> str:
        return f"{self._name} heals {target} for a small amount"


class Bloomelle(HealCapability, Creature):
    def __init__(self, name="Bloomelle", type_="Grass/Fairy"):
        self._name = name
        self._type = type_

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def describe(self) -> str:
        return super().describe()

    def heal(self, target: str = "itself") -> str:
        return f"{self._name} heals {target} for a large amount"


# == Transform Creature ==
class Shiftling(TransformCapability, Creature):
    def __init__(self, name="Shiftling", type_="Normal"):
        self._name = name
        self._type = type_
        self.state = False

    def attack(self) -> str:
        if self.state:
            return f"{self._name} performs a boosted strike!"
        else:
            return f"{self._name} attacks normally"

    def describe(self) -> str:
        return super().describe()

    def transform(self) -> str:
        self.state = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self.state = False
        return f"{self._name} returns to normal"


class Morphagon(TransformCapability, Creature):
    def __init__(self, name="Morphagon", type_="Normal/Dragon"):
        self._name = name
        self._type = type_
        self.state = False

    def attack(self) -> str:
        if self.state:
            return f"{self._name} unleashes a devastating morph strike!"
        else:
            return f"{self._name} attacks normally"

    def describe(self) -> str:
        return super().describe()

    def transform(self) -> str:
        self.state = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.state = False
        return f"{self._name} stabilizes its form."