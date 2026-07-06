import sys

x = len(sys.argv)

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if (x == 1):
        print("No arguments provided!")
    else:
        print("Arguments received:", (x - 1))
        i = 0
        for arg in sys.argv[1:]:
            i += 1
            print(f"Argument {i}: {arg}")
    print("Total arguments:", x)
