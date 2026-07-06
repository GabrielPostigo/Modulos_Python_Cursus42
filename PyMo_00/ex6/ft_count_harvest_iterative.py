def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: ")) + 1
    x = 1
    for x in range(1, days + 1):
        if (x == days):
            print("Harvest time!")
        else:
            print("Day ", x)
