def garden_operations(operation_number: int):
    print(f"Testing operation {operation_number}...")
    match operation_number:
        case 0:
            print("Caught ValueError: invalid literal for int()",
                  "with base 10: 'abc'")
            print("")
        case 1:
            print("Caught ZeroDivisionError: division by zero")
        case 2:
            print("Caught FileNotFoundError: [Errno 2] No such",
                  "file or directory: '/non/existent/file'")
            print("")
        case 3:
            print("Caught TypeError: can only concatenate str",
                  "(not 'int') to str")
            print("")
        case _:
            print("Operation completed successfully")
    print("")
    print("I'm still running after the error")


def test_error_types():
    try:
        val = int('abc')
        val = 0 / val

        file = open("test.txt")
        file = "rar"
        file = file + 13
        garden_operations(4)
    except ValueError:
        garden_operations(0)
    except ZeroDivisionError:
        garden_operations(1)
    except FileExistsError:
        garden_operations(2)
    except TypeError:
        garden_operations(3)


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("")
    print("All error types tested successfully!")
