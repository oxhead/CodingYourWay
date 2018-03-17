"""
https://leetcode.com/problems/unique-paths-ii

Related:
  - lt_62_unique-paths
"""

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(n)
        dp = [1] * len(obstacleGrid[0])
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])): 
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif i == 0:
                    dp[j] = dp[j - 1]
                elif j == 0:
                    continue
                else:
                    dp[j] += dp[j-1]
        return dp[-1]

if __name__ == '__main__':
    test_cases = [
        #([[0]], 1),
        ([[1, 0]], 0),
        #([[0,0,0], [0,1,0], [0,0,0]], 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().uniquePathsWithObstacles(test_case[0])
        print('output:', output)
        assert output == test_case[1]

