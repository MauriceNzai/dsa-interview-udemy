#!/usr/bin/env python3
"""
This module provides functions to reverse and rotate an array.
It contains two functions: `reverse_array` to reverse a portion of the array &
`rotate_array` to rotate entire array to the right by given number of steps.

Example:
    array = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result = rotate_array(array, k)
    print(result)  # Output: [5, 6, 7, 1, 2, 3, 4]
"""


def reverse_array(array, start, end):
    """
    Reverse the elements of the array from index `start` to index `end`.

    Args:
        array (List[int]): The list of integers to be reversed.
        start (int): The starting index of the portion to reverse.
        end (int): The ending index of the portion to reverse.

    Returns:
        List[int]: The array with the specified portion reversed.

    Example:
        >>> array = [1, 2, 3, 4, 5]
        >>> reverse_array(array, 1, 3)
        [1, 4, 3, 2, 5]
    """

    #
    while(start < end):
        #
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    #
    return array


def rotate_array(array, k):
    """
    Rotate the array to the right by k steps.

    Args:
        array (List[int]): A list of integers.
        k (int): The number of steps to rotate the array.

    Returns:
        List[int]: The rotated array.

    Example:
        >>> array = [1, 2, 3, 4, 5, 6, 7]
        >>> k = 3
        >>> rotate_array(array, k)
        [5, 6, 7, 1, 2, 3, 4]

    This function rotates the array in place by:
        first reversing the entire array,
        then reversing the first k elements, and
        finally reversing the remaining elements.
    """
    n = len(array)
    if n == 0:
        return []

    k = k % n

    # Reverse the entire array
    reverse_array(array, 0, n - 1)

    # Reverse the first k elements
    reverse_array(array, 0, k - 1)

    # Reverse the remaining elements
    reverse_array(array, k, n - 1)

    return array


# Example usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate_array(array, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
