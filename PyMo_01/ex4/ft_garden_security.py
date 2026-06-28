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
            self.height = self._height

    def set_age(self, new_a: int) -> None:
        if new_a >= 0:
            print(f"Age updated: {new_a} days")
            self.age = new_a
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            self.age = self._age


if __name__ == "__main__":
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
