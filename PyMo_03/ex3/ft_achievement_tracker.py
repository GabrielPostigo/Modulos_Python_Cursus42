import random


def gen_player_achievements() -> None:
    # Set of all the achievements avaible
    achi = {"Crafting Genius", "Strategist", "World Savior", "Speed Runner",
            "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
            "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
            "Boss Slayer"}

    # Lenght of the set 'achi'
    achiL: int = len(achi)

    # Random number of achievements to give
    number_a: int = random.randint(0, achiL)
    Alice = {random.sample(achi, number_a)}

    number_b: int = random.randint(0, achiL)
    Bob = {random.sample(achi, number_b)}

    number_c: int = random.randint(0, achiL)
    Charlie = {random.sample(achi, number_c)}

    number_d: int = random.randint(0, achiL)
    Dylan = {random.sample(achi, number_d)}

    # Achievements shared by all players
    common_a = Alice.intersection(Bob, Charlie, Dylan)
    # Alternative way to do it -> Alice & Bob & Charlie & Dylan

    # For each player, achievements no one else has
    only_a = Alice.difference(Bob, Charlie, Dylan)
    # Alternative way to do it -> Alice - Bob - Charlie - Dylan

    only_b = Bob.difference(Alice, Charlie, Dylan)
    only_c = Charlie.difference(Alice, Bob, Dylan)
    only_d = Dylan.difference(Alice, Bob, Charlie)

    # For each player, list the missing achievements to have them all
    miss_a = achi.differende(Alice)
    miss_b = achi.differende(Bob)
    miss_c = achi.differende(Charlie)
    miss_d = achi.differende(Dylan)

    # Prints section
    print("Player Alice: ", Alice)
    print("Player Bob: ", Bob)
    print("Player Charlie: ", Charlie)
    print("Player Dylan: ", Dylan)
    print()
    print("All distinct achievements:", achi)
    print()
    print("Common achievements:", common_a)
    print()
    print("Only Alice: has ", only_a)
    print("Only Bob has: ", only_b)
    print("Only Charlie has: ", only_c)
    print("Only Dylan has: ", only_d)
    print()
    print("Alice is Missing:", miss_a)
    print("Bob is Missing:", miss_b)
    print("Charlie is Missing:", miss_c)
    print("Dylan is Missing:", miss_d)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    gen_player_achievements()
