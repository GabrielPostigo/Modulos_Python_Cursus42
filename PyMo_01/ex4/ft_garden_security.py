class Plant:
    def __init__(self, name: str, start_height: float, start_age: int):
        self.name = name
        self._start_height = start_height
        self._start_age = start_age
        self._height = self._start_height
        self._age = self._start_age

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


print("=== Garden Security System ===")
rose = Plant.creation("Rose", 15.0, 10)
print("")
rose.set_height(25.0)
rose.set_age(30)
print("")
rose.set_height(-25.0)
rose.set_age(-30)
print("")
print("Current status:")
rose.show()
