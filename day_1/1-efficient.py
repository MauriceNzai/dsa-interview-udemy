#!/usr/bin/env python3
"""
This module provides a function to return a sorted array of the squares of the
input array.
It contains a single function `sorted_squared` which takes an array of integers
and returns a new array with the squares of each number, sorted in
non-decreasing order.

Example:
    array = [-4, -1, 0, 3, 10]
    result = sorted_squared(array)
    print(result)  # Output: [0, 1, 9, 16, 100]
"""


def sorted_squared(array):
    """
    Return a sorted array of the squares of the input array.

    Args:
        array (List[int]): A list of integers sorted in non-decreasing order.

    Returns:
        List[int]: A new list of the squares of each number in the input
        array, sorted in non-decreasing order.

    Example:
        >>> array = [-4, -1, 0, 3, 10]
        >>> sorted_squared(array)
        [0, 1, 9, 16, 100]

    This function uses a two-pointer approach to fill a result array from the
    end, comparing the absolute values of elements from both ends of the
    input array.
    """
    n = len(array)
    i, j = 0, n - 1  # i and j points first and last array indices respectively
    result = [0] * n  # initialize result array with 0

    # fill result array from the last index
    # If value of i squared greater than j squared, largest element of result
    # array is filled, i increamented or j decreaented as appropriate
    for k in reversed(range(n)):
        if array[i] ** 2 > array[j] ** 2:
            result[k] = array[i] ** 2
            i += 1
        else:
            result[k] = array[j] ** 2
            j -= 1

    return result


# Example usage:
if __name__ == "__main__":
    array = [-4, -1, 0, 3, 10]
    print(sorted_squared(array))  # Output: [0, 1, 9, 16, 100]
