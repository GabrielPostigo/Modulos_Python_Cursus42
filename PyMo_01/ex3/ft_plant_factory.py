class Plant:
    def __init__(self, name: str, start_height: float, start_age: int):
        self.name = name
        self.start_height = start_height
        self.start_age = start_age
        self.height = self.start_height
        self.age = self.start_age

    @classmethod
    def creation(cls, name: str, start_height: float, start_age: int):
        print(f"Created: {name}, {start_height}cm, {start_age} days old")
        return cls(name, start_height, start_age)

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height = self.height + 0.8

    def agemore(self):
        self.age = self.age + 1


print("=== Plant Factory Output ===")
rose = Plant.creation("Rose", 25.0, 30)
oak = Plant.creation("Oak", 200.0, 365)
cactus = Plant.creation("Cactus", 5.0, 90)
sunfl = Plant.creation("Sunflower", 80.0, 45)
fern = Plant.creation("Fern", 15.0, 120)
# print("")
# rose.show()
# oak.show()
# cactus.show()
# sunfl.show()
# fern.show()
