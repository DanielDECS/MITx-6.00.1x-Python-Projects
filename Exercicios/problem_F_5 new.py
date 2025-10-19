"""
Problem 3
0.0/10.0 points (graded)
Implement a function that meets the specifications below.

"""


def sum_digits(s):
    sum = 0
    for i in s:
        try:
            sum += int(i)
        except ValueError:
            None
    return sum