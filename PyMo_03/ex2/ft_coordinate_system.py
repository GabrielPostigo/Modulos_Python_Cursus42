import math


def get_player_pos() -> None:
    try:
        x = float(input("Enter the X value: "))
        y = float(input("Enter the Y value: "))
        z = float(input("Enter the Z value: "))
    except TypeError:
        print("Invalid syntax, retrying")
        x = float(input("Enter the X value: "))
        y = float(input("Enter the Y value: "))
        z = float(input("Enter the Z value: "))

    tu = tuple(x, y, z)
    ce = tuple(0.0, 0.0, 0.0)

    dis = math.sqrt((ce[0]-tu[0])**2 + (ce[1]-tu[1])**2 + (ce[2]-tu[2])**2)

    print("Got a first tuple:", tu)
    print(f"It includes: X={tu[0]}, Y={tu[1]}, Z={tu[2]}")

    print("Distance to center:", dis)
    print()

    print("Get a second set of coordinates")
    try:
        x2 = float(input("Enter the X value: "))
        y2 = float(input("Enter the Y value: "))
        z2 = float(input("Enter the Z value: "))
    except TypeError:
        print("Invalid syntax, retrying")
        x2 = float(input("Enter the X value: "))
        y2 = float(input("Enter the Y value: "))
        z2 = float(input("Enter the Z value: "))

    tu2 = tuple(x2, y2, z2)
    dis2 = math.sqrt((tu2[0]-tu[0])**2 + (tu2[1]-tu[1])**2 + (tu2[2]-tu[2])**2)

    print("Distance between the 2 sets of coordinates:", dis2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    get_player_pos()
