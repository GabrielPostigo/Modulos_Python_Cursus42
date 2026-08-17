from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def battle(lis: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    cont = 0
    for op in lis:
        cont += 1
        for i in lis in range(cont, len(lis)):


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
