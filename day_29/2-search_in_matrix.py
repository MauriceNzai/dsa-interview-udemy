#!/usr/bin/env python3
"""
This module provides a function to search for a
target value in a sorted 2D matrix.
The function `search_in_matrix` uses binary search to
identify if the target value exists within the matrix.

Example usage:
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    result = search_in_matrix(matrix, target)
    print(result)  # Output: True
"""


def search_in_matrix(matrix, target):
    """
    Search for a target value in a sorted 2D matrix.

    Args:
        matrix (list of list of int): The sorted 2D matrix.
        target (int): The target value to search for.

    Returns:
        bool: True if the target is found, False otherwise.
    """
    columns = len(matrix[0])
    rows = len(matrix)

    # Binary search to identify relevent row where target may be found
    top = 0
    bottom = rows - 1
    while(top <= bottom):
        mid = (top + bottom) // 2

        # Check if target is in the current row
        if target < matrix[mid][0]:
            bottom = mid - 1
        elif target > matrix[mid][columns - 1]:
            top = mid + 1
        else:
            break
    if top > bottom:
        return False

    #  Binary search the identify row to find if target is present
    left = 0
    right = columns - 1

    #
    while(left <= right):
        middle = (left + right) // 2

        if target == matrix[mid][middle]:
            return True
        elif target < matrix[mid][middle]:
            right = middle - 1
        else:
            left = middle + 1
    return False


# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3
    print(search_in_matrix(matrix, target))  # Output: True
