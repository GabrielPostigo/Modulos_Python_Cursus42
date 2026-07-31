import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0  ===")
    print("Using grimoire module directly")
    print("Testing record light spell: ", end="")
    print(alchemy.grimoire.light_validator())
    print()


if __name__ == "__main__":
    main()
