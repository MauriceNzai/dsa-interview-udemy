#!/usr/bin/env python3
"""
This module provides a function to check if a given array is monotonic.
A monotonic array is one that is either entirely non-increasing or
non-decreasing.

Example:
    array = [1, 2, 2, 3]
    result = monotonic_array(array)
    print(result)  # Output: True
"""


def monotonic_array(array):
    """
    Check if the input array is monotonic.

    Args:
        array (List[int]): A list of integers.

    Returns:
        bool: True if the array is monotonic, False otherwise.

    Example:
        >>> array = [1, 2, 2, 3]
        >>> monotonic_array(array)
        True

    An array is considered monotonic if it is either entirely
    non-increasing or non-decreasing.
    """
    n = len(array)
    if n == 0:  # Check if the array is empty
        return True

    increasing = decreasing = True

    for i in range(1, n):
        if array[i] > array[i - 1]:
            decreasing = False
        if array[i] < array[i - 1]:
            increasing = False

    return increasing or decreasing


# Example usage:
if __name__ == "__main__":
    array = [1, 2, 2, 3]
    print(monotonic_array(array))  # Output: True
