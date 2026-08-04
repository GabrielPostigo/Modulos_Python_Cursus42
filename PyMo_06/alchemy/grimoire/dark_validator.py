from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    ing_or: list[str] = dark_spell_allowed_ingredients()
    ing_new: list[str] = ingredients.split()
    cont: int = 0

    for ele in ing_new:
        for non in ing_or:
            if ele == non:
                cont += 1

    if cont >= 1:
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
