#!/usr/bin/env python3
"""
This module provides a function to group a list of strings into anagrams.
It contains a single function `group_anagrams` which takes a list of strings
and returns a list of lists, where each sublist contains anagrams.

Example:
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strings)
    print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""


def group_anagrams(strings):
    """
    Group a list of strings into anagrams.

    Args:
        strings (list of str): The input list of strings.

    Returns:
        list of list of str: A list of lists, each sublist contains anagrams.

    Example:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    if len(strings) == 0:
        return []

    # Sort each string in the list and use the sorted string as the key
    sorted_strings = [''.join(sorted(i)) for i in strings]

    hash = {}
    # Group strings by their sorted version
    for i in range(len(sorted_strings)):
        #
        if sorted_strings[i] in hash:
            hash[sorted_strings[i]].append(strings[i])
        else:
            hash[sorted_strings[i]] = [strings[i]]

    #
    return list(hash.values())


# Example usage:
if __name__ == "__main__":
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [['eat', 'tea', 'ate'], ['tan'    , 'nat'], ['bat']]
    print(group_anagrams(strings))
