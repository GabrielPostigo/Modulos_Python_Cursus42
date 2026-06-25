class Plant:
    def __init__(self, name: str, start_height: float, start_age: int):
        self.name = name
        self.start_height = start_height
        self.start_age = start_age
        self.height = self.start_height
        self.age = self.start_age
        self.stats = self.Stadistics()

    @classmethod
    def creation(cls,
                 name: str, start_height: float, start_age: int) -> "Plant":
        print(f"Created: {name}, {start_height}cm, {start_age} days old")
        return cls(name, start_height, start_age)

    @classmethod
    def anony_creation(cls) -> "Plant":
        any_name = "Unknown Plant"
        any_start_height = 0.0
        any_start_age = 0
        return cls(any_name, any_start_height, any_start_age)

    @staticmethod
    def isyear(self) -> None:
        a = self.age
        if (a > 365):
            print(f"Is {a} days more than a year? -> False")
        else:
            print(f"Is {a} days more than a year? -> True")

    class Stadistics:
        def __init__(self):
            self._gc = 0
            self._ac = 0
            self._sc = 0
            self._pc = 0

    def show(self) -> None:
        self.stats._sc += 1
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.stats._gc += 1
        self.height = self.height + 0.8

    def agemore(self) -> None:
        self.stats._ac += 1
        self.age = self.age + 1

    def set_height(self, new_h: float) -> None:
        if new_h >= 0:
            print(f"Height updated: {new_h}cm")
            self.height = new_h
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            self.height = self.start_height

    def set_age(self, new_a: int) -> None:
        if new_a >= 0:
            print(f"Age updated: {new_a} days")
            self.age = new_a
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            self.age = self.start_age


class Flower(Plant):
    def __init__(self, name, start_height, start_age, color: str):
        super().__init__(name, start_height, start_age)
        self.color = color
        self.blo = False

    def show(self) -> None:
        self.stats._gc += 1
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        if not self.blo:
            print(f"{self.name} has not bloomed yet")
            self.blo = True
        else:
            print(f"{self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name, start_height, start_age, color, seeds: int):
        super().__init__(name, start_height, start_age, color)
        self.seeds = seeds

    def show(self) -> None:
        self.stats._sc += 1
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Color: {self.color}")
        print(f"Seeds: {self.seeds}")

    def grow_20(self) -> None:
        print("[make tomato grow and age for 20 days]")
        self.stats._gc += 1
        self.stats._ac += 1
        self.age = self.age + 20
        self.height = self.height + 30
        self.seeds += 42


class Tree(Plant):
    def __init__(self, name, start_height, start_age, trunk_diameter: float):
        super().__init__(name, start_height, start_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self.stats._pc += 1
        print(f"Trunk diameter: {self.trunk_diameter}m")
        print("[asking the oak to produce shade]")
        print("Tree", self.name, "now produces a shade of",
              self.start_height, "cm long and", self.trunk_diameter,
              "cm wide")


class Vegetable(Plant):
    def __init__(self, name, start_height, start_age, har_season, nutri_val):
        super().__init__(name, start_height, start_age)
        self.har_season = har_season
        self.nutri_val = nutri_val

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.har_season}")
        print(f"Nutritional value: {self.nutri_val}")
        self.stats._gc += 1

    def grow_20(self) -> None:
        print("[make tomato grow and age for 20 days]")
        self.stats._gc += 20
        self.age = self.age + 20
        self.height = self.height + 42
        self.nutri_val = self.nutri_val + 20


def show_stats(obj) -> None:
    name_class = type(obj).__name__

    print(f"[statistics for {obj.name}]")
    if (name_class == 'Tree'):
        print("Stats:", obj.stats._gc, "grow", obj.stats._ac,
              "age", obj.stats._sc, "show")
        print(f"{obj.stats._pc} shade")
    else:
        print("Stats:", obj.stats._gc, "grow", obj.stats._ac,
              "age", obj.stats._sc, "show")


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
    pru1.isyear(pru1)
    pru2.isyear(pru2)
    print("")

    print("=== Flower")
    rose.show()
    rose.bloom()
    print("[asking the rose to grow and bloom]")
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
    show_stats(sunflower)
    sunflower.grow_20()
    sunflower.show()
    show_stats(sunflower)
    print("")

    print("=== Anonymous")
    anon.show()
    show_stats(anon)
