class Plant:
    def __init__(self,
                 name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age

    @classmethod
    def creation(cls,
                 name: str, height: float, age: int) -> "Plant":
        print(f"Created: {name}: {height}cm, {age} days old")
        return cls(name, height, age)

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = self._height + 0.8

    def agemore(self) -> None:
        self._age = self._age + 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_h: float) -> None:
        if new_h >= 0:
            print(f"Height updated: {new_h}cm")
            self.height = new_h
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_a: int) -> None:
        if new_a >= 0:
            print(f"Age updated: {new_a} days")
            self.age = new_a
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self._color}")

    def bloom(self, blo: bool = False) -> None:
        self.show()
        if not blo:
            print(f"{self.name} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            self.bloom(blo=True)
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self, sha: bool = False) -> None:
        if not sha:
            print(f"[asking the {self.name} to produce shade]")
            self.produce_shade(sha=True)
        else:
            print(f"Tree {self.name} now produces",
                  f"a shade of {self._height}cm long "
                  f"and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, har_season: str,
                 nutri_val: int):
        super().__init__(name, height, age)
        self._har_season = har_season
        self._nutri_val = nutri_val

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self._har_season}")
        print(f"Nutritional value: {self._nutri_val}")

    def grow(self) -> None:
        self._height = self._height + 2.1
        self._nutri_val = self._nutri_val + 1

    def agemore(self) -> None:
        self._age = self._age + 1
        self._nutri_val = self._nutri_val + 1

    def grow_20(self) -> None:
        print(f"[make {self.name} grow and age for 20 days]")
        self._age = self._age + 20
        self._height = self._height + 42
        self._nutri_val = self._nutri_val + 20


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.bloom()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    tomato.grow_20()
    tomato.show()
