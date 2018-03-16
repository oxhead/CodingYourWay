"""
https://leetcode.com/problems/paint-house

Related:
  - lt_198_house-robber
  - lt_213_house-robber-ii
  - lt_265_paint-house-ii
  - lt_276_paint-fence
"""

"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
"""

class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        if not costs: return 0
        dp = [[float('inf')] * 3 for _ in range(len(costs))]
        dp[0] = [c for c in costs[0]]
        for i in range(1, len(dp)):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        return min(dp[-1])

    def minCost_failed(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        elif len(costs) == 1: return min(costs[0])

        dp = [[float('inf')] * 3 for _ in range(len(costs))]
        dp[0] = [c for c in costs[0]]
        for i in range(1, len(dp)):
            dp[i][0] = min(dp[i-1][0] + min(costs[i][1], costs[i][2]), min(dp[i-1][1], dp[i-1][2]) + costs[i][0])
            dp[i][1] = min(dp[i-1][1] + min(costs[i][0], costs[i][2]), min(dp[i-1][0], dp[i-1][2]) + costs[i][1])
            dp[i][2] = min(dp[i-1][2] + min(costs[i][0], costs[i][1]), min(dp[i-1][0], dp[i-1][1]) + costs[i][2])
        return min(dp[-1])

if __name__ == '__main__':
    test_cases = [
        #([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 4),
        #([[17, 2, 17], [16, 16, 5], [14, 3, 19]], 10),
        ([[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]], 26),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minCost(test_case[0])
        print('output:', output)
        assert output == test_case[1]

