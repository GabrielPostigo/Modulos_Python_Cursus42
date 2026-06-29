class Plant:
    def __init__(self,
                 name: str,
                 start_height: float,
                 start_age: int):
        self.name = name
        self.start_height = start_height
        self.start_age = start_age
        self.height = self.start_height
        self.age = self.start_age

    @classmethod
    def creation(cls,
                 name: str,
                 start_height: float,
                 start_age: int) -> "Plant":
        print(f"Created: {name}: {start_height}cm, {start_age} days old")
        return cls(name, start_height, start_age)

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def agemore(self) -> None:
        self.age = self.age + 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant.creation("Rose", 25.0, 30)
    rose.show()
    rose.agemore()
    rose.grow()
    rose.show()
    print()
    oak = Plant.creation("Oak", 200.0, 365)
    oak.show()
    oak.agemore()
    oak.grow()
    oak.show()
    print()
    cactus = Plant.creation("Cactus", 5.0, 90)
    cactus.show()
    cactus.agemore()
    cactus.grow()
    cactus.show()
    print()
    sunfl = Plant.creation("Sunflower", 80.0, 45)
    sunfl.show()
    sunfl.agemore()
    sunfl.grow()
    sunfl.show()
    print()
    fern = Plant.creation("Fern", 15.0, 120)
    fern.show()
    fern.agemore()
    fern.grow()
    fern.show()
