#!/usr/bin/python3
"""
prime game.
"""


def isWinner(x, nums):
    """
    Determine the winner of a game of prime number removal.

    Args:
        x (int): The number of rounds of the game.
        nums (list): The set of consecutive integers from 1 to n.

    Returns:
        str or None: The name of the player that won the most rounds, or
        None if the winner cannot be determined.
    """
    # Create a sieve of Eratosthenes to find all prime numbers up to the
    # maximum number in the set.
    sieve = [True] * (max(nums) + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max(nums) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max(nums) + 1, i):
                sieve[j] = False

    # Create a list of the prime numbers in the set.
    primes = [num for num in nums if sieve[num]]

    # Create a list of the multiples of each prime number in the set.
    multiples = []
    for prime in primes:
        multiples += [num for num in nums if num % prime == 0]

    # Create a set of all the prime numbers and their multiples in the set.
    removed = set(primes + multiples)

    # Create a list of the remaining numbers in the set.
    remaining = [num for num in nums if num not in removed]

    # Create a dictionary to store the number of wins for each player.
    wins = {"Maria": 0, "Ben": 0}

    # Play the game.
    for round in range(x):
        # If Maria has no moves, Ben wins the round.
        if not remaining:
            wins["Ben"] += 1
            break

        # Find the smallest prime number in the remaining set.
        smallest_prime = min(remaining)

        # Maria removes the smallest prime number and its multiples
        # from the set.
        for num in remaining:
            if num % smallest_prime == 0:
                removed.add(num)
                remaining.remove(num)

        # If Ben has no moves, Maria wins the round.
        if not remaining:
            wins["Maria"] += 1
            break

        # Ben removes a prime number from the set.
        ben_prime = min(set(nums) - removed)
        removed.add(ben_prime)
        remaining.remove(ben_prime)

    # Determine the winner of the game.
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
