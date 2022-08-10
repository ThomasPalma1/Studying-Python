from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Ana", "age": 24},
    {"name": "Lucas", "age": 30},
    {"name": "Miguel", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Miguel", itemgetter("name")))
