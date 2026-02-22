"""Practicing with "while" loops, first challenge question."""

__author__ = "730859406"


def num_instances(phrase: str, search_char: str) -> int:
    """Return the number of times search_char appears in phrase."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1  # if the character is found, add to the count
        index += 1
    return count


def get_evens(numbers: str) -> str:
    """Return only the even numbers in a string of integers."""
    evens: str = ""  # used to store even numbers
    index: int = 0
    while index < len(numbers):
        ch = numbers[index]
        if int(ch) % 2 == 0:
            evens += ch
        index += 1
    return evens
