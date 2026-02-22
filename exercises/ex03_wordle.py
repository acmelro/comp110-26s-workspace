"""Coding a word guessing game, based off wordle using while loops and f'strings."""

__author__ = "730859406"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    max_turns: int = 6
    won: bool = False
    while (turn <= max_turns) and (not won):  # prompt for correct-length guess
        print(f"=== Turn {turn}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))  # print emojis based off guess
        if guess == secret:  # check if won or not
            won = True
        else:
            turn += 1
    if won:
        print(f"You won in {turn}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Allows someone to enter a guess that is the correct length."""
    guess = input(f"Enter a {secret_word_len}-letter guess: ")
    # uses an f-string to incorporate the correct length for the word
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Returns True if the single-character string 'char_guess' is found
    in the string 'secret_word'. If not, returns False."""
    assert len(char_guess) == 1  # ensure the second one is exactly one character long
    for letter in secret_word:  # check each index of the search string for the char
        if letter == char_guess:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Creates emojies for the guess word, green for correct in right place,
    yellow if correct in wrong place, white for incorrect."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    result: str = ""
    index: int = 0
    while index < len(secret):  # check characters, returns green box if correct
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            # check characters, returns yellow box if almost correct
            result += YELLOW_BOX
        else:  # check characters, returns white box if incorrect
            result += WHITE_BOX
        index += 1
    return result


if __name__ == "__main__":
    main(secret="codes")
