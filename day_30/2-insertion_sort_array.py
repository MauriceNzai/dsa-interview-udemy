#!/usr/bin/env python3
"""
This module provides a function to perform insertion sort on an array.
The function `insertion_sort_array` takes an array of integers and sorts it in ascending order.

Example usage:
    array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort_array(array)
    print(sorted_array)  # Output: [5, 6, 11, 12, 13]
"""


def insertion_sort_array(array):
    """
    Perform insertion sort on the given array.

    Args:
        array (list of int): The array of integers to be sorted.

    Returns:
        list of int: The sorted array in ascending order.

    Example:
        >>> insertion_sort_array([12, 11, 13, 5, 6])
        [5, 6, 11, 12, 13]
    """
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]

        #
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp

    return array


# Example usage:
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort_array(array)
    print(sorted_array)  # Output: [5, 6, 11, 12, 13]
