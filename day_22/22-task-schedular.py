#!/usr/bin/env python3
"""
This module solves the problem of scheduling tasks with a cooldown period.
The function `leastInterval` which calculates the minimum number of intervals
needed to execute all given tasks with the specified cooldown
period between identical tasks.

Example:
    tasks = ['A', 'A', 'A', 'B', 'B', 'B']
    n = 2
    result = leastInterval(tasks, n)
    print(result)  # Output: 8
"""


def leastInterval(tasks, n):
    """
    Calculate the least number of intervals needed to execute all tasks with
    a given cooldown period.

    Args:
        tasks (List[str]): A list of tasks represented by uppercase
        English letters.
        n (int): The cooldown period between two same tasks.

    Returns:
        int: The minimum number of intervals needed to execute all tasks.

    Example:
        >>> tasks = ['A', 'A', 'A', 'B', 'B', 'B']
        >>> n = 2
        >>> leastInterval(tasks, n)
        8

    The function works by calculating the frequency of each task
    and then determining the structure of the most frequent tasks to
    find the total intervals required, including any necessary idle periods.
    """
    # array to hold count/frequency of 26 possible tasks each initialized to 0
    count_frequency = [0] * 26
    highest_frequency = 0  # stores the highest frequency
    number_highest_frequency = 0  # number of tasks with the highest frequency
    # Calculate the frequency of each task
    for task in tasks:
        # identify the index at which to store frequency of that particular
        # task in the count_frequency
        index = ord(task) - ord('A')
        count_frequency[index] += 1  # increment value at that particular index

        # Update highest_frequency and number_highest_frequency
        # check if highest_frequency is less than count_frequency[index]
        # means this task has a higher frequency than the earlier considered
        if highest_frequency < count_frequency[index]:
            highest_frequency = count_frequency[index]
            # highest_frequency has changed, reset previous tasks identified
            number_highest_frequency = 1

        # check if highest_frequency equals count_frequency[index]
        # means this task also has highest frequency in addition to earlier
        elif highest_frequency == count_frequency[index]:
            number_highest_frequency += 1
    # Calculate the number of parts, slots per part, and total slots in parts
    parts = highest_frequency - 1
    slots_per_part = n - (number_highest_frequency - 1)
    total_slots_in_parts = parts * slots_per_part
    remaining_tasks = len(tasks) - highest_frequency * number_highest_frequency
    empty_slots = max(0, total_slots_in_parts - remaining_tasks)

    # Return the total time including the empty slots
    return len(tasks) + empty_slots


# Example usage:
# Wrapp example usage in a if __name__ == "__main__": block
# to ensure it runs only when the script is executed directly
if __name__ == "__main__":
    tasks = ['A', 'A', 'A', 'B', 'B', 'B']
    n = 2
    print(leastInterval(tasks, n))  # Output should be 8
