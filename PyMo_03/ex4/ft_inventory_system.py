from sys import argv

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    # Creation of the list of all arguments
    lis = argv[1:]

    # Creation of the Dictionary
    dc: dict[str, int] = {}

    for i in lis:
        if ':' not in i:
            print(f"Error - invalid parameter '{i}'")
            continue
        item, qua = i.split(':', 1)
        if not qua.isdigit():
            print(f"Quantity error for '{item}':"
                  f" invalid literal for int() with base 10: '{qua}'")
            continue
        if item in dc:
            print(f"Redundant item {item} - discarding")
        if item not in dc:
            dc[item] = int(qua)

    print("Got inventory:", dc)

    # ---

    if len(dc) == 0:
        print("Error: No valid items in inventory")
        exit()

    # Lenght of the Dictionary
    dc_len = len(dc)

    # Calcularion of the %
    dc_keys = dc.keys()
    dc_values = dc.values()
    total = 0

    print("Item list:", list(dc.keys()))

    # Calculate the total of the values
    for x in dc_values:
        total += x

    print(f"Total quantity of the {dc_len} items: {total}")

    # Calculate the quantity percentage it represents in the inventory
    p: float = 0.0
    for y in dc_keys:
        p = (dc[y] / total) * 100
        print(f"Item {y} represents {p:.1f}%")

    # ---

    # the most and least abundant items
    ma = max(dc, key=lambda x: dc[x])
    ma_va = dc[ma]
    mi = min(dc, key=lambda x: dc[x])
    mi_va = dc[mi]

    print(f"Item most abundant: {ma} with quantity {ma_va}")
    print(f"Item least abundant: {mi} with quantity {mi_va}")

    # ---

    # Add a new item
    dc.update({"magic_item": 1})
    print("Updated inventory:", dc)
