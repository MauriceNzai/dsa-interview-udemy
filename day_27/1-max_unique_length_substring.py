#!/usr/bin/env python3
"""
This module provides a function to find the length of the longest substring
without repeating characters in a given string.
It contains a single function `max_unique_length_substring` which
takes a string and returns the length of the longest
substring with all unique characters.

Example:
    s = "abcabcbb"
    result = max_unique_length_substring(s)
    print(result)  # Output: 3
"""


def max_unique_length_substring(string):
    """
    Find the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring with all unique characters.

    Example:
        >>> max_unique_length_substring("abcabcbb")
        3
    """
    max_len = 0
    start = 0
    characters = {}

    for i in range(len(string)):
        char = string[i]
        if char in characters:
            start = max(start, characters[char] + 1)

        max_len = max(max_len, i - start + 1)
        characters[char] = i

    return max_len


# Example usage:
if __name__ == "__main__":
    s = "abcabcbb"
    print(max_unique_length_substring(s))  # Output: 3
