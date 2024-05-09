#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    island_perimeter - Calculates the perimeter of the island described in grid

    Args:
    - grid: A list of lists of integers representing the island grid

    Returns:
    - perimeter: The perimeter of the island
    """

    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the cell is land
            if grid[i][j] == 1:
                # Count the number of adjacent water cells
                adjacent_water = 0
                if i == 0 or grid[i - 1][j] == 0:
                    adjacent_water += 1
                if j == 0 or grid[i][j - 1] == 0:
                    adjacent_water += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    adjacent_water += 1
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    adjacent_water += 1
                # Add the number of adjacent water cells to the perimeter
                perimeter += adjacent_water

    return perimeter
