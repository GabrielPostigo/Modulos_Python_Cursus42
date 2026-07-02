class GardenError(Exception):
    def __init__(self, message="Unknown Garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown Plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown Water error"):
        super().__init__(message)


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as p:
        print(f"Caught PlantError: {p}")
    print()

    print("Testing PlantError...")
    try:
        test_water_error()
    except WaterError as w:
        print(f"Caught PlantError: {w}")
    print()

    print("Testing catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly")
