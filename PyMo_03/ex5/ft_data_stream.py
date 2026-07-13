import random as ra


# Function that picks a random name from a list
# of players, and a random action from a list of actions.
def gen_event():
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    actions = ["eat", "sleep", "grab", "run", "move", "climb",
               "swim", "release"]
    sel_n = ra.choice(names)
    sel_a = ra.choice(actions)
    # tu = tuple(sel_n, sel_a)
    yield (sel_n, sel_a)


# Function that takes the previously created
# list, randomly pick one of its elements, remove it from the list, and yields
# it, until the list is empty.
def consume_event(li: list):
    sel = ra.choice(li)
    print("Got event from list:", sel)
    li.remove(sel)
    print("Remains in list:", li)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    i = 0
    events = []
    for j in range(12):
        g = gen_event()
        tup: tuple = next(g)
        if (i <= 9):
            events.append(tup)
        i += 1
        print(tup)
        # print(f"Event {j}: Player {tup[0]} did action {tup[1]}")
    print("Built list of 10 events:", events)
    for de in range(1, len(events) + 1):
        consume_event(events)
