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
    if x < 1 or not nums:
        return None

    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    marias_wins, bens_wins = 0, 0
    for _, n in zip(range(x), nums):
        prime_count = sum(1 for num in range(2, n + 1) if is_prime(num))
        bens_wins += prime_count % 2 == 0
        marias_wins += prime_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
