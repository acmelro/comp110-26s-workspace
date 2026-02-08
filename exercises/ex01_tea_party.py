"""Finding out how much money I will need for tea party supplies"""

__author__ = "730859406"


def main_planner(guests: int) -> None:
    """Putting everything together in one cohesive planner."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # All of these print functions took me the longest, tried it a few times without
    # the "str()" function and was getting quite frustated, eventually figured it
    # out by looking at my notes and trying a few things.
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    # got stuck on this one, tried to call back starting with "tea_count", wasn't
    # working so I tried to call back the original "tea_bags" and "treats"
    # functions, which ended up working.
    return None


def tea_bags(people: int) -> int:
    """Seeing how many tea bags I will need."""
    return 2 * people


def treats(
    people: int,
) -> int:
    # First time I ran into some trouble,
    # some of it was my code, some of it was the fact
    # that I forgot to reload my trailhead every time I updated the code.
    # Eventually figured it out.
    """Seeing how many treats I will need."""
    int(people)
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Seeing how much both the tea bags and treats will cost"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
