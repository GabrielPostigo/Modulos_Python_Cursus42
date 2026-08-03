def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    match operation_number:
        case 0:
            val = int("abc")
            print(val)
        case 1:
            res = 1/0
            print(res)
        case 2:
            file = open("/non/existent/file")
            print(file.read())
        case 3:
            result = "text" + 13  # type: ignore[operator]
            print(result)
        case _:  # default value
            print("Operation completed successfully")


def test_error_types() -> None:
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    try:
        garden_operations(2)
    except (ValueError, FileNotFoundError) as e:
        print(f"Caught FileNotFoundError: {e}")

    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    garden_operations(4)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("")
    print("All error types tested successfully!")
