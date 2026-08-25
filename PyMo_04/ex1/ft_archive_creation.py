import sys
# from typing import IO

if __name__ == "__main__":
    try:
        n: str = sys.argv[1]

        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file {n}")
        file = open(n, "r")
        content = file.read()

        print("---")
        print()
        print(content)
        print()
        print("---")

        file.close()
        print(f"File '{n}' closed")

        trans_lines: list[str] = []
        for line in content.split('\n'):
            if line:
                trans_lines.append(line + '#')
            else:
                trans_lines.append(line)

        trans_content: str = '\n'.join(trans_lines)

        print("Transform data:")
        print("---")
        print()
        print(trans_content)
        print()
        print("---")

        us_name = str(input("Enter new file name (or empty): "))
        if not us_name:
            print("Not saving data")
        else:
            new_file = open(us_name, "w")
            new_file.write(trans_content)
            new_file.close()
            print(f"Saving data to '{us_name}'")
            print(f"Data saved in file '{us_name}'")

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
