"""A simple program with a function call"""


def perimeter(length: float, width: float) -> float:
    """Calculates the perimeter of a rectangle"""
    return 2 * length + 2 * width


print(perimeter(length=10.0, width=8.0))
