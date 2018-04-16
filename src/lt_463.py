"""
https://leetcode.com/problems/island-perimeter

Related:
  - lt_695_max-area-of-island
  - lt_733_flood-fill
"""

"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += 4
                    if i > 0 and grid[i-1][j] == 1: count -= 2
                    if j > 0 and grid[i][j - 1] == 1: count -= 2
        return count

    def islandPerimeter_verbose(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        count = 0
        overlapped = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                count += 1
                if i < len(grid) - 1:
                    if grid[i + 1][j]: overlapped += 1
                if j < len(grid[i]) - 1:
                    if grid[i][j + 1]: overlapped += 1
                if i > 0:
                    if grid[i - 1][j]: overlapped += 1
                if j > 0:
                    if grid[i][j - 1]: overlapped += 1
        return count * 4 - overlapped


if __name__ == '__main__':
    test_cases = [
        ([[1, 1], [1, 1]], 8),
        ([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]], 16),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().islandPerimeter(test_case[0])
        print('output:', output)
        assert output == test_case[1]

