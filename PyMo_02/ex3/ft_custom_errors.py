class GardenError(Exception):
    def __init__(self, message, plant_n, water):
        super.__init__(message)
        if not plant_n:
            self.errors = "Unknown Plant error"
        else:
            self.plant_n = plant_n
        self.plant_n = plant_n
        self.water = water

    def __str__(self):
        if self.water < 20:
            return ("Caught", self.__class__.__name__,
                    ": Not enough water in the tank!")
        else:
            return ("Caught", self.__class__.__name__,
                    ": The", self.plant_n, "plant is wilting!")


class PlantError(GardenError):
    def __init__(self, message, name):
        super.__init__(message)
        if not name:
            self.errors = "Unknown Plant error"
        else:
            self.name = name

    def __str__(self):
        return ("Caught", self.__class__.__name__,
                ": The", self.name, "plant is wilting!")


class WaterError(GardenError):
    def __init__(self, message, water):
        super.__init__(message, water)

    def __str__(self):
        if self.water < 20:
            return ("Caught", self.__class__.__name__,
                    ": Not enough water in the tank!")
        else:
            return ("Caught", self.__class__.__name__,
                    ": The", self.plant_n, "plant is wilting!")


# class Plant():
#     def __init__(self, name, water):
#         self.name = name
#         self.water = water

#     def show(self):
#         try:

#             print(f"{self.name} is watering ")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    raise PlantError("Tomato")
    print("")
    print("Testing WaterError...")
