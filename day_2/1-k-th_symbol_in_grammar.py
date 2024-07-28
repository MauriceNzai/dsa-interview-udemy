#!/usr/bin/env python3
"""
This module provides a function to determine the k-th symbol in the n-th row of
a special binary sequence.
It contains a single function `kth_symbol` which takes the row number `n` and
the position `k` and returns the k-th symbol in the n-th row.

Example:
    n = 4
    k = 5
    result = kth_symbol(n, k)
    print(result)  # Output: 1
"""


def kth_symbol(n, k):
    """
    Determine the k-th symbol in the n-th row of a special binary sequence.

    Args:
        n (int): The row number (1-indexed).
        k (int): The position in the row (1-indexed).

    Returns:
        int: The k-th symbol in the n-th row (0 or 1).

    Example:
        >>> kth_symbol(4, 5)
        1

    The function uses a recursive approach to find the k-th symbol by
    leveraging the properties of the sequence. The sequence is built such that
    each row is derived from the previous row.
    The first half of the row is the same as the previous row, and the
    second half is the binary complement.
    """
    if n == 1:
        return 0

    length = 2 ** (n - 1)
    mid = length // 2

    # If k is in the first half, it is the same as
    # the k-th symbol in the previous row
    if k <= mid:
        return kth_symbol(n-1, k)
    # If k is in the second half, it is the complement of
    # the (k - mid)-th symbol in the previous row
    else:
        return int(not kth_symbol(n - 1, k - mid))
        # return 1 - kth_symbol(n - 1, k - mid)


# Example usage:
if __name__ == "__main__":
    n = 4
    k = 5
    print(kth_symbol(n, k))  # Output: 1
