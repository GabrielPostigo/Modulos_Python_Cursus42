from sys import argv


class NoImError(Exception):
    def __init__(self, message="Unknown Input") -> None:
        super().__init__(message)


def score_ana() -> None:
    try:
        lis: list[int] = []

        # Allow me to verify that the list only has int or nothing
        for arg in argv[1:]:
            try:
                lis.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")

        if (len(lis) == 0):
            raise NoImError("No scores provided."
                            "Usage: python3 ft_score_analytics.py <score1> "
                            "<score2> ...")

        # Lenght and Total of the list
        lenl: int = len(lis)

        total: int = sum(lis)

        # Max and Min of the list
        top: int = max(lis)

        bot: int = min(lis)

        # Range of the List
        ran: int = top - bot

        # Average of the List
        aver: float = (total / lenl)

        # The Print section
        print("Scores processed:", lis)
        print("Total players:", lenl)
        print("Total score:", total)
        print("Average score:", aver)
        print("High score:", top)
        print("Low score:", bot)
        print("Score range:", ran)
    except NoImError as n:
        print(n)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_ana()
