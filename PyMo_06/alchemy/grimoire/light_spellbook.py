from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:

    ingredients: list[str] = ["earth", "air", "fire", "water"]

    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    '''
    A function light_spell_record(spell_name: str, ingredients: str) that re-
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
