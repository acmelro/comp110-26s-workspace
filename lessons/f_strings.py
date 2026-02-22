def mystery(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + mystery(n - 1)


print(mystery(n=3))


def my_func(x: int) -> int:
    if x > 10:
        return 0
    return x + my_func(x=x + 1)


print(my_func(x=0))


def icarus(x: int) -> int:
    print(f"Height: {x}")
    return icarus(x=x + 1)


def safe_icarus(x: int) -> int:
    if x >= 2:
        return 1
    else:
        return 1 + safe_icarus(x=x + 1)


print(safe_icarus(x=0))


"""Writing Code for Quiz 1 Review"""


def goldilocks(porridge_temp: int, low: int, high: int) -> str:
    if porridge_temp < low:
        return "too cold!"
    elif porridge_temp > high:
        return "too hot!"
    else:
        return "just right!"


print(goldilocks(10, 5, 15))


def initials(first: str, middle: str, last: str) -> str:
    if middle == "":
        return f"{first[0]}{last[0]}"
    else:
        return f"{first[0]}{middle[0]}{last[0]}"


print(initials("Anna", "Claire", "Melroy"))


def shipping_cost(weight: float, has_label: bool, international: bool) -> float:
    if has_label is False:
        return 0.0
    if international is False and weight <= 1:
        return 5.0
    if international is False and weight > 5:
        return 20.0
    if international is False and 1 < weight <= 5:
        return 10.0
    if international is True and weight <= 1:
        return 10.0 + 5.0
    if international is True and weight > 5:
        return 10.0 + 10.0
    if international is True and 1 < weight <= 5:
        return 10.0 + 20.0
    return 0.0


print(shipping_cost(0.5, True, False))
print(shipping_cost(weight=3.0, has_label=True, international=True))
print(shipping_cost(weight=8.0, has_label=True, international=True))
print(shipping_cost(weight=2.0, has_label=False, international=False))
