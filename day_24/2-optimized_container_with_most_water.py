#!/usr/bin/env python3
"""
This module provides a function to find the maximum area of water that can be
contained between two vertical lines on the x-axis using an optimal approach.
It contains a single function `max_area_optimum` which takes an array
representing the heights of the lines and returns the maximum area of
water that can be trapped.

Example:
    array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = max_area_optimum(array)
    print(result)  # Output: 49
"""


def max_area_optimum(array):
    """
    Find the maximum area of water that can be contained between two vertical
    lines using an optimal approach.

    Args:
        array (List[int]): A list of integers representing the
        heights of the lines.

    Returns:
        int: The maximum area of water that can be contained.

    Example:
        >>> array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        >>> max_area_optimum(array)
        49

    The function uses a two-pointer approach to calculate the area by moving
    the pointers inward from the ends of the array and finding th maximum area.
    """
    left = 0
    right = len(array) - 1
    max_area = 0

    # Move the two pointers towards each other
    while(left < right):
        # Calculate the area between the lines at index left and right
        area = min(array[left], array[right]) * (right - left)

        # Update the maximum area if the current area is larger
        max_area = max(max_area, area)

        # Move the pointer pointing to the shorter line inward
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Example usage:
if __name__ == "__main__":
    array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area_optimum(array))  # Output: 49
