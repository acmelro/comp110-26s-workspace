"""EX02 - Chardle - A cute step toward Wordle."""

___author___ = "730859406"

"""Putting it all together to run smoothly."""


def main() -> None:
    return contains_char(user_word=input_word(), user_letter=input_letter())


def input_word() -> str:
    """Prompt the user for a 5-character word and return it."""
    user_word: str = input("Enter a 5-character word.")
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters")
        exit()
    return user_word


# This specific line of code took me a second to figure out but,
# after looking through my notes and trial and fails I was able to get it.
# This made the next two definitions a lot easier.


def input_letter() -> str:
    """Prompt the user for a single character and returns it."""
    user_letter: str = input("Enter a single character.")
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return user_letter


def contains_char(user_word: str, user_letter: str) -> None:
    """Trying to find a specific character in a word"""
    print("Searching for " + user_letter + " in " + user_word)
    count: int = 0
    if user_word[0] == user_letter:
        print(str(user_letter) + " found at index 0")
        count = count + 1
    if user_word[1] == user_letter:
        print(str(user_letter) + " found at index 1")
        count = count + 1
    if user_word[2] == user_letter:
        print(str(user_letter) + " found at index 2")
        count = count + 1
    if user_word[3] == user_letter:
        print(str(user_letter) + " found at index 3")
        count = count + 1
    if user_word[4] == user_letter:
        print(str(user_letter) + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + user_letter + " found in " + user_word)
    else:
        print(str(count) + " instances of " + user_letter + " found in " + user_word)


# The counts in this one also took me a while, but I was eventually able to
# figure it out.
# I was mostly having trouble with where to place the variable, but after trial and error
# I figured it out.

if __name__ == "__main__":
    main()
# At first, I forgot to put parenthesis after the main,
# this caused a little bit of trouble for a second but,
# I eventually figured it out.
