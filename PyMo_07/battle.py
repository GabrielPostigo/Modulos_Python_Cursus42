from ex0 import FlameFactory, AquaFactory


def main():

    flm_fac = FlameFactory()
    aqua_fac = AquaFactory()

    flm_cre = flm_fac.create_base()
    flm_cre_ev = flm_fac.create_evolved()

    aqua_cre = aqua_fac.create_base()
    aqua_cre_ev = aqua_fac.create_evolved()

    print(
        "Testing factory",
        flm_cre.describe(),
        flm_cre.attack(),
        flm_cre_ev.describe(),
        flm_cre_ev.attack(),
        "", sep="\n"
        )
    print(
        "Testing factory",
        aqua_cre.describe(),
        aqua_cre.attack(),
        aqua_cre_ev.describe(),
        aqua_cre_ev.attack(),
        "", sep="\n"
        )
    print(
        "Testing battle",
        flm_cre.describe(),
        " vs.",
        aqua_cre.describe(),
        " fight!",
        flm_cre.attack(),
        aqua_cre.attack(),
        "", sep="\n"
        )


if __name__ == "__main__":
    main()
