

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    try:
        print(dark_spell_record("KA", "BOOM"))
    except ImportError as e:
        print(e)
    print()


if __name__ == "__main__":
    main()
