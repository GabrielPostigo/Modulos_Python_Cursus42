import alchemy


def main() -> None:
    print("=== Distillation 1  ===")
    print("Using: 'import alchemy'structure to access potion")
    print("Testing strength_potion: ", end="")
    print(alchemy.strength_potion())
    print("Testing heal alias: ", end="")
    print(alchemy.heal())
    print()


if __name__ == "__main__":
    main()
