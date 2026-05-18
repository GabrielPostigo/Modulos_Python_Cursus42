def ft_count_harvest_iterative():
    days = int(input("Days until harvest: ")) + 1
    x = 1
    for x in range(days + 1):
        if (x == days):
            print("Harvest time!")
        else:
            print("Day ", x)


ft_count_harvest_iterative()
