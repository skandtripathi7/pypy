
""" Problem

Write a function that takes a number and:

returns "Positive" if > 0

returns "Negative" if < 0

returns "Zero" if the number is 0

What interviewer checks

Can you write a function

Can you use if / elif / else

Do you return values correctly"""


def funct(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"