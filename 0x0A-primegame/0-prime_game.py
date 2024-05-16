#!/usr/bin/python3

"""prime game module."""


def isWinner(x, nums):
    """
    Determine the winner of the game based on the number of prime
    numbers in each round.

    Args:
        x (int): The number of rounds of the game.
        nums (list): The set of consecutive integers from 1 to n for
        each round.

    Returns:
        str or None: The name of the player that won the most rounds, or
        None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(
           1 for num in range(2, n + 1)
           if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        )

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
