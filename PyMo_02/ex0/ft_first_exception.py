def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int: int = int(temp_str)
        return temp_int
    except ValueError:
        print("Caught input_temperature error: invalid literal "
              "for int() with base 10: '", temp_str, "'")


def test_temperature() -> str:
    print(f"Temperature is now {input_temperature('25')}°C \n")
    input_temperature("abc")
    print()
    return ("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature === \n")
    print(test_temperature())
