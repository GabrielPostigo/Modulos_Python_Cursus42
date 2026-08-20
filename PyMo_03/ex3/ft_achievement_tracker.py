from random import randint, sample

ACHIEVEMENTS: set = {"Crafting Genius", "Strategist", "World Savior",
                     "Speed Runner", "Survivor", "Master Explorer",
                     "Treasure Hunter", "Unstoppable", "First Steps",
                     "Collector Supreme", "Untouchable", "Sharp Mind",
                     "Boss Slayer"}


def gen_player_achievements() -> set[str]:
    # Random number of achievements to give
    number_a: int = randint(0, len(ACHIEVEMENTS))
    return set(sample(sorted(ACHIEVEMENTS), number_a))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    Alice = gen_player_achievements()
    Bob = gen_player_achievements()
    Charlie = gen_player_achievements()
    Dylan = gen_player_achievements()

    # Achievements shared by all players
    common_a = Alice.intersection(Bob, Charlie, Dylan)

    # For each player, achievements no one else has
    only_a = Alice.difference(Bob, Charlie, Dylan)
    only_b = Bob.difference(Alice, Charlie, Dylan)
    only_c = Charlie.difference(Alice, Bob, Dylan)
    only_d = Dylan.difference(Alice, Bob, Charlie)

    # For each player, list the missing achievements to have them all
    miss_a = ACHIEVEMENTS.difference(Alice)
    miss_b = ACHIEVEMENTS.difference(Bob)
    miss_c = ACHIEVEMENTS.difference(Charlie)
    miss_d = ACHIEVEMENTS.difference(Dylan)

    print("Player Alice:", Alice)
    print("Player Bob:", Bob)
    print("Player Charlie:", Charlie)
    print("Player Dylan:", Dylan)
    print()
    print("All distinct achievements:", ACHIEVEMENTS)
    print()
    print("Common achievements:", common_a)
    print()
    print("Only Alice: has", only_a)
    print("Only Bob has:", only_b)
    print("Only Charlie has:", only_c)
    print("Only Dylan has:", only_d)
    print()
    print("Alice is Missing:", miss_a)
    print("Bob is Missing:", miss_b)
    print("Charlie is Missing:", miss_c)
    print("Dylan is Missing:", miss_d)
