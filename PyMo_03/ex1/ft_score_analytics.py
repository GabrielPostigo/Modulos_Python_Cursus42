import sys

lis = sys.argv[1:]

lon = len(lis)

total = 0
for arg in sys.argv[1:]:
    total += int(arg)

top = 0
for arg in sys.argv[1:]:
    if (int(arg) > top):
        top = int(arg)

bot = sys.argv[1]
for arg in sys.argv[1:]:
    if (int(arg) < bot):
        bot = int(arg)

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    print("Scores processed:", lis)
    print("Total Players:", lon)
    print("Total score:", total)
    print("High Score:", top)
    
