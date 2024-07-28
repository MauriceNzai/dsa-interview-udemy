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

    The function uses a recursive helper function to simulate the
    elimination process.
    """
    def helper(n):
        """
        Recursively determine the position of winner in the Josephus problem.

        Args:
            n (int): The number of people remaining.

        Returns:
            int: The position of the last remaining person (0-indexed).
        """
        # Base condition:  only one person remains[[O
        if n == 1:
            return 0

        # Recursive case: eliminate every k-th person and find the position
        return (helper(n - 1) + k) % n
    # The result from the helper function is 0-indexed, so we add 1 to make
    # it 1-indexed
    return helper(n) + 1


# Example usage:
if __name__ == "__main__":
    n = 5
    k = 2
    print(find_the_winner(n, k))  # Output: 3
