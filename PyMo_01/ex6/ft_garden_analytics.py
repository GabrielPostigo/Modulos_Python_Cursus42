class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age
        self.stats = self.Stadistics()

    @classmethod
    def creation(cls,
                 name: str, height: float, age: int) -> "Plant":
        print(f"Created: {name}: {height}cm, {age} days old")
        return cls(name, height, age)

    @classmethod
    def anony_creation(cls) -> "Plant":
        any_name = "Unknown plant"
        any_height = 0.0
        any_age = 0
        return cls(any_name, any_height, any_age)

    @staticmethod
    def isyear(agey: int) -> None:
        if (agey > 365):
            print(f"Is {agey} days more than a year? -> True")
        else:
            print(f"Is {agey} days more than a year? -> False")

    class Stadistics:
        def __init__(self) -> None:
            self._gc = 0
            self._ac = 0
            self._sc = 0
            self._pc = 0

        def display(self) -> None:
            print(f"Stats: {self._gc} grow, {self._ac} age, {self._sc} show")

        def display_shade(self) -> None:
            print(f"{self._pc} shade")

    def show(self) -> None:
        self.stats._sc += 1
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self.stats._gc += 1
        self._height = self._height + 8.0

    def agemore(self) -> None:
        self.stats._ac += 1
        self._age = self._age + 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_h: float) -> None:
        if new_h >= 0:
            print(f"Height updated: {new_h}cm")
            self._height = new_h
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_a: int) -> None:
        if new_a >= 0:
            print(f"Age updated: {new_a} days")
            self._age = new_a
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")


class Flower(Plant):
    def __init__(self, name: str,
                 height: float, age: int,
                 color: str):
        super().__init__(name, height, age)
        self.color = color
        self.blo = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        if not self.blo:
            print(f"{self.name} has not bloomed yet")
            self.blo = True
        else:
            print(f"{self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str,
                 height: float, age: int,
                 color: str, seeds: int):
        super().__init__(name, height, age, color)
        self.seeds = seeds
        self.blo = False

    def show(self) -> None:
        super().show()
        self.bloom()
        print(f"Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()

    def grow_20(self) -> None:
        print(f"[make {self.name.lower()} grow, age and bloom]")
        self.stats._gc += 1
        self.stats._ac += 1
        self._age = self._age + 20
        self._height = self._height + 30
        if self.blo:
            self.seeds += 42


class Tree(Plant):
    def __init__(self, name: str,
                 height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.stats._pc += 1
        print(f"[asking the {self.name.lower()} to produce shade]")
        print("Tree", self.name, "now produces a shade of", self._height,
              "cm long and", self.trunk_diameter, "cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, har_season: str, nutri_val: int):
        super().__init__(name, height, age)
        self.har_season = har_season
        self.nutri_val = nutri_val

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.har_season}")
        print(f"Nutritional value: {self.nutri_val}")

    def grow_20(self) -> None:
        print(f"[make {self.name} grow and age for 20 days]")
        self.stats._gc += 1
        self.stats._ac += 1
        self._age = self._age + 20
        self._height = self._height + 42
        self.nutri_val = self.nutri_val + 20


def show_stats(obj) -> None:
    print(f"[statistics for {obj.name}]")
    obj.stats.display()
    if isinstance(obj, Tree):
        obj.stats.display_shade()


if __name__ == "__main__":
    pru1 = Plant("Prueba1", 20.0, 30)
    pru2 = Plant("Prueba2", 20.0, 400)
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    anon = Plant.anony_creation()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    pru1.isyear(pru1._age)
    pru2.isyear(pru2._age)
    print("")

    print("=== Flower")
    rose.show()
    rose.bloom()
    show_stats(rose)
    print(f"[asking the {rose.name.lower()} to grow and bloom]")
    rose.show()
    rose.grow()
    rose.bloom()
    show_stats(rose)
    print("")

    print("=== Tree")
    oak.show()
    show_stats(oak)
    oak.produce_shade()
    show_stats(oak)
    print("")

    print("=== Seed")
    sunflower.show()
    sunflower.grow_20()
    sunflower.show()
    show_stats(sunflower)
    print("")

    print("=== Anonymous")
    anon.show()
    show_stats(anon)
