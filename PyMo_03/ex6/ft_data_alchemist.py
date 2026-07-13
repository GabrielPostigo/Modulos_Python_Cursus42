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

    # Print Zone
    print("Initial list", players)
    print()
    print("Only capitalize:", players_only)
    print()
    print("All list capitallize:", players_cap)
