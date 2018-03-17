"""
https://leetcode.com/problems/paint-house-ii

Related:
  - lt_238_product-of-array-except-self
  - lt_239_sliding-window-maximum
  - lt_256_paint-house
  - lt_276_paint-fence
"""

"""
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
"""

class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Time: O(n * k)
        # Space: O(n * k)
        if not costs or len(costs) == 0: return 0

        dp = [[float('inf')] * len(costs[i]) for i in range(len(costs))]
        dp[0] = [n for n in costs[0]]
        for i in range(1, len(costs)):
            for j in range(len(costs[i])):
                dp[i][j] = costs[i][j] + min(dp[i-1][:j] + dp[i-1][j+1:])
        return min(dp[-1])

if __name__ == '__main__':
    test_cases = [
        ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], 4),
        ([[17, 2, 17], [16, 16, 5], [14, 3, 19]], 10),
        ([[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]], 26),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minCostII(test_case[0])
        print('output:', output)
        assert output == test_case[1]

