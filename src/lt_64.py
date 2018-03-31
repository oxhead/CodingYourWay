"""
https://leetcode.com/problems/minimum-path-sum

Related:
  - lt_62_unique-paths
  - lt_174_dungeon-game
  - lt_741_cherry-pickup
"""

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

[[1,3,1],
 [1,5,1],
 [4,2,1]]

Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(m * n)
        if not grid or len(grid) == 0: return 0
        dp = [[float('inf')] * len(grid[i]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    test_cases = [
        ([[1,3,1], [1,5,1], [4,2,1]], 7),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minPathSum(test_case[0])
        print('output:', output)
        assert output == test_case[1]

