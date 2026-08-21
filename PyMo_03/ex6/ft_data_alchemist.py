from random import randint


if __name__ == "__main__":
    players = ['Alice', 'bob',
               'Charlie', 'dylan', 'Emma', 'Gregory',
               'john', 'kevin', 'Liam']

    #  list with all names capitalized
    players_cap = [x.capitalize() for x in players]

    # list with only the capitalized names from the initial list
    players_only = [x for x in players if x == x.capitalize()]

    # Dictionary from this full capitalized list
    score = {name: randint(1, 1000) for name in players_cap}

    # Average of scores
    aver = float(sum(score.values()) / (len(score)))

    # Dictionary with scores higher than the average
    high_scores = {name: val for name, val in score.items() if val > aver}

    # Print Zone
    print("=== Game Data Alchemist === \n")
    print("Initial list", players)
    print()
    print("Only capitalize:", players_only)
    print()
    print("All list capitallize:", players_cap)
    print()
    print("Score dict:", score)
    print()
    print(f"Score average is {aver:.2f}")
    print()
    print("High scores:", high_scores)
