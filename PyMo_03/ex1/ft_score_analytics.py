import sys


def NoImError(Exception):
    def __init__(self, message="Unknown Input"):
        super().__init__(message)


lis = sys.argv[1:]

for i in lis:
    if not type(i) is int:
        raise TypeError("Invalid parameter:", i)

lenl = len(lis)
lis_org = lis.sort()

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

aver: float = (total / lenl)

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        if (lenl == 1):
            raise NoImError("No scores provided.",
                            "Usage: python3 ft_score_analytics.py <score1>",
                            "<score2> ...")
        print("Scores processed:", lis)
        print("Total Players:", lon)
        print("Total score:", total)
        print("High Score:", top)
    except NoImError:
        print("No scores provided. Usage:",
              "python3 ft_score_analytics.py <score1> <score2> ...")
