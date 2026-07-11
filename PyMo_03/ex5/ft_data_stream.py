import typing as ty
import random as ra


def gen_event():
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    actions = ["eat", "sleep", "grab", "run", "move", "climb",
               "swim", "release"]
    n_len = len(names)
    a_len = len(actions)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in gen_event():
        print(i)
