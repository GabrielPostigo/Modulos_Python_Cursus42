class GardenError(Exception):
    def __init__(self, message="Unknown Garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown Plant error"):
        super().__init__(message)


def water_plant(plant_name: str):
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(pn1: str, pn2: str, pn3: str):
    print("Opening watering system")
    try:
        water_plant(pn1)
        water_plant(pn2)
        water_plant(pn3)
    except PlantError as p:
        print(f"Caught GardenError: {p}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")
    print()
    print("Testing invalid plants...")
    test_watering_system("Tomato", "lettuce", "Carrots")
    print()
    print("Cleanup always happens, even with errors!")
