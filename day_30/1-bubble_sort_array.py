#!/usr/bin/env python3
"""
This module provides a function to perform bubble sort on an array.
The function `bubble_sort_array` takes an array of
integers and sorts it in ascending order.

Example usage:
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort_array(array)
    print(sorted_array)  # Output: [11, 12, 22, 25, 34, 64, 90]
"""


def bubble_sort_array(array):
    """
    Perform bubble sort on the given array.

    Args:
        array (list of int): The array of integers to be sorted.

    Returns:
        list of int: The sorted array in ascending order.

    Example:
        >>> bubble_sort_array([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    sorted = False
    counter = 0
    
    #
    while not sorted:
        sorted = True
        #
        for i in range(len(array) - 1 - counter):
            #
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        counter += 1
    return array


# Example usage:
if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort_array(array)
    print(sorted_array)  # Output: [11, 12, 22, 25, 34, 64, 90]
