# Find if a string is rotated string of another string


def is_rotated_string(first: str, second: str) -> bool:
    first += first
    if first.__contains__(second) and len(first) == 2 * len(second):
        return True


print(is_rotated_string("waterbottle", "erbottlewat"))
