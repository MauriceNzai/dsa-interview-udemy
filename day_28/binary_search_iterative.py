#!/usr/bin/env python3
"""
This module provides a function to perform binary search on a sorted array.
It contains a single function `binary_search` which takes a sorted array and a
target value, and returns the index of the target value
if found, or -1 if not found.

Example:
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search(array, target)
    print(result)  # Output: 4
"""


def binary_search(array, target):
    """
    Perform binary search on a sorted array to find the target value.

    Args:
        array (list of int): The sorted array in which to search for the target
        target (int): The target value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.

    Example:
        >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
        4
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(binary_search(array, target))  # Output: 4
