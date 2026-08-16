from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main():
    h_fac = HealingCreatureFactory()
    t_fac = TransformCreatureFactory()

    spro = h_fac.create_base()
    bloom = h_fac.create_evolved()

    print("Testing Creature with healing capability \n base:")
    print(spro.describe(), spro.attack(), spro.heal("itself"), sep="\n")
    print("evolved:")
    print(bloom.describe(), bloom.attack(),
          bloom.heal("itself and others"), sep="\n")
    print()

    shift = t_fac.create_base()
    morp = t_fac.create_evolved()

    print("Testing Creature with transform capability \n base:")
    print(shift.describe(), shift.attack(),
          shift.transform(), shift.attack(),
          shift.revert(), sep="\n")
    print("evolved:")
    print(morp.describe(), morp.attack(),
          morp.transform(), morp.attack(),
          morp.revert(), sep="\n")


if __name__ == "__main__":
    main()
