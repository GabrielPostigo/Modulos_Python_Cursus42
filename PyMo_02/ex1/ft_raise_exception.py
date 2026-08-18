def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int: int = int(temp_str)
        if (0 > temp_int):
            raise ValueError(f"Caught input_temperature error: {temp_int} °C "
                             f"is too cold for plants(max 40°C)")
        elif (temp_int > 40):
            raise ValueError(f"Caught input_temperature error: {temp_int} °C "
                             f"is too hot for plants(min 0°C)")
        else:
            return (f"Temperature is now {temp_int}°C")

    except TypeError:
        return (f"Caught input_temperature error: invalid literal"
                f"for int() with base 10: '{temp_str}'")
    except ValueError as e:
        return (e)


def test_temperature() -> str:
    print(f"Temperature is now {input_temperature('25')} \n")
    print(input_temperature('abc'), '\n')
    print(input_temperature('100'), '\n')
    print(input_temperature('-50'), '\n')
    return ("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature === \n")
    print(test_temperature())
