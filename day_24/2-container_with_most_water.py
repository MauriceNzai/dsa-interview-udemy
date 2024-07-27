#!/usr/bin/env python3
"""
This module provides a function to find the maximum area of water that
can be contained between two vertical lines on the x-axis.
It contains a single function `max_area` which takes an array representing the
heights of the lines and returns the maximum area of water that can be trapped.

Example:
    array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = max_area(array)
    print(result)  # Output: 49
"""


def max_area(array):
    """
    Find the maximum area of water that can be contained between
    two vertical lines.

    Args:
        array (List[int]): A list of integers representing the
        heights of the lines.

    Returns:
        int: The maximum area of water that can be contained.

    Example:
        >>> array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        >>> max_area(array)
        49

    The function uses a brute-force approach to calculate the area by
    considering every possible pair of lines and finding the maximum area.
    """
    max_area = 0
    n = len(array)

    # Check each pair of lines to find the maximum area
    for i in range(n - 1):
        #
        for j in range(i + 1, n):
            # Calculate the area between the lines at index i and j
            area = min(array[i], array[j]) * (j - i)
            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)

    return max_area


# Example usage:
if __name__ == "__main__":
    array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(array))  # Output: 49
