class Plant:
    def __init__(self, name: str, height, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height = self.height + 0.8

    def agemore(self):
        self.age = self.age + 1


plant = Plant("Rose", 25.0, 30)
res = plant.height
res1 = 0
print("=== Garden Plant Growth ===")
for day in range(1, 8):
    print(f"=== Day {day} ===")
    print(f"{plant.name}: {plant.height:.1f}cm, {plant.age} days old")
    res1 = plant.height
    plant.grow()
    plant.agemore()
res = res1 - res
print(f"Growth this week: {res:.1f}cm")
