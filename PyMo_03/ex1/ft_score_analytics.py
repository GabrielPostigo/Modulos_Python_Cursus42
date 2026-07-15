import sys


class NoImError(Exception):
    def __init__(self, message="Unknown Input"):
        super().__init__(message)


def score_ana() -> None:
    try:
        lis = sys.argv[1:]

        # Lenght of the list
        lenl = len(lis)

        # Allow me to verify that the list only has int or nothing
        for arg in lis:
            try:
                lis.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: {arg}")

        if (lenl == 0):
            raise NoImError("No scores provided.",
                            "Usage: python3 ft_score_analytics.py <score1>",
                            "<score2> ...")
        # Sort the list
        lis = lis.sort()

        total = sum(lis)

        top = lis[0]
        # for arg in sys.argv[1:]:
        #     if (int(arg) > top):
        #         top = int(arg)

        bot = lis[-1]
        # for arg in sys.argv[1:]:
        #     if (int(arg) < bot):
        #         bot = int(arg)

        # Range of the List
        ran = top - bot

        # Average of the List
        aver: float = (total / lenl)

        # The Print section
        print("Scores processed:", lis)
        print("Total Players:", lenl)
        print("Total score:", total)
        print("Average score:", aver)
        print("High Score:", top)
        print("Low score:", bot)
        print("Score range:", ran)
    except NoImError as n:
        print(n)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_ana()
