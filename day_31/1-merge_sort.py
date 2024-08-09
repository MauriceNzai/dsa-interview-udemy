#!/usr/bin/env python3
"""
This script implements the merge sort algorithm to sort an array.
"""


def merge_sorted_arrays(left, right):
    """
    Merge two sorted arrays into a single sorted array.

    Args:
        left (list of int): The first sorted array.
        right (list of int): The second sorted array.

    Returns:
        list of int: The merged and sorted array.
    """
    n = len(left)
    m = len(right)
    result = []
    i, j = 0, 0

    # Merge the arrays while both have elements
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (if any) from the left array
    while i < n:
        result.append(left[i])
        i += 1

    # Append remaining elements (if any) from the right array
    while j < m:
        result.append(right[j])
        j += 1

    return result


def merge_sort(array):
    """
    Sort an array using the merge sort algorithm.

    Args:
        array (list of int): The array to be sorted.

    Returns:
        list of int: The sorted array.
    """
    n = len(array)

    # Base Condition: If the array has 1 or 0 elements, it is already sorted.
    if n <= 1:
        return array

    middle = n // 2
    # Recursively split and merge the array
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    # Merge the sorted halves
    return merge_sorted_arrays(left, right)


# Example usage:
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(array)
    print(sorted_array)  # Output: [3, 9, 10, 27, 38, 43, 82]
