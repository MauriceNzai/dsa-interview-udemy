#!/usr/bin/env python3
"""
This module provides a function to determine if two strings are isomorphic.
Two strings are isomorphic if the characters in one string can be replaced
to get the second string.

Example:
    s = "egg"
    t = "add"
    result = isomorphic_strings(s, t)
    print(result)  # Output: True
"""


def isomorphic_strings(s, t):
    """
    Determine if two strings s and t are isomorphic.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if the strings are isomorphic, False otherwise.

    Example:
        >>> s = "egg"
        >>> t = "add"
        >>> isomorphic_strings(s, t)
        True

    Two strings are isomorphic if the characters in s can be replaced to get t.
    No two characters may map to the same character, but a character may map to
    itself.
    """
    if len(s) != len(t):
        return False

    s_hash, t_hash = {}, {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s not in s_hash:
            s_hash[char_s] = char_t
        if char_t not in t_hash:
            t_hash[char_t] = char_s
        if s_hash[char_s] != char_t or t_hash[char_t] != char_s:
            return False
    return True


# Example Usage
if __name__ == "__main__":
    s = "egg"
    t = "add"
    print(isomorphic_strings(s, t))  # Output: True
