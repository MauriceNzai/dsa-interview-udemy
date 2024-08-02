#!/usr/bin/env python3
"""
This module provides a function to check if a given string is a palindrome.
It contains a single function `is_palindrome` which takes a string and
returns a boolean indicating whether the string is a palindrome.

Example:
    s = "abcba"
    result = is_palindrome(s)
    print(result)  # Output: True
"""


def is_palindrome(s):
    """
    Check if a given string is a palindrome.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Example:
        >>> is_palindrome("abcba")
        True
    """
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


# Example usage:
if __name__ == "__main__":
    s = "abcba"
    print(is_palindrome(s))  # Output: True
