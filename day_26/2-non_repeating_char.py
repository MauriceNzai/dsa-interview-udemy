#!/usr/bin/env python3
"""
This module provides a function to find the first
non-repeating character in a string.
It contains a single function `non_repeating_char` which takes a string and
returns the index of the first character that does not repeat in the string.

Example:
    s = "swiss"
    result = non_repeating_char(s)
    print(result)  # Output: 2 (index of 'w')
"""


def non_repeating_char(str):
    """
    Find the index of the first non-repeating character in a string.

    Args:
        s (str): The input string.

    Returns:
        int: The index of the first non-repeating character, or
        None if all characters repeat.

    Example:
        >>> non_repeating_char("swiss")
        2
    """
    # Dictionary to store the frequency of each character
    char_count = {}

    # First pass: count the frequency of each character
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # # Second pass: find the first character with a count of 1
    for i in range(len(str)):
        if char_count[str[i]] == 1:
            return i
    return None


# Example usage:
if __name__ == "__main__":
    s = "swiss"
    print(non_repeating_char(s))  # Output: 2 (index of 'w')
