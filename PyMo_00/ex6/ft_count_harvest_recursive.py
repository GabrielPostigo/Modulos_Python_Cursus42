def ft_count_harvest_recursive(day: int | None = None, x1: int = 1) -> None:
    if day is None:
        days = int(input("Days until harvest: ")) + 1
        day = days
    if (x1 == day):
        print("Harvest time!")
    else:
        print("Day ", x1)
        ft_count_harvest_recursive(day, x1 + 1)
