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

    def set_height(self, new_h: float):
        if new_h >= 0:
            print(f"Height updated: {new_h}cm")
            self.height = new_h
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            self.height = self._start_height

    def set_age(self, new_a: int):
        if new_a >= 0:
            print(f"Age updated: {new_a} days")
            self.age = new_a
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            self.age = self._start_age


class Flower(Plant):
    def __init__(self, name, start_height, start_age, color: str):
        super().__init__(name, start_height, start_age)
        self.color = color

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Color: {self.color}")

    def bloom(self, blo=False):
        self.show()
        if not blo:
            print(f"{self.name} has not bloomed yet")
            print("[asking the rose to bloom]")
            self.bloom(blo=True)
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, start_height, start_age, trunk_diameter: float):
        super().__init__(name, start_height, start_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, sha=False):
        self.show()
        print(f"Trunk diameter: {self.trunk_diameter}m")
        if not sha:
            print("[asking the oak to produce shade]")
            self.produce_shade(sha=True)
        else:
            print(f"Tree {self.name} now produces")
            print(f"a shade of {self.start_height}cm long")
            print(f"and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, start_height, start_age, har_season, nutri_val):
        super().__init__(name, start_height, start_age)
        self.har_season = har_season
        self.nutri_val = nutri_val

    def show(self):
        super().show()
        print(f"Harvest Season: {self.har_season}")
        print(f"Nutritional value: {self.nutri_val}")

    def grow_20(self):
        print("[make tomato grow and age for 20 days]")
        self.age = self.age + 20
        self.height = self.height + 42
        self.nutri_val = self.nutri_val + 20


rose = Flower("Rose", 15.0, 10, "red")
oak = Tree("Oak", 200.0, 365, 5.0)
tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
print("=== Garden Plant Types ===")
print("=== Flower")
rose.bloom()
print()
print("=== Tree")
oak.produce_shade()
print()
print("=== Vegetable")
tomato.show()
tomato.grow_20()
tomato.show()
