class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 agev: int):
        self.name = name
        self.height = height
        self.agev = agev

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.agev} days old")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.agev = self.agev + 1


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    res = plant.height
    res1 = 0.0
    print("=== Garden Plant Growth ===")
    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        res1 = plant.height
        plant.age()
        plant.show()
    res = res1 - res
    print(f"Growth this week: {res:.1f}cm")
