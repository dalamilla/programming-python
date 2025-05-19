"""
2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""


def Euler005(n):
    """Solution of fifth Euler problem."""
    found = True
    number = 0

    while found:
        i = 1
        number += n

        while number % i == 0 and i <= n:
            if i == n:
                found = False
            i += 1

    return number
