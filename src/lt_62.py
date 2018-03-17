"""
https://leetcode.com/problems/unique-paths

Related:
  - lt_63_unique-paths-ii
  - lt_64_minimum-path-sum
  - lt_174_dungeon-game
"""

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * m
        for j in range(1, n):
            for i in range(1, m):
                dp[i] += dp[i-1]
        return dp[-1]

    def uniquePaths_double(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]
        i = j = 0
        for i in range(1, m):
            for j in range(1, n):
               dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    test_cases = [
        ((1, 1), 1),
        ((1, 2), 1),
        ((2, 2), 2),
        ((2, 3), 3),
        ((3, 3), 6),
        ((3, 7), 28),
        ((4, 4), 20),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().uniquePaths(*test_case[0])
        #output = Solution().uniquePaths_double(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

