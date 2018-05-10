"""
https://leetcode.com/problems/max-area-of-island
https://leetcode.com/problems/island-perimeter

Related:
  - lt_200_number-of-islands
  - lt_463_island-perimeter
"""

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]

Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50. 
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Time: O(m*n)
        # Space: O(1) or O(m*n) for call stack
        def search(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0: return 0
            count = 1
            grid[i][j] = 0
            for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                count += search(a, b)
            return count
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                c = search(i, j)
                count = max(count, c)
        return count
         

if __name__ == '__main__':
    test_cases = [
        ([[0,0,0,0,0,0,0,0]], 0),
        ([[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxAreaOfIsland(test_case[0])
        print('output:', output)
        assert output == test_case[1]

