class PlantError(Exception):
    def __init__(self, message="Unknown Plant error"):
        super().__init__(message)


def water_plant(plant_name: str):
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else
        raise PlantError("")
    
if __name__ == "__main__":
    print("Testing valid plants...")
    print("Opening watering system")
    water_plant("Tomato")
