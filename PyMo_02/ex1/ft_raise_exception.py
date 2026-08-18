def input_temperature(temp_str: str) -> int | None:
    print(f"Input data is '{temp_str}'")
    temp_int: int = 0
    try:
        temp_int = int(temp_str)
        if (0 > temp_int):
            raise ValueError(f"Caught input_temperature error: {temp_int} °C "
                             f"is too cold for plants(max 40°C)")
        elif (temp_int > 40):
            raise ValueError(f"Caught input_temperature error: {temp_int} °C "
                             f"is too hot for plants(min 0°C)")

    except TypeError:
        print(f"Caught input_temperature error: invalid literal"
              f"for int() with base 10: '{temp_str}'")
    except ValueError as e:
        print(e)
    return temp_int


def test_temperature() -> str:
    print(f"Temperature is now {input_temperature('25')}ºC \n")
    input_temperature('abc')
    print()
    input_temperature('100')
    print()
    input_temperature('-50')
    print()
    return ("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature === \n")
    print(test_temperature())
