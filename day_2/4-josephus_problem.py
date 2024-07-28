#!/usr/bin/env python3
"""
This module provides a function to determine the winner of the Josephus problem
It contains a single function `find_the_winner` which takes the number of
people `n` and the step count `k`, and returns the position of the winner.

Example:
    n = 5
    k = 2
    result = find_the_winner(n, k)
    print(result)  # Output: 3
"""


def find_the_winner(n, k):
    """
    Determine the winner of the Josephus problem.

    Args:
        n (int): The number of people standing in the circle.
        k (int): The step count to determine which person will be eliminated.

    Returns:
        int: The position of the winner (1-indexed).

    Example:
        >>> find_the_winner(5, 2)
        3

    The function uses an iterative approach to simulate the elimination process
    """
    winner = 0
    for i in range(2, n + 1):
        winner = (winner + k) % i

    return winner + 1


# Example usage:
if __name__ == "__main__":
    n = 5
    k = 2
    print(find_the_winner(n, k))  # Output: 3
