"""
https://leetcode.com/problems/triangle

Related:
"""

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Time: O(m * n)
        # Space: O(n)
        dp = [float('inf')] * len(triangle[-1])
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            previous = [n for n in dp]
            for j in range(i + 1):
                if j == 0:
                    dp[j] = previous[0] + triangle[i][j]
                elif j == i:
                    dp[j] = previous[j-1] + triangle[i][j]
                else:
                    dp[j] = min(previous[j-1], previous[j]) + triangle[i][j]
        return min(dp)

    def minimumTotal_dp2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[float('inf')] * len(triangle[-1]) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i-1][0] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
        return min(dp[-1])
        

if __name__ == '__main__':
    test_cases = [
        ([[2], [3,4], [6,5,7], [4,1,8,3]], 11),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minimumTotal(test_case[0])
        print('output:', output)
        assert output == test_case[1]

