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
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Zero coins needed for zero total

    # Iterate through each coin value
    for coin in coins:
        # Update min_coins for each amount from coin to total
        for amt in range(coin, total + 1):
            min_coins[amt] = min(min_coins[amt], min_coins[amt - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
