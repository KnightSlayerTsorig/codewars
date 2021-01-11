# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

from collections import Counter


def find_it(seq):
    a = dict(Counter(seq))
    for num, times in a.items():
        if times % 2 != 0:
            solution = int(num)
            return solution


