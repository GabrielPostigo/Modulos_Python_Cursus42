def ft_count_harvest_recursive(day=None, x1=1):
    if day is None:
        days = int(input("Days until harvest: ")) + 1
        day = days
    if (x1 == day):
        print("Harvest time!")
    else:
        print("Day ", x1)
        ft_count_harvest_recursive(day, x1 + 1)


ft_count_harvest_recursive()
