def can_eat(allergic: bool, temp: float) -> bool:
    """Is it safe to eat this food?"""
    return not allergic and temp >= 165.0


print(can_eat(allergic=False, temp=160.0))


def can_order(got_paid: bool, cost: float) -> bool:
    """Can I afford to eat this?"""
    return got_paid or cost < 5.0


print(can_order(got_paid=True, cost=9.0))


def check_first_letter(word: str, letter: str) -> str:
    """Return "match" if letter is first char of word, else retunr "no match"."""
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter(word="happy", letter="s"))
