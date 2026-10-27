def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    ing_or: list[str] = light_spell_allowed_ingredients()
    ing_new: list[str] = [w.strip(",.;:!?").lower()
                          for w in ingredients.split()]
    cont: int = 0

    for ele in ing_new:
        for non in ing_or:
            if ele == non:
                cont += 1

    if cont >= 1:
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
