#!/usr/bin/python3
"""
Make change determines the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """Returns the fewest number of coins otherwise -1"""
    if total <= 0:
        return 0

    coins.reverse()
    count = 0

    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1

    if total == 0:
        return count
    else:
        return -1
