#!/usr/bin/env python3
"""
This module provides functions to find the leftmost and rightmost
indices of a target value in a sorted array.
It contains functions 'find_left_extrem', 'find_right_extreme', and
'binary_search_range_iterative' which help in finding the
range of indices for a target value in the array.

Example usage:
    array = [4, 5, 6, 7, 7, 7, 8, 10]
    target = 7
    result = binary_search_range_iterative(array, target)
    print(result)  # Output: [3, 5]
"""


def find_left_extreeme(array, target):
    """
    Find the leftmost index of the target value in the sorted array.

    Args:
        array (list of int): The sorted array to search within.
        target (int): The target value to search for.

    Returns:
        int: The leftmost index of the target value if found, otherwise -1.
    """
    left = 0
    right = len(array) - 1

    #
    while(left <= right):
        mid = (left + right) // 2
        #
        if array[mid] == target:
            if mid == 0 or array[mid - 1] != target:
                return mid
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_right_extreeme(array, target):
    """
    Find the rightmost index of the target value in the sorted array.

    Args:
        array (list of int): The sorted array to search within.
        target (int): The target value to search for.

    Returns:
        int: The rightmost index of the target value if found, otherwise -1.
    """
    left = 0
    right = len(array) - 1

    #
    while (left <= right):
        mid = (left + right) // 2
        #
        if array[mid] == target:
            if mid == len(array) - 1 or array[mid + 1] != target:
                return mid
            left = mid + 1
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_range_iterative(array, target):
    """
    Find the range of indices (leftmost and rightmost) for
    the target value in the sorted array.

    Args:
        array (list of int): The sorted array to search within.
        target (int): The target value to search for.

    Returns:
        list of int: A list containing the leftmost and rightmost
        indices of the target value.
    """
    left_extreeme = find_left_extreeme(array, target)
    right_extreeme = find_right_extreeme(array, target)
    return [left_extreeme, right_extreeme]


# Example usage:
if __name__ == "__main__":
    array = [4, 5, 6, 7, 7, 7, 8, 10]
    target = 7
    print(binary_search_range_iterative(array, target))  # Output: [3, 5]
