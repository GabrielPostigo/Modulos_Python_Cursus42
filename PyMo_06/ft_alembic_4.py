import alchemy

'''
    The create_earth() function will not be exposed through the module
    interface and raise an exception when called (you can catch the exception
    or not, this is only for pedagogical purposes).
    A mypy error will also raise, again, on purpose
'''


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", end="")
    print(alchemy.create_air())
    print("Now show that not all functions can be reached")
    print(alchemy.create_earth())
    print()


if __name__ == "__main__":
    main()
