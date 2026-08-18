def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp_int: int = 0
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Caught input_temperature error: invalid literal "
              f"for int() with base 10: '{temp_str}'")
    return temp_int


def test_temperature() -> str:
    print(f"Temperature is now {input_temperature('25')}°C \n")
    input_temperature("abc")
    print()
    return ("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature === \n")
    print(test_temperature())
