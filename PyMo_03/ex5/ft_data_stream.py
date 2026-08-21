from typing import Generator
from random import choice


# Function that picks a random name from a list
# of players, and a random action from a list of actions.
def gen_event() -> Generator[tuple[str, str], None, None]:
    names = ["alice", "bob", "charlie", "dylan"]
    actions = ["eat", "sleep", "grab", "run", "move", "climb",
               "swim", "release"]
    while True:
        yield (choice(names), choice(actions))


# Function that takes the previously created
# list, randomly pick one of its elements, remove it from the list, and yields
# it, until the list is empty.
def consume_event(li: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while li:
        sel = choice(li)
        yield sel


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    events: list[tuple[str, str]] = []
    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        if i < 10:
            events.append(event)
    print("\n Built list of 10 events:", events)
    print()
    for eve in consume_event(events):
        print("Got event from list:", eve)
        events.remove(eve)
        print("Remains in list:", events)
