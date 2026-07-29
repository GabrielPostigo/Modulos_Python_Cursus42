def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        if (0 > temp_int):
            raise Exception("Caught input_temperature error:",
                            {temp_int}, "°C is too cold for plants(max 40°C)")
        elif (temp_int > 40):
            raise Exception("Caught input_temperature error:",
                            {temp_int}, "°C  is too hot for plants(min 0°C)")
        else:
            print(f"Temperature is now {temp_int}°C")

    except ValueError:
        print("Caught input_temperature error: invalid literal"
              "for int() with base 10: '", temp_str, "'")
    except Exception as e:
        print(e)


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")
    return ("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print(test_temperature())
