from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy
from ex2 import InvalidCreatureError


def battle(lis: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(lis)} opponents involved")

    for op in range(len(lis)):
        for op2 in range(op + 1, len(lis)):
            factory_a, strategy_a = lis[op]
            factory_b, strategy_b = lis[op2]

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print()
            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidCreatureError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:

    ''' Strategies'''
    n_s = NormalStrategy()
    a_s = AggressiveStrategy()
    d_s = DefensiveStrategy()

    # Tournament 0: (Flameling+Normal vs Healing+Defensive) - basic
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), n_s),
        (HealingCreatureFactory(), d_s),
    ])
    print()

    # Tournament 1: (Flameling+Aggressive vs Healing+Defensive) - Error
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), a_s),
        (HealingCreatureFactory(), d_s),
    ])
    print()

    # Tournament 2 - multiple
    # (Aquabub+Normal, Healing+Defensive, Transform+Aggressive)
    print("Tournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )
    battle([
        (AquaFactory(), n_s),
        (HealingCreatureFactory(), d_s),
        (TransformCreatureFactory(), a_s),
    ])


if __name__ == "__main__":
    main()
