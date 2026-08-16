from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def main() -> None:
    t_fac = TransformCreatureFactory()
    h_fac = HealingCreatureFactory()

    n_s = NormalStrategy()
    a_s = AggressiveStrategy()
    d_s = DefensiveStrategy


if __name__ == "__main__":
    main()
