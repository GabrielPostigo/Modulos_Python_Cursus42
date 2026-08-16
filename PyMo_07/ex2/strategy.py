from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, cre: Creature) -> str:
        '''
        method will be called by the tournament script
        '''
        pass

    @abstractmethod
    def is_valid(self, cre: Creature) -> bool:
        '''
        method returns a bool indicating that a Creature is suitable
        for the strategy
        '''
        pass


class NormalStrategy(BattleStrategy):
    def act(self, cre: Creature) -> str:
        return cre.attack()

    def is_valid(self, cre: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, cre: Creature):
        if isinstance(cre, TransformCapability):
            return True
        else:
            return False

    def act(self, cre):
        if not self.is_valid(cre):
            raise ValueError(
                f"Invalid creature '{cre._name}' for this Aggressive Strategy"
            )
        print(cre.transform(), cre.attack(),
              cre.revert(), sep="\n")  # type: ignore[attr-defined]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, cre: Creature):
        if isinstance(cre, HealCapability):
            return True
        else:
            return False

    def act(self, cre):
        if not self.is_valid(cre):
            raise ValueError(
                f"Invalid creature '{cre._name}' for this Defensive Strategy")
        print(cre.attack(), cre.heal(), sep="\n")  # type: ignore[attr-defined]
