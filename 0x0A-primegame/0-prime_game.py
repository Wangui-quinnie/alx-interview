#!/usr/bin/python3

""" A function that determines who the winner of each game is.
"""


def isWinner(x, nums):
    """
    Determines the winner of each round of the game.

    Args:
        x (int): The number of rounds to play.
        nums (list): List of integers representing the upper bounds
        for each round.

    Returns:
        str or None: The name of the player that won the most rounds
        (Maria or Ben).
                     Returns None if the winner cannot be determined.

    Raises:
        None

    """

    def is_prime(n):
        """
        Check if a number is prime.

        Args:
            n (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.

        """
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

    def calculate_winner(round_nums):
        """
        Calculate the winner of each round based on the number of primes.

        Args:
            round_nums (list): List of integers representing the upper bounds
            for each round.

        Returns:
            str or None: The name of the player that won the most rounds
            (Maria or Ben).
                         Returns None if the winner cannot be determined.

        """
        maria_wins = 0
        ben_wins = 0
        for n in round_nums:
            prime_count = sum(1 for num in range(2, n + 1) if is_prime(num))
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

    return calculate_winner(nums)
