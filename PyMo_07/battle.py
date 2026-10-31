from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print(
        "Testing factory",
        creature.describe(),
        creature.attack(),
        evolved_creature.describe(),
        evolved_creature.attack(),
        "",
        sep="\n",
    )


def battle(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print(
        "Testing battle",
        creature_a.describe(),
        " vs.",
        creature_b.describe(),
        " fight!",
        creature_a.attack(),
        creature_b.attack(),
        "",
        sep="\n",
    )


def main():
    flm_fac = FlameFactory()
    aqua_fac = AquaFactory()

    test_factory(flm_fac)
    test_factory(aqua_fac)
    battle(flm_fac, aqua_fac)


if __name__ == "__main__":
    main()
