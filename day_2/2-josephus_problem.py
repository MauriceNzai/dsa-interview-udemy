#!/usr/bin/env python3
"""
This module provides a function to determine the winner
of the Josephus problem.
It contains single function `find_the_winner` which takes the number of people
`n` and the step count `k`, and returns the position of the winner.

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

    # Create an array representing the people standing in the circle
    array = [i + 1 for i in range(n)]

    def helper(array, start_index):
        """
        Recursively eliminate every k-th person until only one person remains.

        Args:
            array (List[int]): The list of remaining people.
            start_index (int): The index to start counting from.

        Returns:
            int: The position of the last remaining person.
        """
        # base case: only one person remains
        if len(array) == 1:
            return array[0]

        # recursive case
        # Calculate the index of the person to eliminate
        index_to_remove = (start_index + k - 1) % len(array)

        #  Remove the person from the circle
        del array[index_to_remove]

        # Continue the process with the remaining people
        return helper(array, index_to_remove)

    return helper(array, 0)


# Example usage:
if __name__ == "__main__":
    n = 5
    k = 2
    print(find_the_winner(n, k))  # Output: 3
