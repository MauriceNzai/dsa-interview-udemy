#!/usr/bin/env python3
"""
This script implements the quicksort algorithm to sort an array.
"""


def swap_elements(array, i, j):
    """
    Swap the elements at index i and j in the array.

    Args:
        array (list of int): The array in which elements are to be swapped.
        i (int): Index of the first element.
        j (int): Index of the second element.
    """
    array[i], array[j] = array[j], array[i]


def partition_array(array, start=0, end=None):
    """
    Partition the array around a pivot such that elements less than the pivot
    are on the left and elements greater than the pivot are on the right.

    Args:
        array (list of int): The array to be partitioned.
        start (int): Starting index of the array segment.
        end (int): Ending index of the array segment.

    Returns:
        int: The index of the pivot after partitioning.
    """
    if end is None:
        end = len(array) - 1

    middle = (start + end) // 2
    swap_elements(array, start, middle)

    pivot = array[start]
    i = start + 1
    j = end

    while i <= j:
        # In worst case this takes O(n)
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1

        if i < j:
            swap_elements(array, i, j)

    swap_elements(array, start, j)
    return j


def quick_sort(array, start=0, end=None):
    """
    Perform quicksort on the array.

    Args:
        array (list of int): The array to be sorted.
        start (int): Starting index of the array segment.
        end (int): Ending index of the array segment.

    Returns:
        list of int: The sorted array.
    """
    if end is None:
        end = len(array) - 1

    while start < end:
        pivot_index = partition_array(array, start, end)

        # Recurively call quick_sort_array on lower sized subarray
        if pivot_index - start < end - pivot_index:
            quick_sort(array, start, pivot_index - 1)
            start = pivot_index + 1
        else:
            quick_sort(array, pivot_index + 1, end)
            end = pivot_index - 1

    return array


# Example usage:
if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(array)
    print(sorted_array)  # Output: [1, 1, 2, 3, 6, 8, 10]
