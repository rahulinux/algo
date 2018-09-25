#!/usr/bin/env python
import random

"""
Binary Search
"""


def binary_search(lst, item):
    """
    Return position of item from list
    """
    low = 0
    high = len(lst)-1

    while high >= low:
        guess = (high+low)/2
        print guess, lst[guess]
        if item == lst[guess]:
            return guess
        if item > lst[guess]:
            low = guess + 1
        if item < lst[guess]:
            high = guess - 1


lst = [12, 17, 50, 127, 284, 1289, 1548, 4957, 8740, 25847, 26395, 34759, 46595, 50363, 57498, 95465]
search_for = random.choice(lst)
print lst, search_for
print binary_search(lst, search_for)

