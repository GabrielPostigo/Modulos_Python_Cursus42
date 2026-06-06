def input_temperature(temp_str: str):
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        print(f"Temperature is now {temp_int}°C")
    except ValueError:
        print("Caught input_temperature error: invalid literal"
              "for int() with base 10: '", temp_str, "'")


def test_temperature():
    input_temperature("25")
    input_temperature("abc")
    return ("All tests completed - program didn't crash!")


print("=== Garden Temperature ===")
print(test_temperature())
