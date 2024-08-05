#!/usr/bin/env python3
"""
This module provides functions to find the leftmost and rightmost
indices of a target value in a sorted array.
It contains functions 'find_left_extreme', 'find_right_extreme', and
'search_for_range' which help in finding the range of indices for
a target value in the array.

Example usage:
    array = [4, 5, 6, 7, 7, 7, 8, 10]
    target = 7
    result = search_for_range(array, target)
    print(result)  # Output: [3, 5]
"""


def find_left_extreeme(array, target, result, left, right):
    """
    Find the leftmost index of the target value in the sorted array.

    Args:
        array (list of int): The sorted array to search within.
        target (int): The target value to search for.
        result (list of int): The result list to store the index.
        left (int): The left boundary for the search.
        right (int): The right boundary for the search.

    Returns:
        None
    """
    # Base Case
    if left > right:
        return

    mid = (left + right) // 2
    #
    if array[mid] == target:
        #
        if mid == 0:
            result[0] == 0
        elif array[mid - 1] == target:
            find_left_extreeme(array, target, result, left, mid - 1)
        else:
            result[0] = mid
    elif target < array[mid]:
        find_left_extreeme(array, target, result, left, mid - 1)
    else:
        find_left_extreeme(array, target, result, mid + 1, right)


def find_right_extreeme(array, target, result, left, right):
    """
    Find the rightmost index of the target value in the sorted array.

    Args:
        array (list of int): The sorted array to search within.
        target (int): The target value to search for.
        result (list of int): The result list to store the index.
        left (int): The left boundary for the search.
        right (int): The right boundary for the search.

    Returns:
        None
    """
    # Base Case
    #
    if left > right:
        return

    mid = (left + right) // 2
    #
    if array[mid] == target:
        #
        if mid == len(array) - 1:
            result[1] = mid
        elif array[mid + 1] == target:
            find_right_extreeme(array, target, result, mid + 1, right)
        else:
            result[1] = mid

    elif target < array[mid]:
        find_right_extreeme(array, target, result, mid - 1, right)
    else:
        find_right_extreeme(array, target, result, mid + 1, right)


def search_for_range(array, target):
    """
    Find the range of indices (leftmost and rightmost) for
    the target value in the sorted array.

    Args:
        array (list of int): The sorted array to search within.
        target (int): The target value to search for.

    Returns:
        list of int: A list containing the leftmost and
        rightmost indices of the target value.
    """
    result = [-1, -1]
    find_left_extreeme(array, target, result, 0, len(array) - 1)
    find_right_extreeme(array, target, result, 0, len(array) - 1)
    return result


# Example usage:
if __name__ == "__main__":
    array = [4, 5, 6, 7, 7, 7, 8, 10]
    target = 7
    print(search_for_range(array, target))
