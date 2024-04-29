"""
This is a short program that outputs a sentence derived from user input.
"""

name: str = input("Enter a name: ")
noun_a: str = input("Enter a noun: ")
noun_b: str = input("Enter another noun: ")
verb_a: str = input("Enter a verb: ")
verb_b: str = input("Enter a verb (past tense): ")
number_a: str = input("Enter a number ")
number_b: str = input("Enter another number ")
times: int

try:
    times = int(number_a) + int(number_b)
    story: str = f"""
    ---------------------------------------------------------------------------------------------------
    There once was a {noun_a} named {name}, who loved to {verb_a} as a living.

    {name} once {verb_b} and won a {noun_b} as a prize.
    Isn't that incredible?

    To add on to that achievement, {name} {verb_b} {times} times has retired from adventures.

    But the story will live on forever...

    ---------------------------------------------------------------------------------------------------
    """
except ValueError:
    story = f"Value Error. Cannot add: {number_a} + {number_b}"

print(story)
