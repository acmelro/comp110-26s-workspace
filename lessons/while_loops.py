"""Practice w/ "while" loops to iterate over a string"""


def find_small_card(cards: str) -> int:
    index: int = 0
    low_card: int = int(cards[0])  # converst 1st character in cards to int
    while index < len(cards):
        current_card: int = int(cards[index])
        if current_card < low_card:
            low_card = current_card
        index = index + 1
    return low_card


print(find_small_card(cards="329403294"))
