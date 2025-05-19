"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-startDigit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-startDigit numbers.
"""


def is_palindrome(n):
    """function helper for fourth Euler problem."""
    rn = 0
    on = n

    while n != 0:
        remainder = int(n % 10)
        rn = (rn * 10) + remainder
        n = int(n / 10)

    return on == rn


def Euler004(n):
    """Solution of fourth Euler problem."""
    startDigit = pow(10, n - 1)
    endDigit = pow(10, n)
    max = 0

    for i in range(startDigit, endDigit):
        for j in range(startDigit, endDigit):
            if is_palindrome(i * j) and (i * j > max):
                max = i * j

    return max
