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
age: int

try:
    age = int(number_a) + int(number_b)
    story: str = f"""
    ---------------------------------------------------------------------------------------------------
    This is a story about {name}, a strong (and beautiful) {noun_a} who loved to {verb_a}.

    {name} once {verb_b} and won a {noun_b} as a prize.
    Isn't that incredible?

    Today, {name} is {age} years old and has retired from adventures.

    But the story will live on forever...

    ---------------------------------------------------------------------------------------------------
    """
except ValueError:
    story = f"Value Error. Cannot add: {number_a} + {number_b}"

print(story)
