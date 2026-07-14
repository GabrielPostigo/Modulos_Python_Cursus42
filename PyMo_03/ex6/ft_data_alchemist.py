import random

if __name__ == "__main__":
    players = ['Alice', 'bob',
               'Charlie', 'dylan', 'Emma', 'Gregory',
               'john', 'kevin', 'Liam']

    #  list with all names capitalized
    players_cap = [x.capitalize() for x in players]

    # list with only the capitalized names from the initial list
    players_only = [x for x in players if x == x.capitalize()]

    # Dictionary from this full capitalized list
    score = {}
    gen = (p for p in players_cap)
    for x in range(len(players)):
        score[next(gen)] = random.randint(1, 1000)

    # Average of scores
    aver = float(sum(score.values()) / (len(score)))

    # Dictionary with scores higher than the average
    high_scores = dict(score.items())
    nom = high_scores.keys()
    nh_nom = [n for n in nom if high_scores[n] > aver]
    high_scores = {high_scores.pop(n) for n in nh_nom}

    # nom = ""
    # gen2 = [p for p in high_scores.keys()]
    # for x in range(len(high_scores)):
    #     nom = gen2[x]
    #     if (high_scores.get(nom) < aver):
    #         high_scores.pop(nom)
    # for x in range(len(players)):
    #     score[next(gen)] = random.randint(1, 1000)

    # Print Zone
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
