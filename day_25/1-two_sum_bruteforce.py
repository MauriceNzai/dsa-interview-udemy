#!/usr/bin/env python3
"""
This module provides a function to find two indices in an array such that the
elements at those indices add up to a specific target value.
It contains a single function `two_sum` which takes an array of integers and a
target value, and returns the indices of the two numbers
that add up to the target.

Example:
    array = [2, 7, 11, 15]
    target = 9
    result = two_sum(array, target)
    print(result)  # Output: [0, 1]
"""


def two_sum(array, target):
    """
    Find two indices in the array such that the elements at those indices add
    up to the target value.

    Args:
        array (List[int]): A list of integers.
        target (int): The target sum value.

    Returns:
        List[int]: A list containing the indices of the two numbers that add
        up to the target value. Returns an empty list if no such indices exist.

    Example:
        >>> array = [2, 7, 11, 15]
        >>> target = 9
        >>> two_sum(array, target)
        [0, 1]

    This function uses a brute-force approach, checking all pairs of indices to
    find the two numbers that add up to the target value.
    """
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]
    return []


# Example usage:
if __name__ == "__main__":
    array = [2, 7, 11, 15]
    target = 9
    print(two_sum(array, target))  # Output: [0, 1]
