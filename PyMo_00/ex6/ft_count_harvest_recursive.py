x = 1
days = int(input("Days until harvest: ")) + 1   

def ft_recursive(day , x1):
    if (x1 == day):
        print("Harvest time!")
    else:
        print("Day ", x1)
        ft_recursive(day, x1 + 1)
    
ft_recursive(days, x)