import sys
# from typing import IO

if __name__ == "__main__":
    try:
        n: str = sys.argv[1]

        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file {n}")
        file = open(n, "r")

        print("---")
        print()
        print(file.read())
        print()
        print("---")

        file.close()
        print(f"File '{n}' closed")
    except IndexError:
        print("Usage: ft_ancient_text.py <file>")
        print()
    except FileNotFoundError:
        print(f"Error opening file '{n}': [Errno 2]",
              f"No such file or directory: '{n}'")
        print()
    except PermissionError:
        print(f"Error opening file '{n}': [Errno 13] Permission denied: '{n}'")
        print()
