from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion: ", end="")
    print(strength_potion())
    print("Testing healing_potion: ", end="")
    print(healing_potion())
    print()


if __name__ == "__main__":
    main()
