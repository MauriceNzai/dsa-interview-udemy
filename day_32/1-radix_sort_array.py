#!/usr/bin/env python3
"""
Radix Sort implementation in Python.
"""


def radix_sort(array):
    """
    Sorts an array using radix sort algorithm.

    Args:
        array (list of int): The list of integers to be sorted.

    Returns:
        list of int: The sorted list in ascending order.
    """
    if len(array) == 0:
        return []

    # Find the maximum number to determine the number of digits
    # finding the maxand the number of digits
    greatest_number = max(array)
    number_of_digits = len(str(greatest_number))

    # number of times counting sort is to be done = digits in greatest number
    # for each digit perform counting sort => O(d*(nk))
    # d is the number of digits, n is the number of elements, k is the base
    # Perform counting sort for each digit, start from least significant digit
    for i in range(number_of_digits):
        counting_sort(array, i)

    return array


def counting_sort(array, place):
    """
    A helper function for radix sort; performs counting sort based
    on the digit at the specified place value.

    Args:
        array (list of int): The list of integers to be sorted.
        place (int): The digit place (1 for units, 10 for tens, etc.).
    """
    n = len(array)
    output = [0] * n
    temp = [0] * 10     # for base 10
    digit_place = 10 ** place

    # counting occurrence of digits => O(n)
    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1

    # calculate cumulative count    => O(k), k is the base i.e 10
    for i in range(1, 10):
        temp[i] += temp[i - 1]

    # populate output array => O(n)
    for j in range(n - 1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]

    # Copy the output array to the original array
    array[:] = output[:]


# Example usage:
if __name__ == "__main__":
    array = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_array = radix_sort(array)
    print(sorted_array)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]
