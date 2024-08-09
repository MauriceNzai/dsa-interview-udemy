#!/usr/bin/env python3
"""
Perform selection sort on the given list of numbers.

    Args:
        nums (list of int): The list of integers to be sorted.

    Returns:
        list of int: The sorted list in ascending order.

    Example:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
"""


def selection_sort(nums):
    """
    Perform selection sort on the given list of numbers.

    Args:
        nums (list of int): The list of integers to be sorted.

    Returns:
        list of int: The sorted list in ascending order.

    Example:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
    """
    n = len(nums)
    i = 0
    #
    while i < n - 1:
        smallest = i
        # Find index of the smallest element in the remaining unsorted array
        for j in range(i + 1, n):
            if nums[j] < nums[smallest]:
                smallest = j
        # Swap the found smallest element with the first element.
        if i != smallest:
            nums[i], nums[smallest] = nums[smallest], nums[i]

        i += 1

    return nums


# Example usage:
if __name__ == "__main__":
    array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(array)
    print(sorted_array)  # Output: [11, 12, 22, 25, 64]
