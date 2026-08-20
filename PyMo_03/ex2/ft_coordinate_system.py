from math import sqrt


def get_player_pos() -> tuple[float, float, float]:
    bo: bool = True
    while bo:
        try:
            x, y, z = map(float,
                          input("Enter coordinates as x,y,z: ").split(','))
            bo = False
        except ValueError:
            print("Invalid syntax, retrying")

    tu: tuple[float, float, float] = (x, y, z)
    return tu


def rest(tu: tuple[float, float, float]) -> None:
    ce: tuple[float, float, float] = (0.0, 0.0, 0.0)

    dis: float = sqrt((ce[0]-tu[0])**2 + (ce[1]-tu[1])**2 + (ce[2]-tu[2])**2)

    print("Distance to center:", dis)
    print()

    print("Get a second set of coordinates")
    bo: bool = True
    while bo:
        try:
            x2, y2, z2 = map(float,
                             input("Enter coordinates as x,y,z: ").split(','))
            bo = False
        except ValueError:
            print("Invalid syntax, retrying")

    tu2: tuple[float, float, float] = (x2, y2, z2)
    dis2 = sqrt((tu2[0]-tu[0])**2 + (tu2[1]-tu[1])**2 + (tu2[2]-tu[2])**2)

    print("Distance between the 2 sets of coordinates:", dis2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    tu: tuple = get_player_pos()

    print("Got a first tuple:", tu)
    print(f"It includes: X={tu[0]}, Y={tu[1]}, Z={tu[2]}")

    rest(tu)
