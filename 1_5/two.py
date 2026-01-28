"""Given a list of integers:

nums = [2, 4, 6, 9, 11]


Write a function that:

returns a new list of only odd numbers"""

nums = [2, 4, 6, 9, 11]


def is_odd(nums):
    odd = []

    for num in nums:
        if num%2 == 1:
            odd.append(num)

    return odd