from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(lis: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    pass


def main() -> None:
    ''' Creature Factories '''
    f_fac = FlameFactory()
    a_fac = AquaFactory()
    t_fac = TransformCreatureFactory()
    h_fac = HealingCreatureFactory()

    ''' Strategies'''
    n_s = NormalStrategy()
    a_s = AggressiveStrategy()
    d_s = DefensiveStrategy


if __name__ == "__main__":
    main()
