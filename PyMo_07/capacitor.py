from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main():
    h_fac = HealingCreatureFactory()
    t_fac = TransformCreatureFactory()

    spro = h_fac.create_base()
    bloom = h_fac.create_evolved()

    print("Testing Creature with healing capability \n base:")
    spro.describe()
    spro.attack()
    spro.heal("itself")
    print("evolved:")
    bloom.describe()
    bloom.attack()
    bloom.heal("itself and others")
    print()

    shift = t_fac.create_base()
    morp = t_fac.create_evolved()

    print("Testing Creature with transform capability \n base:")
    shift.describe()
    shift.attack()
    shift.transform()
    shift.attack()
    shift.revert()
    print("evolved:")
    morp.describe()
    morp.attack()
    morp.transform()
    morp.attack()
    morp.revert()


if __name__ == "__main__":
    main()
