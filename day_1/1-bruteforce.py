#!/usr/bin/env python3
"""
This module provides a function to return a sorted array of the squares of the
input array.
It contains a single function `sorted_squared` which takes an array of integers
and returns a new array with the squares of each number, sorted in
[[Inon-decreasing order.

Example:
    array = [-4, -1, 0, 3, 10]
    result = sorted_squared(array)
    print(result)  # Output: [0, 1, 9, 16, 100]
"""


def sorted_squared(array):
    """
    Return a sorted array of the squares of the input array.

    Args:
        array (List[int]): A list of integers.

    Returns:
        List[int]: A new list of the squares of each number in the input array,
        sorted in non-decreasing order.

    Example:
        >>> array = [-4, -1, 0, 3, 10]
        >>> sorted_squared(array)
        [0, 1, 9, 16, 100]

    This function squares each element of the input array and then sorts the
    resulting array.
    """
    n = len(array)
    result = [0] * n  # Initialize the result array with zeros

    # Square each element and store it in the result array
    for i in range(n):
        result[i] = array[i] ** 2

    # Sort the result array
    result.sort()

    return result


# Example usage:
if __name__ == "__main__":
    array = [-4, -1, 0, 3, 10]
    print(sorted_squared(array))  # Output: [0, 1, 9, 16, 100]
