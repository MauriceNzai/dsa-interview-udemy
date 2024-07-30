#!/usr/bin/env python3
"""
This module provides a function to find the first
non-repeating character in a string.
It contains a single function `non_repeating_char` which takes a string and
returns the index of the first character that does not repeat in the string.

Example:
    s = "swiss"
    result = non_repeating_char(s)
    print(result)  # Output: 0 (index of 's')
"""


def non_repeating_char(str):
    """
    Find the index of the first non-repeating character in a string.

    Args:
        s (str): The input string.

    Returns:
        int: The index of the first non-repeating character,
        or None if all characters repeat.

    Example:
        >>> non_repeating_char("swiss")
        0
    """

    # Iterate over each character in the string
    for i in range(len(str)):
        repeat = False
        for j in range(len(str)):
            # Check if the current character is found again in the string
            if str[j] == str[i] and i != j:
                repeat = True
                break

        if repeat is False:
            return i

    return None


# Example usage:
if __name__ == "__main__":
    s = "swiss"
    print(non_repeating_char(s))  # Output: 2 (index of 'w')
