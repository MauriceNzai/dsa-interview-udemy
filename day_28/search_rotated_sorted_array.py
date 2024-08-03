#!/usr/bin/env python3
"""
This module provides a function to perform a search on a rotated sorted array.
It contains a single function `search_rotated_sorted_array` which takes
a rotated sorted array and a target value, and returns the index of the
target value if found, or -1 if not found.

Example:
    array = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = search_rotated_sorted_array(array, target)
    print(result)  # Output: 4
"""


def search_rotated_sorted_array(array, target):
    """
    Perform a search on a rotated sorted array to find the target value.

    Args:
        array (list of int): The rotated sorted array in which to
            search for the target.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.

    Example:
        >>> search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0)
        4
    """
    left = 0
    right = len(array) - 1

    # Perform binary search
    while (left <= right):
        mid = (left + right) // 2

        # Check if mid is the target
        if array[mid] == target:
            return mid

        # Determine which part is sorted
        if array[left] <= array[mid]:
            # left part is sorted
            if target >= array[left] and target < array[mid]:
                # Target is in the left part
                right = mid - 1
            else:
                # Target is in the right part
                left = mid + 1
        #
        else:
            # right part is sorted
            if target <= array[left] and target > array[mid]:
                # Target is in the right part
                left = mid + 1
            else:
                # Target is in the left part
                right = mid - 1

    return -1


# Example usage:
if __name__ == "__main__":
    array = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search_rotated_sorted_array(array, target))  # Output: 4
