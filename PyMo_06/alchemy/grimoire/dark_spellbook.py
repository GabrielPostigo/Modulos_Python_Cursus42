from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:

    ingredients: list[str] = ["bats", "frogs", "arsenic", "eyeball"]

    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    '''
    A function dark_spell_record(spell_name: str, ingredients: str) that re-
    turns a string that indicates whether the spell is recorded or rejected.
    The decision comes from the validation function described below
    '''
    tested: str = validate_ingredients(ingredients)
    splited: list[str] = tested.split()
    conf: bool = False

    for word in splited:
        if word == 'VALID':
            conf = True
        elif word == 'INVALID':
            conf = False

    if conf:
        return f"Spell recorded: {spell_name} ({tested})"

    return f"Spell rejected: {spell_name} ({tested})"
