#!/usr/bin/env python3
"""
This module provides a function to perform bubble sort on an array.
The function `bubble_sort` takes an array of integers
and sorts it in ascending order.

Example usage:
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(array)
    print(sorted_array)  # Output: [11, 12, 22, 25, 34, 64, 90]
"""


def bubble_sort(array):
    """
    Perform bubble sort on the given array.

    Args:
        array (list of int): The array of integers to be sorted.

    Returns:
        list of int: The sorted array in ascending order.

    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """

    n = len(array)
    #
    for counter in range(n - 1):
        for i in range(n - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


# Example
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    sorted_array = bubble_sort(array)
    print(sorted_array)  # Output: [5, 6, 11, 12, 13]
