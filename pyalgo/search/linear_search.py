from typing import Any


def linear_search(array: list, target: Any) -> int:
    for i, value in enumerate(array):
        if target == value:
            return i
    return -1