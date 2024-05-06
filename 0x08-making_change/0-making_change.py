#!/usr/bin/python3
"""Determines the fewest number of coins needed to meet a given
amount total.
"""


def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet the total.

    Args:
    - coins: A list of the values of the coins in your possession.
    - total: The total amount to make change for.

    Returns:
    - The fewest number of coins needed to meet the total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    fewest = 0
    for coin in coins:
        if total <= 0:
            break
        fewest += total // coin
        total %= coin
    if total != 0:
        return -1
    return fewest
