#!/usr/bin/env python3
"""
This module provides a function to calculate the minimum
cost to fly people to two cities.
It contains a single function `twoCityScheduleCost` which takes a list of costs
for flying people to two cities and returns the minimum cost.

Example:
    costs = [[10, 20], [30, 200], [50, 50], [200, 30]]
    result = twoCityScheduleCost(costs)
    print(result)  # Output: 120
"""


def twoCityScheduleCost(costs):
    """
    Calculate the minimum cost to fly people to two cities such that exactly
    half of the people arrive in each city.

    Args:
        costs (List[List[int]]): A list where each element is
        a list of two integers.
        The first integer represents the cost of flying to city A,
        and the second integer represents the cost of flying to city B.

    Returns:
        int: The minimum cost to fly people to the two cities.

    Example:
        >>> costs = [[10, 20], [30, 200], [50, 50], [200, 30]]
        >>> twoCityScheduleCost(costs)
        120

    The function sorts the costs based on the difference in cost between
    flying to city A and city B.
    It then adds the cost of flying the first half of the sorted list to
    city A and the second half to city B.
    """
    # sort costs array based on difference in cost to city A and B
    costs.sort(key=lambda x: x[0] - x[1])    

    cost = 0
    n = len(costs)

    # Add cost of flying first half to city A
    for i in range(n//2):
        cost += costs[i][0]

    # Add cost of flying second half to city B
    for i in range(n//2, n):
        cost += costs[i][1]

    return cost


# Example usage:
if __name__ == "__main__":
    costs = [[10, 20], [30, 200], [50, 50], [200, 30]]
    print(twoCityScheduleCost(costs))  # Output: 110
