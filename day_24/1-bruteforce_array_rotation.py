#!/usr/bin/env python3
"""
This module provides a function to rotate an array to the right by a given
number of steps.
It contains a single function `rotate_array` which takes an array and an
integer `k` and returns the array rotated to the right by `k` steps.

Example:
    array = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result = rotate_array(array, k)
    print(result)  # Output: [5, 6, 7, 1, 2, 3, 4]
"""


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

    This function handles cases where k is greater than the length of the array
    by using modulo operation.
    It also ensures that the original array is rotated in place.
    """
    length = len(array)
    k = k % length

    #  Copy the last k elements to a temporary list
    temp = array[length - k:]

    # Shift the remaining elements to the right starting from the highest index
    for i in reversed(range(length - k)):
        array[i + k] = array[i]

    # Copy the temporary list back to the beginning of the array
    for i in range(k):
        array[i] = temp[i]

    return array


# Example usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate_array(array, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
