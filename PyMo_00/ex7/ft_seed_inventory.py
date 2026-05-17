def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if (unit == "packets"):
        print(seed_type,"seeds:", quantity, unit, "avaible" )
    elif (unit == "grams"):
        print(seed_type,"seeds:", quantity, unit, "total" )
    elif (unit == "area"):
        print(seed_type,"seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")

seed = str(input("Semilla de "))
quan = int(input("siendo la cantidad "))
un = str(input("y la unidad "))

ft_seed_inventory(seed, quan, un)
